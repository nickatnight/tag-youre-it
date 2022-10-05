from abc import ABC, abstractmethod
from typing import AsyncIterator, Optional, Type, TypeVar, Union

import asyncpraw
from asyncpraw.models.base import AsyncPRAWBase


DbType = TypeVar("DbType")

ModelType = TypeVar("ModelType")
SchemaType = TypeVar("SchemaType")


class AbstractStream(ABC):
    """interface to stream different Reddit objects Comments, Messaging, etc"""

    @abstractmethod
    async def pre_flight_check(self, db_client: Type[DbType], obj: AsyncPRAWBase) -> bool:
        """check/process messages that were not comments

        these are private messages or things like mod mail

        :param db_client:           database client for interacting with database
        :param obj:                 AsyncPRAW Reddit object
        :return:                    True if further processing needed, False otherwise
        """
        ...

    @abstractmethod
    async def process(
        self, db_client: Type[DbType], obj: AsyncPRAWBase, game_id: Optional[str]
    ) -> Optional[str]:
        """process Reddit object since this was most likely a 'tag' message

        :param db_client:           database client for interacting with database
        :param obj:                 AsyncPRAW Reddit object
        :param game_id:             Id of the Game database object
        :return:                    New game id TODO: come back to this logic
        """
        ...

    @abstractmethod
    def stream(
        self, reddit: asyncpraw.Reddit
    ) -> AsyncIterator[Union["asyncpraw.models.Comment", "asyncpraw.models.Message"]]:
        """stream incoming Reddit objects

        :param reddit:              Main Reddit wrapper object
        :return:                    Reddit obejct generator
        """
        ...
