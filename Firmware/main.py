from machine import Pin, PWM, I2C
from time import ticks_ms, sleep
import dht
from lcd_i2c import LCD


# ---------------- SENSORES ----------------

pir = Pin(15, Pin.IN)

led = Pin(16, Pin.OUT)

buzzer = PWM(Pin(17))

dht_sensor = dht.DHT11(Pin(18))


# ---------------- LCD ----------------

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

lcd = LCD(i2c, 0x27)


# ---------------- VARIABLES ----------------

intruder = False

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


# ---------------- BUZZER ----------------

def alarma_intruso(now):
    global alarm_step, last_alarm

    if now - last_alarm < 100:
        return

    last_alarm = now

    # beep - pausa - beep - pausa - beep
    if alarm_step in [0, 2, 4]:

        buzzer.freq(2000)
        buzzer.duty_u16(30000)

    else:
        buzzer.duty_u16(0)


    alarm_step += 1


    if alarm_step >= 10:
        alarm_step = 0



# ---------------- DHT ----------------

def read_dht():

    global temp, hum

    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()

    except:
        pass



print("SATELITE GUARDIAN ONLINE")


# ---------------- LOOP PRINCIPAL ----------------

while True:

    now = ticks_ms()


    # -------- PIR --------

    if pir.value():

        sleep(0.03)

        if pir.value():
            intruder = True

    else:
        intruder = False



    # -------- LED SIEMPRE ACTIVO --------

    if intruder:
        led_speed = 100     # alerta
    else:
        led_speed = 600     # normal


    if now - last_led > led_speed:

        led_state = not led_state

        led.value(led_state)

        last_led = now



    # -------- BUZZER --------

    if intruder:

        alarma_intruso(now)

    else:

        buzzer.duty_u16(0)
        alarm_step = 0



    # -------- DHT11 --------

    if now - last_dht > 3000:

        read_d_h_t = True

        read_dht()

        last_dht = now



    # -------- LCD --------

    if now - last_lcd > 2500:


        lcd.clear()


        if lcd_mode == 0:

            lcd.putstr("   SATELIDOM")
            
            lcd.move_to(0,1)
            
            lcd.putstr("   ESTEISSY")


        else:

            lcd.putstr("Temp: {}C".format(temp))

            lcd.move_to(0,1)

            lcd.putstr("Hum: {}%".format(hum))


        lcd_mode = 1 - lcd_mode

        last_lcd = now