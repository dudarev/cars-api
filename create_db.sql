-- id,name,active,created_at,updated_at
CREATE TABLE make
(
    id         TEXT PRIMARY KEY,
    name       TEXT,
    active     TEXT CHECK (active='t' OR active='f'),
    created_at TEXT,
    updated_at TEXT
);

-- id,name,active,make_id,created_at,updated_at
CREATE TABLE model
(
    id         TEXT PRIMARY KEY,
    name       TEXT,
    active     TEXT CHECK (active='t' OR active='f'),
    make_id    TEXT,
    created_at TEXT,
    updated_at TEXT,
    FOREIGN KEY (make_id) REFERENCES make (id)
);

-- id,name,active,model_id,created_at,updated_at
CREATE TABLE submodel
(
    id         TEXT PRIMARY KEY,
    name       TEXT,
    active     TEXT CHECK (active='t' OR active='f'),
    model_id   TEXT,
    created_at TEXT,
    updated_at TEXT,
    FOREIGN KEY (model_id) REFERENCES model (id)
);

-- id,active,year,mileage,price,make_id,model_id,submodel_id,body_type,transmission,fuel_type,exterior_color,created_at,updated_at
CREATE TABLE car
(
    id             TEXT PRIMARY KEY,
    active         TEXT CHECK (active='t' OR active='f'),
    year           INT CHECK (year >= 1900),
    mileage        INT CHECK (mileage >= 0),
    price          INT CHECK (price >= 0),
    make_id        TEXT,
    model_id       TEXT,
    submodel_id    TEXT,
    body_type      TEXT,
    transmission   TEXT,
    fuel_type      TEXT,
    exterior_color TEXT,
    created_at     TEXT,
    updated_at     TEXT,
    FOREIGN KEY (make_id) REFERENCES make (id),
    FOREIGN KEY (model_id) REFERENCES model (id),
    FOREIGN KEY (submodel_id) REFERENCES submodel (id)
);

CREATE INDEX update_at_index ON car (updated_at);
CREATE INDEX price_index ON car (price);
CREATE INDEX mileage_index ON car (mileage);
