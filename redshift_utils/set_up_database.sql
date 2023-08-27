DROP SCHEMA IF EXISTS house_procesing CASCADE;

CREATE SCHEMA house_procesing;

CREATE TABLE house_procesing.dim_house (
    id_house INT,
    area FLOAT,
    beds INT,
    baths INT,
    detail_url VARCHAR(8000),
    image_url VARCHAR(8000),
    id INT PRIMARY KEY
);

CREATE TABLE house_procesing.dim_broker (
    id INT NOT NULL PRIMARY KEY,
    broker_name varchar(255)
);

CREATE TABLE house_procesing.dim_province (
    id INT PRIMARY KEY,
    province VARCHAR(255)
);

CREATE TABLE house_procesing.dim_dstreet (
    id INT PRIMARY KEY,
    number_street VARCHAR(255),
    key_province INT,
    CONSTRAINT fk_dstreet_province
    FOREIGN KEY (key_province)
    REFERENCES house_procesing.dim_province(id)
);

CREATE TABLE house_procesing.fact_post (
    id INT NOT NULL PRIMARY KEY,
    price FLOAT,
    key_broker INT,
    key_province INT,
    key_house INT,
    status_type varchar(255),
    status_text varchar(255),
    CONSTRAINT fk_post_province
    FOREIGN KEY (key_province)
    REFERENCES house_procesing.dim_province(id),
    CONSTRAINT fk_post_broker
    FOREIGN KEY (key_broker)
    REFERENCES house_procesing.dim_broker(id),
    CONSTRAINT fk_post_house
    FOREIGN KEY (key_house)
    REFERENCES house_procesing.dim_house(id)
)