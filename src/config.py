from pydantic_settings import BaseSettings, SettingsConfigDict
from urllib.parse import quote_plus


class Settings(BaseSettings):
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    REDIS_URL: str = "redis://localhost:6379/0"
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True
    DOMAIN: str

    # Dynamically construct the DATABASE_URL
    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{quote_plus(self.DB_USERNAME)}:{quote_plus(self.DB_PASSWORD)}@db:5432/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# Load the configuration
Config = Settings()
