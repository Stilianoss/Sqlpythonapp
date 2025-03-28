from connection import get_connection

def insert_book(tittle,category,size,color,material):
    connection = get_connection()
    cursor = connection.cursor()
    sql - "INSERT INTO clothes (tittle,category,size,color,material) VALUES (%s, %s, %s)"
    values = (tittle,category,size,color,material)
    cursor.execute(sql, values)
    connextion.commit()
    print("Ta rouxa paradothikan")
    cursor.close()
    connection.close()

tittle = input("Eisagete titlo")
category = input("Eisagete katigoria")
size = input("Eisagete megethos")
color = input("Eisagete xrwma")
material = input("Eisagete iliko")
    
insert_book(tittle,category,size,color,material)
