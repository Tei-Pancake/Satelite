# 🛰️ SATELIDOM

![CAD Model](Images/cad.png)
> A cute, compact, square-shaped satellite designed to monitor temperature, humidity, and movement, and alert me whenever someone enters my room while I'm away from my desk.

**SATELIDOM** is a satellite-inspired project powered by a Raspberry Pi Pico W.

---

✨ Features

The device can monitor:

🌡️ Temperature

💧 Humidity

🔐 Motion (Technically it detects presence using a PIR sensor, but "motion detection" is easier to understand.)

![Guardian Satellite](Images/satellite.jpg)

---

It also has several features that can be controlled from a phone:

* Enable or disable motion detection ( useful when I'm at my desk and don't want to hear the *beep beep*)
* Check the current temperature and humidity remotely.

All of this is possible through a Telegram bot.

I can't make my bot public because it's configured specifically for **MY** satellite and contains sensitive information, but you can easily create your own Telegram bot if you'd like to build this project.

If you don't want to spend time setting that up, don't worry! The version available in this GitHub repository is a fully functional **offline version**, so it works perfectly even without WiFi.

---

I spent a long time working on this satellite, even before I started building it. I hope you enjoy it as much as I enjoyed creating it.

Created by **Andrea Esteissy Rosario Martinez**

Built with:

* Raspberry Pi Pico W
* MicroPython
* Electronics
* Curiosity 🚀

**PD:** I put too much effort in this README cause I wanted that look *Profeshonal* sooooooooooo, pls READ IT! thanks for watching ;) 




# 🔧 Hardware

## Main Components

| Component | Function |
|-----------|----------|
| Raspberry Pi Pico W | Main controller and WiFi communication |
| PIR Motion Sensor | Motion detection |
| DHT11 Sensor | Temperature and humidity measurement |
| 16x2 LCD I2C | Information display |
| Passive Buzzer | Audible alarm |
| LED | Status indicator |
| 10kΩ Resistor | DHT11 pull-up resistor |

---

# 🔌 Connections

| Raspberry Pi Pico W | Component | Pin |
|---------------------|-----------|-----|
| GP0 | LCD I2C | SDA |
| GP1 | LCD I2C | SCL |
| VBUS | LCD I2C | VCC |
| GND | LCD I2C | GND |
| GP15 | PIR Sensor | OUT |
| VBUS | PIR Sensor | VCC |
| GND | PIR Sensor | GND |
| GP16 | LED | Positive |
| GND | LED | Negative |
| GP17 | Passive Buzzer | Signal |
| GND | Passive Buzzer | GND |
| GP18 | DHT11 | DATA |
| 3V3 OUT | DHT11 | VCC |
| GND | DHT11 | GND |

### DHT11 Configuration

A **10kΩ pull-up resistor** is connected between:

- VCC
- DATA

---

# 🔋 Portable Power System

The final version is designed to work without a computer.

Planned power system:

- 🔋 18650 Li-ion Battery
- 🔌 18650 Battery Holder with ON/OFF Switch
- ⚡ 18650 Battery Charger

Connection:

| Battery | Pico W |
|---------|--------|
| Positive (+) | VSYS |
| Negative (-) | GND |

---

# 💻 Software

## Programming

- MicroPython
- Thonny IDE

## Libraries

- DHT11 MicroPython Library
- LCD I2C Library
- urequests
- Telegram Bot API

---

# 📱 Telegram Integration

The Telegram version allows the satellite to communicate remotely.

Available commands:

```
/activar
```

Activates Guardian Mode.

```
/desactivar
```

Disables Guardian Mode.

```
/status
```

Returns:

- System status
- Temperature
- Humidity
- Current mode

# 🚧 Current Status

## Completed ✅

- [x] Raspberry Pi Pico W integration
- [x] PIR motion detection
- [x] Temperature monitoring
- [x] Humidity monitoring
- [x] LCD interface
- [x] LED status system
- [x] Audible alarm
- [x] Telegram communication
- [x] Remote commands

## Planned 🔜

- [ ] 3D printed satellite enclosure
- [ ] Portable battery system
- [ ] Final soldered version
- [ ] Improved power management

---

# 🌌 Vision

The Guardian Satellite is more than a sensor box.

It is a small autonomous monitoring system designed to demonstrate how embedded electronics, programming, communication, and engineering can work together in a compact device.

A miniature satellite that watches over its environment. 🛰️

---

# 👨‍🚀 Author

Created by **Andrea Esteissy Rosario Martinez**

Project developed with:
- Raspberry Pi Pico W
- MicroPython
- Electronics
- Curiosity 🚀

PD: I put too much effort in this README cause I wanted that look *Profeshonal* sooooooooooo, pls READ IT! thanks for watching ;)
