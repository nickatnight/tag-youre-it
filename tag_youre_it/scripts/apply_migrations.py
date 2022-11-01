# Python script to apply migrations up to head eg. 'apply-migrations'
# Will not work via 'poetry run'
import os

import alembic.config


tag_youre_it_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
alembic_args = ["-c", os.path.join(tag_youre_it_dir, "alembic.ini"), "upgrade", "head"]


def main():
    alembic.config.main(argv=alembic_args)


if __name__ == "__main__":
    main()
