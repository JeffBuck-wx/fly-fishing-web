#!/usr/bin/env python3
import db_admin
import time


def main():
    # connect to database using db_admin module
    config = {
        'user': 'jeff',
        'password':'Diana!2005',
        'host':'localhost'
    }
    db = db_admin.DBA(config)
    db_name = 'fly_fishing'
    
    # drop any existing database
    drop_database(db, db_name)

    # create database
    create_database(db, db_name)

    # create users
    create_user_api(db)
    create_user_dba(db)
    
    # create tables
    create_tables_outings(db)
    create_tables_hooks(db)
    create_tables_beads(db)
    create_tables_thread(db)
    
    # insert data
    insert_eye_types(db)
    insert_hook_types(db)
    insert_bend_types(db)
    insert_shank_types(db)
    insert_hook_lengths(db)
    insert_hook_weights(db)
    insert_thread_materials(db)

    #close
    db.close()

    print("Works")
    return

def drop_database(db, database_name):
    description='Dropping {}.'.format(database_name)
    db.run_query("DROP DATABASE IF EXISTS fly_fishing", query_description=description)
    return

def create_database(db, database_name):
    db.create_database(database_name)
    return

def create_tables_outings(db):
    TABLES = {}
    # table 1
    TABLES["trout_outings"] = (
        "CREATE TABLE IF NOT EXISTS trout_outings ("
        "    trout_outing_id INT(5) NOT NULL AUTO_INCREMENT,"
        "    outing_date DATE NOT NULL,"
        "    location VARCHAR(512) NOT NULL,"
        "    weather VARCHAR(64) NOT NULL,"
        "    description VARCHAR(512),"
        "    brown int(2) NOT NULL DEFAULT 0,"
        "    brook int(2) NOT NULL DEFAULT 0,"
        "    rainbow int(2) NOT NULL DEFAULT 0,"
        "    tiger int(2) NOT NULL DEFAULT 0,"
        "    other int(2) NOT NULL DEFAULT 0,"
        "    PRIMARY KEY (trout_outing_id)"
        ") ENGINE=InnoDB"
    )
    db.create_multiple_tables(TABLES)
    return

def create_tables_hooks(db):
    TABLES = {}
    TABLES['hook_lengths'] = (
        "CREATE TABLE IF NOT EXISTS hook_lengths ("
        "    hook_length_id INT(2) NOT NULL AUTO_INCREMENT,"
        "    length VARCHAR(4) NOT NULL,"
        "    description VARCHAR(32),"
        "  PRIMARY KEY (hook_length_id),"
        "  CONSTRAINT uc_hook_length_name UNIQUE (length)"
        ") ENGINE=InnoDB"
    )
    TABLES['hook_weights'] = (
        "CREATE TABLE IF NOT EXISTS hook_weights ("
        "    hook_weight_id INT(2) NOT NULL AUTO_INCREMENT,"
        "    weight VARCHAR(4) NOT NULL,"
        "    description VARCHAR(32),"
        "  PRIMARY KEY (hook_weight_id),"
        "  CONSTRAINT uc_hook_weight_name UNIQUE (weight)"
        ") ENGINE=InnoDB"
    )   
    TABLES['eye_types'] = (
        "CREATE TABLE IF NOT EXISTS eye_types ("
        "    eye_type_id INT(2) NOT NULL AUTO_INCREMENT,"
        "    type VARCHAR(16) NOT NULL,"
        "    description VARCHAR(512),"
        "  PRIMARY KEY (eye_type_id),"
        "  CONSTRAINT uc_eye_type UNIQUE (type)" 
        ") ENGINE=InnoDB"
    )
    TABLES['hook_types'] = (
        "CREATE TABLE IF NOT EXISTS hook_types ("
        "    hook_type_id INT(2) NOT NULL AUTO_INCREMENT,"
        "    type VARCHAR(16) NOT NULL,"
        "    description VARCHAR(512),"
        "  PRIMARY KEY (hook_type_id),"
        "  CONSTRAINT uc_hook_type UNIQUE (type)" 
        ") ENGINE=InnoDB"
    )
    TABLES['bend_types'] = (
        "CREATE TABLE IF NOT EXISTS bend_types ("
        "    bend_type_id INT(2) NOT NULL AUTO_INCREMENT,"
        "    type VARCHAR(16) NOT NULL,"
        "    description VARCHAR(512),"
        "  PRIMARY KEY (bend_type_id),"
        "  CONSTRAINT uc_bend_type UNIQUE (type)" 
        ") ENGINE=InnoDB"
    )
    TABLES['shank_types'] = (
        "CREATE TABLE IF NOT EXISTS shank_types ("
        "    shank_type_id INT(2) NOT NULL AUTO_INCREMENT,"
        "    type VARCHAR(16) NOT NULL,"
        "    description VARCHAR(512),"
        "  PRIMARY KEY (shank_type_id),"
        "  CONSTRAINT uc_shank_type UNIQUE (type)" 
        ") ENGINE=InnoDB"
    )
    TABLES['hooks'] = (
        "CREATE TABLE IF NOT EXISTS hooks ("
        "    hook_id INT(4) NOT NULL AUTO_INCREMENT,"
        "    brand VARCHAR(16) NOT NULL,"
        "    model VARCHAR(16) NOT NULL,"
        "    length VARCHAR(4) NOT NULL DEFAULT '0X',"
        "    weight VARCHAR(4) NOT NULL DEFAULT '0X',"
        "    eye_type VARCHAR(16) NOT NULL,"
        "    hook_type VARCHAR(16) NOT NULL,"
        "    bend_type VARCHAR(16) NOT NULL,"
        "    shank_type VARCHAR(16) NOT NULL,"
        "    barbless BOOLEAN NOT NULL DEFAULT 0,"
        "  PRIMARY KEY (hook_id),"
        "  CONSTRAINT fk_hook_length"
        "    FOREIGN KEY (length)"
        "      REFERENCES hook_lengths (length)"
        "      ON DELETE RESTRICT"
        "      ON UPDATE CASCADE,"
        "  CONSTRAINT fk_hook_weights"
        "    FOREIGN KEY (weight)"
        "      REFERENCES hook_weights (weight)"
        "      ON DELETE RESTRICT"
        "      ON UPDATE CASCADE,"
        "  CONSTRAINT fk_eye_type"
        "    FOREIGN KEY (eye_type)"
        "      REFERENCES eye_types (type)"
        "      ON DELETE RESTRICT"
        "      ON UPDATE CASCADE,"
        "  CONSTRAINT fk_hook_type"
        "    FOREIGN KEY (hook_type)"
        "      REFERENCES hook_types (type)"
        "      ON DELETE RESTRICT"
        "      ON UPDATE CASCADE,"
        "  CONSTRAINT fk_bend_type"
        "    FOREIGN KEY (bend_type)"
        "      REFERENCES bend_types (type)"
        "      ON DELETE RESTRICT"
        "      ON UPDATE CASCADE,"
        "  CONSTRAINT fk_shank_type"
        "    FOREIGN KEY (shank_type)"
        "      REFERENCES shank_types (type)"
        "      ON DELETE RESTRICT"
        "      ON UPDATE CASCADE"        
        ") ENGINE=InnoDB"
    )
    
    db.create_multiple_tables(TABLES)
    return

