#!/usr/bin/env python3
import flyfishing_db_utils
import time


def main():
    # connect to database using flyfishing_db_utils module
    db_name = 'fly_fishing'
    config = {
        'user': 'jeff',
        'password':'Diana1',
        'host':'localhost',
        'database': db_name,
        'autocommit': True
    }
    db = flyfishing_db_utils.DBA(config)

    
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


def insert_eye_types(db):
    query = 'INSERT INTO eye_types(type, description) VALUES (?, ?)'
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
    query = "INSERT INTO fly_fishing.hook_weights(weight, description) VALUES (?, ?)"
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
        ('Brass', None),
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
        ('silk', None)
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

