from azure.monitor.opentelemetry import configure_azure_monitor
from logging import getLogger, INFO

from opentelemetry import trace

# Configure OpenTelemetry to use Azure Monitor with the 
# APPLICATIONINSIGHTS_CONNECTION_STRING environment variable.
configure_azure_monitor()

logger = getLogger(__name__)
logger.setLevel(INFO)