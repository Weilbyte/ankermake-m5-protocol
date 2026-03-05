import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the AnkerMake sensors."""
    # TODO: Fetch the active Printers from hass.data[DOMAIN][entry.entry_id]
    # that were initialized in __init__.py `async_setup_entry`
    
    # Example placeholder:
    # api = hass.data[DOMAIN][entry.entry_id]["api"]
    # coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]
    
    entities = []
    
    # We will loop over the known printers from the API fetch and
    # register sensor entities (Extruder Temp, Bed Temp, Print Progress)
    # entities.append(AnkerMakeTempSensor(coordinator, printer, "Extruder"))
    
    async_add_entities(entities, True)


class AnkerMakeTempSensor(CoordinatorEntity, SensorEntity):
    """Representation of an AnkerMake Temperature Sensor."""

    def __init__(self, coordinator, printer, sensor_type):
        """Pass coordinator to CoordinatorEntity."""
        super().__init__(coordinator)
        self.printer = printer
        self.sensor_type = sensor_type

        # Important Entity attributes
        self._attr_name = f"{printer.name} {sensor_type} Temperature"
        self._attr_unique_id = f"{printer.sn}_{sensor_type.lower()}_temp"
        self._attr_native_unit_of_measurement = "°C"
        
    @property
    def native_value(self):
        """Return the state of the sensor."""
        # TODO: Return `self.coordinator.data[self.printer.sn]["nozzle_temp"]`
        return 0

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        # True if MQTT is connected and actively supplying data
        return self.coordinator.last_update_success
