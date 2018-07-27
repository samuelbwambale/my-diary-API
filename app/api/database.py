import psycopg2
from pprint import pprint


class Database:

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname = mydiary_db user=postgres password=postgres host=localhost port =5432")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            pprint("Connection successfull")
        except:
            pprint("Connection to db has failed.")