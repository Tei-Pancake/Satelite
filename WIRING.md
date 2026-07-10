# 🔌 Wiring Diagram

**Project:** Guardian Satellite - SATELIDOM ESTEISSY

This document describes the electrical connections between the Raspberry Pi Pico W and all modules.

---

# Raspberry Pi Pico W Connections

| Pico W Pin | Component | Component Pin | Description |
|------------|-----------|---------------|-------------|
| GP0 | LCD I2C | SDA | LCD data communication |
| GP1 | LCD I2C | SCL | LCD clock communication |
| VBUS | LCD I2C | VCC | LCD power supply |
| GND | LCD I2C | GND | Common ground |
| GP15 | PIR Sensor | OUT | Motion signal |
| VBUS | PIR Sensor | VCC | Sensor power |
| GND | PIR Sensor | GND | Common ground |
| GP16 | LED | Positive (+) | Status output |
| GND | LED | Negative (-) | Ground |
| GP17 | Passive Buzzer | Signal | Alarm control |
| GND | Passive Buzzer | GND | Ground |
| GP18 | DHT11 | DATA | Sensor data |
| 3V3 OUT | DHT11 | VCC | Sensor power |
| GND | DHT11 | GND | Common ground |

---

# DHT11 Pull-up Resistor

The DHT11 requires a pull-up resistor:

| Connection | Component |
|------------|-----------|
| VCC → DATA | 10kΩ resistor |

---

# LCD I2C Configuration

| Parameter | Value |
|-----------|-------|
| Address | 0x27 |
| SDA | GP0 |
| SCL | GP1 |
| Power | VBUS (5V) |

---

# Portable Battery Connection

## 18650 Battery System

| Battery Holder | Pico W |
|----------------|--------|
| Positive (+) | VSYS |
| Negative (-) | GND |

⚠️ Do not connect the battery directly to the 3V3 pin.

---

# Communication

## Telegram

The Raspberry Pi Pico W uses WiFi only for:

- Remote commands
- Status messages
- Motion alerts

No camera, microphone, or personal data collection is used.

---

# Development Connections

During prototyping:

- Breadboard is used for temporary connections.
- Male-to-Male and Female-to-Male jumper wires are used.
- Final assembly may use soldered connections and Female-to-Female wiring where required.
