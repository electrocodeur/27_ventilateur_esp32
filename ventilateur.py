from machine import Pin
import time

relais_ventilateur = Pin(23, Pin.OUT) # Règle la broche D23 de la carte ESP32 en mode sortie

while True:
    relais_ventilateur.value(0) # faire tourner le ventilateur
    time.sleep(5)
    
    relais_ventilateur.value(1) # faire arrêter le ventilateur
    time.sleep(5)
