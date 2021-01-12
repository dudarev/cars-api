# DONE

- [x] List all makes, models, and submodels
- [x] List all cars with their matching make, model and submodel names
- [x] Add new cars 
- [x] Query cars within a certain price and mileage and return a list of matches sorted by `updated_at` (where the newest element is first)
  - [x] Include the car names here as well
  - [x] Make sure to validate user input and provide meaningful responses when input is wrong.
  - [x] Validate price_min <= price_max, mileage_min <= mileage_max
- [x] Enforce consistency of the inserted data directly in the database
  - [x] Constrain on active in db
- [x] Unit test each of your endpoints to verify your implementation
- [x] Index on necessary fields
- [x] README


# TODO

- [ ] More tests for conner cases and validation
- [ ] Setup test coverage report
- [ ] Describe constrains in models.py
- [ ] Constrain on date format in db
- [ ] Normalize times to UTC
- [ ] Clean input data
- [ ] Migrate to PostgreSQL
- [ ] Use Docker
- [ ] Usage of boolean for `active`