# tag-youre-it :runner:
Play virutal tag with other users on Reddit

## How To Play
For now, this bot will only support subreddit-level play, one active game per sub (See the TODO for future enhancements):

Invoke `u/TagYoureItBot` by replying to a Reddit post or comment with the phrase `!tag`. 1 of 2 things can happen:
- There is no active game. `u/TagYoureItBot` will reply to the same post or comment notifying the author they are now "it". A countdown will start and this author will have an alloted time to "tag" another Reddit user (within the same sub). If the countdown expires and the auther has not tagged another user, the game will end. Otherwise...
- There is an active game. If you are the "it" user, the game will continue (see previous paragraph). If you're not it, the bot will reply to your comment stating such. The comment will include a countdown time of how much longer the current tagged user has to tag someone until the game automatically ends. 


## Rules
You can't...
1. tag yourself
2. tag back (yet)
3. tag a user who has opted out of playing

To opt out of playing, send `u/TagYoureItBot` a private message which contains 'i dont want to play tag' as the subject :heart:

If you would like to opt back in, send `u/TagYoureItBot` a private message with 'i want to play tag again' as the subject

## Why did I build this?
A few years ago I read a [reddit blog post](https://www.redditinc.com/blog/how-we-built-rplace/), where they outlined how r/Place was built. I got inspired by the community aspect of the project, and wanted to create something similar (obvioulsy no where near the scale/volume). I pushed a closed source v1 last year, but the game logic was coupled to the web api code (FastApi). I decided to decompose the bot logic into an open source package and keep the web api closed source.

I'm also curious to see stats of user engagement (how long did a game chain last, how many users did it contain, which subreddit plays the most, etc)

See [r/TagYoureItBot](https://www.reddit.com/r/TagYoureItBot) for more updates.

## Running Locally
1. Clone repo `git clone https://github.com/nickatnight/tag-youre-it`
2. `cd tag-youre-it`
3. `mv .env_example .env` to add environment variables as needed
4. Install [Docker](https://www.docker.com/products/docker-desktop)
5. `docker build -t tag-youre-it:latest .`
6. `docker run --env-file .env tag-youre-it:latest`

## Development
Requires [Poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) to manage dev environment.  Once installed:
1. install packages with `poetry install`
2. black `poetry run black .`
3. flake8 `poetry run flake8`
4. test `poetry run pytest --cov=tag_youre_it tests/`
5. build sdist `poetry build --format sdist`
6. create new setup.py
```shell
$ tar -xvf dist/*-`poetry version -s`.tar.gz -O '*/setup.py' > setup.py
```

## TODO
- github action for ci/cd workflow
- move db client to stream service
- check for downvotes on recent comments
- extra `CommentStreamService` to stream incoming comments from sub
- tests
- public web api
- frontend (gameplay stats)
- multi subreddit play (basically all subs)
- tag back flag
