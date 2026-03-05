import asyncio
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, CONF_EMAIL, CONF_PASSWORD, CONF_COUNTRY

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor", "camera"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up AnkerMake from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    email = entry.data.get(CONF_EMAIL)
    password = entry.data.get(CONF_PASSWORD)
    country = entry.data.get(CONF_COUNTRY)

    _LOGGER.info(f"Setting up AnkerMake integration for: {email} in region: {country}")

    # TODO: Wrap libflagship HTTP and MQTT in asyncio executors here
    # 1. Initialize AnkerHTTPApiV2
    # 2. Login synchronously via hass.async_add_executor_job()
    # 3. Request Profile Data and Printer List
    # 4. Kick off the MQTT daemon thread

    hass.data[DOMAIN][entry.entry_id] = {
        # "api": api_instance,
        # "mqtt": mqtt_instance
    }

    # Forward the setup to the sensor/camera platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        # TODO: clean up the background MQTT threads here
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
