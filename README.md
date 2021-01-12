# Cars API

## How to Run

To run it locally:

- create a Sqlite database file and database tables with `make db`
- place CSV data into `data/` folder
- populate the database with data with `make data`
- install all dependencies into your virtualenv with `pip install -r requirements.txt`
- run the app with `make run`

Navigate to http://127.0.0.1:8000/docs and explore the API

If data needs to be cleaned, run `make clean`.

## Tests

To run tests:

- install tests dependencies into your virtualenv with `pip install -r test-requirements.txt`
- run tests with `make test`

## Planning

Future development plans are tracked in [TODO](TODO.md).