class TagYoureItException(Exception):
    pass


class ImproperlyConfigured(TagYoureItException):
    pass


class NoPlayersFoundError(TagYoureItException):
    pass


class GameNotFoundError(TagYoureItException):
    pass
