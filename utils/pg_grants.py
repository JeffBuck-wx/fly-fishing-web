#!/usr/bin/env python3
import utils_pg
import sys



def pg_grants():
    # connect to database using utils_pg module
    config = {
        'user': 'postgres',
        'password':'Minnesota+1991',
        'host':'localhost'
    }
    db = utils_pg.DBA(config)
    
    # database
    dbname   = 'fly_fishing'

    # basic priviliges for programmatic access
    username = 'fly_fisher'
    db.set_basic_grants(username, dbname)


    # higher priviliges for admin access
    username = 'fly_master'
    # grant connection privileges
    grants_list = ['CONNECT', 'CREATE', 'TEMP']
    db.database_grants(dbname, username, grants_list)
    # grant priviledges on tables
    grants_list = ['ALL']
    tables = []
    schema='public'
    db.table_grants(tables, username, grants_list, schema)

    # close up
    db.close()



if __name__ == '__main__':
    pg_grants()
    sys.exit()
