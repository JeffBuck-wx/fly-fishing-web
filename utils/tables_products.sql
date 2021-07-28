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
CREATE TYPE hook_size AS ENUM ('26', '24', '22', '20', '18', '16', '14', '12', '10', '8', '6', '4', '2', '1', '1/0', '2/0', '4/0');
CREATE TYPE hook_length AS ENUM ('3X short', '2X short', '1X short', '0X standard', '1X long', '2X long', '3X long', '4X long', '6X long');
CREATE TYPE hook_weight AS ENUM ('2X fine', '1X fine', '0X standard', '1X heavy', '2X heavy', '3X heavy');
CREATE TYPE hook_type AS ENUM ('dry', 'nymph', 'scud', 'streamer');
CREATE TYPE eye_type AS ENUM ('down', 'jig 60', 'jig 90', 'straight', 'up');
CREATE TYPE bend_type AS ENUM ('round', 'sproat');
CREATE TYPE shank_type AS ENUM ('curved', 'humped', 'straight');
CREATE TYPE bead_size AS ENUM ('1/16 in', '5/64 in', '3/32 in', '7/64 in', '1/8 in', '5/32 in', '3/16 in', '2 mm', '2.5 mm', '3 mm', '3.5 mm', '4 mm', 'small', 'medium', 'large');
CREATE TYPE bead_material AS ENUM ('nickel', 'tungsten', 'other');
CREATE TYPE bead_shape AS ENUM ('round', 'cone', 'prism', 'fish head', 'nymph head', 'other');
CREATE TYPE bead_hole AS ENUM ('counter sunk', 'slotted', 'other');
CREATE TYPE thread_size AS ENUM ('70 denier', '140 denier', '210 denier', '280 denier', '12/0', '8/0', '6/0');
CREATE TYPE thread_twist AS ENUM ('straight', 'twist', 'braid')
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
    length hook_length NOT NULL,
    weight hook_weight NOT NULL,
    type hook_type,
    eye eye_type,
    bend bend_type,
    shank shank_type,
    PRIMARY KEY (category, id),
    UNIQUE (id),
    CONSTRAINT fk_hook_id
        FOREIGN KEY (category, id)
            REFERENCES materials (category, id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS beads (
    id SERIAL NOT NULL,
    category product_category CHECK (category = 'bead'),
    size bead_size NOT NULL,
    color VARCHAR(32) NOT NULL,
    material bead_material NOT NULL,
    shape bead_shape NOT NULL,
    hole bead_hole NOT NULL,
    PRIMARY KEY (category, id),
    UNIQUE (id),
    CONSTRAINT fk_bead_id
        FOREIGN KEY (category, id)
            REFERENCES material (category, id)
            ON DELETE CASCADE
            ON UPDATE CASCADE 
);

CREATE TABLE IF NOT EXISTS thread (
    id SERIAL NOT NULL,
    category product_category CHECK (category = 'thread'),
    size thread_size NOT NULL,
    color VARCHAR(32) NOT NULL,
    twist thread_twist,
    waxed BOOLEAN DEFAULT 'false',
    PRIMARY KEY (category, id),
    UNIQUE (id),
    CONSTRAINT fk_thread_id
        FOREIGN KEY (category, id)
            REFERENCES material (category, id)
            ON DELETE CASCADE
            ON UPDATE CASCADE 
);
COMMIT;
