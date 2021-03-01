#!/usr/bin/env python3
import mariadb


class DBA:
    """Class to contain 449north DBA functions"""

    """Class properties"""
    conn = None
    cursor = None
    config = None
    host = ''
    database = ''
    autocommit = False
    verbose = False



    """Class methods"""
    def __init__(self, config):
        """Initialize the DB connection and cursor"""
        # host
        self.host = config['host']
        
        # database
        try:
            self.database = config['database']
        except:
            print('WARNING: database name not set.')
        
        # autocommit
        try:
            if isinstance(config['autocommit'], bool):
                self.autocommit = config['autocommit']
        except:
            # leave it False/default
            pass


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
            self.conn  = mariadb.connect(**config)
            print("OK. Connected to {}".format(config['host']))
            return_value = True
        except mariadb.Error as err:
            print(f"Error connecting to MariaDB Platform: {err}")
            #if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            #    print("ERROR: Incorrect username or password")
            #elif err.errno == errorcode.ER_BAD_DB_ERROR:
            #    print("ERROR: Database does not exist")
            #else:
            #    print(err)
            return_value = False
        return return_value



    def create_cursor(self):
        """Return a DB cursor"""
        try:
            self.cursor = self.conn.cursor()
            return_value = True
        except mariadb.Error as err:
            print("ERROR. Could not create cursor.")
            return_value = False
        return return_value



    def close(self):
        """Close Database connection."""
        self.close_cursor()
        self.conn.close()
        return True



    def close_cursor(self):
        """Close cursor."""
        self.cursor.close()
        return True



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
        description = 'Rows inserted'.format(len(data))
        return_value = self.run_query(query, data, description)
        return return_value



    def create_database(self, database_name, char_set='utf8', use_database=True):
        """Create a new database"""
        description='Creating {}.'.format(database_name)
        query = "CREATE DATABASE IF NOT EXISTS %s DEFAULT CHARACTER SET %s;"
        data = (database_name, char_set)
        return_value = self.run_query(query % data, query_description=description)

        if return_value:
            self.use_database(database_name)

        return return_value



    def use_database(self, database):
        """Use database given"""
        self.database = database
        description = 'Using {}.'.format(database)
        query = "USE %s;"
        data = (database,)
        return_value = self.run_query(query % data, query_description=description)
        return return_value


    def drop_user(self, username):
        """Drop a USER"""
        description = 'Dropping user ({})'.format(username)
        query = "DROP USER IF EXISTS %s;"
        data = (username)
        return_value = self.run_query(query % data, query_description=description)
        if not return_value:
            print('ERROR. Uanble to drop user {}'.format(username))
            return_value = False
        return return_value


    def create_user(self, username, password, hostname, database, grants):
        """Create a USER"""
        grants = grants.upper()
        
        # Create the user
        description = 'Creating user ({})'.format(username)
        query = "CREATE USER IF NOT EXISTS '%s'@'%s' IDENTIFIED BY '%s'"
        data = (username, hostname, password)
        return_value_user = self.run_query(query % data, query_description=description)
        print(query % data)

        # Set grants
        description = 'Updating grants on {} ({})'.format(database, username)
        if grants == 'SUPERUSER':
            query = "GRANT ALL ON %s.* TO %s@'%s'"
        elif grants == 'ADMIN':
            query = "GRANT ALL ON %s.* TO %s@'%s' WITH GRANT OPTION"
        else:
            query = "GRANT INSERT,UPDATE,SELECT ON %s.* TO %s@'%s'"
        data = (database, username, hostname)
        return_value_grant = self.run_query(query % data, query_description=description)
        print(query % data)

        # Flush privileges
        return_value_flush = self.flush_privileges()

        return return_value_user and return_value_grant and return_value_flush



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



    def flush_privileges(self):
        """Flush privileges."""
        return self.run_query('FLUSH PRIVILEGES', query_description='Flush privileges.')



    def run_query(self, query_string, data=(), query_description=''):
        """Run a query."""
        if len(query_description) > 0:
            query_description = ' {}'.format(query_description)
        if self.verbose:
            print('QUERY: {}'.format(query_string % data))
            if len(data) > 0:
                print('DATA: {}'.format(data))
        
        try:
            self.cursor.execute(query_string, data)
            print('OK.{}'.format(query_description))
            return_value = True
        except mariadb.Error as err:
            print('ERROR. {}\n    {}'.format(query_description, err))
            return_value = False
        return return_value
