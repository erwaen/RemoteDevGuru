from config.settings.base import BackendBaseSettings
from config.settings.environment import Environment


class BackendStageSettings(BackendBaseSettings):

    DESCRIPTION: str | None = "Test Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.STAGING