def create_tables_beads(db):
    TABLES = {}
    TABLES['hole_types'] = (
        "CREATE TABLE IF NOT EXISTS hole_types ("
        "    hole_type_id INT(2) NOT NULL AUTO_INCREMENT,"
        "    type VARCHAR(16) NOT NULL,"
        "    description VARCHAR(128),"
        "  PRIMARY KEY (hole_type_id)"
        ") ENGINE=InnoDB"
    )
    TABLES['bead_shapes'] = (
        "CREATE TABLE IF NOT EXISTS bead_shapes ("
        "    bead_shape_id INT(2) NOT NULL AUTO_INCREMENT,"
        "    shape VARCHAR(16) NOT NULL,"
        "    description VARCHAR(128),"
        "  PRIMARY KEY (bead_shape_id),"
        "  CONSTRAINT uc_bead_shape_type UNIQUE (shape)"
        ") ENGINE=InnoDB"
    )
    TABLES['bead_material_types'] = (
        "CREATE TABLE IF NOT EXISTS bead_material_types ("
        "    bead_material_id INT(2) NOT NULL AUTO_INCREMENT,"
        "    material VARCHAR(16) NOT NULL,"
        "    description VARCHAR(128),"
        "  PRIMARY KEY (bead_material_id),"
        "  CONSTRAINT uc_bead_material_type UNIQUE (material)"
        ") ENGINE=InnoDB"
    )
    TABLES['beads'] = (
        "CREATE TABLE IF NOT EXISTS beads ("
        "    bead_id INT(4) NOT NULL AUTO_INCREMENT,"
        "    size VARCHAR(8) NOT NULL,"
        "    unit ENUM('standard', 'metric') NOT NULL,"
        "    shape VARCHAR(16) NOT NULL,"
        "    color VARCHAR(16) NOT NULL,"
        "    material VARCHAR(16) NOT NULL,"
        "    hole_type VARCHAR(16) NOT NULL,"
        "  PRIMARY KEY (bead_id),"
        "  CONSTRAINT fk_hole_type"
        "    FOREIGN KEY (hole_type)"
        "      REFERENCES hole_types(type)"
        "      ON DELETE RESTRICT"
        "      ON UPDATE CASCADE,"
        "  CONSTRAINT fk_bead_shape"
        "    FOREIGN KEY (shape)"
        "      REFERENCES bead_shapes(shape)"
        "      ON DELETE RESTRICT"
        "      ON UPDATE CASCADE,"
        "  CONSTRAINT fk_material_type"
        "    FOREIGN KEY (material)"
        "      REFERENCES bead_material_types(material)"
        "      ON DELETE RESTRICT"
        "      ON UPDATE CASCADE"
        ") ENGINE=InnoDB"
    )
    TABLES['bead_to_hook'] = (
        "CREATE TABLE IF NOT EXISTS bead_to_hook ("
        "    bead_to_hook_id INT(4) NOT NULL AUTO_INCREMENT,"
        "    baed_id INT(4) NOT NULL,"    
        "    bead_size VARCHAR(8) NOT NULL,"
        "    hook_size INT(2) NOT NULL,"
        "  PRIMARY KEY (bead_to_hook_id)"
        ") ENGINE=InnoDB"
    )
    
    db.create_multiple_tables(TABLES)
    return

