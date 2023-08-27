USE airflow;

CREATE TABLE IF NOT EXISTS dim_house (
    id INT NOT NULL PRIMARY KEY,
    id_house INT,
    area FLOAT,
    beds INT,
    baths INT,
    detail_url varchar(8000),
    image_url varchar(8000)
);

CREATE TABLE IF NOT EXISTS dim_broker (
    id INT NOT NULL PRIMARY KEY,
    broker_name varchar(255)
);

CREATE TABLE IF NOT EXISTS dim_province (
    id INT NOT NULL PRIMARY KEY,
    province varchar(255)
);

CREATE TABLE IF NOT EXISTS dim_dstreet (
    id INT NOT NULL PRIMARY KEY,
    number_street varchar(255),
    key_province INT,
    CONSTRAINT fk_dstreet_province
    FOREIGN KEY (key_province)
    REFERENCES dim_province(id)
);

CREATE TABLE IF NOT EXISTS fact_post (
    id INT NOT NULL PRIMARY KEY,
    price FLOAT,
    key_house INT,
    key_broker INT,
    key_province INT,
    status_type varchar(255),
    status_text varchar(255),
    CONSTRAINT fk_post_province
    FOREIGN KEY (key_province)
    REFERENCES dim_province(id),
    CONSTRAINT fk_post_broker
    FOREIGN KEY (key_broker)
    REFERENCES dim_broker(id),
    CONSTRAINT fk_post_house
    FOREIGN KEY (key_house)
    REFERENCES dim_house(id)
);