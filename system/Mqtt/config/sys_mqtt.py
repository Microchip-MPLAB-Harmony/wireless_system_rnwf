# coding: utf-8
"""*****************************************************************************
Copyright (C) 2020-2021 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*****************************************************************************"""

################################################################################
#### Global Variables ####
################################################################################
global mqtt_helpkeyword
sysrnwfMqttSubTopicInstance = []
sysrnwfMqttAzureSubQos = []
sysrnwfMqttMaxTopic = 5
sysmqttTopicNumPrev = 1

mqtt_helpkeyword = "mcc_h3_RNWF_mqtt_system_service_configurations"
################################################################################
#### Business Logic ####
################################################################################

################################################################################
#### Component ####
################################################################################
def instantiateComponent(sysMQTTComponent):
    global mqtt_helpkeyword

    # Basic Configuration
    sysMqttEnableCloudCons = sysMQTTComponent.createMenuSymbol("SYS_RNWF_MQTT_CLOUD_CONF", None)
    sysMqttEnableCloudCons.setLabel("Cloud Configuration")
    sysMqttEnableCloudCons.setHelp(mqtt_helpkeyword)
    sysMqttEnableCloudCons.setVisible(True)
		
    sysmqttBrokerName = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_CLOUD_URL", sysMqttEnableCloudCons)
    sysmqttBrokerName.setLabel("Cloud URL")
    sysmqttBrokerName.setHelp(mqtt_helpkeyword)
    sysmqttBrokerName.setVisible(True)
    sysmqttBrokerName.setDescription(" Configure Cloud provider endpoint / MQTT Broker URL")
    sysmqttBrokerName.setDefaultValue("")
    sysmqttBrokerName.setDependencies(mqttSNIAutoMenu, ["SYS_RNWF_MQTT_CLOUD_URL"])

    sysmqttPort = sysMQTTComponent.createIntegerSymbol("SYS_RNWF_MQTT_CLOUD_PORT", sysMqttEnableCloudCons)
    sysmqttPort.setLabel("Cloud Port")
    sysmqttPort.setHelp(mqtt_helpkeyword)
    sysmqttPort.setMin(1)
    sysmqttPort.setMax(65535)
    sysmqttPort.setDescription("Configure Cloud/MQTT port")
    sysmqttPort.setDefaultValue(8883)

    sysMqttAzureDpsEnable = sysMQTTComponent.createBooleanSymbol("SYS_RNWF_MQTT_AZURE_DPS_ENABLE", sysMqttEnableCloudCons)
    sysMqttAzureDpsEnable.setLabel("Azure DPS Enable")
    sysMqttAzureDpsEnable.setHelp(mqtt_helpkeyword)
    sysMqttAzureDpsEnable.setVisible(True)
    sysMqttAzureDpsEnable.setDefaultValue(False)  

    sysmqttScopeId = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_SCOPE_ID", sysMqttAzureDpsEnable)
    sysmqttScopeId.setLabel("Scope Id")
    sysmqttScopeId.setHelp(mqtt_helpkeyword)
    sysmqttScopeId.setVisible(False)
    sysmqttScopeId.setDescription(" Provide Scope ID from Azure IoT Central portal for registered device")
    sysmqttScopeId.setDefaultValue("")
    sysmqttScopeId.setDependencies(sysMqttSubMenuVisible, ["SYS_RNWF_MQTT_AZURE_DPS_ENABLE"])

    sysmqttDeviceTemplate = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_DEVICE_TEMPLATE", sysMqttAzureDpsEnable)
    sysmqttDeviceTemplate.setLabel("Device Template")
    sysmqttDeviceTemplate.setHelp(mqtt_helpkeyword)
    sysmqttDeviceTemplate.setVisible(False)
    sysmqttDeviceTemplate.setDescription("Configure Cloud DPS specific device template")
    sysmqttDeviceTemplate.setDefaultValue("")
    sysmqttDeviceTemplate.setDependencies(sysMqttSubMenuVisible, ["SYS_RNWF_MQTT_AZURE_DPS_ENABLE"])

    sysmqttUserName = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_CLOUD_USER_NAME", sysMqttEnableCloudCons)
    sysmqttUserName.setLabel("User Name")
    sysmqttUserName.setHelp(mqtt_helpkeyword)
    sysmqttUserName.setVisible(True)
    sysmqttUserName.setDescription("Configure Cloud Client user name")
    sysmqttUserName.setDefaultValue("")

    sysmqttPassword = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_PASSWORD", sysMqttEnableCloudCons)
    sysmqttPassword.setLabel("Password")
    sysmqttPassword.setHelp(mqtt_helpkeyword)
    sysmqttPassword.setVisible(True)
    sysmqttPassword.setDescription("Enter the cloud client password")
    sysmqttPassword.setDefaultValue("")

    sysmqttClientId = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_CLIENT_ID", sysMqttEnableCloudCons)
    sysmqttClientId.setLabel("Client Id")
    sysmqttClientId.setHelp(mqtt_helpkeyword)
    sysmqttClientId.setVisible(True)
    sysmqttClientId.setDescription("MQTT Client Id which should be unique for the MQTT Broker. If empty, the id will be randomly generated")
    sysmqttClientId.setDefaultValue("rnwf02_device_01")

    sysmqttversion = sysMQTTComponent.createComboSymbol("SYS_RNWF_MQTT_VERSION", sysMqttEnableCloudCons, ["V3.1.1", "V5"])
    sysmqttversion.setLabel("MQTT Protocol version")
    sysmqttversion.setHelp(mqtt_helpkeyword)
    sysmqttversion.setDescription("Enter MQTT Protocol version")
    sysmqttversion.setDefaultValue("V3.1.1")
    sysMqttAzurePublish = sysMQTTComponent.createBooleanSymbol("SYS_RNWF_MQTT_AZURE_PUBLISH", sysMqttEnableCloudCons)
    sysMqttAzurePublish.setLabel("Publish")
    sysMqttAzurePublish.setHelp(mqtt_helpkeyword)
    sysMqttAzurePublish.setVisible(True)
    sysMqttAzurePublish.setDefaultValue(False) 

    sysmqttPubTopicName = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_PUB_TOPIC_NAME", sysMqttAzurePublish)
    sysmqttPubTopicName.setLabel("Publish Topic Name")
    sysmqttPubTopicName.setHelp(mqtt_helpkeyword)
    sysmqttPubTopicName.setVisible(False)
    sysmqttPubTopicName.setDescription("Enter the cloud client password")
    sysmqttPubTopicName.setDefaultValue("")
    sysmqttPubTopicName.setDependencies(sysMqttSubMenuVisible, ["SYS_RNWF_MQTT_AZURE_PUBLISH"])

    sysMqttQosType = sysMQTTComponent.createComboSymbol("SYS_RNWF_MQTT_QOS_TYPE", sysMqttAzurePublish , ["QOS0", "QOS1" , "QOS2"])
    sysMqttQosType.setLabel("Pub. QoS")
    sysMqttQosType.setHelp(mqtt_helpkeyword)
    sysMqttQosType.setVisible(False)
    sysMqttQosType.setDescription("QoS type for the message ::RNWF_MQTT_QOS_t")
    sysMqttQosType.setDefaultValue("QOS0")
    sysMqttQosType.setDependencies(sysMqttSubMenuVisible, ["SYS_RNWF_MQTT_AZURE_PUBLISH"])

    sysMqttAzureRetainFlag = sysMQTTComponent.createBooleanSymbol("SYS_RNWF_MQTT_AZURE_RETAIN_FLAG", sysMqttAzurePublish)
    sysMqttAzureRetainFlag.setLabel("Retain Flag")
    sysMqttAzureRetainFlag.setHelp(mqtt_helpkeyword)
    sysMqttAzureRetainFlag.setVisible(False)
    sysMqttAzureRetainFlag.setDefaultValue(False) 
    sysMqttAzureRetainFlag.setDependencies(sysMqttSubMenuVisible, ["SYS_RNWF_MQTT_AZURE_PUBLISH"])
    
    sysMqttAzureKeepAlive = sysMQTTComponent.createBooleanSymbol("SYS_RNWF_MQTT_AZURE_KEEP_ALIVE", sysMqttEnableCloudCons)
    sysMqttAzureKeepAlive.setLabel("Keep Alive")
    sysMqttAzureKeepAlive.setHelp(mqtt_helpkeyword)
    sysMqttAzureKeepAlive.setVisible(True)
    sysMqttAzureKeepAlive.setDefaultValue(False)

    sysMqttAzureKeepAliveInt = sysMQTTComponent.createIntegerSymbol("SYS_RNWF_MQTT_KEEP_ALIVE_INT", sysMqttAzureKeepAlive)
    sysMqttAzureKeepAliveInt.setLabel("Keep Alive Interval")
    sysMqttAzureKeepAliveInt.setHelp(mqtt_helpkeyword)
    sysMqttAzureKeepAliveInt.setVisible(False)
    sysMqttAzureKeepAliveInt.setDescription("Configure the field in the range of 1-1000 (in seconds)")
    sysMqttAzureKeepAliveInt.setMin(0)
    sysMqttAzureKeepAliveInt.setMax(10000)
    sysMqttAzureKeepAliveInt.setDefaultValue(60)
    sysMqttAzureKeepAliveInt.setDependencies(sysMqttSubMenuVisible, ["SYS_RNWF_MQTT_AZURE_KEEP_ALIVE"])

    sysMqttLwtEnable = sysMQTTComponent.createBooleanSymbol("SYS_RNWF_MQTT_LWT_ENABLE", sysMqttEnableCloudCons)
    sysMqttLwtEnable.setLabel("Last Will and Testament(LWT) ")
    sysMqttLwtEnable.setHelp(mqtt_helpkeyword)
    sysMqttLwtEnable.setVisible(True)
    sysMqttLwtEnable.setDefaultValue(False)

    sysMqttLwtMessage = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_LWT_MESSAGE", sysMqttLwtEnable)
    sysMqttLwtMessage.setLabel("LWT Message ")
    sysMqttLwtMessage.setHelp(mqtt_helpkeyword)
    sysMqttLwtMessage.setVisible(False)
    sysMqttLwtMessage.setDescription("LWT Message ")
    sysMqttLwtMessage.setDefaultValue("Disconnecting ....Bye")
    sysMqttLwtMessage.setDependencies(sysMqttSubMenuVisible, ["SYS_RNWF_MQTT_LWT_ENABLE"])

    sysMqttAzureSubscribe = sysMQTTComponent.createBooleanSymbol("SYS_RNWF_MQTT_AZURE_SUBSCRIBE", sysMqttEnableCloudCons)
    sysMqttAzureSubscribe.setLabel("Subscribe")
    sysMqttAzureSubscribe.setHelp(mqtt_helpkeyword)
    sysMqttAzureSubscribe.setVisible(True)
    sysMqttAzureSubscribe.setDefaultValue(False) 

    sysMqttAzureTotalSubTopics = sysMQTTComponent.createIntegerSymbol("SYS_RNWF_MQTT_TOTAL_SUB_TOPICS", sysMqttAzureSubscribe)
    sysMqttAzureTotalSubTopics.setLabel("Total Subscribe Topics")
    sysMqttAzureTotalSubTopics.setHelp(mqtt_helpkeyword)
    sysMqttAzureTotalSubTopics.setVisible(False)
    sysMqttAzureTotalSubTopics.setDescription("Number of subscribe tipics (1 to 5)")
    sysMqttAzureTotalSubTopics.setMin(1)
    sysMqttAzureTotalSubTopics.setMax(sysrnwfMqttMaxTopic)
    sysMqttAzureTotalSubTopics.setDefaultValue(3)
    sysMqttAzureTotalSubTopics.setDependencies(sysMqttSubMenuVisible, ["SYS_RNWF_MQTT_AZURE_SUBSCRIBE"])


    # Get Size of Each Slot
    for slot in range(0,sysrnwfMqttMaxTopic):
       sysrnwfMqttSubTopicInstance.append(sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_SUB_TOPIC"+str(slot),sysMqttAzureTotalSubTopics))
       sysrnwfMqttSubTopicInstance[slot].setLabel("Sub Topic "+ str(slot))
       sysMqttAzureTotalSubTopics.setHelp(mqtt_helpkeyword)
       print(sysMqttAzureTotalSubTopics.getValue())

       if (slot < sysMqttAzureTotalSubTopics.getValue()):
            sysrnwfMqttSubTopicInstance[slot].setVisible(True)
       else:
            sysrnwfMqttSubTopicInstance[slot].setVisible(False)
       sysrnwfMqttSubTopicInstance[slot].setDependencies(sysmqttTopicInstanceEnable,["SYS_RNWF_MQTT_AZURE_SUBSCRIBE","SYS_RNWF_MQTT_TOTAL_SUB_TOPICS"])


    sysMqttAzureSubQos = sysMQTTComponent.createComboSymbol("SYS_RNWF_MQTT_SUB_QOS_TYPE", sysMqttAzureSubscribe , ["QOS0", "QOS1" , "QOS2"])
    sysMqttAzureSubQos.setLabel("Sub. QoS")
    sysMqttAzureSubQos.setHelp(mqtt_helpkeyword)
    sysMqttAzureSubQos.setVisible(False)
    sysMqttAzureSubQos.setDescription("QoS type for the message ::RNWF_MQTT_QOS_t")
    sysMqttAzureSubQos.setDefaultValue("QOS0")
    sysMqttAzureSubQos.setDependencies(sysMqttSubMenuVisible, ["SYS_RNWF_MQTT_AZURE_SUBSCRIBE"])

    sysMqttAzureEnableTls = sysMQTTComponent.createBooleanSymbol("SYS_MQTT_AZURE_ENABLE_TLS", sysMqttEnableCloudCons)
    sysMqttAzureEnableTls.setLabel("Enable TLS")
    sysMqttAzureEnableTls.setHelp(mqtt_helpkeyword)
    sysMqttAzureEnableTls.setVisible(True)
    sysMqttAzureEnableTls.setDefaultValue(False)

    sysMqttTlsPeeerAuth = sysMQTTComponent.createBooleanSymbol("SYS_MQTT_AZURE_ENABLE_PEER_AUTH", sysMqttAzureEnableTls)
    sysMqttTlsPeeerAuth.setLabel("Peer authentication")
    sysMqttTlsPeeerAuth.setHelp(mqtt_helpkeyword)
    sysMqttTlsPeeerAuth.setVisible(False)
    sysMqttTlsPeeerAuth.setDefaultValue(False)
    sysMqttTlsPeeerAuth.setDependencies(sysMqttSubMenuVisible, ["SYS_MQTT_AZURE_ENABLE_TLS"])
    sysMqttTlsServerCert = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_SERVER_CERT", sysMqttTlsPeeerAuth)
    sysMqttTlsServerCert.setLabel("Root CA")
    sysMqttTlsServerCert.setHelp(mqtt_helpkeyword)
    sysMqttTlsServerCert.setVisible(False)
    sysMqttTlsServerCert.setDescription("TLS Server Certificate Name")
    sysMqttTlsServerCert.setDefaultValue("")
    sysMqttTlsServerCert.setDependencies(sysMqttSubMenuVisible, ["SYS_MQTT_AZURE_ENABLE_TLS"])
    
    sysMqttTlsDeviceCert = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_DEVICE_CERT", sysMqttAzureEnableTls)
    sysMqttTlsDeviceCert.setLabel("Device Certificate")
    sysMqttTlsDeviceCert.setHelp(mqtt_helpkeyword)
    sysMqttTlsDeviceCert.setVisible(False)
    sysMqttTlsDeviceCert.setDescription("TLS Device Certificate Name")
    sysMqttTlsDeviceCert.setDefaultValue("")
    sysMqttTlsDeviceCert.setDependencies(sysMqttSubMenuVisible, ["SYS_MQTT_AZURE_ENABLE_TLS"])

    sysMqttTlsDeviceKey = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_DEVICE_KEY", sysMqttAzureEnableTls)
    sysMqttTlsDeviceKey.setLabel("Device Key")
    sysMqttTlsDeviceKey.setHelp(mqtt_helpkeyword)
    sysMqttTlsDeviceKey.setVisible(False)
    sysMqttTlsDeviceKey.setDescription("TLS Device Key")
    sysMqttTlsDeviceKey.setDefaultValue("")
    sysMqttTlsDeviceKey.setDependencies(sysMqttSubMenuVisible, ["SYS_MQTT_AZURE_ENABLE_TLS"])  

    sysMqttTlsDeviceKeyPassword = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_DEVICE_KEY_PSK", sysMqttAzureEnableTls)
    sysMqttTlsDeviceKeyPassword.setLabel("Device Key Password")
    sysMqttTlsDeviceKeyPassword.setHelp(mqtt_helpkeyword)
    sysMqttTlsDeviceKeyPassword.setVisible(False)
    sysMqttTlsDeviceKeyPassword.setDescription("TLS Device Key Password")
    sysMqttTlsDeviceKeyPassword.setDefaultValue("")
    sysMqttTlsDeviceKeyPassword.setDependencies(sysMqttSubMenuVisible, ["SYS_MQTT_AZURE_ENABLE_TLS"]) 
    
    sysMqttTlsServerName = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_TLS_SERVER_NAME", sysMqttAzureEnableTls)
    sysMqttTlsServerName.setLabel("Server Name")
    sysMqttTlsServerName.setHelp(mqtt_helpkeyword)
    sysMqttTlsServerName.setVisible(False)
    sysMqttTlsServerName.setDescription("TLS Server name")
    sysMqttTlsServerName.setDefaultValue("")
    sysMqttTlsServerName.setDependencies(sysMqttSubMenuVisible, ["SYS_MQTT_AZURE_ENABLE_TLS"])

    sysrnwfMqttTlsDomainNameverify = sysMQTTComponent.createBooleanSymbol("SYS_MQTT_AZURE_DOMAIN_NAME_VERIFY", sysMqttAzureEnableTls)
    sysrnwfMqttTlsDomainNameverify.setLabel("Domain Name Verify")
    sysrnwfMqttTlsDomainNameverify.setHelp(mqtt_helpkeyword)
    sysrnwfMqttTlsDomainNameverify.setVisible(False)
    sysrnwfMqttTlsDomainNameverify.setDefaultValue(False)
    sysrnwfMqttTlsDomainNameverify.setDependencies(sysMqttSubMenuVisible, ["SYS_MQTT_AZURE_ENABLE_TLS"])

    
    sysMqttTlsDomainName = sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_TLS_DOMAIN_NAME", sysMqttAzureEnableTls)
    sysMqttTlsDomainName.setLabel("Domain Name")
    sysMqttTlsDomainName.setHelp(mqtt_helpkeyword)
    sysMqttTlsDomainName.setVisible(False)
    sysMqttTlsDomainName.setDescription("TLS Domain name")
    sysMqttTlsDomainName.setDefaultValue("")
    sysMqttTlsDomainName.setDependencies(sysMqttSubMenuVisible, ["SYS_MQTT_AZURE_ENABLE_TLS"])

    sysmqttadvancedconfigurations = sysMQTTComponent.createCommentSymbol("SYS_RNWF_ADV_CONF", None)
    sysmqttadvancedconfigurations.setLabel("Advanced Configurations ")
    sysmqttadvancedconfigurations.setHelp(mqtt_helpkeyword)

    sysmqttdebuglogs = sysMQTTComponent.createBooleanSymbol("SYS_RNWF_MQTT_DEBUG_LOGS", sysmqttadvancedconfigurations)
    sysmqttdebuglogs.setLabel("MQTT Debug logs")
    sysmqttdebuglogs.setHelp(mqtt_helpkeyword)
    sysmqttdebuglogs.setDefaultValue(False)
    sysmqttdebuglogs.setDescription("Select to enable MQTT service debug logs ")

    sysmqttCallbackHandler= sysMQTTComponent.createStringSymbol("SYS_RNWF_MQTT_CALLBACK_HANDLER", None)
    sysmqttCallbackHandler.setLabel("MQTT Callback Handler ")
    sysmqttCallbackHandler.setHelp(mqtt_helpkeyword)
    sysmqttCallbackHandler.setVisible(True)
    sysmqttCallbackHandler.setDescription("MQTT Callback Handler ")
    sysmqttCallbackHandler.setDefaultValue("APP_MQTT_Callback")

    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    sysrnwfmqttHeaderFile = sysMQTTComponent.createFileSymbol("SYS_RNWF_MQTT_HEADER", None)
    sysrnwfmqttHeaderFile.setSourcePath("system/Mqtt/templates/sys_rnwf02_mqtt_service.h.ftl")
    sysrnwfmqttHeaderFile.setOutputName("sys_rnwf_mqtt_service.h")
    sysrnwfmqttHeaderFile.setDestPath("system/mqtt/")
    sysrnwfmqttHeaderFile.setProjectPath("config/" + configName + "/system/mqtt/")
    sysrnwfmqttHeaderFile.setType("HEADER")
    sysrnwfmqttHeaderFile.setOverwrite(True)
    sysrnwfmqttHeaderFile.setEnabled(False)
    sysrnwfmqttHeaderFile.setDependencies(sysrnwf02mqttFilesEnable, ["sysWifiRNWF.SYS_RNWF_MQTT_ENABLE"])

    print("Mqtt Service Component Header Path %s", sysrnwfmqttHeaderFile.getProjectPath())
	
    sysrnwfmqttSourceFile = sysMQTTComponent.createFileSymbol("SYS_RNWF_MQTT_SOURCE", None)
    sysrnwfmqttSourceFile.setSourcePath("system/Mqtt/templates/src/sys_rnwf02_mqtt_service.c.ftl")
    sysrnwfmqttSourceFile.setOutputName("sys_rnwf_mqtt_service.c")
    sysrnwfmqttSourceFile.setDestPath("system/mqtt/src")
    sysrnwfmqttSourceFile.setProjectPath("config/" + configName + "/system/mqtt/")
    sysrnwfmqttSourceFile.setType("SOURCE")
    sysrnwfmqttSourceFile.setOverwrite(True)
    sysrnwfmqttSourceFile.setEnabled(False)
    sysrnwfmqttSourceFile.setDependencies(sysrnwf02mqttFilesEnable, ["sysWifiRNWF.SYS_RNWF_MQTT_ENABLE"])

    sysrnwfmqttSystemConfigFile = sysMQTTComponent.createFileSymbol("SYS_RNWF_CONSOLE_SYS_CONFIG", None)
    sysrnwfmqttSystemConfigFile.setType("STRING")
    sysrnwfmqttSystemConfigFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION")
    sysrnwfmqttSystemConfigFile.setSourcePath("system/Mqtt/templates/system/system_config_rnwf02.h.ftl")
    sysrnwfmqttSystemConfigFile.setMarkup(True)
    sysrnwfmqttSystemConfigFile.setOverwrite(True)
    sysrnwfmqttSystemConfigFile.setEnabled(False)
    sysrnwfmqttSystemConfigFile.setDependencies(sysrnwf02mqttFilesEnable, ["sysWifiRNWF.SYS_RNWF_MQTT_ENABLE"])


		
    ### WINCS02 Code #######

    sysrnwfmqttWincs02HeaderFile = sysMQTTComponent.createFileSymbol("SYS_RNWF_WINCS02_MQTT_HEADER", None)
    sysrnwfmqttWincs02HeaderFile.setSourcePath("system/Mqtt/templates/sys_wincs02_mqtt_service.h.ftl")
    sysrnwfmqttWincs02HeaderFile.setOutputName("sys_wincs_mqtt_service.h")
    sysrnwfmqttWincs02HeaderFile.setDestPath("system/mqtt/")
    sysrnwfmqttWincs02HeaderFile.setProjectPath("config/" + configName + "/system/mqtt/")
    sysrnwfmqttWincs02HeaderFile.setType("HEADER")
    sysrnwfmqttWincs02HeaderFile.setMarkup(True)
    sysrnwfmqttWincs02HeaderFile.setOverwrite(True)
    sysrnwfmqttWincs02HeaderFile.setEnabled(False)
    sysrnwfmqttWincs02HeaderFile.setDependencies(syswincs02mqttFilesEnable, ["sysWifiRNWF.SYS_RNWF_MQTT_ENABLE"])

    sysrnwfmqttWincSourceFile = sysMQTTComponent.createFileSymbol("SYS_RNWF_WINCS02_MQTT_SOURCE", None)
    sysrnwfmqttWincSourceFile.setSourcePath("system/Mqtt/templates/src/sys_wincs02_mqtt_service.c.ftl")
    sysrnwfmqttWincSourceFile.setOutputName("sys_wincs_mqtt_service.c")
    sysrnwfmqttWincSourceFile.setDestPath("system/mqtt/src")
    sysrnwfmqttWincSourceFile.setProjectPath("config/" + configName + "/system/mqtt/")
    sysrnwfmqttWincSourceFile.setType("SOURCE")
    sysrnwfmqttWincSourceFile.setMarkup(True)
    sysrnwfmqttWincSourceFile.setOverwrite(True)
    sysrnwfmqttWincSourceFile.setEnabled(False)
    sysrnwfmqttWincSourceFile.setDependencies(syswincs02mqttFilesEnable, ["sysWifiRNWF.SYS_RNWF_MQTT_ENABLE"])


    syswincsmqttSystemConfigFile = sysMQTTComponent.createFileSymbol("SYS_WINCS_CONSOLE_SYS_CONFIG", None)
    syswincsmqttSystemConfigFile.setType("STRING")
    syswincsmqttSystemConfigFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION")
    syswincsmqttSystemConfigFile.setSourcePath("system/Mqtt/templates/system/system_config_wincs02.h.ftl")
    syswincsmqttSystemConfigFile.setMarkup(True)
    syswincsmqttSystemConfigFile.setOverwrite(True)
    syswincsmqttSystemConfigFile.setEnabled(False)
    syswincsmqttSystemConfigFile.setDependencies(syswincs02mqttFilesEnable, ["sysWifiRNWF.SYS_RNWF_MQTT_ENABLE"])

    sysrnwfmqttRnwf11HeaderFile = sysMQTTComponent.createFileSymbol("SYS_RNWF11_MQTT_HEADER", None)
    sysrnwfmqttRnwf11HeaderFile.setSourcePath("system/Mqtt/templates/sys_rnwf11_mqtt_service.h.ftl")
    sysrnwfmqttRnwf11HeaderFile.setOutputName("sys_rnwf_mqtt_service.h")
    sysrnwfmqttRnwf11HeaderFile.setDestPath("system/mqtt/")
    sysrnwfmqttRnwf11HeaderFile.setProjectPath("config/" + configName + "/system/mqtt/")
    sysrnwfmqttRnwf11HeaderFile.setType("HEADER")
    sysrnwfmqttRnwf11HeaderFile.setOverwrite(True)
    sysrnwfmqttRnwf11HeaderFile.setEnabled(False)
    sysrnwfmqttRnwf11HeaderFile.setDependencies(sysrnwfmqttRnwf11FilesEnable, ["sysWifiRNWF.SYS_RNWF_MQTT_ENABLE"])

    sysrnwfmqttRnwf11SourceFile = sysMQTTComponent.createFileSymbol("SYS_RNWF11_MQTT_SOURCE", None)
    sysrnwfmqttRnwf11SourceFile.setSourcePath("system/Mqtt/templates/src/sys_rnwf11_mqtt_service.c.ftl")
    sysrnwfmqttRnwf11SourceFile.setOutputName("sys_rnwf_mqtt_service.c")
    sysrnwfmqttRnwf11SourceFile.setDestPath("system/mqtt/src")
    sysrnwfmqttRnwf11SourceFile.setProjectPath("config/" + configName + "/system/mqtt/")
    sysrnwfmqttRnwf11SourceFile.setType("SOURCE")
    sysrnwfmqttRnwf11SourceFile.setOverwrite(True)
    sysrnwfmqttRnwf11SourceFile.setEnabled(False)
    sysrnwfmqttRnwf11SourceFile.setDependencies(sysrnwfmqttRnwf11FilesEnable, ["sysWifiRNWF.SYS_RNWF_MQTT_ENABLE"])
############################################################################
#### Dependency ####
############################################################################


def sysmqttTopicInstanceEnable(symbol, event):
    global sysmqttTopicNumPrev
    print("Start sysmqttTopicInstanceEnable")
    if(event["id"] == "SYS_RNWF_MQTT_AZURE_SUBSCRIBE"):
        mqttTopicEnable = Database.getSymbolValue("sysrnwfMqttAzureSubscribe","SYS_RNWF_MQTT_AZURE_SUBSCRIBE")
        fileIndex = int(symbol.getID().strip("SYS_RNWF_MQTT_SUB_TOPIC"))
        print("File Slot " + str(fileIndex))
        print(sysmqttTopicNumPrev)
        if(mqttTopicEnable == True):
            if(fileIndex < sysmqttTopicNumPrev ):
                symbol.setVisible(True)
        else:
            symbol.setVisible(False)
 
    else:
        print(symbol.getID())
        print(event["id"])
        sysmqttTopicNumValue = event["value"]
        print(sysmqttTopicNumValue)
        print(sysmqttTopicNumPrev)
        if (sysmqttTopicNumValue > sysmqttTopicNumPrev):
            sysrnwfMqttSubTopicInstance[sysmqttTopicNumPrev].setVisible(True)
            sysrnwfMqttSubTopicInstance[sysmqttTopicNumPrev].setValue("")
            sysmqttTopicNumPrev = sysmqttTopicNumPrev + 1
        else:
            if(sysmqttTopicNumValue < sysmqttTopicNumPrev):
                sysmqttTopicNumPrev = sysmqttTopicNumPrev - 1
                sysrnwfMqttSubTopicInstance[sysmqttTopicNumPrev].setVisible(False)
                sysrnwfMqttSubTopicInstance[sysmqttTopicNumPrev].setValue("")
                print("Set False " + str(sysmqttTopicNumPrev))
 
            else:
                print("Do Nothing "+ str(sysmqttTopicNumPrev))
    print("END sysmqttTopicInstanceEnable")



def sysrnwf02mqttFilesEnable(symbol, event):
    print("mqtt sysrnwfwifirnwf02FilesEnable")
    if(Database.getComponentByID("sysWifiRNWF") == None):
        print("mqtt NONE  sysrnwfwifiRnwf02FilesEnable1")

    host = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_HOST")
    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    if ((host == "SAME54X-pro") and (device == "RNWF02") and (interface== "UART")):
        print("mqtt File : Host and Device are SUPPORTED - RN")
        symbol.setEnabled(True)
    else:
        print("mqtt File : Host and Device are NOT SUPPORTED")


def syswincs02mqttFilesEnable(symbol, event):
    print("mqtt sysrnwfwifiWincs02FilesEnable")
    # data = Database.getComponentByID("sysWifiRNWFComponent")
    if(Database.getComponentByID("sysWifiRNWF") == None):
        print("mqtt NONE  sysrnwfwifiWincs02FilesEnable")

    host = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_HOST")
    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    print("mqtt host      : "+str(host))
    print("mqtt device    : "+str(device))
    print("mqtt interface : "+str(interface))

    if ((host == "SAME54X-pro") and (device == "WINCS02") and (interface == "SPI")):
        print("mqtt : Host and Device are SUPPORTED - NC")
        symbol.setEnabled(True)
    else:
        print("mqtt : Host and Device are NOT SUPPORTED")

def sysrnwfmqttRnwf11FilesEnable(symbol, event):
    print("Mqtt sysrnwfmqttrnwf11FilesEnable")
    if(Database.getComponentByID("sysWifiRNWF") == None):
        print("mqtt NONE  sysrnwfwifiRnwf02FilesEnable1")

    host = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_HOST")
    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    if ((host == "SAME54X-pro") and (device == "RNWF11") and (interface== "UART")):
        print("mqtt File : Host and Device are SUPPORTED - RN")
        symbol.setEnabled(True)
    else:
        print("mqtt File : Host and Device are NOT SUPPORTED")


def finalizeComponent(sysMQTTComponent):
    print("finalizeComponent sysMQTTComponent.")
    if(Database.getSymbolValue("sysWifiRNWF", "SYS_RNWF_MQTT_ENABLE") == False):
        print("Setting SYS_RNWF_WIFI_SER_PROV_ENABLE.")
        Database.setSymbolValue("sysWifiRNWF", "SYS_RNWF_MQTT_ENABLE", True)


def genAppCode(symbol, event):
    print("genAppCode.")
        
def setVal(component, symbol, value):
    print("setVal.")
        

def sysMqttSubMenuVisible(symbol, event):
    print("sysMqttSubMenuVisible.")
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


def onAttachmentConnected(source, target):
    print("onAttachmentConnected.")


def onAttachmentDisconnected(source, target):
    print(onAttachmentDisconnected)

def mqttTlsAutoMenu(symbol, event):
    print("mqttTlsAutoMenu.")

def mqttSNIAutoMenu(symbol, event):
    print("mqttSNIAutoMenu.")

def mqttALPNAutoMenu(symbol, event):
    print("mqttALPNAutoMenu.")

def mqttIntfAutoMenu(symbol, event):
    print("mqttIntfAutoMenu.")

        
