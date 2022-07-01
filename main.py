#use python package for serial communication
import serial
#python package to interface with msysql server
import mysql.connector

#read serial from this port (COM8)
port = serial.Serial('COM8',9600)

while(True):
#execute for as long as possible 

    #read from port 
    rfid = port.readline().decode('ascii')
    # print("out of this loop")

    if rfid:
        #update value in mysql table
        mydb = mysql.connector.connect(host="localhost", user="root", database="elevator")
        mycursor = mydb.cursor()
        bill_query = "UPDATE cards_rfid SET status='active' WHERE card_rfid=%s"
        val = rfid
        mycursor.execute(bill_query, val)
        mydb.commit()

# When everything done, release the capture
