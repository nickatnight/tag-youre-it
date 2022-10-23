# flake8: noqa


from tag_youre_it.core.utils import _emojize


TAG_TIME = 480  # seconds


class TagEnum:
    KEY = "!tag"
    ENABLE_PHRASE = "i want to play tag again"
    DISABLE_PHRASE = "i dont want to play tag"


COMMENT_REPLY_YOURE_IT = """
Tag you're it!

You have been tagged by u/{author}. Let's see how long we can keep this game going...you have 5 minutes to tag another user! They can be tagged by mentioning my username in a comment with '!tag' trigger.

If you haven't tagged anybody within the allotted time, the game will reset and break the chain. If you would like to opt out of playing, send me a private message with 'i dont want to play tag' as the subject (this will reset the game).
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
Sorry but you are {tag_over_time}s late to tag. A new game will start.
"""

FOOTER = (
    "^^[&nbsp;how&nbsp;to&nbsp;use]"
    "(https://www.reddit.com/r/TagYoureItBot/comments/pgmpsa/beta_version_release/)"
    "&nbsp;|&nbsp;[creator](https://www.reddit.com/message/compose/?to=betazoid_one)"
    "&nbsp;|&nbsp;[source&nbsp;code](https://github.com/nickatnight/tag-youre-it)"
)


class ReplyEnum:
    @staticmethod
    def _e(reply_string: str) -> str:
        return _emojize(f"{reply_string}\n___\n{FOOTER}")

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
