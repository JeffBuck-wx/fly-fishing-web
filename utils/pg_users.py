#!/usr/bin/env python3
import utils_pg
import sys



def pg_users():
    # connect to database using utils_pg module
    db_name = 'postgres'
    config = {
        'user': 'jeff',
        'password':'Diana1',
        'host':'localhost',
        'dbname': db_name
    }
    db = utils_pg.DBA(config, autocommit=True)

    users = [
        {'username': 'fly_master', 'password': 'Orvis.Hydros.Mend'},
        {'username': 'fly_fisher', 'password': 'WhitewaterNo.5_45'},
    ]

    for user in users:
        db.drop_user(user['username'])  # remove if exists
        db.create_user(**user)


if __name__ == '__main__':
    pg_users()
    sys.exit()

