######################  RNWF Wireless System Services  ######################
def loadModule():
    print('Load Module: RNWF Wireless System Services')

    sysWifiRNWFComponent = Module.CreateComponent('sysWifiRNWF', 'RNWF WINCS Wi-Fi Service','/Wireless/System Services/', 'system/Wifi/config/sys_wifi.py')
    
    sysWifiProvRNWFComponent = Module.CreateComponent('sysWifiProvRNWF', 'RNWF WINCS Wi-Fi Provisioning Service', '/Wireless/System Services/', 'system/Wifiprov/config/sys_wifiprov.py')
    
    sysMQTTRNWFComponent = Module.CreateComponent('sysMqttRNWF', 'RNWF WINCS Mqtt Service', '/Wireless/System Services/', 'system/Mqtt/config/sys_mqtt.py')
    
    sysOTARNWFComponent = Module.CreateComponent('sysOtaRNWF', 'RNWF WINCS Ota Service', '/Wireless/System Services/', 'system/Ota/config/sys_ota.py')

    ########################## Harmony Network Net Service #################################    
    sysNetRNWFComponent = Module.CreateComponent("sysNetRNWF", "RNWF WINCS Net Service", "/Wireless/System Services/","system/Net/config/sys_net.py")

