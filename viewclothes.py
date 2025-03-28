from connection import get_connection

def view_books():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM clothes"
    cursor.execute(sql)
    clothes = cursor.fetchall()

    if clothes:
        print("Kathgories rouxwn")
        for clothe in clothes:
            print(f"Id: {clothe[0]}, tittle: {clothe[1]}, category: {clothe[2]}, size: {clothe[3]}, color: {clothe[4]}, material: {clothe[5]}")
    else:
         print("den yparxoun rouxa")
    cursor.close()
    connection.close()

view_clothes()
         