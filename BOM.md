# 🧾 Bill of Materials (BOM)

**Project:** Guardian Satellite  
**Version:** v1.1

This document contains all components required to build the Guardian Satellite.

---

# 🔌 Electronics

| Component | Quantity | Status | Purpose |
|-----------|:--------:|:------:|---------|
| Raspberry Pi Pico W | 1 | ✅ Available | Main controller and WiFi communication |
| PIR Motion Sensor | 1 | ✅ Available | Motion detection |
| DHT11 Temperature & Humidity Sensor | 1 | ✅ Available | Environmental monitoring |
| 16x2 LCD I2C Display | 1 | ✅ Available | Display system information |
| Passive Buzzer | 1 | ✅ Available | Audible alarm |
| LED | 1 | ✅ Available | Visual status indicator |
| 10kΩ Resistor | 1 | ✅ Available | DHT11 pull-up resistor |

---

# 🧪 Prototyping

| Component | Quantity | Status | Purpose |
|-----------|:--------:|:------:|---------|
| Breadboard | 1 | ✅ Available | Circuit prototyping |
| Male-to-Male Jumper Wires | Several | ✅ Available | Breadboard connections |
| Female-to-Male Jumper Wires | Several | ✅ Available | Connecting modules to breadboard |
| Female-to-Female Jumper Wires | Several | ⏳ Needed | Final module connections |

---

# 🔋 Portable Power System

| Component | Quantity | Status | Purpose |
|-----------|:--------:|:------:|---------|
| 18650 Li-ion Battery | 1 | ⏳ Needed | Portable power source |
| 18650 Battery Holder with ON/OFF Switch | 1 | ⏳ Needed | Battery connection and power control |
| 18650 Battery Charger | 1 | ⏳ Needed | Recharge the battery |

---

# 🛠️ Assembly Tools

| Component | Quantity | Status | Purpose |
|-----------|:--------:|:------:|---------|
| Soldering Iron | 1 | ⏳ Needed | Permanent connections |
| Solder Wire | 1 | ⏳ Needed | Solder electronic components |
| Soldering Flux | 1 | ⏳ Optional | Improve solder quality |

---

# 🛰️ Enclosure

| Component | Quantity | Status | Purpose |
|-----------|:--------:|:------:|---------|
| 3D Printed Satellite Enclosure | 1 | ⏳ Planned | Protect and contain electronics |

---

# 💻 Software Requirements

| Software | Purpose |
|----------|---------|
| MicroPython | Firmware |
| Thonny IDE | Programming environment |
| Telegram Bot API | Remote communication |
| LCD I2C Library | Display control |

---

# Notes

- The DHT11 requires a **10kΩ pull-up resistor** between VCC and DATA.
- The prototype version uses a breadboard.
- The final version will use soldered connections where necessary.
- WiFi is only required for Telegram communication.
- The system can operate locally without internet.
