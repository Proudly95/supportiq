from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_enconding="utf-8")

    database_url: str = "postgresql+psycopg://supportia:supportiq@localhost:5432/supportiq"


settings = Settings()
