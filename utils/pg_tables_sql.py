#!/usr/bin/env python3
import utils_pg
import time



def main():
    # connect to database using utils_pg module
    config = {
        'user': 'jeff',
        'password':'Diana1',
        'host':'localhost',
        'dbname':'fly_fishing'
    }
    db = utils_pg.DBA(config)
    print("Using Database: %s" % db.database)

    # create tables
    db.set_autocommit(True)

    db.close()

    print("Works")
    return

def create_tables_from_script(script):

    return

    
if __name__ == '__main__':
    main()

