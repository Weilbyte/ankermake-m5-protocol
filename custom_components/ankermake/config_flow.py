import logging
from typing import Any, Dict, Optional

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, CONF_EMAIL, CONF_PASSWORD, CONF_COUNTRY

_LOGGER = logging.getLogger(__name__)

# Schema for the Configuration UI
USER_SCHEMA = vol.Schema({
    vol.Required(CONF_EMAIL): str,
    vol.Required(CONF_PASSWORD): str,
    vol.Required(CONF_COUNTRY, default="US"): vol.In(["US", "EU", "GB", "DE"]), # Expand as necessary
})


class AnkerMakeConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for AnkerMake."""

    VERSION = 1

    async def async_step_user(
        self, user_input: Optional[Dict[str, Any]] = None
    ) -> config_entries.ConfigFlowResult:
        """Handle the initial step."""
        errors: Dict[str, str] = {}

        if user_input is not None:
            # TODO: Add logic here to connect out to AnkerHTTPApiV2 using hassles.async_add_executor_job()
            # to verify that the email, password, and country code are valid before
            # creating the config entry.

            # If login successful:
            return self.async_create_entry(
                title=user_input[CONF_EMAIL],
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=USER_SCHEMA,
            errors=errors,
        )
