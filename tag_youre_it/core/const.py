# flake8: noqa


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
You can't tag yourself! xD
"""

USER_OPTS_OUT_GAME = """
u/{author} has opted out of playing tag 
"""

USER_OPTS_OUT_GAME_INFO = """
I'm sorry to see you go {author}.

If you would like to tag back in, send me a private message which contains 'i want to play tag again' as the subject :heart:
"""

CURRENT_ACTIVE_GAME = """
There is already an active game of Tag
"""

WELCOME_BACK = """
Welcome back to the game u/{author}! :wave:
"""
