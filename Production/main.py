from machine import Pin, PWM, I2C
from time import ticks_ms, sleep
import dht
import network
import urequests
import json

from lcd_i2c import LCD


# ==============================
# CONFIGURACION
# ==============================

WIFI_SSID = "ALTICE_41B28D"
WIFI_PASSWORD = "LaPrincesaDiana141522"

BOT_TOKEN = "8983116105:AAGkSrKdVMOlISLeEFoaxeoELIxvkAHry2Q"
CHAT_ID = "6588579247"


# ==============================
# HARDWARE
# ==============================

pir = Pin(15, Pin.IN)

led = Pin(16, Pin.OUT)

buzzer = PWM(Pin(17))
buzzer.duty_u16(0)

dht_sensor = dht.DHT11(Pin(18))


# LCD

i2c = I2C(
    0,
    sda=Pin(0),
    scl=Pin(1),
    freq=400000
)

lcd = LCD(i2c, 0x27)


# ==============================
# ESTADO DEL SISTEMA
# ==============================

intruder = False
guardian_mode = True
motion_sent = False

wifi_ok = False
wifi_restored = False


# LED

last_led = 0
led_state = 0


# LCD

last_lcd = 0
lcd_mode = 0


# DHT

last_dht = 0
temp = 0
hum = 0


# Alarma

alarm_step = 0
last_alarm = 0


# Telegram

last_update = 0


# ============================================================
# RECONEXION AUTOMATICA WIFI (OPCIONAL)
#
# Si alguna vez sospechas que esta parte da problemas,
# puedes eliminar:
#
# 1) Esta variable.
# 2) El bloque de RECONEXION del while principal.
#
# El satelite seguira funcionando:
#  - PIR
#  - DHT11
#  - LCD
#  - LED
#  - BUZZER
#
# Solo perdera la reconexion automatica de Telegram.
# ============================================================

last_wifi_check = 0



# ==============================
# INICIO LIMPIO
# ==============================

led.value(0)



# ==============================
# WIFI
# ==============================

def connect_wifi():

    wlan = network.WLAN(network.STA_IF)

    wlan.active(True)

    if wlan.isconnected():

        return True


    print("Connecting WiFi...")


    try:

        wlan.connect(
            WIFI_SSID,
            WIFI_PASSWORD
        )

    except:

        return False


    timeout = 10


    while not wlan.isconnected() and timeout > 0:

        print(".", end="")

        sleep(1)

        timeout -= 1


    if wlan.isconnected():

        print("\nWiFi OK")
        print(wlan.ifconfig())

        return True


    print("\nWiFi FAILED")

    return False




# ==============================
# TELEGRAM
# ==============================

def send_telegram(message):

    if not wifi_ok:

        return


    url = (
        "https://api.telegram.org/bot"
        + BOT_TOKEN
        + "/sendMessage"
    )


    payload = (
        "chat_id="
        + CHAT_ID
        + "&text="
        + message.replace(" ", "%20")
        .replace("\n", "%0A")
    )


    try:

        response = urequests.post(
            url,
            headers={
                "Content-Type":
                "application/x-www-form-urlencoded"
            },
            data=payload
        )

        print(response.text)

        response.close()


    except Exception as e:

        print("Telegram:", e)




def get_telegram():

    global last_update


    if not wifi_ok:

        return


    url = (
        "https://api.telegram.org/bot"
        + BOT_TOKEN
        + "/getUpdates?offset="
        + str(last_update + 1)
    )


    try:

        response = urequests.get(url)

        data = response.json()

        response.close()


        if data["ok"]:

            for update in data["result"]:

                last_update = update["update_id"]

                if "message" in update:

                    handle_command(
                        update["message"]["text"]
                    )

    except:

        pass
    
    # ==============================
# COMANDOS TELEGRAM
# ==============================

def handle_command(command):

    global guardian_mode


    if command == "/activar":

        guardian_mode = True

        send_telegram(
            "Guardian ACTIVADO"
        )


    elif command == "/desactivar":

        guardian_mode = False

        send_telegram(
            "Guardian DESACTIVADO"
        )


    elif command == "/status":

        if guardian_mode:

            mode = "VIGILANDO"

        else:

            mode = "NO VIGILO"


        send_telegram(
            "Guardian Status\n"
            "Modo: " + mode +
            "\nTemp: " + str(temp) + "C" +
            "\nHum: " + str(hum) + "%"
        )



