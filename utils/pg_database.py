#!/usr/bin/env python3
import utils_pg
import sys



def pg_databases():
    # connect to database using utils_pg module
    db_name = 'postgres'
    config = {
        'user': 'postgres',
        'password':'Minnesota+1991',
        'host':'localhost'
    }
    db = utils_pg.DBA(config)
    
    db.drop_database('fly_fishing')
    db.create_database('fly_fishing', 'fly_master')


if __name__ == '__main__':
    pg_databases()
    sys.exit()
