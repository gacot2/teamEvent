import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    sql_create_categoryTypes_table = """ CREATE TABLE IF NOT EXISTS categoryTypes(
                                            categoryTypeId int NOT NULL,
                                            categoryType text NOT NULL
                                        ); """

    sql_create_category_table = """CREATE TABLE IF NOT EXISTS category(
                                            categoryId integer PRIMARY KEY,
                                            categoryName text NOT NULL,
                                            categoryType text
                                            FOREIGN KEY (categoryTypeId) REFERENCES categoryType (categoryTypeId)
                                        );"""

    sql_create_adress_table = """CREATE TABLE IF NOT EXISTS adress(
                                            adressId integer PRIMARY KEY,
                                            streetNumber integer NOT NULL,
                                            appNumber text,
                                            roadName text NOT NULL,
                                            zipCode text NOT NULL,
                                            country text NOT NULL,
                                            province text NOT NULL);"""

    sql_create_events_table = """CREATE TABLE IF NOT EXISTS events(
                                            eventId integer PRIMARY KEY,
                                            eventName text NOT NULL,
                                            startDate date NOT NULL,
                                            endDate date NOT NULL,
                                            creationDate date NOT NULL,
                                            eventStatus text NOT NULL,
                                            vote integer
                                            FOREIGN KEY (adressId) REFERENCES adress (adressId)
                                            FOREIGN KEY (categoryId) REFERENCES category (categoryId)
                                            );"""
    
    sql_create_user_table = """CREATE TABLE IF NOT EXISTS user(
                                            userId integer PRIMARY KEY,
                                            firstName text NOT NULL,
                                            lastName text NOT NULL,
                                            userPassword text NOT NULL,
                                            email text NOT NULL,
                                            creationDate date NOT NULL,
                                            dateOfBirth date NOT NULL,
                                            FOREIGN KEY (adressId) REFERENCES adress (adressId)
                                            );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create categoryTypes table
        create_table(conn, sql_create_categoryTypes_table)

        # create category table
        create_table(conn, sql_create_category_table)

        # create adress table
        create_table(conn, sql_create_adress_table)

        # create events table
        create_table(conn, sql_create_events_table)

        # create user table
        create_table(conn, sql_create_user_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()