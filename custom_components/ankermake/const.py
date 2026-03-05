from datetime import timedelta

DOMAIN = "ankermake"

CONF_EMAIL = "email"
CONF_PASSWORD = "password"
CONF_COUNTRY = "country"

# Default Polling interval for API updates (if we are doing HTTP polling instead of pure MQTT)
# Usually we rely on MQTT, but we might poll the HTTPS API every so often
SCAN_INTERVAL = timedelta(minutes=5)

# Keys used to store our data coordinator and API instances
DATA_COORDINATOR = "coordinator"
DATA_API = "api"
DATA_MQTT = "mqtt"
