# -*- coding: utf-8 -*-
from setuptools import setup


packages = [
    "tag_youre_it",
    "tag_youre_it.core",
    "tag_youre_it.migrations",
    "tag_youre_it.migrations.versions",
    "tag_youre_it.models",
    "tag_youre_it.repository",
    "tag_youre_it.schemas",
    "tag_youre_it.services",
    "tag_youre_it.services.stream",
]

package_data = {"": ["*"]}

install_requires = [
    "asyncpraw>=7.5.0,<8.0.0",
    "emoji>=2.1.0,<3.0.0",
    "pydantic>=1.10.2,<2.0.0",
    "sqlmodel>=0.0.8,<0.0.9",
]

setup_kwargs = {
    "name": "tag-youre-it",
    "version": "2.1.4",
    "description": "Play tag with other Redditors",
    "long_description": '<p align="center">\n    <a href="https://github.com/nickatnight/tag-youre-it/actions">\n        <img alt="GitHub Actions status" src="https://github.com/nickatnight/tag-youre-it/actions/workflows/main.yml/badge.svg">\n    </a>\n    <a href="https://codecov.io/gh/nickatnight/tag-youre-it">\n        <img alt="Coverage" src="https://codecov.io/gh/nickatnight/tag-youre-it/branch/master/graph/badge.svg?token=E03I4QK6D9"/>\n    </a>\n    <a href="https://github.com/nickatnight/tag-youre-it/releases">\n        <img alt="Release Status" src="https://img.shields.io/github/v/release/nickatnight/tag-youre-it">\n    </a>\n    <a href="https://github.com/nickatnight/tag-youre-it/blob/master/LICENSE">\n        <img alt="License Shield" src="https://img.shields.io/github/license/nickatnight/tag-youre-it">\n    </a>\n</p>\n\n<p align="center">\n    <a href="https://c.tenor.com/Sf4IW_C95v4AAAAC/tag.gif"><img alt="tag" src="https://c.tenor.com/Sf4IW_C95v4AAAAC/tag.gif"></a>\n</p>\n\n# tag-youre-it :runner:\nPlay virtual tag with other users on Reddit\n\n## How To Play\nFor now, this bot will only supports subreddit-level play (one active game per sub). This prevents trolls from locking a global game to a (private)subreddit (See the TODO for future enhancements):\n\nInvoke `u/TagYoureItBot` by replying to a Reddit post or comment with the phrase `!tag` e.g. `u/TagYoureItBot !tag`. 1 of 2 things can happen:\n- There is no active game. `u/TagYoureItBot` will reply to the same post or comment notifying the author they are now "it". A countdown will start and this author will have an allotted time to "tag" another Reddit user (within the same sub). If the countdown expires and the author has not tagged another user, the game will end. Otherwise...\n- There is an active game. If you are the "it" user, the game will continue (see previous paragraph). If you\'re not it, the bot will reply to your comment stating such. The comment will include a countdown time of how much longer the current tagged user has to tag someone until the game automatically ends.\n\n\n## Rules\nYou can\'t tag...\n1. yourself\n2. back....yet\n3. a user who has opted out of playing\n4. u/TagYoureItBot\n\nTo opt out of playing, send `u/TagYoureItBot` a private message which contains \'i dont want to play tag\' as the subject :heart:\n\nIf you would like to opt back in, send `u/TagYoureItBot` a private message with \'i want to play tag again\' as the subject\n\n## Why did I build this?\na) A few years ago I read a [reddit blog post](https://www.redditinc.com/blog/how-we-built-rplace/), where they outlined how r/Place was built. I got inspired by the community aspect of the project, and wanted to create something similar (obviously no where near the scale/volume). I pushed a closed source v1 last year, but the game logic was coupled to the web api code (FastApi). I decided to decompose the bot logic into an open source package and keep the web api closed source.\n\nb) Want keep my Python skills fresh since I\'ve been doing a lot of full-stack development in my current role (React/Java).\n\nc) Showcase the ecosystem of my open source projects and how they work together: [Create Release GHA](https://github.com/nickatnight/releases-action), [FastAPI Backend Base](https://github.com/nickatnight/fastapi-backend-base), [Reddit Bot Base](https://github.com/nickatnight/docker-reddit-bot-base).\n\nd) I\'m curious to see stats of user engagement (how long did a game chain last, how many users did it contain, which subreddit plays the most, etc)\n\nSee [r/TagYoureItBot](https://www.reddit.com/r/TagYoureItBot) for more updates.\n\n## Running Locally\n1. Clone repo `git clone https://github.com/nickatnight/tag-youre-it`\n2. `cd tag-youre-it`\n3. `mv .env_example .env` to add environment variables as needed\n4. Install [Docker](https://www.docker.com/products/docker-desktop)\n5. `docker compose up`\n6. If you\'ve included succifienct credentials in `.env`, the bot will start streaming incoming `Messages` from your inbox\n\n## Development\nRequires [Poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) to manage dev environment.  Once installed:\n1. install packages with `poetry install`\n\n### Helpful commands\nBlack\n```shell\n$ poetry run black tag_youre_it/\n```\n\nFlake8\n```shell\n$ poetry run flake8 tag_youre_it/\n```\n\nTest\n```shell\n$ poetry run pytest --cov=tag_youre_it tests/\n```\n\nPackage dist and create new setup.py\n```shell\n$ poetry build --format sdist\n$ tar -xvf dist/*-`poetry version -s`.tar.gz -O \'*/setup.py\' > setup.py\n```\n\nInitialize first migration (project must be up with docker compose up and contain no \'version\' files)\n```shell\n$ docker compose run --rm tag alembic revision --autogenerate -m "init"\n```\n\nCreate new migration file\n```shell\n$ docker compose run --rm tag alembic revision --autogenerate -m "add a new field or something cool"\n```\n\nApply migrations\n```shell\n$ docker compose run --rm tag alembic upgrade head\n```\n\n## TODO\n- ~github action for ci/cd workflow~ [#2](https://github.com/nickatnight/tag-youre-it/pull/2)\n- move db client to stream service init\n- check for downvotes on recent comments\n- extra `CommentStreamService` to stream incoming comments from sub\n- ~add simple tests~ [#3](https://github.com/nickatnight/tag-youre-it/pull/3) [#9](https://github.com/nickatnight/tag-youre-it/pull/9)\n- public web api\n- frontend (gameplay stats)\n- multi subreddit play (basically all subs)\n- "tag back" flag\n- add exception handling\n- ~add docker compose for local testing/dev~ [#6](https://github.com/nickatnight/tag-youre-it/pull/6)\n- increase coverage to sensible percentage\n- refactor DbClient and AbstractRepository\n- ~setup mypy~ [#14](https://github.com/nickatnight/tag-youre-it/pull/14)\n- ~add subreddit check when stream processing~ [#12](https://github.com/nickatnight/tag-youre-it/pull/12)\n- ~finish process() logic~ [#16](https://github.com/nickatnight/tag-youre-it/pull/16)\n- decorator for yielding database sessions\n- add loader method for apraw objects\n- add flowchart\n- add smaller steps to GHA\n- add PgAdmin\n',
    "author": "nickatnight",
    "author_email": "nickkelly.858@gmail.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://github.com/nickatnight/tag-youre-it",
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.9,<4.0",
}


setup(**setup_kwargs)
