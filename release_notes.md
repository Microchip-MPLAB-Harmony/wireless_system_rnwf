[![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png)](https://www.microchip.com)
[![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png)](https://www.microchip.com/en-us/tools-resources/configure/mplab-harmony)

# Microchip MPLAB® Harmony 3 Release Notes

### Harmony 3 wireless system service for RNWF02 and WINCS02 v3.2.0

### Bug Fixes

- **Net System Service (WINCS02):** Fix peer disconnect handling, TLS server socket setup, socket cleanup on close, and recv error reporting
- **Wi-Fi System Service (WINCS02):** Fix callback NULL safety, scan continuation, IPv6 link-local detection, and power-save handle usage
- **Wi-Fi System Service (RNWF02):** Fix AT command error handling in STA/AP config, regulatory domain typo, and callback typedef
- **Wi-Fi System Service (RNWF11):** Fix BSSID AT command, AP channel configuration, and parameter struct alignment
- **OTA System Service (RNWF02/RNWF11):** Fix DFU flash write logic, HTTP request buffer overflow, Content-Length parsing, and add flash erase timeout and NULL guards
- **OTA System Service (WINCS02):** Add NULL check for OTA callback handler

### Known Issues
- None

### Development Tools

* [MPLAB® X IDE v6.25](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v4.60](https://www.microchip.com/mplab/compilers)
* MPLAB® X IDE plug-ins:
    * MPLAB® Code Configurator (MCC) v5.6.2  
* SAM E54 DFP  : v3.9.244
* SAM9X75 DFP : v1.9.170


### Harmony 3 wireless system service for RNWF02 and WINCS02 v3.1.0

### New Features
 
- This release includes below system services implementation for WINCS02 device.
    - **OTA System Service**


* [MPLAB® X IDE v6.25](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v4.60](https://www.microchip.com/mplab/compilers)
* MPLAB® X IDE plug-ins:
    * MPLAB® Code Configurator (MCC) v5.6.2  
* SAM E54 DFP  : v3.9.244
* SAM9X75 DFP : v1.9.170



### Harmony 3 wireless system service for RNWF02 and WINCS02 v3.0.0

### New Features
 
- Updated RNWF02 and WINCS02 system services with MQTT v5.0 features.
- This release includes below system services implementation for WINCS02 device with SAM9X75 Host.
    - **Wi-Fi SystemService**
    - **Wi-Fi Provisioning System service**
    - **Net System Service**
    - **MQTT System service**

* [MPLAB® X IDE v6.20](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v4.45](https://www.microchip.com/mplab/compilers)
* MPLAB® X IDE plug-ins:
    * MPLAB® Code Configurator (MCC) v5.5.1  
* SAM E54 DFP  : v3.8.234
* SAM9X75 DFP : v1.4.151



### Harmony 3 wireless system service for RNWF02 and WINCS02 v2.0.0

### New Features
 
- Updated RNWF02 system services with IPV6, Regulatory domain, low power and Wi-Fi-BT coexistence features
- This release includes below system services implementation for WINCS02 device
    - **Wi-Fi SystemService**
    - **Wi-Fi Provisioning System service**
    - **Net System Service**
    - **MQTT System service**

* [MPLAB® X IDE v6.20](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v4.35](https://www.microchip.com/mplab/compilers)
* MPLAB® X IDE plug-ins:
    * MPLAB® Code Configurator (MCC) v5.5.0  
* SAME54 DFP : v3.8.234



### Harmony 3 wireless system service for RNWF family v1.0.0 

### New Features

- This release includes support below services for RNWF02 device 
    - **Wi-Fi System Service**
    - **Wi-Fi Provisioning System service**
    - **Net System Service**
    - **OTA System Service**
    - **MQTT System service**

### Known Issues
### Development Tools

* [MPLAB® X IDE v6.15](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v4.35](https://www.microchip.com/mplab/compilers)
* MPLAB® X IDE plug-ins:
    * MPLAB® Code Configurator (MCC) v5.4.1  
* SAME54 DFP : v3.8.234

