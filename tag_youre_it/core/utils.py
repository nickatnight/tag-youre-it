import inspect
import logging

from emoji import emojize
from pydantic import BaseModel as DanticBaseModel


logger = logging.getLogger(__name__)


def _emojize(s: str) -> str:
    return emojize(s, variant="emoji_type", language="alias")


# https://github.com/pydantic/pydantic/issues/1223
def optional(*fields):  # type: ignore
    def dec(_cls):  # type: ignore
        for field in fields:
            _cls.__fields__[field].required = False
        return _cls

    if fields and inspect.isclass(fields[0]) and issubclass(fields[0], DanticBaseModel):
        cls = fields[0]
        fields = cls.__fields__  # type: ignore
        return dec(cls)  # type: ignore
    return dec
