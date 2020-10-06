# coding: utf-8


import numpy as np
import mysql.connector
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt
import json

def db_connect(ip, username, password, db):
    return mysql.connector.connect(
        host=ip,
        user=username,
        password=password,
        database=db
    )

#bezpieczna wysokość nad pudelkiem/magazynem
Z_jump = 100;

#DataBase Box real coordinates information [matrix]
#(1, '[1,1]', 1, 'Red') -> ID, [row, column], prog, 'RED'
db = db_connect('192.168.99.90', 'iotuser', 'iotuser', 'showroom')
cursor = db.cursor()
sql = f"SELECT * FROM showroom.delta_box_mat"
cursor.execute(sql)

myresult = cursor.fetchall()
mytuple = []
Box_mat = []
for j in range(0,len(myresult[0])-1):
    for i in range(1,len(myresult[0])):
        mytuple.append(tuple(map(int, myresult[j][i].split(','))))
Box_mat = mytuple 
Box_mat = np.array_split(Box_mat, len(myresult[0])-1)

#DataBase real coordinates warehouse information
db = db_connect('192.168.99.90', 'iotuser', 'iotuser', 'showroom')
cursor = db.cursor()
sql = f"SELECT * FROM showroom.delta_warehouse_mat WHERE (`row` = '0')"
cursor.execute(sql)
myresult = cursor.fetchall()
mytuple = []
for i in range(1,len(myresult[0])):
    mytuple.append(tuple(map(int, myresult[0][i].split(','))))
Warehouse_mat = mytuple 


while True:
    #komunikacja broker MQTT
    MQTT_BROKER_IP = '192.168.99.90'
    MQTT_BROKER_PORT = 1883
    #MQTT_TOPIC = 'SERVICES/DELTA/BOX'
    
    #subscribe to DELTA status Jeśli 210 to delta gotowa idź dalej sprawdzenie TAG
    #czekanie na odpowiedz PLC Delty z potwierdzeniem dostarczenia kulki
    Delt_Stat = ""
    while Delt_Stat != "210":
        Delt_Stat = subscribe.simple('LINE/DELTA/STATUS', hostname=MQTT_BROKER_IP)
    
    #subscribe to RFID TAG
    Tag = subscribe.simple('LINE/RFID/RFID01/DELTA', hostname=MQTT_BROKER_IP)   
    
    #Odczytanie jaki Tag/jaka paletka jest akrualnie nad modulem z robotem Delta
    Tag = Tag.payload.decode("Utf-8")
    #DataBase ->informacja o konfiguracji pudelka na podstawie informacji z bazy danych
    #(1, '[1,1]', 1, 'Red') -> ID, [row, column], prog, 'RED'
    db = db_connect('192.168.99.90', 'iotuser', 'iotuser', 'showroom')
    cursor = db.cursor()
    sql = f"SELECT * FROM showroom.production_order_decomposition WHERE (status = '200' AND palette_id = '{Tag}')"
    cursor.execute(sql)

    #input
    #box ID -> from MQTT RFID
    ID_b = cursor.fetchall()[0][3]

    #row, column -> From MySql -> based on the correct box ID
    Mat = [1,1]
    #color {"Red","Blue","Empty", "Green","Yellow"} -> From MySql -> based on the correct box ID
    color = ""
    #Init Matrix BOX
    Mat_Box = []
    #Init Matrix Warehouse
    Mat_Warh = []

    #DataBase Connection Box information
    #(1, '[1,1]', 1, 'Red') -> ID, [row, column], prog, 'RED'
    db = db_connect('192.168.99.90', 'iotuser', 'iotuser', 'showroom')
    cursor = db.cursor()
    sql = f"SELECT * FROM showroom.delta WHERE id = '{ID_b}'"
    cursor.execute(sql)
    #odczytanie informacji o pudelku z paletki
    myresult = cursor.fetchall()
    
    
    for i in range(len(myresult)):
        #szczegółowa informacja o pudelku, KOLOR
        color = myresult[i][3]
        #Zapytanie o konkretny kolor skryptu z siecia neuronowa
        request = color
        print("Sending request %s …" % request)
        publish.single('SERVICES/DELTA/COLOR/REQ', request ,hostname = MQTT_BROKER_IP,port = MQTT_BROKER_PORT) 

        #  Get the reply. / Czekanie na odpowiedź na której kolumnie znajduje sie kulka o porzadanym kolorze
        msg = subscribe.simple('SERVICES/DELTA/COLOR/ANS', hostname=MQTT_BROKER_IP)
        msg = msg.payload.decode()
        print("Received reply %s [ %s ]" % (request, msg))

        #Output
        #array[point above warehouse -> message from Server_Kulki
        #point above desire object 
        #point above warehouse
        #point above box -> Mat
        #point in box 
        #point above box]
        
        WH_End = Warehouse_mat[int(msg)]
        pos = myresult[i][1].split(',')
        Box_End = Box_mat[int(pos[1])][int(pos[0])]
        #Generowanie ścieżki z 6 punktów, pobranie kulki o konkretnym kolorze
        Path = {
          "1": str(WH_End[0])+","+str(WH_End[1])+","+str(WH_End[2]-Z_jump),
          "2": str(WH_End[0])+","+str(WH_End[1])+","+str(WH_End[2]),
          "3": str(WH_End[0])+","+str(WH_End[1])+","+str(WH_End[2]-Z_jump),
          "4": str(Box_End[0])+","+str(Box_End[1])+","+str(Box_End[2]-Z_jump),
          "5": str(Box_End[0])+","+str(Box_End[1])+","+str(Box_End[2]),
          "6": str(Box_End[0])+","+str(Box_End[1])+","+str(Box_End[2]-Z_jump)
        }

        # convert into JSON:
        y = json.dumps(Path)
        print(y)
        #wysłanie informacji do PLC Delty, JSON z konfiguracją punktów
        publish.single('LINE/DELTA/PATH', y ,hostname = MQTT_BROKER_IP,port = MQTT_BROKER_PORT)
        

        #print(f"Pozycja pierwsza {Path[0]} nad magazynem \nDruga pozycja    {Path[1]}       magazyn \nTrzecia pozycja  {Path[2]} nad magazynem \nCzwarta pozycja  {Path[3]} nad pudełkiem \nPiąta pozycja    {Path[4]}       pudełko \nSzósta pozycja   {Path[5]} nad pudełkiem")
        #czekanie na odpowiedz PLC Delty z potwierdzeniem dostarczenia kulki
        Delt_Stat = ""
        while Delt_Stat != "210":
            Delt_Stat = subscribe.simple('LINE/DELTA/STATUS', hostname=MQTT_BROKER_IP)

    publish.single('LINE/DELTA/REQ',"DONE",hostname = MQTT_BROKER_IP,port = MQTT_BROKER_PORT)