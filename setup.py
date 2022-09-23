# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tag_youre_it',
 'tag_youre_it.core',
 'tag_youre_it.domain',
 'tag_youre_it.services']

package_data = \
{'': ['*']}

install_requires = \
['asyncpraw>=7.5.0,<8.0.0', 'emoji>=2.1.0,<3.0.0', 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'tag-youre-it',
    'version': '2.0.0',
    'description': 'Play tag with other Redditors',
    'long_description': None,
    'author': 'nickatnight',
    'author_email': 'nickkelly.858@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
