from typing import Any, Optional

from decouple import config as config_decouple


def config(value: str, default_value: Optional[Any], cast=str) -> Any:
    ssm_enable = config_decouple("SSM_ENABLE", cast=bool)
    if not ssm_enable:
        return config_decouple(value, default_value, cast=cast)
