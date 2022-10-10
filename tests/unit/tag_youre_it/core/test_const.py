from tag_youre_it.core.const import ReplyEnums


def test_welcome_back_enum():
    test_str = ReplyEnums.welcome_back("test")
    assert "\nWelcome back to the game u/test! 👋\n" == test_str


def test_active_game_enum():
    test_str = ReplyEnums.active_game()
    assert "\nThere's already an active game of Tag 🏃\n" == test_str


def test_unable_to_tag_self_enum():
    test_str = ReplyEnums.unable_to_tag_self()
    assert "\nYou can't tag yourself! ⛔️\n" == test_str


def test_user_opts_out_enum():
    test_str = ReplyEnums.user_opts_out("test")
    assert "\nu/test has opted out of playing tag 🙅\n" == test_str


def test_user_opts_out_info_enum():
    test_str = ReplyEnums.user_opts_out_info("test")
    assert (
        "\nI'm sorry to see you go u/test.\n\nIf you would like to tag back in, send me a private message which contains 'i want to play tag again' as the subject ❤️\n"  # noqa
        == test_str
    )


def test_comment_reply_tag_enum():
    test_str = ReplyEnums.comment_reply_tag("test")
    assert (
        "\nTag you're it!\n\nYou have been tagged by u/test. Let's see how long we can keep this game going...you have 5 minutes to tag another user! They can be tagged by mentioning my username in a comment with '!tag' trigger. eg 'u/TagYoureItBot !tag'.\n\nIf you haven't tagged anybody within the allotted time, the game will reset and break the chain. If you would like to opt out of playing, send me a private message with 'i dont want to play tag' as the subject (this will reset the game).\n"  # noqa
        == test_str
    )
