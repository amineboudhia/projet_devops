import pymysql

# Connect to the database
def get_connection():

    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    return  connection


db='flask'

try:
    def create_db():

        connection = get_connection()

        with connection:
            with connection.cursor() as cursor:
                sql="CREATE DATABASE "+db+";"
                cursor.execute(sql)
                result = cursor.fetchall()

        return result
    create_db()
except:
    print('la db existe déjà')


connection_db= pymysql.connect(host='localhost',user='root',password='root',db=db,cursorclass=pymysql.cursors.DictCursor)


try:
    def create_table():

        connection = connection_db
        with connection:
            with connection.cursor() as cursor:
                sql="CREATE TABLE Information(Nom varchar(32), Prenom varchar(32), Age int);"
                cursor.execute(sql)
                result = curosr.fetchall()
        return result
    create_table()
except:
    print('la table existe déjà')



