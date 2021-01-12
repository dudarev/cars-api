.PHONY: clean data test db data

clean:
	rm data.db
	rm test.db

db:
	sqlite3 data.db < create_db.sql

data:
	sqlite3 data.db < import_data.sql

run:
	uvicorn app.main:app --reload

test:
	pytest
