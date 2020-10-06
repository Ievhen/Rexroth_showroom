# coding: utf-8


import numpy as np
import sys
import mysql.connector
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt
import json


MQTT_BROKER_IP = '192.168.99.90'
MQTT_BROKER_PORT = 1883
MQTT_TOPIC = 'SERVICES/DELTA/BOX'
    
TAG = "TAG02"
publish.single('SERVICES/DELTA/BOX', TAG ,hostname = MQTT_BROKER_IP,port = MQTT_BROKER_PORT)