CREATE TABLE IF NOT EXISTS outings (
    outing_id SERIAL NOT NULL,
    outing_date DATE NOT NULL,
    location VARCHAR(512) NOT NULL,
    weather VARCHAR(64) NOT NULL,
    description VARCHAR(512),
    PRIMARY KEY (outing_id)
);

CREATE TABLE IF NOT EXISTS fish (
    fish_id SERIAL NOT NULL,
    outing_id INT NOT NULL,
    species VARCHAR(32) NOT NULL,
    count INT DEFAULT 0,
    length INT,
    PRIMARY KEY (fish_id),
    CONSTRAINT fk_outing_id
        FOREIGN KEY (outing_id)
            REFERENCES outings (outing_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);
COMMIT;

CREATE TYPE product_category AS ENUM ('bead', 'dubbing', 'hook', 'thread', 'wire');
CREATE TYPE hook_size AS ENUM ('3X short', '2X short', '1X short', '0X standard', '1X long', '2X long', '3X long', '4X long', '6X long');
CREATE TYPE hook_weight AS ENUM ('2X fine', '1X fine', '0X standard', '1X heavy', '2X heavy', '3X heavy');
CREATE TYPE hook_type AS ENUM ('dry', 'nymph', 'scud', 'streamer');
CREATE TYPE eye_type AS ENUM ('down', 'jig 60', 'jig 90', 'straight', 'up');
CREATE TYPE bend_type AS ENUM ('round', 'sproat');
CREATE TYPE shank_type AS ENUM ('curved', 'humped', 'straight');
COMMIT;

CREATE TABLE IF NOT EXISTS materials (
    id SERIAL NOT NULL,
    category product_category NOT NULL,
    brand VARCHAR(64) NOT NULL,
    model VARCHAR(64) NOT NULL,
    description VARCHAR(512),
    PRIMARY KEY (category, id),
    UNIQUE (id)
);

CREATE TABLE IF NOT EXISTS hooks (
    id SERIAL NOT NULL,
    category product_category CHECK (category = 'hook'),
    size hook_size NOT NULL,
    weight hook_weight NOT NULL,
    type hook_type,
    eye eye_type NOT NULL,
    bend bend_type,
    shank shank_type,
    PRIMARY KEY (category, id),
    CONSTRAINT fk_hook_id
        FOREIGN KEY (category, id)
            REFERENCES materials (category, id)
            ON DELETE CASCADE
);
COMMIT;
