import mysql.connector



class Jedzenie:
    @staticmethod
    def return_table():
        tab=[]
        mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       password='password1234',
                                       db='jedzenie')
        cur = mydb.cursor()
        cur.execute("SELECT * FROM baza_jedzenia")

        for row in cur.fetchall():
            tab.append(row)
        cur.close()
        mydb.close()
        return tab

    def add_product(name, amount):
        connection = mysql.connector.connect(host='localhost',
                                             database='jedzenie',
                                             user='root',
                                             password='password1234')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO baza_jedzenia (nazwa,ilosc) 
                                    VALUES (%s, %s) """

        recordTuple = (name, amount)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        cursor.close()
        connection.close()

    def delete_product(id):
        connection = mysql.connector.connect(host='localhost',
                                             database='jedzenie',
                                             user='root',
                                             password='password1234')
        cursor = connection.cursor()
        mySql_delete_query = """DELETE FROM baza_jedzenia where id=%s"""

        cursor.execute(mySql_delete_query, (id,))
        connection.commit()
        cursor.close()
        connection.close()

    def update_product_amount(id, amount):
        connection = mysql.connector.connect(host='localhost',
                                             database='jedzenie',
                                             user='root',
                                             password='password1234')
        cursor = connection.cursor()
        mySql_update_query = """UPDATE baza_jedzenia SET ilosc = %s WHERE id=%s;"""

        recordTuple = (amount, id)
        cursor.execute(mySql_update_query, recordTuple)
        connection.commit()
        cursor.close()
        connection.close()
