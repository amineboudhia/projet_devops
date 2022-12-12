import pymysql

connection = pymysql.connect(host='localhost',user='root',password='root',db='flask',cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

def inserto(nom,prenom,age):
	sql = "INSERT INTO `Information` (`Nom`, `Prenom`, `Age`) VALUES (%s, %s, %s)"
	cursor.execute(sql, (nom, prenom, age))
	connection.commit()
	return 1

def get_data():
	cursor.execute('SELECT * FROM `Information`')
	data = cursor.fetchall()
	return data


