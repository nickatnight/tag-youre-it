import logging

from emoji import emojize


logger = logging.getLogger(__name__)


def _emojize(s: str) -> str:
    return emojize(s, variant="emoji_type", language="alias")
