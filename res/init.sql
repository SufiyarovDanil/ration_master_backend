CREATE TABLE product (
        pk_id UUID NOT NULL, 
        name VARCHAR(64) NOT NULL, 
        calorie SMALLINT NOT NULL,
        protein SMALLINT NOT NULL,
        weight SMALLINT NOT NULL,
        carbohydrate SMALLINT NOT NULL,
        PRIMARY KEY (pk_id),
        UNIQUE (name)
)

CREATE TABLE ration (
        pk_id UUID NOT NULL,
        fk_product_id UUID NOT NULL,
        product_gramm SMALLINT NOT NULL,
        meal_time SMALLINT NOT NULL,
        time_to_eat TIMESTAMP NOT NULL,
        PRIMARY KEY (pk_id),
        FOREIGN KEY(fk_product_id) REFERENCES product (pk_id) ON DELETE SET NULL
)
