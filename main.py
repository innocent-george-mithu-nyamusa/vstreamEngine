import serial
import mysql.connector


port = serial.Serial('COM8',9600)

while(True):
#
    rfid = port.readline().decode('ascii')
    # print("out of this loop")

    if rfid:

        mydb = mysql.connector.connect(host="localhost", user="root", database="elevator")
        mycursor = mydb.cursor()
        bill_query = "UPDATE cards_rfid SET status='active' WHERE card_rfid=%s"
        val = rfid
        mycursor.execute(bill_query, val)
        mydb.commit()

# When everything done, release the capture