def create_tables_thread(db):
    TABLES = {}
    TABLES['thread_material_types'] = (
        "CREATE TABLE IF NOT EXISTS thread_material_types ("
        "    thread_material_id int(2) NOT NULL AUTO_INCREMENT,"
        "    material VARCHAR(16) NOT NULL,"
        "    description VARCHAR(128),"
        "  PRIMARY KEY (thread_material_id),"
        "  CONSTRAINT uc_thread_material UNIQUE (material)"
        ") ENGINE=InnoDB"
    )
    TABLES['thread_material_types'] = (
        "CREATE TABLE IF NOT EXISTS thread_twist_types ("
        "    thread_twist_id int(2) NOT NULL AUTO_INCREMENT,"
        "    twist VARCHAR(16) NOT NULL,"
        "    description VARCHAR(128),"
        "  PRIMARY KEY (thread_material_id),"
        "  CONSTRAINT uc_thread_twist UNIQUE (twist)"
        ") ENGINE=InnoDB"
    )
    TABLES['thread'] = (
        "CREATE TABLE IF NOT EXISTS thread ("
        "    thread_id INT(4) NOT NULL AUTO_INCREMENT,"
        "    brand VARCHAR(16) NOT NULL,"
        "    color VARCHAR(16) NOT NULL,"
        "    material VARCHAR(16) NOT NULL,"
        "    size VARCHAR(4) NOT NULL,"
        "    waxed BOOLEAN NOT NULL DEFAULT 0,"
        "    twist VARCHAR(16) NOT NULL," 
        "    strength INT(3),"
        "  PRIMARY KEY (thread_id),"
        "  CONSTRAINT fk_thread_material"
        "    FOREIGN KEY (material)"
        "      REFERENCES thread_material_types(material)"
        "      ON DELETE RESTRICT"
        "      ON UPDATE CASCADE,"
        "  CONSTRAINT fk_thread_twist"
        "    FOREIGN KEY (twist_type)"
        "      REFERENCES thread_twist_types(twist)"
        "      ON DELETE RESTRICT"
        "      ON UPDATE CASCADE"
        ") ENGINE=InnoDB"
    )
    db.create_multiple_tables(TABLES)
    return

def insert_eye_types(db):
    query = 'INSERT INTO eye_types(type, description) VALUES (%s, %s)'
    data_sets = [
        ('straight','Eye in-line with the shank. Common with treamers and trailing hook on articulated streamers. Larger hook gap compared to down eye. Arguably better hook-set rate.'),
        ('down','Eye bent in toward hook gap. Typically used with nymphs and soft hackles. Provids a nice bead seat and provides extra room for matieral. Helps prevent crowding of the eye.'),
        ('up','Frequently uses with emergers. Allows larger hook gap on smaller patterns. Larger knots will not interfer with hook-sets.'),
        ('jig-60','60-degree bend. Forces the hook point to ride upright. The hook eye is typically parallel to the hook shank. Popular with competition style nymphing. Can be used with many nymphs, some emergers and streamers.'),
        ('jig-90','90-degree bend. Forces the hook point to ride upright. The hook eye is typically parallel to the hook shank. Popular with competition style nymphing. Can be used with many nymphs, some emergers and streamers.')
    ]
    db.insert_multiple_rows(query, data_sets, 'eye_types')
    return

def insert_hook_types(db):
    query = 'INSERT INTO hook_types(type, description) VALUES (%s, %s)'
    data_sets = [
        ('nymph','Commonly used for nymphs and wet flies, smaller sized suitable for some dry flies.'),
        ('dry fly', 'Thin wire hook appropriate for dry flies.'),
        ('scud', 'Curved shank imitates scud bodies and other nymphs/midges and dries.'),
        ('streamer', 'Longer shanked hooks perfect for streamers.')
    ]
    db.insert_multiple_rows(query, data_sets, 'hook_types')
    return

