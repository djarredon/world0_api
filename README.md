# world0 API

## Setup

Required tools:

- [Python 3.6+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/)
- [git](https://git-scm.com/)

Installation:

    git clone https://github.com/world0/api
    cd api
    virtualenv venv
    echo "\nPYTHONPATH=`pwd`" >> venv/bin/activate
    source venv/bin/activate
    pip install -r requirements.txt

By default the application uses [sqlite](https://sqlite.org/). To change this
to another database engine, override `DATABASE_URI` in `config.py`.

Example of a postgres URI:

    echo "\nDATABASE_URL = 'postgres://db_user:db_pass@db_host/db_name'" >> config.py

Create the database (uses `DATABASE_URI` from `config.py`, falling back
to `configdist.py` if `config.py` is not present):

    source venv/bin/activate
    ./manage.py create_db

## Development server

Flask comes with a built in development server. To use it:

    source venv/bin/activate
    ./manage.py runserver -dr

The development server is accessible at [http://localhost:5000](http://localhost:5000).

## Adding a user

Adding a user can be done via the CLI or the API.

Via the CLI:

    ./manage.py add_user example_user user@example.com example_password

Via the API (using [cURL](https://curl.haxx.se/)):

    curl -i -X POST \
    -d '{"username": "example_user", "email": "user@example.com", "password": "foo"}' \
    -H "Content-Type: application/json" \
    http://localhost:5000/api/v1/account/register
