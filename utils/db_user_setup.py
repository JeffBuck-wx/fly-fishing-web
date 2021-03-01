#!/usr/bin/env python3
import flyfishing_db_utils
import sys


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
    

    users = [
        {'username': 'admin', 'password': 'Dan+The+Man-2014', 'hostname': '%', 'database': '*', 'grants': 'Superuser'},
        {'username': 'fly_master', 'password': 'Orvis.Hydros.Mend', 'hostname': '%', 'database': db_name, 'grants': 'Superuser'},
        {'username': 'flyfisher', 'password': 'WhitewaterNo.5_45', 'hostname': '%', 'database': db_name, 'grants': 'User'},
        {'username': 'fly_api', 'password': 'Alley@1839_Carl', 'hostname': '%', 'database': db_name, 'grants': 'User'}
    ]

    db.drop_user('flyfisher')

    for user in users:
        db.create_user(**user)


if __name__ == '__main__':
    main()
    sys.exit()

#query = ("SELECT User FROM mysql.user;")
#cursor.execute(query)
#
#for (User) in cursor:
#    print("User: {}".format(User[0]))
