<p align="center">
    <a href="https://github.com/nickatnight/tag-youre-it/actions">
        <img alt="GitHub Actions status" src="https://github.com/nickatnight/tag-youre-it/actions/workflows/main.yml/badge.svg">
    </a>
    <a href="https://codecov.io/gh/nickatnight/tag-youre-it">
        <img alt="Coverage" src="https://codecov.io/gh/nickatnight/tag-youre-it/branch/master/graph/badge.svg?token=E03I4QK6D9"/>
    </a>
    <a href="https://github.com/nickatnight/tag-youre-it/releases">
        <img alt="Release Status" src="https://img.shields.io/github/v/release/nickatnight/tag-youre-it">
    </a>
    <a href="https://github.com/nickatnight/tag-youre-it/blob/master/LICENSE">
        <img alt="License Shield" src="https://img.shields.io/github/license/nickatnight/tag-youre-it">
    </a>
</p>

<p align="center">
    <a href="https://c.tenor.com/Sf4IW_C95v4AAAAC/tag.gif"><img alt="tag" src="https://c.tenor.com/Sf4IW_C95v4AAAAC/tag.gif"></a>
</p>

# tag-youre-it :runner:
Play virtual tag with other users on Reddit

## How To Play
For now, this bot will only supports subreddit-level play (one active game per sub). This prevents trolls from locking a global game to a (private)subreddit (See the TODO for future enhancements):

Invoke `u/TagYoureItBot` by replying to a Reddit post or comment with the phrase `!tag` e.g. `u/TagYoureItBot !tag`. 1 of 2 things can happen:
- There is no active game. `u/TagYoureItBot` will reply to the same post or comment notifying the author they are now "it". A countdown will start and this author will have an allotted time to "tag" another Reddit user (within the same sub). If the countdown expires and the author has not tagged another user, the game will end. Otherwise...
- There is an active game. If you are the "it" user, the game will continue (see previous paragraph). If you're not it, the bot will reply to your comment stating such. The comment will include a countdown time of how much longer the current tagged user has to tag someone until the game automatically ends.


## Rules
You can't tag...
1. yourself
2. back....yet
3. a user who has opted out of playing
4. u/TagYoureItBot

To opt out of playing, send `u/TagYoureItBot` a private message which contains 'i dont want to play tag' as the subject :heart:

If you would like to opt back in, send `u/TagYoureItBot` a private message with 'i want to play tag again' as the subject

## Why did I build this?
a) A few years ago I read a [reddit blog post](https://www.redditinc.com/blog/how-we-built-rplace/), where they outlined how r/Place was built. I got inspired by the community aspect of the project, and wanted to create something similar (obviously no where near the scale/volume). I pushed a closed source v1 last year, but the game logic was coupled to the web api code (FastApi). I decided to decompose the bot logic into an open source package and keep the web api closed source.

b) Want keep my Python skills fresh since I've been doing a lot of full-stack development in my current role (React/Java).

c) Showcase the ecosystem of my open source projects and how they work together: [Create Release GHA](https://github.com/nickatnight/releases-action), [FastAPI Backend Base](https://github.com/nickatnight/fastapi-backend-base), [Reddit Bot Base](https://github.com/nickatnight/docker-reddit-bot-base).

d) I'm curious to see stats of user engagement (how long did a game chain last, how many users did it contain, which subreddit plays the most, etc)

See [r/TagYoureItBot](https://www.reddit.com/r/TagYoureItBot) for more updates.

## Running Locally
1. Clone repo `git clone https://github.com/nickatnight/tag-youre-it`
2. `cd tag-youre-it`
3. `mv .env_example .env` to add environment variables as needed
4. Install [Docker](https://www.docker.com/products/docker-desktop)
5. `docker compose up`
6. If you've included succifienct credentials in `.env`, the bot will start streaming incoming `Messages` from your inbox

## Development
Requires [Poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) to manage dev environment.  Once installed:
1. install packages with `poetry install`

### Helpful commands
Black
```shell
$ poetry run black tag_youre_it/
```

Flake8
```shell
$ poetry run flake8 tag_youre_it/
```

Test
```shell
$ poetry run pytest --cov=tag_youre_it tests/
```

Package dist and create new setup.py
```shell
$ poetry build --format sdist
$ tar -xvf dist/*-`poetry version -s`.tar.gz -O '*/setup.py' > setup.py
```

Initialize first migration (project must be up with docker compose up and contain no 'version' files)
```shell
$ docker compose run --rm tag alembic revision --autogenerate -m "init"
```

Create new migration file
```shell
$ docker compose run --rm tag alembic revision --autogenerate -m "add a new field or something cool"
```

Apply migrations
```shell
$ docker compose run --rm tag alembic upgrade head
```

## TODO
- ~github action for ci/cd workflow~ [#2](https://github.com/nickatnight/tag-youre-it/pull/2)
- move db client to stream service init
- check for downvotes on recent comments
- extra `CommentStreamService` to stream incoming comments from sub
- ~add simple tests~ [#3](https://github.com/nickatnight/tag-youre-it/pull/3) [#9](https://github.com/nickatnight/tag-youre-it/pull/9)
- public web api
- frontend (gameplay stats)
- multi subreddit play (basically all subs)
- "tag back" flag
- add exception handling
- ~add docker compose for local testing/dev~ [#6](https://github.com/nickatnight/tag-youre-it/pull/6)
- increase coverage to sensible percentage
- refactor DbClient and AbstractRepository
- ~setup mypy~ [#14](https://github.com/nickatnight/tag-youre-it/pull/14)
- ~add subreddit check when stream processing~ [#12](https://github.com/nickatnight/tag-youre-it/pull/12)
- ~finish process() logic~
- decorator for yielding database sessions
- add loader method for apraw objects
- add flowchart
