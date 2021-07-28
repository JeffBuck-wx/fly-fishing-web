#!/usr/bin/env python3
import utils_pg
import sys



def pg_users():
    # connect to database using utils_pg module
    config = {
        'user': 'postgres',
        'password':'Minnesota+1991',
        'host':'localhost'
    }
    db = utils_pg.DBA(config, autocommit=True)

    users = [
        {'username': 'fly_fisher', 'password': 'WhitewaterNo.5_45'},
    ]

    for user in users:
        db.create_user(**user)

    # close up
    db.close()


if __name__ == '__main__':
    pg_users()
    sys.exit()

