from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Base de datos
    DATABASE_URL: str = "postgresql://jobkit:jobkit@db:5432/jobkit"

    # Redis
    REDIS_URL: str = "redis://redis:6379"

    # LLM
    LLM_PROVIDER: str = "ollama"
    LLM_MODEL: str = "llama3.2"
    OLLAMA_BASE_URL: str = "http://ollama:11434"

    # API Keys (opcionales)
    ANTHROPIC_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    GOOGLE_API_KEY: str = ""

    model_config = {"env_file": ".env"}


settings = Settings()
