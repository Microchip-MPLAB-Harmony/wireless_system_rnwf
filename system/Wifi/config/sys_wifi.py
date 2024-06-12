# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

################################################################################
#### Global Variables ####
################################################################################
global wifi_helpkeyword

wifi_helpkeyword = "mcc_h3_RNWF_wifi_system_service_configurations"
################################################################################
#### Business Logic ####
################################################################################

################################################################################
#### Component ####
################################################################################

from datetime import datetime


def instantiateComponent(sysWifiRNWFComponent):
    global wifi_helpkeyword
    syswifiEnable = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_WIFI_ENABLE", None)
    syswifiEnable.setHelp(wifi_helpkeyword)
    syswifiEnable.setVisible(False)
    syswifiEnable.setDefaultValue(True)

    sysrnwfwifiEnableErrMsg = sysWifiRNWFComponent.createCommentSymbol("SYS_RNWF_WIFI_ERR", None)
    sysrnwfwifiEnableErrMsg.setLabel("**Placeholder for error display")
    sysrnwfwifiEnableErrMsg.setHelp(wifi_helpkeyword)
    sysrnwfwifiEnableErrMsg.setVisible(False)

    sysrnwfwifiMode = sysWifiRNWFComponent.createComboSymbol("SYS_RNWF_WIFI_MODE", None, ["STA", "AP", "PROV" ])
    sysrnwfwifiMode.setLabel("Device Mode")
    sysrnwfwifiMode.setHelp(wifi_helpkeyword)
    sysrnwfwifiMode.setDescription("Select the Device Boot Mode ")
    sysrnwfwifiMode.setDefaultValue("STA")

    sysrnwfwifistaEnable = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_WIFI_MODE_STA", sysrnwfwifiMode)
    sysrnwfwifistaEnable.setLabel("STA Mode")
    sysrnwfwifistaEnable.setHelp(wifi_helpkeyword)
    sysrnwfwifistaEnable.setDefaultValue(True)
    sysrnwfwifistaEnable.setDescription("Enable STA mode Configuration ")
    sysrnwfwifistaEnable.setDependencies(syswifiSTAautoMenu, ["SYS_RNWF_WIFI_MODE_STA"])
    
    sysrnwfServices = sysWifiRNWFComponent.createCommentSymbol("SYS_SYSTEM_SERVICE", None)
    sysrnwfServices.setLabel("Advanced Configurations ")
    sysrnwfServices.setHelp(wifi_helpkeyword)
        
    sysrnwfwifiHost = sysWifiRNWFComponent.createComboSymbol("SYS_RNWF_HOST", sysrnwfServices , ["None" , "SAME54X-pro"])
    sysrnwfwifiHost.setLabel("Select Host ")
    sysrnwfwifiHost.setHelp(wifi_helpkeyword)
    sysrnwfwifiHost.setDescription("Select the Host Device")
    sysrnwfwifiHost.setDefaultValue("None")

    sysrnwfwifiDevice = sysWifiRNWFComponent.createComboSymbol("SYS_RNWF_WIFI_DEVICE", sysrnwfServices , ["None","RNWF02","WINCS02"])
    sysrnwfwifiDevice.setLabel("Select Wifi device ")
    sysrnwfwifiDevice.setHelp(wifi_helpkeyword)
    sysrnwfwifiDevice.setVisible(False)
    sysrnwfwifiDevice.setDescription("Select the Wifi Device")
    sysrnwfwifiDevice.setDefaultValue("None")
    sysrnwfwifiDevice.setDependencies(sysrnwfwifiDeviceMenuVisible,["SYS_RNWF_HOST"])
    
    
    sysrnwfinterfaceMode = sysWifiRNWFComponent.createComboSymbol("SYS_RNWF_INTERFACE_MODE", sysrnwfServices , ["None","UART","SPI"])
    sysrnwfinterfaceMode.setLabel("Interface Mode")
    sysrnwfinterfaceMode.setHelp(wifi_helpkeyword)
    sysrnwfinterfaceMode.setVisible(False)
    sysrnwfinterfaceMode.setDescription("Select the Device Interface Mode ")
    sysrnwfinterfaceMode.setDefaultValue("None")
    sysrnwfinterfaceMode.setDependencies(syscomponentautoactivate,["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])
    

    sysrnwfwifistaSsid = sysWifiRNWFComponent.createStringSymbol("SYS_RNWF_WIFI_STA_SSID_NAME", sysrnwfwifistaEnable)
    sysrnwfwifistaSsid.setLabel("SSID")
    sysrnwfwifistaSsid.setHelp(wifi_helpkeyword)
    sysrnwfwifistaSsid.setVisible(True)
    sysrnwfwifistaSsid.setDescription("Enter STA Mode SSID.The maximum length is 32 characters.")
    sysrnwfwifistaSsid.setDefaultValue("DEMO_AP")
    sysrnwfwifistaSsid.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_MODE_STA"])

    sysrnwfwifistaAuth = sysWifiRNWFComponent.createComboSymbol("SYS_RNWF_WIFI_STA_SECURITY", sysrnwfwifistaEnable, ["OPEN", "WPA2-MIXED" , "WPA2" , "WPA3-TRANS" , "WPA3"])
    sysrnwfwifistaAuth.setLabel("Security type")
    sysrnwfwifistaAuth.setHelp(wifi_helpkeyword)
    sysrnwfwifistaAuth.setDescription("Enter STA Mode Security type")
    sysrnwfwifistaAuth.setDefaultValue("WPA2")
    sysrnwfwifistaAuth.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_MODE_STA"])

    sysrnwfwifistaPwd = sysWifiRNWFComponent.createStringSymbol("SYS_RNWF_WIFI_STA_PWD_NAME", sysrnwfwifistaEnable)
    sysrnwfwifistaPwd.setLabel("Password")
    sysrnwfwifistaPwd.setHelp(wifi_helpkeyword)
    sysrnwfwifistaPwd.setVisible(True)
    sysrnwfwifistaPwd.setDescription("Enter STA Mode Password.WPA2/WPA3 - Maximum key length is 63 characters.Minimum key length is 8 characters.")
    sysrnwfwifistaPwd.setDefaultValue("password")
    sysrnwfwifistaPwd.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_MODE_STA"])

    sysrnwfwifistaAuto = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_WIFI_STA_AUTOCONNECT", sysrnwfwifistaEnable)
    sysrnwfwifistaAuto.setLabel("Auto Connect")
    sysrnwfwifistaAuto.setHelp(wifi_helpkeyword)
    sysrnwfwifistaAuto.setDescription("Enable Auto Connect Feature")
    sysrnwfwifistaAuto.setDefaultValue(True)
    sysrnwfwifistaAuto.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_MODE_STA"])

    sysrnwfwifiapEnable = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_WIFI_MODE_AP", sysrnwfwifiMode)
    sysrnwfwifiapEnable.setLabel("AP Mode")
    sysrnwfwifiapEnable.setHelp(wifi_helpkeyword)
    sysrnwfwifiapEnable.setDefaultValue(False)
    sysrnwfwifiapEnable.setDescription("Enable AP Mode Configuration")
    sysrnwfwifiapEnable.setDependencies(syswifiAPautoMenu, ["SYS_RNWF_WIFI_MODE_AP"])

    sysrnwfwifiapSsid = sysWifiRNWFComponent.createStringSymbol("SYS_RNWF_WIFI_AP_SSID_NAME", sysrnwfwifiapEnable)
    sysrnwfwifiapSsid.setLabel("SSID")
    sysrnwfwifiapSsid.setHelp(wifi_helpkeyword)
    sysrnwfwifiapSsid.setVisible(False)
    sysrnwfwifiapSsid.setDescription("Enter AP Mode SSID.The maximum length is 32 characters")
    sysrnwfwifiapSsid.setDefaultValue("DEMO_AP_SOFTAP")
    sysrnwfwifiapSsid.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_MODE_AP"])

    sysrnwfwifiapAuth = sysWifiRNWFComponent.createComboSymbol("SYS_RNWF_WIFI_AP_SECURITY", sysrnwfwifiapEnable, ["OPEN", "WPA2-MIXED" , "WPA2" , "WPA3-TRANS" , "WPA3"])
    sysrnwfwifiapAuth.setLabel("Security")
    sysrnwfwifiapAuth.setHelp(wifi_helpkeyword)
    sysrnwfwifiapAuth.setVisible(False)
    sysrnwfwifiapAuth.setDescription("Enter AP Mode Security")
    sysrnwfwifiapAuth.setDefaultValue("WPA2")
    sysrnwfwifiapAuth.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_MODE_AP"])

    sysrnwfwifiapPwd = sysWifiRNWFComponent.createStringSymbol("SYS_WIFI_AP_PWD_NAME", sysrnwfwifiapEnable)
    sysrnwfwifiapPwd.setLabel("Password")
    sysrnwfwifiapPwd.setHelp(wifi_helpkeyword)
    sysrnwfwifiapPwd.setVisible(False)
    sysrnwfwifiapPwd.setDescription("Enter AP Mode Password.WPA2/WPA3 - Maximum key length is 63 characters.Minimum key length is 8 characters.")
    sysrnwfwifiapPwd.setDefaultValue("password")
    sysrnwfwifiapPwd.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_MODE_AP"])   

    sysrnwfwifiAPChannel = sysWifiRNWFComponent.createIntegerSymbol("SYS_RNWF_WIFI_AP_CHANNEL", sysrnwfwifiapEnable)
    sysrnwfwifiAPChannel.setLabel("Channel Number")
    sysrnwfwifiAPChannel.setHelp(wifi_helpkeyword)
    sysrnwfwifiAPChannel.setVisible(False)
    sysrnwfwifiAPChannel.setMin(0)
    sysrnwfwifiAPChannel.setMax(13)
    sysrnwfwifiAPChannel.setDescription("Enable AP Mode Channel")
    sysrnwfwifiAPChannel.setDefaultValue(1)
    sysrnwfwifiAPChannel.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_MODE_AP"])

    sysrnwfwifiProvEnable = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_WIFI_MODE_PROV", sysrnwfwifiMode)
    sysrnwfwifiProvEnable.setLabel("Provision Mode")
    sysrnwfwifiProvEnable.setHelp(wifi_helpkeyword)
    sysrnwfwifiProvEnable.setDefaultValue(False)
    sysrnwfwifiProvEnable.setDescription("Enable Provision Mode Configuration")
    sysrnwfwifiProvEnable.setDependencies(syswifiAPautoMenu, ["SYS_RNWF_WIFI_MODE_PROV"])

    sysrnwfwifiprovSsid = sysWifiRNWFComponent.createStringSymbol("SYS_RNWF_WIFI_PROV_SSID_NAME", sysrnwfwifiProvEnable)
    sysrnwfwifiprovSsid.setLabel("SSID")
    sysrnwfwifiprovSsid.setHelp(wifi_helpkeyword)
    sysrnwfwifiprovSsid.setVisible(False)
    sysrnwfwifiprovSsid.setDescription("Enter AP Mode SSID.The maximum length is 32 characters")
    sysrnwfwifiprovSsid.setDefaultValue("DEMO_AP_SOFTAP")
    sysrnwfwifiprovSsid.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_MODE_PROV"])

    sysrnwfwifiProvAuth = sysWifiRNWFComponent.createComboSymbol("SYS_RNWF_WIFI_PROV_SECURITY", sysrnwfwifiProvEnable, ["OPEN", "WPA2-MIXED" , "WPA2" , "WPA3-TRANS" , "WPA3"])
    sysrnwfwifiProvAuth.setLabel("Security")
    sysrnwfwifiProvAuth.setHelp(wifi_helpkeyword)
    sysrnwfwifiProvAuth.setVisible(False)
    sysrnwfwifiProvAuth.setDescription("Enter Provision Mode Security")
    sysrnwfwifiProvAuth.setDefaultValue("WPA2")
    sysrnwfwifiProvAuth.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_MODE_PROV"])

    sysrnwfwifiProvPwd = sysWifiRNWFComponent.createStringSymbol("SYS_WIFI_PROV_PWD_NAME", sysrnwfwifiProvEnable)
    sysrnwfwifiProvPwd.setLabel("Password")
    sysrnwfwifiProvPwd.setHelp(wifi_helpkeyword)
    sysrnwfwifiProvPwd.setVisible(False)
    sysrnwfwifiProvPwd.setDescription("Enter AP Mode Password.WPA2/WPA3 - Maximum key length is 63 characters.Minimum key length is 8 characters.")
    sysrnwfwifiProvPwd.setDefaultValue("password")
    sysrnwfwifiProvPwd.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_MODE_PROV"])
    
    sysrnwfwifiProvMethod = sysWifiRNWFComponent.createComboSymbol("SYS_RNWF_WIFI_PROV_METHOD", sysrnwfwifiProvEnable, ["PROV_WEB_SERVER", "PROV_MOBILE_APP" ])
    sysrnwfwifiProvMethod.setLabel("Provision Method")
    sysrnwfwifiProvMethod.setHelp(wifi_helpkeyword)
    sysrnwfwifiProvMethod.setVisible(False)
    sysrnwfwifiProvMethod.setDescription("Enter Provision method")
    sysrnwfwifiProvMethod.setDefaultValue("PROV_MOBILE_APP")
    sysrnwfwifiProvMethod.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_MODE_PROV"])

    sysrnwfwifiProvChannel = sysWifiRNWFComponent.createIntegerSymbol("SYS_RNWF_WIFI_PROV_CHANNEL", sysrnwfwifiProvEnable)
    sysrnwfwifiProvChannel.setLabel("Channel Number")
    sysrnwfwifiProvChannel.setHelp(wifi_helpkeyword)
    sysrnwfwifiProvChannel.setVisible(False)
    sysrnwfwifiProvChannel.setMin(0)
    sysrnwfwifiProvChannel.setMax(13)
    sysrnwfwifiProvChannel.setDescription("Enable Provision Mode Channel")
    sysrnwfwifiProvChannel.setDefaultValue(1)
    sysrnwfwifiProvChannel.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_MODE_PROV"])

        
    ##### Advanced Configuration ########
    

    sysrnwfcountrycode = sysWifiRNWFComponent.createComboSymbol("SYS_RNWF_COUNTRYCODE", sysrnwfServices , ["GEN" , "USA", "EMEA"])
    sysrnwfcountrycode.setLabel("Country Code")
    sysrnwfcountrycode.setHelp(wifi_helpkeyword)
    sysrnwfcountrycode.setDescription("Enable Country code \n Support channels per Country code: \n GEN - 1 to 13, \n USA - 1 to 11,")
    sysrnwfcountrycode.setDefaultValue("GEN")
    sysrnwfcountrycode.setVisible(False)
    sysrnwfcountrycode.setDependencies(syswifiAdvancedConfMenuVisible, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwfwifidebuglogs = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_WIFI_DEBUG_LOGS", sysrnwfServices)
    sysrnwfwifidebuglogs.setLabel("Wi-Fi Debug logs")
    sysrnwfwifidebuglogs.setHelp(wifi_helpkeyword)
    sysrnwfwifidebuglogs.setDefaultValue(False)
    sysrnwfwifidebuglogs.setDescription("Select to enable Wi-Fi service debug logs ")
    sysrnwfwifidebuglogs.setVisible(False)
    sysrnwfwifidebuglogs.setDependencies(syswifiAdvancedConfMenuVisible, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwfwifibtcoexist = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_WIFI_BT_COEXIST", sysrnwfServices)
    sysrnwfwifibtcoexist.setLabel("Wi-Fi BT Coexistance")
    sysrnwfwifibtcoexist.setHelp(wifi_helpkeyword)
    sysrnwfwifibtcoexist.setDefaultValue(False)
    sysrnwfwifibtcoexist.setDescription("Select to enable Wi-Fi BT coexistance ")
    sysrnwfwifibtcoexist.setVisible(False)
    sysrnwfwifibtcoexist.setDependencies(syswifiAdvancedConfMenuVisible, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwfinftype = sysWifiRNWFComponent.createComboSymbol("SYS_RNWF_INF_TYPE", sysrnwfwifibtcoexist , ["3-wire" , "2-wire"])
    sysrnwfinftype.setLabel("Interface type")
    sysrnwfinftype.setHelp(wifi_helpkeyword)
    sysrnwfinftype.setVisible(False)
    sysrnwfinftype.setDescription("BT/Wi-Fi coexistence arbiter interface type : 3-wire interface (BT_Act, BT_Prio, WLAN_Act) , 2-wire interface (BT_Prio, WLAN_Act)")
    sysrnwfinftype.setDefaultValue("3-wire")
    sysrnwfinftype.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_BT_COEXIST"])
    

    sysrnwfwifirxpriority = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_WLAN_RX_PRIO", sysrnwfwifibtcoexist)
    sysrnwfwifirxpriority.setLabel("WLAN Rx priority higher than BT Low Priority")
    sysrnwfwifirxpriority.setHelp(wifi_helpkeyword)
    sysrnwfwifirxpriority.setVisible(False)
    sysrnwfwifirxpriority.setDefaultValue(True)
    sysrnwfwifirxpriority.setDescription("Select to enable WLAN Rx priority higher than BT Low Priority ")
    sysrnwfwifirxpriority.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_BT_COEXIST"])

    sysrnwfwifitxpriority = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_WLAN_TX_PRIO", sysrnwfwifibtcoexist)
    sysrnwfwifitxpriority.setLabel("WLAN Tx priority higher than BT Low Priority")
    sysrnwfwifitxpriority.setHelp(wifi_helpkeyword)
    sysrnwfwifitxpriority.setVisible(False)
    sysrnwfwifitxpriority.setDefaultValue(True)
    sysrnwfwifitxpriority.setDescription("Select to enable WLAN Tx priority higher than BT Low Priority ")
    sysrnwfwifitxpriority.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_BT_COEXIST"])

    sysrnwfantennatype = sysWifiRNWFComponent.createComboSymbol("SYS_RNWF_INTENNA_TYPE", sysrnwfwifibtcoexist , ["Dedicated Antenna" , "Shared Antenna"])
    sysrnwfantennatype.setLabel("Antenna type")
    sysrnwfantennatype.setHelp(wifi_helpkeyword)
    sysrnwfantennatype.setVisible(False)
    sysrnwfantennatype.setDescription("Select the Antenna type")
    sysrnwfantennatype.setDefaultValue("Dedicated Antenna")
    sysrnwfantennatype.setDependencies(syswifiMenuVisible, ["SYS_RNWF_WIFI_BT_COEXIST"])

    sysrnwfpowersavemode = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_POWER_SAVE_MODE", sysrnwfServices)
    sysrnwfpowersavemode.setLabel("Power Save Mode")
    sysrnwfpowersavemode.setHelp(wifi_helpkeyword)
    sysrnwfpowersavemode.setVisible(False)
    sysrnwfpowersavemode.setDefaultValue(False)
    sysrnwfpowersavemode.setDescription("Select to enable Wi-Fi power save in STA mode ")
    sysrnwfpowersavemode.setDependencies(syswifiAdvancedConfMenuVisible, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwfSNTPserver = sysWifiRNWFComponent.createStringSymbol("SYS_RNWF_SNTP_ADDRESS", sysrnwfServices)
    sysrnwfSNTPserver.setLabel("SNTP Server address")
    sysrnwfSNTPserver.setHelp(wifi_helpkeyword)
    sysrnwfSNTPserver.setDefaultValue("")
    sysrnwfSNTPserver.setDescription("Enter the sntp serover address ")
    sysrnwfSNTPserver.setVisible(False)
    sysrnwfSNTPserver.setDependencies(syswifiAdvancedConfMenuVisible, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwfdns = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_ENABLE_DNS", sysrnwfServices)
    sysrnwfdns.setLabel("Enable DNS ")
    sysrnwfdns.setHelp(wifi_helpkeyword)
    sysrnwfdns.setDefaultValue(False)
    sysrnwfdns.setDescription("Select to enable DNS finctionality")

    sysrnwfping = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_PING", sysrnwfServices)
    sysrnwfping.setLabel("Ping")
    sysrnwfping.setHelp(wifi_helpkeyword)
    sysrnwfping.setDefaultValue(False)
    sysrnwfping.setDescription("Select to enable PING finctionality")
    sysrnwfping.setVisible(False)
    sysrnwfping.setDependencies(syswifiAdvancedConfMenuVisible, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])


    sysrnwfpingaddress = sysWifiRNWFComponent.createStringSymbol("SYS_RNWF_PING_ADDRESS", sysrnwfping)
    sysrnwfpingaddress.setLabel("Ping Address")
    sysrnwfpingaddress.setHelp(wifi_helpkeyword)
    sysrnwfpingaddress.setVisible(False)
    sysrnwfpingaddress.setDefaultValue("192.168.0.1")
    sysrnwfpingaddress.setDescription("Enter the Ping IP address")
    sysrnwfpingaddress.setDependencies(syswifiMenuVisible, ["SYS_RNWF_PING"])

    sysrnwfinfdebuglogs = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_INF_DEBUG_LOGS", sysrnwfServices)
    sysrnwfinfdebuglogs.setLabel("Interface Debug logs")
    sysrnwfinfdebuglogs.setHelp(wifi_helpkeyword)
    sysrnwfinfdebuglogs.setDefaultValue(False)
    sysrnwfinfdebuglogs.setDescription("Select to enable Interface debug logs ")
    sysrnwfinfdebuglogs.setVisible(False)
    sysrnwfinfdebuglogs.setDependencies(syswifiAdvancedConfMenuVisible, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwfwifiSerprovEnable = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_WIFI_SER_PROV_ENABLE", None)
    sysrnwfwifiSerprovEnable.setLabel("RNWF WiFi Provisioning Service")
    sysrnwfwifiSerprovEnable.setHelp(wifi_helpkeyword)
    sysrnwfwifiSerprovEnable.setDefaultValue(False)
    sysrnwfwifiSerprovEnable.setDescription("Enable WiFi Provisioning System Service ")
    sysrnwfwifiSerprovEnable.setDependencies(syswifiprovautoInclude, ["SYS_RNWF_WIFI_SER_PROV_ENABLE"])
    

    sysrnwfmqttEnable = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_MQTT_ENABLE", None)
    sysrnwfmqttEnable.setLabel("RNWF MQTT Service")
    sysrnwfmqttEnable.setHelp(wifi_helpkeyword)
    sysrnwfmqttEnable.setDefaultValue(False)
    sysrnwfmqttEnable.setDescription("Enable mqtt System Service ")
    sysrnwfmqttEnable.setDependencies(sysmqttautoInclude, ["SYS_RNWF_MQTT_ENABLE"])

    sysrnwfotaSerEnable = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_OTA_SER_ENABLE", None)
    sysrnwfotaSerEnable.setLabel("RNWF OTA Service")
    sysrnwfotaSerEnable.setHelp(wifi_helpkeyword)
    sysrnwfotaSerEnable.setDefaultValue(False)
    sysrnwfotaSerEnable.setDescription("Enable ota System Service ")
    sysrnwfotaSerEnable.setDependencies(sysotaautoInclude, ["SYS_RNWF_OTA_SER_ENABLE"])

    sysrnwfnetSerEnable = sysWifiRNWFComponent.createBooleanSymbol("SYS_RNWF_NET_SER_ENABLE", None)
    sysrnwfnetSerEnable.setLabel("RNWF NET Service")
    sysrnwfnetSerEnable.setHelp(wifi_helpkeyword)
    sysrnwfnetSerEnable.setDefaultValue(False)
    sysrnwfnetSerEnable.setDescription("Enable net System Service ")
    sysrnwfnetSerEnable.setDependencies(sysnetautoInclude, ["SYS_RNWF_NET_SER_ENABLE"])


    sysrnwfwifiCallbackHandler = sysWifiRNWFComponent.createStringSymbol("SYS_RNWF_WIFI_CALLBACK_HANDLER", sysrnwfServices)
    sysrnwfwifiCallbackHandler.setLabel("WiFi callback handler")
    sysrnwfwifiCallbackHandler.setHelp(wifi_helpkeyword)
    sysrnwfwifiCallbackHandler.setDescription("WiFi callback handler")
    sysrnwfwifiCallbackHandler.setDefaultValue("APP_WIFI_Callback")
    sysrnwfwifiCallbackHandler.setVisible(False)
    sysrnwfwifiCallbackHandler.setDependencies(syswifiAdvancedConfMenuVisible, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    


    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    sysrnwfwifiSourceFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF_WIFI_SOURCE", None)
    sysrnwfwifiSourceFile.setSourcePath("system/Wifi/templates/src/sys_rnwf02_wifi_service.c.ftl")
    sysrnwfwifiSourceFile.setOutputName("sys_rnwf_wifi_service.c")
    sysrnwfwifiSourceFile.setDestPath("system/wifi/src")
    sysrnwfwifiSourceFile.setProjectPath("config/" + configName + "/system/wifi/")
    sysrnwfwifiSourceFile.setType("SOURCE")
    sysrnwfwifiSourceFile.setMarkup(True)
    sysrnwfwifiSourceFile.setEnabled(False)
    sysrnwfwifiSourceFile.setOverwrite(True)
    sysrnwfwifiSourceFile.setDependencies(sysrnwfwifiRnwf02FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwfwifiHeaderFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF_WIFI_HEADER", None)
    sysrnwfwifiHeaderFile.setSourcePath("system/Wifi/templates/sys_rnwf02_wifi_service.h.ftl")
    sysrnwfwifiHeaderFile.setOutputName("sys_rnwf_wifi_service.h")
    sysrnwfwifiHeaderFile.setDestPath("system/wifi/")
    sysrnwfwifiHeaderFile.setProjectPath("config/" + configName + "/system/wifi/")
    sysrnwfwifiHeaderFile.setType("HEADER")
    sysrnwfwifiHeaderFile.setMarkup(True)
    sysrnwfwifiHeaderFile.setOverwrite(True)
    sysrnwfwifiHeaderFile.setEnabled(False)
    sysrnwfwifiHeaderFile.setDependencies(sysrnwfwifiRnwf02FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])
    
    sysrnwfInterfaceSourceFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF_INTERFACE_SOURCE", None)
    sysrnwfInterfaceSourceFile.setSourcePath("system/Wifi/templates/src/sys_rnwf02_interface.c.ftl")
    sysrnwfInterfaceSourceFile.setOutputName("sys_rnwf_interface.c")
    sysrnwfInterfaceSourceFile.setDestPath("system/inf/src")
    sysrnwfInterfaceSourceFile.setProjectPath("config/" + configName + "/system/inf/")
    sysrnwfInterfaceSourceFile.setType("SOURCE")
    sysrnwfInterfaceSourceFile.setMarkup(True)
    sysrnwfInterfaceSourceFile.setOverwrite(True)
    sysrnwfInterfaceSourceFile.setEnabled(False)
    sysrnwfInterfaceSourceFile.setDependencies(sysrnwfwifiRnwf02FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwfInterfaceHeaderFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF_INTERFACE_HEADER", None)
    sysrnwfInterfaceHeaderFile.setSourcePath("system/Wifi/templates/sys_rnwf02_interface.h.ftl")
    sysrnwfInterfaceHeaderFile.setOutputName("sys_rnwf_interface.h")
    sysrnwfInterfaceHeaderFile.setDestPath("system/inf/")
    sysrnwfInterfaceHeaderFile.setProjectPath("config/" + configName + "/system/inf/")
    sysrnwfInterfaceHeaderFile.setType("HEADER")
    sysrnwfInterfaceHeaderFile.setMarkup(True)
    sysrnwfInterfaceHeaderFile.setOverwrite(True)
    sysrnwfInterfaceHeaderFile.setEnabled(False)
    sysrnwfInterfaceHeaderFile.setDependencies(sysrnwfwifiRnwf02FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwfInterfaceSysSourceFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF_INF_SYSTEM_SOURCE", None)
    sysrnwfInterfaceSysSourceFile.setSourcePath("system/System/templates/src/sys_rnwf02_system_service.c.ftl")
    sysrnwfInterfaceSysSourceFile.setOutputName("sys_rnwf_system_service.c")
    sysrnwfInterfaceSysSourceFile.setDestPath("system/")
    sysrnwfInterfaceSysSourceFile.setProjectPath("config/" + configName + "/system/")
    sysrnwfInterfaceSysSourceFile.setType("SOURCE")
    sysrnwfInterfaceSysSourceFile.setOverwrite(True)
    sysrnwfInterfaceSysSourceFile.setEnabled(False)
    sysrnwfInterfaceSysSourceFile.setDependencies(sysrnwfwifiRnwf02FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])


    sysrnwfInterfaceSysHeaderFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF_INF_SYSTEM_HEADER", None)
    sysrnwfInterfaceSysHeaderFile.setSourcePath("system/System/templates/sys_rnwf02_system_service.h.ftl")
    sysrnwfInterfaceSysHeaderFile.setOutputName("sys_rnwf_system_service.h")
    sysrnwfInterfaceSysHeaderFile.setDestPath("system/")
    sysrnwfInterfaceSysHeaderFile.setProjectPath("config/" + configName + "/system/")
    sysrnwfInterfaceSysHeaderFile.setType("HEADER")
    sysrnwfInterfaceSysHeaderFile.setOverwrite(True)
    sysrnwfInterfaceSysHeaderFile.setEnabled(False)
    sysrnwfInterfaceSysHeaderFile.setDependencies(sysrnwfwifiRnwf02FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    #### System Files #####

    sysrnwfwifiSystemConfFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF_WIFI_CONFIGURATION_H", None)
    sysrnwfwifiSystemConfFile.setType("STRING")
    sysrnwfwifiSystemConfFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
    sysrnwfwifiSystemConfFile.setSourcePath("system/Wifi/templates/system/system_config_rnwf02.h.ftl")
    sysrnwfwifiSystemConfFile.setMarkup(True)
    sysrnwfwifiSystemConfFile.setOverwrite(True)
    sysrnwfwifiSystemConfFile.setEnabled(False)
    sysrnwfwifiSystemConfFile.setDependencies(sysrnwfwifiRnwf02FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])


    # #### WINCS02 Code Generation

    sysrnwfwifiWincs02SourceFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF_WIFI_WINCS02_SOURCE", None)
    sysrnwfwifiWincs02SourceFile.setSourcePath("system/Wifi/templates/src/sys_wincs02_wifi_service.c.ftl")
    sysrnwfwifiWincs02SourceFile.setOutputName("sys_wincs_wifi_service.c")
    sysrnwfwifiWincs02SourceFile.setDestPath("system/wifi/src")
    sysrnwfwifiWincs02SourceFile.setProjectPath("config/" + configName + "/system/wifi/")
    sysrnwfwifiWincs02SourceFile.setType("SOURCE")
    sysrnwfwifiWincs02SourceFile.setMarkup(True)
    sysrnwfwifiWincs02SourceFile.setEnabled(False)
    sysrnwfwifiWincs02SourceFile.setOverwrite(True)
    sysrnwfwifiWincs02SourceFile.setDependencies(sysrnwfwifiWincs02FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwfwifiWincs02HeaderFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF_WIFI_WINCS02_HEADER", None)
    sysrnwfwifiWincs02HeaderFile.setSourcePath("system/Wifi/templates/sys_wincs02_wifi_service.h.ftl")
    sysrnwfwifiWincs02HeaderFile.setOutputName("sys_wincs_wifi_service.h")
    sysrnwfwifiWincs02HeaderFile.setDestPath("system/wifi/")
    sysrnwfwifiWincs02HeaderFile.setProjectPath("config/" + configName + "/system/wifi/")
    sysrnwfwifiWincs02HeaderFile.setType("HEADER")
    sysrnwfwifiWincs02HeaderFile.setMarkup(True)
    sysrnwfwifiWincs02HeaderFile.setOverwrite(True)
    sysrnwfwifiWincs02HeaderFile.setEnabled(False)
    sysrnwfwifiWincs02HeaderFile.setDependencies(sysrnwfwifiWincs02FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])
    

    sysrnwfWincs02SysSourceFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF_INF_WINCS02_SYSTEM_SOURCE", None)
    sysrnwfWincs02SysSourceFile.setSourcePath("system/System/templates/src/sys_wincs02_system_service.c.ftl")
    sysrnwfWincs02SysSourceFile.setOutputName("sys_wincs_system_service.c")
    sysrnwfWincs02SysSourceFile.setDestPath("system/")
    sysrnwfWincs02SysSourceFile.setProjectPath("config/" + configName + "/system/")
    sysrnwfWincs02SysSourceFile.setType("SOURCE")
    sysrnwfWincs02SysSourceFile.setOverwrite(True)
    sysrnwfWincs02SysSourceFile.setEnabled(False)
    sysrnwfWincs02SysSourceFile.setDependencies(sysrnwfwifiWincs02FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])


    sysrnwfWincs02SysHeaderFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF_INF_WINCS02_SYSTEM_HEADER", None)
    sysrnwfWincs02SysHeaderFile.setSourcePath("system/System/templates/sys_wincs02_system_service.h.ftl")
    sysrnwfWincs02SysHeaderFile.setOutputName("sys_wincs_system_service.h")
    sysrnwfWincs02SysHeaderFile.setDestPath("system/")
    sysrnwfWincs02SysHeaderFile.setProjectPath("config/" + configName + "/system/")
    sysrnwfWincs02SysHeaderFile.setType("HEADER")
    sysrnwfWincs02SysHeaderFile.setOverwrite(True)
    sysrnwfWincs02SysHeaderFile.setEnabled(False)
    sysrnwfWincs02SysHeaderFile.setDependencies(sysrnwfwifiWincs02FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    #### System Files #####
    syswincs02wifiSystemConfFile = sysWifiRNWFComponent.createFileSymbol("SYS_WINCS_WIFI_CONFIGURATION_H", None)
    syswincs02wifiSystemConfFile.setType("STRING")
    syswincs02wifiSystemConfFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
    syswincs02wifiSystemConfFile.setSourcePath("system/Wifi/templates/system/system_config_wincs02.h.ftl")
    syswincs02wifiSystemConfFile.setMarkup(True)
    syswincs02wifiSystemConfFile.setOverwrite(True)
    syswincs02wifiSystemConfFile.setEnabled(False)
    syswincs02wifiSystemConfFile.setDependencies(sysrnwfwifiWincs02FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])
	### RNWF11 Code Generation #################

    sysrnwf11wifiSourceFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF11_WIFI_SOURCE", None)
    sysrnwf11wifiSourceFile.setSourcePath("system/Wifi/templates/src/sys_rnwf11_wifi_service.c.ftl")
    sysrnwf11wifiSourceFile.setOutputName("sys_rnwf_wifi_service.c")
    sysrnwf11wifiSourceFile.setDestPath("system/wifi/src")
    sysrnwf11wifiSourceFile.setProjectPath("config/" + configName + "/system/wifi/")
    sysrnwf11wifiSourceFile.setType("SOURCE")
    sysrnwf11wifiSourceFile.setMarkup(True)
    sysrnwf11wifiSourceFile.setEnabled(False)
    sysrnwf11wifiSourceFile.setOverwrite(True)
    sysrnwf11wifiSourceFile.setDependencies(sysrnwfwifiRnwf11FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwf11wifiHeaderFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF11_WIFI_HEADER", None)
    sysrnwf11wifiHeaderFile.setSourcePath("system/Wifi/templates/sys_rnwf11_wifi_service.h.ftl")
    sysrnwf11wifiHeaderFile.setOutputName("sys_rnwf_wifi_service.h")
    sysrnwf11wifiHeaderFile.setDestPath("system/wifi/")
    sysrnwf11wifiHeaderFile.setProjectPath("config/" + configName + "/system/wifi/")
    sysrnwf11wifiHeaderFile.setType("HEADER")
    sysrnwf11wifiHeaderFile.setMarkup(True)
    sysrnwf11wifiHeaderFile.setOverwrite(True)
    sysrnwf11wifiHeaderFile.setEnabled(False)
    sysrnwf11wifiHeaderFile.setDependencies(sysrnwfwifiRnwf11FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwf11InterfaceSourceFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF11_INTERFACE_SOURCE", None)
    sysrnwf11InterfaceSourceFile.setSourcePath("system/Wifi/templates/src/sys_rnwf11_interface.c.ftl")
    sysrnwf11InterfaceSourceFile.setOutputName("sys_rnwf_interface.c")
    sysrnwf11InterfaceSourceFile.setDestPath("system/inf/src")
    sysrnwf11InterfaceSourceFile.setProjectPath("config/" + configName + "/system/inf/")
    sysrnwf11InterfaceSourceFile.setType("SOURCE")
    sysrnwf11InterfaceSourceFile.setMarkup(True)
    sysrnwf11InterfaceSourceFile.setOverwrite(True)
    sysrnwf11InterfaceSourceFile.setEnabled(False)
    sysrnwf11InterfaceSourceFile.setDependencies(sysrnwfwifiRnwf11FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwf11InterfaceHeaderFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF11_INTERFACE_HEADER", None)
    sysrnwf11InterfaceHeaderFile.setSourcePath("system/Wifi/templates/sys_rnwf11_interface.h.ftl")
    sysrnwf11InterfaceHeaderFile.setOutputName("sys_rnwf_interface.h")
    sysrnwf11InterfaceHeaderFile.setDestPath("system/inf/")
    sysrnwf11InterfaceHeaderFile.setProjectPath("config/" + configName + "/system/inf/")
    sysrnwf11InterfaceHeaderFile.setType("HEADER")
    sysrnwf11InterfaceHeaderFile.setMarkup(True)
    sysrnwf11InterfaceHeaderFile.setOverwrite(True)
    sysrnwf11InterfaceHeaderFile.setEnabled(False)
    sysrnwf11InterfaceHeaderFile.setDependencies(sysrnwfwifiRnwf11FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])
    
    sysrnwf11InterfaceSourceFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF11_INF_SYSTEM_SOURCE", None)
    sysrnwf11InterfaceSourceFile.setSourcePath("system/System/templates/src/sys_rnwf11_system_service.c.ftl")
    sysrnwf11InterfaceSourceFile.setOutputName("sys_rnwf_system_service.c")
    sysrnwf11InterfaceSourceFile.setDestPath("system/")
    sysrnwf11InterfaceSourceFile.setProjectPath("config/" + configName + "/system/")
    sysrnwf11InterfaceSourceFile.setType("SOURCE")
    sysrnwf11InterfaceSourceFile.setOverwrite(True)
    sysrnwf11InterfaceSourceFile.setEnabled(False)
    sysrnwf11InterfaceSourceFile.setDependencies(sysrnwfwifiRnwf11FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

    sysrnwf11InterfaceSysHeaderFile = sysWifiRNWFComponent.createFileSymbol("SYS_RNWF11_INF_SYSTEM_HEADER", None)
    sysrnwf11InterfaceSysHeaderFile.setSourcePath("system/System/templates/sys_rnwf11_system_service.h.ftl")
    sysrnwf11InterfaceSysHeaderFile.setOutputName("sys_rnwf_system_service.h")
    sysrnwf11InterfaceSysHeaderFile.setDestPath("system/")
    sysrnwf11InterfaceSysHeaderFile.setProjectPath("config/" + configName + "/system/")
    sysrnwf11InterfaceSysHeaderFile.setType("HEADER")
    sysrnwf11InterfaceSysHeaderFile.setOverwrite(True)
    sysrnwf11InterfaceSysHeaderFile.setEnabled(False)
    sysrnwf11InterfaceSysHeaderFile.setDependencies(sysrnwfwifiRnwf11FilesEnable, ["SYS_RNWF_HOST","SYS_RNWF_WIFI_DEVICE","SYS_RNWF_INTERFACE_MODE"])

############################################################################
#### Dependency ####
############################################################################
#Set symbols of other components

def syswifiprovGenSourceFile(sourceFile, event):
    print("Device WIFI Menu Visible.")
    sourceFile.setEnabled(event["value"])


def sysrnwfwifiDeviceMenuVisible(symbol, event):
    if (event["value"] == "SAME54X-pro"):
        print("Device WIFI Menu Visible.")
        symbol.setVisible(True)
    else:
        print("WIFI Menu Invisible.")
        symbol.setVisible(False)

def setVal(component, symbol, value):
    triggerSvDict = {"Component":component,"Id":symbol, "Value":value}
    if(Database.sendMessage(component, "SET_SYMBOL", triggerSvDict) == None):
        print("Set Symbol Failure" + component + ":" + symbol + ":" + str(value))
        return False
    else:
        return True

#Handle messages from other components
def handleMessage(messageID, args):
    retDict= {}
    if (messageID == "SET_SYMBOL"):
        print("handleMessage: Set Symbol")
        retDict= {"Return": "Success"}
        Database.setSymbolValue(args["Component"], args["Id"], args["Value"])
    else:
        retDict= {"Return": "UnImplemented Command"}
    return retDict

def onAttachmentConnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]


def onAttachmentDisconnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

def syswifiMenuVisible(symbol, event):
    if (event["value"] == True):
        print("WIFI Menu Visible.")
        symbol.setVisible(True)
    else:
        print("WIFI Menu Invisible.")
        symbol.setVisible(False)

def syswifiSTASecurityMenu(symbol, event):
    print("syswifiSTASecurityMenu")

def syswifiAPSecurityMenu(symbol, event):
    print("syswifiAPSecurityMenu")

def syswifiChannelErr(symbol, event):
    print("syswifiChannelErr")

def syswifiSTAMenu(symbol, event):
    print("syswifiSTAMenu")

def syswifiAPMenu(symbol, event):
    print("syswifiAPMenu")

def sysrnwfwifiRnwf02FilesEnable(symbol, event):
    print("sysrnwfwifirnwf02FilesEnable")
    data = symbol.getComponent()
    host = data.getSymbolValue("SYS_RNWF_HOST")
    device = data.getSymbolValue("SYS_RNWF_WIFI_DEVICE")
    interface = data.getSymbolValue("SYS_RNWF_INTERFACE_MODE")

    if ((host == "SAME54X-pro") and (device == "RNWF02") and (interface== "UART")):
        print("File : Host and Device are SUPPORTED - RN")
        symbol.setEnabled(True)
    else:
        print("File : Host and Device are NOT SUPPORTED")


def sysrnwfwifiWincs02FilesEnable(symbol, event):
    print("sysrnwfwifiWincs02FilesEnable")
    data = symbol.getComponent()
    host = data.getSymbolValue("SYS_RNWF_HOST")
    device = data.getSymbolValue("SYS_RNWF_WIFI_DEVICE")
    interface = data.getSymbolValue("SYS_RNWF_INTERFACE_MODE")

    if ((host == "SAME54X-pro") and (device == "WINCS02") and (interface == "SPI")):
        print("File : Host and Device are SUPPORTED - NC")
        symbol.setEnabled(True)
    else:
        print("File : Host and Device are NOT SUPPORTED")

def sysrnwfwifiRnwf11FilesEnable(symbol, event):
    print("sysrnwfwifirnwf11FilesEnable")
    data = symbol.getComponent()
    host = data.getSymbolValue("SYS_RNWF_HOST")
    device = data.getSymbolValue("SYS_RNWF_WIFI_DEVICE")
    interface = data.getSymbolValue("SYS_RNWF_INTERFACE_MODE")

    if ((host == "SAME54X-pro") and (device == "RNWF11") and (interface== "UART")):
        print("File : Host and Device are SUPPORTED - RN")
        symbol.setEnabled(True)
    else:
        print("File : Host and Device are NOT SUPPORTED")
		
def syswifiAdvancedConfMenuVisible(symbol, event):
    print("syswifiAdvancedConfMenuVisible")
    data = symbol.getComponent()
    host = data.getSymbolValue("SYS_RNWF_HOST")
    device = data.getSymbolValue("SYS_RNWF_WIFI_DEVICE")
    interface = data.getSymbolValue("SYS_RNWF_INTERFACE_MODE")

    if (((host == "SAME54X-pro") and (device == "RNWF02") and (interface== "UART") )  or ((host == "SAME54X-pro") and (device == "WINCS02") and (interface== "SPI"))):
        print("Menu : Host and Device are SUPPORTED - RN")
        symbol.setVisible(True)
    else:
        print("Menu : Host and Device are NOT SUPPORTED")


def syscomponentautoactivate(symbol, event):
    print("syscomponentautoactivate")
    data = symbol.getComponent()
    host = data.getSymbolValue("SYS_RNWF_HOST")
    device = data.getSymbolValue("SYS_RNWF_WIFI_DEVICE")
    interface = data.getSymbolValue("SYS_RNWF_INTERFACE_MODE")

    print("host      : "+str(host))
    print("device    : "+str(device))
    print("interface : "+str(interface))

    if ((host == "SAME54X-pro") and (device == "RNWF02")):
        print("Device Inf  WIFI Menu Visible.")
        symbol.setVisible(True)
    elif ((host == "SAME54X-pro") and (device == "WINCS02")):
        print("Device Inf  WIFI Menu Visible.")
        symbol.setVisible(True)
    elif ((host == "SAME54X-pro") and (device == "RNWF11")):
        print("Device Inf  WIFI Menu Visible.")
        symbol.setVisible(True)
    else:
        print("Device Inf  NOT visible")
        symbol.setVisible(False)


    if ((host == "SAME54X-pro") and (device == "RNWF02") and (interface == "UART")):
        print("Host and Device are SUPPORTED - RN")

        print("syscomponentautoactivate for RN ")
        if(Database.getComponentByID("BSP_SAM_E54_Xplained_Pro") == None):    
            res = Database.activateComponents(["BSP_SAM_E54_Xplained_Pro"])

        if(Database.getComponentByID("sercom2") == None):    
            res = Database.activateComponents(["sercom2"])
            Database.setSymbolValue("sercom2", "USART_RXPO", 1)
            setVal("sercom2", "USART_OPERATING_MODE", 2)
            Database.setSymbolValue("sercom2", "USART_TX_RING_BUFFER_SIZE", 4096)
            Database.setSymbolValue("sercom2", "USART_RX_RING_BUFFER_SIZE", 4096)

        if(Database.getComponentByID("sercom0") == None):    
            res = Database.activateComponents(["sercom0"])
            Database.setSymbolValue("sercom0", "USART_RXPO", 1)
            Database.setSymbolValue("sercom0", "USART_SFDE", True)
            Database.setSymbolValue("sercom0", "USART_BAUD_RATE", 230400)
            Database.setSymbolValue("sercom0", "USART_OPERATING_MODE", 2)

        if(Database.getComponentByID("HarmonyCore") == None):    
            res = Database.activateComponents(["HarmonyCore"])
            Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_PORTS", True)
            Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_RESET", True)

        Database.setSymbolValue("core","PIN_21_FUNCTION_TYPE","SERCOM0_PAD0")
        Database.setSymbolValue("core","PIN_22_FUNCTION_TYPE","SERCOM0_PAD1")
        Database.setSymbolValue("core","PIN_100_FUNCTION_TYPE","SERCOM2_PAD1")
        Database.setSymbolValue("core","PIN_101_FUNCTION_TYPE","SERCOM2_PAD0")       

        Database.setSymbolValue("core", "DMAC_ENABLE_CH_0", True)
        Database.setSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_0", "SERCOM0_Transmit")
        Database.setSymbolValue("core", "DMAC_ENABLE_CH_1", True)
        Database.setSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_1", "SERCOM0_Receive")
        Database.setSymbolValue("core", "DMAC_ENABLE_CH_2", True)
        Database.setSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_2", "SERCOM2_Transmit")


        if(Database.getComponentByID("sys_console") == None):    
            res = Database.activateComponents(["sys_console"])
        if(Database.getComponentByID("sys_console_0") == None):    
            res = Database.activateComponents(["sys_console_0"])
        if(Database.getComponentByID("sys_debug") == None):    
            res = Database.activateComponents(["sys_debug"])
            print("sys_debug_SYS_CONSOLE_dependency....")
            autoConnectTableCon = [[ "sys_console_0","sys_console" , "sys_debug", "sys_debug_SYS_CONSOLE_dependency"]]
            res = Database.connectDependencies(autoConnectTableCon)
            autoConnectTableuart = [[ "sys_console_0","sys_console_UART_dependency" , "sercom2", "SERCOM2_UART"]]
            res = Database.connectDependencies(autoConnectTableuart)

    elif ((host == "SAME54X-pro") and (device == "WINCS02") and (interface == "SPI")):
        print("Host and Device are SUPPORTED - NC")

        if(Database.getComponentByID("BSP_SAM_E54_Xplained_Pro") == None):    
            res = Database.activateComponents(["BSP_SAM_E54_Xplained_Pro"])

        if(Database.getComponentByID("sercom2") == None):    
            res = Database.activateComponents(["sercom2"])
            Database.setSymbolValue("sercom2", "USART_RXPO", 1)
            setVal("sercom2", "USART_OPERATING_MODE", 2)
            Database.setSymbolValue("sercom2", "USART_TX_RING_BUFFER_SIZE", 4096)
            Database.setSymbolValue("sercom2", "USART_RX_RING_BUFFER_SIZE", 4096)

        if(Database.getComponentByID("HarmonyCore") == None):    
            res = Database.activateComponents(["HarmonyCore"])
            Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_PORTS", True)
            Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_RESET", True)
            Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_INT", True)
            Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_DMA", True)

        

        if(Database.getComponentByID("sys_console") == None):    
            res = Database.activateComponents(["sys_console"])
        if(Database.getComponentByID("sys_console_0") == None):    
            res = Database.activateComponents(["sys_console_0"])
        if(Database.getComponentByID("sys_debug") == None):    
            res = Database.activateComponents(["sys_debug"])
            print("sys_debug_SYS_CONSOLE_dependency....")
            autoConnectTableCon = [[ "sys_console_0","sys_console" , "sys_debug", "sys_debug_SYS_CONSOLE_dependency"]]
            res = Database.connectDependencies(autoConnectTableCon)
            autoConnectTableuart = [[ "sys_console_0","sys_console_UART_dependency" , "sercom2", "SERCOM2_UART"]]
            res = Database.connectDependencies(autoConnectTableuart)

        Database.setSymbolValue("core", "DMAC_ENABLE_CH_2", True)
        Database.setSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_2", "SERCOM2_Transmit")

        Database.setSymbolValue("core","PIN_100_FUNCTION_TYPE","SERCOM2_PAD1")
        Database.setSymbolValue("core","PIN_101_FUNCTION_TYPE","SERCOM2_PAD0")


        if(Database.getComponentByID("sercom4") == None):    
            res = Database.activateComponents(["sercom4"])
            # Database.setSymbolValue("sercom2", "USART_RXPO", 1)
            setVal("sercom4", "SERCOM_MODE", 2)
            Database.setSymbolValue("sercom4", "SPI_DIPO", 3)


        if(Database.getComponentByID("drvWifiWincS02") == None):    
            res = Database.activateComponents(["drvWifiWincS02"])
            # Database.setSymbolValue("sercom2", "USART_RXPO", 1)
            # setVal("drvWifiWincS02", "SERCOM_MODE", 2)
            # Database.setSymbolValue("sercom4", "SPI_DIPO", 3)
            # Database.setSymbolValue("sercom2", "USART_RX_RING_BUFFER_SIZE", 4096)
        
        autoConnectTableCon = [[ "sercom4","SERCOM4_SPI" , "drvWifiWincS02","spi_dependency"]]
        res = Database.connectDependencies(autoConnectTableCon)

        if(Database.getComponentByID("EIC") == None):    
            res = Database.activateComponents(["EIC"])
            Database.setSymbolValue("eic", "EIC_CHAN_7", True)
            Database.setSymbolValue("eic", "EIC_INT_7", True)
            Database.setSymbolValue("eic", "EIC_CONFIG_SENSE_7", 2)

        
        Database.setSymbolValue("sys_time", "SYS_TIME_USE_SYSTICK", True)
        Database.setSymbolValue("drvWifiWincS02", "DRV_WIFI_WINC_TX_RX_DMA", True)
        # Database.setSymbolValue("drvWifiWincS02", "DRV_WIFI_WINC_INT_SRC", 0)
        # Database.setSymbolValue("drvWifiWincS02", "DRV_WIFI_WINC_EIC_SRC_7", True)

        Database.setSymbolValue("core","PIN_102_FUNCTION_TYPE","SERCOM4_PAD1")
        Database.setSymbolValue("core","PIN_103_FUNCTION_TYPE","SERCOM4_PAD0")
        Database.setSymbolValue("core","PIN_104_FUNCTION_TYPE","GPIO")
        Database.setSymbolValue("core","PIN_105_FUNCTION_TYPE","SERCOM4_PAD3")
        Database.setSymbolValue("core","PIN_18_FUNCTION_TYPE","EIC_EXTINT7")
        Database.setSymbolValue("core","PIN_19_FUNCTION_TYPE","GPIO")
        Database.setSymbolValue("core","PIN_23_FUNCTION_TYPE","GPIO")

        Database.setSymbolValue("core","PIN_104_FUNCTION_NAME","WDRV_WINC_SSN")
        Database.setSymbolValue("core","PIN_104_DIR","Out")
        Database.setSymbolValue("core","PIN_104_LAT","High")
        Database.setSymbolValue("core","PIN_19_FUNCTION_NAME","WDRV_WINC_CHIP_EN")
        Database.setSymbolValue("core","PIN_19_DIR","Out")
        Database.setSymbolValue("core","PIN_19_LAT","High")
        Database.setSymbolValue("core","PIN_23_FUNCTION_NAME","WDRV_WINC_RESETN")
        Database.setSymbolValue("core","PIN_23_DIR","Out")
        Database.setSymbolValue("core","PIN_23_INEN","True")
        Database.setSymbolValue("core","PIN_23_LAT","High")
        Database.setSymbolValue("core","PIN_18_FUNCTION_NAME","WDRV_WINC_INT")
        

        Database.setSymbolValue("core","XC32_HEAP_SIZE",80000)

    elif ((host == "SAME54X-pro") and (device == "RNWF11") and (interface == "UART")):
        print("Host and Device are SUPPORTED - RN")
        if(Database.getComponentByID("BSP_SAM_E54_Xplained_Pro") == None):    
            res = Database.activateComponents(["BSP_SAM_E54_Xplained_Pro"])

        if(Database.getComponentByID("sercom2") == None):    
            res = Database.activateComponents(["sercom2"])
            Database.setSymbolValue("sercom2", "USART_RXPO", 1)
            setVal("sercom2", "USART_OPERATING_MODE", 2)
            Database.setSymbolValue("sercom2", "USART_TX_RING_BUFFER_SIZE", 4096)
            Database.setSymbolValue("sercom2", "USART_RX_RING_BUFFER_SIZE", 4096)
        if(Database.getComponentByID("sercom0") == None):    
            res = Database.activateComponents(["sercom0"])
            Database.setSymbolValue("sercom0", "USART_RXPO", 1)
            Database.setSymbolValue("sercom0", "USART_SFDE", True)
            Database.setSymbolValue("sercom0", "USART_BAUD_RATE", 230400)
            Database.setSymbolValue("sercom0", "USART_OPERATING_MODE", 2)

        if(Database.getComponentByID("HarmonyCore") == None):    
            res = Database.activateComponents(["HarmonyCore"])
            Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_PORTS", True)
            Database.setSymbolValue("HarmonyCore", "ENABLE_SYS_RESET", True)

        Database.setSymbolValue("core","PIN_21_FUNCTION_TYPE","SERCOM0_PAD0")
        Database.setSymbolValue("core","PIN_22_FUNCTION_TYPE","SERCOM0_PAD1")
        Database.setSymbolValue("core","PIN_100_FUNCTION_TYPE","SERCOM2_PAD1")
        Database.setSymbolValue("core","PIN_101_FUNCTION_TYPE","SERCOM2_PAD0")       

        Database.setSymbolValue("core", "DMAC_ENABLE_CH_0", True)
        Database.setSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_0", "SERCOM0_Transmit")
        Database.setSymbolValue("core", "DMAC_ENABLE_CH_1", True)
        Database.setSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_1", "SERCOM0_Receive")
        Database.setSymbolValue("core", "DMAC_ENABLE_CH_2", True)
        Database.setSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_2", "SERCOM2_Transmit")


        if(Database.getComponentByID("sys_console") == None):    
            res = Database.activateComponents(["sys_console"])
        if(Database.getComponentByID("sys_console_0") == None):    
            res = Database.activateComponents(["sys_console_0"])
        if(Database.getComponentByID("sys_debug") == None):    
            res = Database.activateComponents(["sys_debug"])
            print("sys_debug_SYS_CONSOLE_dependency....")
            autoConnectTableCon = [[ "sys_console_0","sys_console" , "sys_debug", "sys_debug_SYS_CONSOLE_dependency"]]
            res = Database.connectDependencies(autoConnectTableCon)
            autoConnectTableuart = [[ "sys_console_0","sys_console_UART_dependency" , "sercom2", "SERCOM2_UART"]]
            res = Database.connectDependencies(autoConnectTableuart)

        res = Database.activateComponents(["sysEccRNWF"])
        res = Database.activateComponents(["sys_time"])
        res = Database.activateComponents(["tc0"])
        autoConnectTabletc0 = [["tc0","TC0_TMR" , "sys_time", "sys_time_TMR_dependency"]]
        res = Database.connectDependencies(autoConnectTabletc0)


    else:
        print("Host and Device are NOT SUPPORTED")



def syswifiautoInclude(symbol, event):
    if(Database.getComponentByID("sysWifiRNWF") == None):    
        res = Database.activateComponents(["sysWifiRNWF"])
def syswifiprovautoInclude(symbol, event):
    if (event["value"] == True):
        if(Database.getComponentByID("sysWifiProvRNWF") == None):    
            res = Database.activateComponents(["sysWifiProvRNWF"])
        if(Database.getComponentByID("sysNetRNWF") == None):    
            Database.setSymbolValue("sysWifiRNWF", "SYS_RNWF_NET_SER_ENABLE", True)
            res = Database.activateComponents(["sysNetRNWF"]) 
    if (event["value"] == False):
        res = Database.deactivateComponents(["sysWifiProvRNWF"])
def sysmqttautoInclude(symbol, event):
    if (event["value"] == True):
        if(Database.getComponentByID("sysMqttRNWF") == None):    
            res = Database.activateComponents(["sysMqttRNWF"])
    if (event["value"] == False):
        res = Database.deactivateComponents(["sysMqttRNWF"])
def sysnetautoInclude(symbol, event):
    if (event["value"] == True):
        if(Database.getComponentByID("sysNetRNWF") == None):    
            res = Database.activateComponents(["sysNetRNWF"])
    if (event["value"] == False):
        res = Database.deactivateComponents(["sysNetRNWF"])
def sysotaautoInclude(symbol, event):
    if (event["value"] == True):
        if(Database.getComponentByID("sysOtaRNWF") == None):    
            res = Database.activateComponents(["sysOtaRNWF"])
        if(Database.getComponentByID("sysNetRNWF") == None):    
            Database.setSymbolValue("sysWifiRNWF", "SYS_RNWF_NET_SER_ENABLE", True)
            res = Database.activateComponents(["sysNetRNWF"]) 
    if (event["value"] == False):
        res = Database.deactivateComponents(["sysOtaRNWF"])

def syswifiSTAautoMenu(symbol, event):
    print("syswifiSTAautoMenu")
    
def syswifiAPautoMenu(symbol, event):
    print("syswifiAPautoMenu")
 
def destroyComponent(component):
    print("destroyComponent")
