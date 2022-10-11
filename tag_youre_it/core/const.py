# flake8: noqa


from os import stat

from tag_youre_it.core.utils import _emojize


class TagEnum:
    KEY = "!tag"
    ENABLE_PHRASE = "i want to play tag again"
    DISABLE_PHRASE = "i dont want to play tag"


COMMENT_REPLY_YOURE_IT = """
Tag you're it!

You have been tagged by u/{author}. Let's see how long we can keep this game going...you have 5 minutes to tag another user! They can be tagged by mentioning my username in a comment with '!tag' trigger. eg 'u/TagYoureItBot !tag'.

If you haven't tagged anybody within the allotted time, the game will reset and break the chain. If you would like to opt out of playing, send me a private message with 'i dont want to play tag' as the subject (this will reset the game).
"""

UNABLE_TO_TAG_SELF = """
You can't tag yourself! :no_entry:
"""

USER_OPTS_OUT_GAME = """
u/{author} has opted out of playing tag :no_good:
"""

USER_OPTS_OUT_GAME_INFO = """
I'm sorry to see you go u/{author}.

If you would like to tag back in, send me a private message which contains 'i want to play tag again' as the subject :heart:
"""

CURRENT_ACTIVE_GAME = """
There's already an active game of Tag :runner:
"""

WELCOME_BACK = """
Welcome back to the game u/{author}! :wave:
"""


class ReplyEnum:
    @staticmethod
    def _e(reply_string: str) -> str:
        return _emojize(reply_string)

    @staticmethod
    def comment_reply_tag(author: str) -> str:
        return ReplyEnum._e(COMMENT_REPLY_YOURE_IT.format(author=author))

    @staticmethod
    def welcome_back(author: str) -> str:
        return ReplyEnum._e(WELCOME_BACK.format(author=author))

    @staticmethod
    def active_game() -> str:
        return ReplyEnum._e(CURRENT_ACTIVE_GAME)

    @staticmethod
    def unable_to_tag_self() -> str:
        return ReplyEnum._e(UNABLE_TO_TAG_SELF)

    @staticmethod
    def user_opts_out(author: str) -> str:
        return ReplyEnum._e(USER_OPTS_OUT_GAME.format(author=author))

    @staticmethod
    def user_opts_out_info(author: str) -> str:
        return ReplyEnum._e(USER_OPTS_OUT_GAME_INFO.format(author=author))


class SupportedSubs:
    """names of subreddits (case sensitive)"""

    TAG_YOURE_IT_BOT = "TagYoureItBot"