def insert_bend_types(db):
    query = 'INSERT INTO bend_types(type, description) VALUES (%s, %s)'
    data_sets = [
        ('sproat', 'Hook bend starts out gradaul with a sharper bend closer to the point.'),
        ('round', 'Hood bend curves evenly from start of bend to the barb. Also known as the perfect or classic bend.')
    ]
    db.insert_multiple_rows(query, data_sets, 'bend_types')
    return

def insert_shank_types(db):
    query = 'INSERT INTO shank_types(type, description) VALUES (%s, %s)'
    data_sets = [
        ('straight', 'Hook shank is straigh from eye to the start of the bend.'),
        ('curved', 'Hook bend curves from the eye to the start of bend.'),
        ('humped', 'Slightly curved shank from eye to the start of the bend.')
    ]
    db.insert_multiple_rows(query, data_sets, 'shank_types')
    return

def insert_hook_lengths(db):
    query = 'INSERT INTO hook_lengths(length, description) VALUES (%s, %s)'
    data_sets = [
        ('3XS', '3X short'),
        ('2XS', '2X short'),
        ('1XS', '1X short'),
        ('0X', 'Standard'),
        ('1XL', '1X long'),
        ('2XL', '2X long'),
        ('3XL', '3X long'),
        ('4XL', '4X long'),
        ('6XL', '6X long')
    ]
    db.insert_multiple_rows(query, data_sets, 'hook_lengths')
    return

def insert_hook_weights(db):
    query = 'INSERT INTO hook_weights(weight, description) VALUES (%s, %s)'
    data_sets = [
        ('2XF', '2X fine'),
        ('1XF', '1X fine'),
        ('0X', 'Standard'),
        ('1XH', '1X heavy'),
        ('2XH', '2X heavy'),
        ('3XH', '3X heavy')
    ]
    db.insert_multiple_rows(query, data_sets, 'hook_weights')
    return

def insert_hole_types(db):
    query = 'INSERT INTO hole_types(type, description) VALUES (%s, %s)'
    data_sets = [
        ('counter drilled', 'Standard bead.'),
        ('slotted', 'Designed for jig hooks.'),
        ('other', 'Non-specific hole type.'),
        ('none', 'No hole in bead.')
    ]
    db.insert_multiple_rows(query, data_sets)
    return

def insert_bead_materials(db):
    query = 'INSERT INTO bead_material_types(material, description) VALUES (%s, %s)'
    data_sets = [
        ('Nickel', 'Standard bead material'),
        ('Brass', NULL),
        ('Tungsten', 'For heavier flies, particularly euro-style nymphs'),
        ('Glass', 'Glass bead')
    ]
    db.insert_multiple_rows(query, data_sets)
    return

def insert_thread_materials(db):
    query = 'INSERT INTO thread_material_types(material, description) VALUES (%s, %s)'
    data_sets = [
        ('nylon', 'Common modern thread material. Light, strong, but with more stretch compared to polyester. Available in vibrant colors.'),
        ('polyester', 'Common modern thread material. Light, strong with less streth than nylon.'),
        ('kevlar', 'Super strong, but can be wiry'),
        ('GSP', 'Gel spun polyethylene (GSP). Slightly stronger than Kevlar with a softer feel and texture.'),
        ('silk', NULL)
    ]
    db.insert_multiple_rows(query, data_sets)
    return

def insert_thread_twists(db):
    query = 'INSERT INTO thread_twist_types(twist, description) VALUES (%s, %s)'
    data_sets = [
        ('flat', 'Floss like, un-twisted filaments. Excellent ability to lay flat.'),
        ('mono', 'Single strand thread.'),
        ('twisted', 'Twisted filaments. Usually stronger, but prone to cutting matierals like foam.'),
        ('braid', 'Braided filaments.'),
        ('round', 'Rope like configuration.')
    ]
    db.insert_multiple_rows(query, data_sets)
    return

def create_user_api(db):
    username = 'flyfisher_api'
    db.create_user(username, 'WhitewaterNo.5_451', 'IF NOT EXISTS')
    time.sleep(1)
    db.update_grants(username, 'fly_fishing', ['UPDATE','INSERT','SELECT'])
    db.flush_privileges()
    return

def create_user_dba(db):
    username = 'flyfisher'
    db.create_user(username, 'Alley@1839_Carl', 'IF NOT EXISTS')
    time.sleep(1)
    db.update_grants(username, 'fly_fishing', ['ALL'])
    db.flush_privileges()
    return


    
if __name__ == '__main__':
    main()

