# flake8: noqa
from urllib.parse import quote_plus

from tag_youre_it.core.utils import _emojize


TAG_TIME = 780  # seconds


class TagEnum:
    KEY = "!tag"
    ENABLE_PHRASE = "i want to play tag again"
    DISABLE_PHRASE = "i dont want to play tag"


COMMENT_REPLY_YOURE_IT = """
:robot: Tag you're it!

You have been tagged by u/{author}. Let's see how long we can keep this game going...you have {timer} minutes to tag another user! They can be tagged by mentioning my username in a comment with '!tag' trigger.

If you haven't tagged anybody within the allotted time, the game will end/reset and break the chain.
"""

UNABLE_TO_TAG_SELF = """
You can't tag yourself! :no_entry:
"""

UNABLE_TO_TAG_BOT = """
You can't tag the bot! :no_entry:
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

GAME_OVER = """
The current 'it' users time to tag has expired...{tag_over_time}s too late. The current game will end.
"""

FOOTER = (
    "^^[&nbsp;how&nbsp;to&nbsp;use]"
    "(https://www.reddit.com/r/TagYoureItBot/comments/yi25li/tagyoureitbot_info_v22/)"
    f"&nbsp;|&nbsp;[opt&nbsp;out](https://www.reddit.com/message/compose/?to=TagYoureItBot&subject={quote_plus(TagEnum.DISABLE_PHRASE)})"
    "&nbsp;|&nbsp;[creator](https://www.reddit.com/message/compose/?to=throwie_one)"
    "&nbsp;|&nbsp;[source&nbsp;code](https://github.com/nickatnight/tag-youre-it)"
    "&nbsp;|&nbsp;[wikihow](https://www.wikihow.com/Play-Tag)"
    "&nbsp;|&nbsp;[public&nbsp;api](https://api.tagyoureitbot.com/docs)"
    "&nbsp;|&nbsp;[website](https://tagyoureitbot.com)"
)


class ReplyEnum:
    @staticmethod
    def _e(reply_string: str) -> str:
        return _emojize(f"{reply_string}\n___\n{FOOTER}")

    @staticmethod
    def comment_reply_tag(author: str, timer: str) -> str:
        return ReplyEnum._e(COMMENT_REPLY_YOURE_IT.format(author=author, timer=timer))

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
    def unable_to_tag_bot() -> str:
        return ReplyEnum._e(UNABLE_TO_TAG_BOT)

    @staticmethod
    def user_opts_out(author: str) -> str:
        return ReplyEnum._e(USER_OPTS_OUT_GAME.format(author=author))

    @staticmethod
    def user_opts_out_info(author: str) -> str:
        return ReplyEnum._e(USER_OPTS_OUT_GAME_INFO.format(author=author))

    @staticmethod
    def game_over(tag_over_time: int) -> str:
        return ReplyEnum._e(GAME_OVER.format(tag_over_time=tag_over_time))


class SupportedSubs:
    """names of subreddits (case sensitive)"""

    TAG_YOURE_IT_BOT = "TagYoureItBot"
    DOGECOIN = "dogecoin"
