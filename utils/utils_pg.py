#!/usr/bin/env python3
import psycopg2
from psycopg2 import sql



class DBA:
    """Class to contain 449north DBA functions"""

    """Class properties"""
    conn = None
    cursor = None
    config = None
    host = ''
    dbname = ''
    autocommit = False
    verbose = False



    """Class methods"""
    def __init__(self, config, autocommit=False):
        """Initialize the DB connection and cursor"""
        # host
        self.host = config['host']
        
        # database
        try:
            self.database = config['dbname']
        except:
            print('WARNING: database name not set.')
        
        # autocommit
        if autocommit:
            self.autocommit = True

        print("connecting...")
        self.connect_to_database(config)
        self.create_cursor()
        
        try:
            if not config['verbose']:
                self.verbose = True
        except:
            pass


    def connect_to_database(self, config):
        """Return a DB connection"""
        print('HOST: {}'.format(self.host))
        try:
            self.conn  = psycopg2.connect(**config)
            print("OK. Connected to {}".format(config['host']))
            return_value = True
        except psycopg2.Error as err:
            print(f"Error connecting to DB Platform: {err}")
            return_value = False
        return return_value


    def create_cursor(self):
        """Return a DB cursor"""
        try:
            self.cursor = self.conn.cursor()
            return_value = True
        except psycopg2.Error as err:
            print("ERROR. Could not create cursor. %s" % err)
            return_value = False
        return return_value


    def close(self):
        """Close Cursor and Database connection."""
        self.close_cursor()
        self.close_conn()
        return True

    def close_conn(self):
        """Close the Database connection."""
        self.conn.close()
        return True

    def close_cursor(self):
        """Close cursor connection."""
        self.cursor.close()
        return True


    def set_autocommit(self, setting):
        """Set autocommit."""
        ret_val = False
        try:
            self.conn.autocommit = setting
            self.autocommit = setting
            ret_val = True
        except:
            print("ERROR. Could not set autocommit ({})".format(setting))
        return ret_val


    def create_multiple_tables(self, table_dict):
        """Create one or more tables"""
        return_values = []
        for table_name in table_dict:
            table_description = table_dict[table_name]
            return_values.append(self.create_table(table_name, table_description))
        if all(return_values):
            return_value = True
        else:
            return_value = False
        return return_value


    def create_table(self, table_name, table_description):
        """Create a single table"""
        query = table_description
        description = 'Create table: {}'.format(table_name)
        return_value = self.run_query(query, query_description=description)
        return return_value


    def insert_multiple_rows(self, query, data_sets, table_name=''):
        """Execute multiple inserts"""
        
        print(table_name)
        print(query)
        for d in data_sets:
            print(d)
        print("")
        return_value = self.cursor.executemany(query, data_sets)
        return return_value


    def insert_row(self, query, data):
        """Run an insert"""
        description = 'Rows inserted {}'.format(len(data))
        return_value = self.run_query(query, data, description)
        return return_value


    def create_database(self, database, owner, use_database=False):
        """Create a new database"""
        description='Creating database {}.'.format(database)
        query = sql.SQL("CREATE DATABASE {name} WITH OWNER %s").format(
            name=sql.Identifier(database)
        )
        data = (owner, )

        # disable transactions by setting autocommit to true, then revert setting
        ac_value = self.autocommit
        self.set_autocommit(True)
        return_value = self.run_query(query, data, query_description=description)
        self.set_autocommit(ac_value)

        if return_value and use_database:
            self.use_database(database)

        return return_value


    def drop_database(self, database):
        """Drop database given"""
        description = 'Dropping database {}.'.format(database)
        query = sql.SQL("DROP DATABASE IF EXISTS {name}").format(
            name=sql.Identifier(database)
        )
        
        # disable transactions by setting autocommit to true, then revert setting
        ac_value = self.autocommit
        self.set_autocommit(True)
        return_value = self.run_query(query, query_description=description)
        self.set_autocommit(ac_value)
        
        return return_value


    def drop_user(self, username):
        """Drop a USER"""
        description = 'Dropping user ({})'.format(username)
        query = "DROP ROLE IF EXISTS %s;"
        data = (username, )
        return_value = self.run_query(query % data, query_description=description)
        if not return_value:
            print('ERROR. Uanble to drop user {}'.format(username))
            return_value = False
        return return_value


    def create_user(self, username, password, roles=None):
        """Create a USER"""

        # Create the user
        description = 'Creating user ({})'.format(username)
        query = sql.SQL("CREATE ROLE {username} WITH LOGIN PASSWORD %s").format(
            username=sql.Identifier(username)
        )
        data = (password, )
        return_value_user = self.run_query(query, data, query_description=description)

        return return_value_user


    def database_grants(self, database, username, grants):
        """Grant privileges on database."""
        # chech the type of grants
        grants = self.join_list(grants)

        query = "GRANT {} ON DATABASE {} TO {}".format(grants, database, username)
        description = "Granting %s to %s on database %s" % (grants, username, database)

        return_value = self.run_query(query, query_description=description)
        if return_value:
            self.commit()
        return return_value


    def table_grants(self, tables, username, grants, schema='public'):
        """Grant privileges on table(s)."""
        # chech the type of grants
        grants = self.join_list(grants)

        # check tables for 'all'
        if len(tables) == 0:
            target = schema
            query = "GRANT {} ON ALL TABLES IN  SCHEMA {} TO {}".format(grants, schema, username) 
        else:
            tables = self.join_list(tables)
            target = tables
            query = "GRANT {} ON TABLES {} TO {}".format(grants, target, username) 
        description = "Granting %s on %s to %s" % (grants, target, username)

        return_value = self.run_query(query, query_description=description)
        if return_value:
            self.commit()
        return return_value


    def join_list(self, list_or_string):
        """Return a comma deliminated string of list, or orinal argument if it is a string."""
        # chech the type of grants
        # join if it's a list
        if type(list_or_string).__name__ == 'list':
            string = ','.join(list_or_string) 
        else:
            string = list_or_string
        return string


    def set_basic_grants(self, role, database):
        """Set basic grants for database and public tables."""
        self.database_grants(database, role, 'CONNECT')
        self.table_grants([], role, ['SELECT', 'UPDATE', 'INSERT', 'DELETE'])
        return


    def update_grants(self, username, database, grants=[]):
        """Assign limitedgrants to user"""
        # Examine grants
        possible_grants = [
            'INSERT', 'SELECT', 'UPDATE', 'ALL'
            ]
        allowed_grants = []
        for grant in grants:
            if grant.upper() in grants:
                allowed_grants.append(grant.upper())
        grants_string = ','.join(allowed_grants)
        
        # setup and run query
        description = '{} granted {}.'.format(username, grants_string)
        query = 'GRANT %s ON %s.* TO %s@%s;'
        data = (grants_string, database, username, self.host)
        return_value = self.run_query(query % data, query_description=description)
        return return_value


    def run_query(self, query, data=(), query_description=''):
        """Run a query."""
        if len(query_description) > 0:
            query_description = ' {}'.format(query_description)

        try:
            self.cursor.execute(query, data)
            print('OK.{}'.format(query_description))
            return_value = True
        except psycopg2.Error as err:
            print('ERROR. {}\n    {}'.format(query_description, err))
            return_value = False

        if self.autocommit:
            return_value_commit = self.commit()
        else:
            return_value_commit = True # no commit no error

        return return_value and return_value_commit


    def commit(self):
        """Commit DB changes."""
        try:
            self.conn.commit()
            ret_val = True
        except:
            print("Error commiting changes.") 
            ret_val = False
        return ret_val