# ==============================
# BUZZER
# ==============================

def alarma_intruso(now):

    global alarm_step
    global last_alarm


    if now - last_alarm < 100:

        return


    last_alarm = now


    if alarm_step in [0,2,4]:

        buzzer.freq(2000)

        buzzer.duty_u16(30000)

    else:

        buzzer.duty_u16(0)


    alarm_step += 1


    if alarm_step >= 10:

        alarm_step = 0




# ==============================
# DHT11
# ==============================

def read_dht():

    global temp
    global hum


    try:

        dht_sensor.measure()

        temp = dht_sensor.temperature()

        hum = dht_sensor.humidity()

    except:

        pass




# ==============================
# ARRANQUE
# ==============================

print("==============================")
print("     SATELIDOM ESTEISSY")
print("   Guardian Satellite v1.1")
print("==============================")


print("[OK] LCD Display")
print("[OK] PIR Sensor")
print("[OK] DHT11 Sensor")
print("[OK] Status LED")
print("[OK] Passive Buzzer")


wifi_ok = connect_wifi()


if wifi_ok:

    print("[OK] WiFi Module")

    send_telegram(
        "Guardian ONLINE\n"
        "Modo: PROTEGIENDO"
    )

else:

    print("LOCAL MODE")


sleep(2)

read_dht()

print("Ready for operation.")

# ==============================
# LOOP PRINCIPAL
# ==============================

while True:

    now = ticks_ms()


    # ============================================================
    # RECONEXION AUTOMATICA WIFI (OPCIONAL)
    #
    # Si el WiFi se pierde, el satelite sigue funcionando
    # normalmente (PIR, LCD, DHT11, LED y buzzer).
    #
    # Cada 30 segundos intenta recuperar la conexion.
    #
    # SI ALGUNA VEZ ESTA PARTE DA PROBLEMAS:
    # Borra TODO este bloque.
    # El satelite seguira funcionando en modo local.
    # ============================================================

    if not wifi_ok:

        if now - last_wifi_check >= 30000:

            last_wifi_check = now

            if connect_wifi():

                wifi_ok = True

                send_telegram(
                    "Guardian ONLINE\n"
                    "WiFi Restored"
                )

    # ============================================================



    # --------------------------
    # TELEGRAM
    # --------------------------

    get_telegram()



    # --------------------------
    # PIR
    # --------------------------

    if guardian_mode:

        if pir.value():

            sleep(0.03)

            if pir.value():

                intruder = True

        else:

            intruder = False

    else:

        intruder = False



    # --------------------------
    # ALERTA TELEGRAM
    # --------------------------

    if intruder and not motion_sent:

        if wifi_ok:

            send_telegram(
                "ALERTA\n"
                "Movimiento detectado"
            )

        motion_sent = True


    if not intruder:

        motion_sent = False



    # --------------------------
    # LED
    # --------------------------

    if intruder:

        led_speed = 10

    else:

        led_speed = .25


    if now - last_led > led_speed:

        led_state = not led_state

        led.value(led_state)

        last_led = now



    # --------------------------
    # BUZZER
    # --------------------------

    if intruder:

        alarma_intruso(now)

    else:

        buzzer.duty_u16(0)

        alarm_step = 0



    # --------------------------
    # DHT11
    # --------------------------

    if now - last_dht > 3000:

        read_dht()

        last_dht = now



    # --------------------------
    # LCD
    # --------------------------

    if now - last_lcd > 2500:

        lcd.clear()

        if lcd_mode == 0:

            lcd.putstr("   SATELIDOM")

            lcd.move_to(0,1)

            lcd.putstr("   ESTEISSY")

        else:

            lcd.putstr(
                "Temp: {}C".format(temp)
            )

            lcd.move_to(0,1)

            lcd.putstr(
                "Hum: {}%".format(hum)
            )

        lcd_mode = 1 - lcd_mode

        last_lcd = now