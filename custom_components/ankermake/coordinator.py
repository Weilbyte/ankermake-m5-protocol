import logging
from datetime import timedelta

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from libflagship.mqttapi import AnkerMQTTBaseClient
from libflagship import ROOT_DIR

_LOGGER = logging.getLogger(__name__)

class AnkerMakeCoordinator(DataUpdateCoordinator):
    """Class to manage fetching AnkerMake data via MQTT polling."""

    def __init__(self, hass, account, printers):
        """Initialize."""
        super().__init__(
            hass,
            _LOGGER,
            name="ankermake",
            update_interval=timedelta(seconds=5),
        )
        self.account = account
        self.printers = printers
        self.clients = []
        self.data = {p.sn: {} for p in printers}

    def _setup_clients(self):
        servertable = {
            "eu": "make-mqtt-eu.ankermake.com",
            "us": "make-mqtt.ankermake.com",
        }
        # Fallback to US if region not perfectly mapped
        server = servertable.get(self.account.region.lower(), "make-mqtt.ankermake.com")
        
        for p in self.printers:
            _LOGGER.info(f"Setting up AnkerMake MQTT Client for printer {p.sn}")
            client = AnkerMQTTBaseClient.login(
                p.sn,
                self.account.mqtt_username,
                self.account.mqtt_password,
                p.mqtt_key,
                ca_certs=ROOT_DIR / "ssl/ankermake-mqtt.crt",
                verify=True,
            )
            # connect() loops until connected
            # This blocks, but it's running in async_add_executor_job
            client.connect(server, timeout=10)
            self.clients.append((p.sn, client))

    def _fetch_all(self):
        """Poll the MQTT client queue for new messages. Runs in executor background thread."""
        if not self.clients:
            self._setup_clients()

        for sn, client in self.clients:
            try:
                # fetch() loops the underlying Paho client for a brief moment
                # and returns any parsed payload dictionaries from the queue
                queue = client.fetch(timeout=0.2)
                for msg, body in queue:
                    for obj in body:
                        # Extract Extruder/Bed Temperatures
                        if "currentTemp" in obj:
                            # 1003 is extruder, 1004 is hotbed
                            if obj.get("commandType") == 1003: 
                                self.data[sn]["nozzle_temp"] = obj["currentTemp"] / 100.0
                            elif obj.get("commandType") == 1004:
                                self.data[sn]["hotbed_temp"] = obj["currentTemp"] / 100.0
                        
                        # Extract progress bar
                        if "progress" in obj:
                            self.data[sn]["progress"] = obj["progress"]
                            
            except Exception as e:
                _LOGGER.error(f"Error fetching MQTT for AnkerMake {sn}: {e}")
        
        return self.data

    async def _async_update_data(self):
        """Update data via Home Assistant async executor."""
        return await self.hass.async_add_executor_job(self._fetch_all)
