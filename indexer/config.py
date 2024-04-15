from functools import lru_cache
from typing import Annotated

from pydantic import AnyUrl, AnyHttpUrl, UrlConstraints
from pydantic_settings import BaseSettings, SettingsConfigDict


class AnyWsUrl(AnyUrl):
    allowed_schemes = ["ws"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")

    REGEN_NODE_REST_URL: AnyHttpUrl
    REGEN_NODE_TENDERMINT_WS_URL: Annotated[
        AnyUrl,
        UrlConstraints(
            allowed_schemes=["ws"],
        ),
    ]

    REGEN_RESOLVER_ID: int
    REGEN_RESOLVER_ALIAS: AnyHttpUrl = None

    GRAPH_DB_BASE_URL: AnyHttpUrl
    GRAPH_DB_USERNAME: str
    GRAPH_DB_PASSWORD: str


# Settings dependency.
@lru_cache()
def get_settings():
    return Settings()
