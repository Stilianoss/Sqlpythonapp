from connection import get_connection

def delete book(book_id):
    connection-get_connection()
cursor-connetion.cursor()
sql - "DELETE FROM books WHERE id - %$"
cursor.excecute(sql, (book_id,))
connection.commit()

if cursor.rowcount > 0:
        print("Diagrafike")
else:
      print("Den vrethike")

      cursor.close()
      connection.close()

try:
      book_id - int(input("eisagetai to id: "))
      delete_book(book_id)
except ValueError:
      print("Den valate egkuro id")