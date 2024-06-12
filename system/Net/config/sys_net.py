"""*****************************************************************************
Copyright (C) 2020 released Microchip Technology Inc.  All rights reserved.

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
global net_helpkeyword

sysrnwfnetMaxSockets = 2
sysrnwfnetSocketInstance = []
sysrnwfnetSocketPrev = 1
sysrnwfnetBind = [] 
sysrnwfnetSockPort = []
sysrnwfnetSockType = []
sysrnwfnetSockIPType = []
sysrnwfnetSockTypeIPv4 = []
sysrnwfnetSockIPv4Addr = []
sysrnwfnetSockTypeIPv6 = []
sysrnwfnetSockIPv6Addr = []
sysrnwfnetSockTypeIPv6local = []
sysrnwfnetSockIPv6localAddr = []
sysrnwfnetSockTypeIPv6global = []
sysrnwfnetSockIPv6globalAddr = []
sysrnwfnetMode = []
sysrnwfnetEnableTls = []
sysrnwfnetTlsPeeerAuth = []
sysrnwfnetTlsRootCert = []
sysrnwfnetTlsDevCertificate = []
sysrnwfnetTlsDevKey = []
sysrnwfnetTlsDevKeyPwd = []
sysrnwfnetTlsServerName = []
sysrnwfnetTlsDomainNameverify = []
sysrnwfnetTlsDomainName = []


net_helpkeyword = "mcc_h3_RNWF_net_system_service_configurations"
################################################################################
#### Business Logic ####
################################################################################

################################################################################
#### Component ####
################################################################################
def instantiateComponent(sysrnwfNetComponent):
    global net_helpkeyword

    sysrnwfnetEnableErrMsg = sysrnwfNetComponent.createCommentSymbol("SYS_RNWF_NET_ERR", None)
    sysrnwfnetEnableErrMsg.setLabel("**Placeholder for error display")
    sysrnwfnetEnableErrMsg.setHelp(net_helpkeyword)
    sysrnwfnetEnableErrMsg.setVisible(False)

    sysrnwfnetSocketEnable = sysrnwfNetComponent.createBooleanSymbol("SYS_RNWF_NET_SOCK_CONF", None)
    sysrnwfnetSocketEnable.setLabel("Socket Configurations")
    sysrnwfnetSocketEnable.setHelp(net_helpkeyword)
    sysrnwfnetSocketEnable.setDescription("Debug - Logs and commands")
    sysrnwfnetSocketEnable.setDefaultValue(True)

    sysrnwfnetNoOfSocks = sysrnwfNetComponent.createIntegerSymbol("SYS_RNWF_NET_NO_OF_SOCKS", sysrnwfnetSocketEnable)
    sysrnwfnetNoOfSocks.setLabel("Number of Sockets ")
    sysrnwfnetNoOfSocks.setHelp(net_helpkeyword)
    sysrnwfnetNoOfSocks.setVisible(True)
    sysrnwfnetNoOfSocks.setDefaultValue(1)
    sysrnwfnetNoOfSocks.setMin(1)
    sysrnwfnetNoOfSocks.setMax(sysrnwfnetMaxSockets)
    sysrnwfnetNoOfSocks.setDependencies(sysnetSubMenuVisible, ["SYS_RNWF_NET_SOCK_CONF"])

    # Get Size of Each Slot
    for slot in range(0,sysrnwfnetMaxSockets):
        sysrnwfnetSocketInstance.append(sysrnwfNetComponent.createMenuSymbol("SYS_RNWF_SOCKET"+str(slot), sysrnwfnetNoOfSocks))
        sysrnwfnetSocketInstance[slot].setLabel("Socket "+ str(slot))
        sysrnwfnetNoOfSocks.setHelp(net_helpkeyword)

        # sysrnwfnetBind.append(sysrnwfNetComponent.createComboSymbol("SYS_RNWF_NET_BIND_TYPE"+str(slot), sysrnwfnetSocketInstance[slot], ["LOCAL", "REMOTE", "MCAST", "NONE"]))
        # sysrnwfnetBind[slot].setLabel("Bind type")
        # sysrnwfnetBind[slot].setHelp(net_helpkeyword)
        # sysrnwfnetBind[slot].setDefaultValue("LOCAL")
# ####################################################################################################################
        sysrnwfnetMode.append(sysrnwfNetComponent.createComboSymbol("SYS_RNWF_NET_MODE"+str(slot), sysrnwfnetSocketInstance[slot], ["CLIENT", "SERVER"]))
        sysrnwfnetMode[slot].setLabel("Mode")
        sysrnwfnetMode[slot].setHelp(net_helpkeyword)
        sysrnwfnetMode[slot].setDefaultValue("CLIENT")

        sysrnwfnetSockType.append(sysrnwfNetComponent.createComboSymbol("SYS_RNWF_NET_SOCK_TYPE"+str(slot), sysrnwfnetSocketInstance[slot], ["UDP", "TCP"]))
        sysrnwfnetSockType[slot].setLabel("Ip Protocol")
        sysrnwfnetSockType[slot].setHelp(net_helpkeyword)
        sysrnwfnetSockType[slot].setDefaultValue("TCP")

        sysrnwfnetSockIPType.append(sysrnwfNetComponent.createComboSymbol("SYS_RNWF_NET_SOCK_IP_TYPE"+str(slot), sysrnwfnetSocketInstance[slot], ["IPv4", "IPv6 Local", "IPv6 Global"]))
        sysrnwfnetSockIPType[slot].setLabel("Ip Type")
        sysrnwfnetSockIPType[slot].setHelp(net_helpkeyword)
        sysrnwfnetSockIPType[slot].setDefaultValue("IPv4")

        sysrnwfnetSockIPv4Addr.append(sysrnwfNetComponent.createStringSymbol("SYS_RNWF_NET_SOCK_IP_ADDR"+str(slot),  sysrnwfnetSocketInstance[slot]))
        sysrnwfnetSockIPv4Addr[slot].setLabel("Server Address")
        sysrnwfnetSockIPv4Addr[slot].setHelp(net_helpkeyword)
        sysrnwfnetSockIPv4Addr[slot].setDescription("Server Address")
        sysrnwfnetSockIPv4Addr[slot].setDefaultValue("")
        sysrnwfnetSockIPv4Addr[slot].setDependencies(setVisible_OnValueChanged, ["SYS_RNWF_NET_MODE"+str(slot)])

        sysrnwfnetSockPort.append(sysrnwfNetComponent.createIntegerSymbol("SYS_RNWF_NET_SOCK_PORT"+str(slot), sysrnwfnetSocketInstance[slot]))    
        sysrnwfnetSockPort[slot].setLabel("Socket Port")
        sysrnwfnetSockPort[slot].setHelp(net_helpkeyword)
        sysrnwfnetSockPort[slot].setDefaultValue(80)
        sysrnwfnetSockPort[slot].setMin(1)
        sysrnwfnetSockPort[slot].setMax(65535)

        sysrnwfnetEnableTls.append(sysrnwfNetComponent.createBooleanSymbol("SYS_RNWF_NET_ENABLE_TLS"+str(slot), sysrnwfnetSocketInstance[slot]))
        sysrnwfnetEnableTls[slot].setLabel("Enable TLS")
        sysrnwfnetEnableTls[slot].setHelp(net_helpkeyword)
        sysrnwfnetEnableTls[slot].setDefaultValue(False)

        sysrnwfnetTlsPeeerAuth.append(sysrnwfNetComponent.createBooleanSymbol("SYS_RNWF_NET_PEER_AUTH"+str(slot), sysrnwfnetEnableTls[slot]))
        sysrnwfnetTlsPeeerAuth[slot].setLabel("Peer authentication")
        sysrnwfnetTlsPeeerAuth[slot].setHelp(net_helpkeyword)
        sysrnwfnetTlsPeeerAuth[slot].setVisible(False)
        sysrnwfnetTlsPeeerAuth[slot].setDescription("Peer authentication")
        sysrnwfnetTlsPeeerAuth[slot].setDefaultValue(False)
        sysrnwfnetTlsPeeerAuth[slot].setDependencies(sysnetSubMenuVisible, ["SYS_RNWF_NET_ENABLE_TLS"+str(slot)])

        sysrnwfnetTlsRootCert.append(sysrnwfNetComponent.createStringSymbol("SYS_RNWF_NET_ROOT_CERT"+str(slot), sysrnwfnetTlsPeeerAuth[slot]))
        sysrnwfnetTlsRootCert[slot].setLabel("Root CA")
        sysrnwfnetTlsRootCert[slot].setHelp(net_helpkeyword)
        sysrnwfnetTlsRootCert[slot].setVisible(False)
        sysrnwfnetTlsRootCert[slot].setDescription("TLS Root Certificate Name")
        sysrnwfnetTlsRootCert[slot].setDefaultValue("AmazonRootCA1")
        sysrnwfnetTlsRootCert[slot].setDependencies(sysnetSubMenuVisible, ["SYS_RNWF_NET_PEER_AUTH"+str(slot)])

        sysrnwfnetTlsDevCertificate.append(sysrnwfNetComponent.createStringSymbol("SYS_RNWF_NET_DEVICE_CERTIFICATE"+str(slot), sysrnwfnetEnableTls[slot]))
        sysrnwfnetTlsDevCertificate[slot].setLabel("Device Certificate")
        sysrnwfnetTlsDevCertificate[slot].setHelp(net_helpkeyword)
        sysrnwfnetTlsDevCertificate[slot].setVisible(False)
        sysrnwfnetTlsDevCertificate[slot].setDescription("TLS Key Name")
        sysrnwfnetTlsDevCertificate[slot].setDefaultValue("")
        sysrnwfnetTlsDevCertificate[slot].setDependencies(sysnetSubMenuVisible, ["SYS_RNWF_NET_ENABLE_TLS"+str(slot)])

        sysrnwfnetTlsDevKey.append(sysrnwfNetComponent.createStringSymbol("SYS_RNWF_NET_DEVICE_KEY"+str(slot), sysrnwfnetEnableTls[slot]))
        sysrnwfnetTlsDevKey[slot].setLabel("Device Key")
        sysrnwfnetTlsDevKey[slot].setHelp(net_helpkeyword)
        sysrnwfnetTlsDevKey[slot].setVisible(False)
        sysrnwfnetTlsDevKey[slot].setDescription("Device key ")
        sysrnwfnetTlsDevKey[slot].setDefaultValue("")
        sysrnwfnetTlsDevKey[slot].setDependencies(sysnetSubMenuVisible, ["SYS_RNWF_NET_ENABLE_TLS"+str(slot)])
        
        sysrnwfnetTlsDevKeyPwd.append(sysrnwfNetComponent.createStringSymbol("SYS_RNWD_NET_DEVICE_KEY_PWD"+str(slot), sysrnwfnetEnableTls[slot]))
        sysrnwfnetTlsDevKeyPwd[slot].setLabel("Device Key Password")
        sysrnwfnetTlsDevKeyPwd[slot].setHelp(net_helpkeyword)
        sysrnwfnetTlsDevKeyPwd[slot].setVisible(False)
        sysrnwfnetTlsDevKeyPwd[slot].setDescription("Device key ")
        sysrnwfnetTlsDevKeyPwd[slot].setDefaultValue("")
        sysrnwfnetTlsDevKeyPwd[slot].setDependencies(sysnetSubMenuVisible, ["SYS_RNWF_NET_ENABLE_TLS"+str(slot)])
        
        sysrnwfnetTlsServerName.append(sysrnwfNetComponent.createStringSymbol("SYS_RNWF_NET_SERVER_NAME"+str(slot), sysrnwfnetEnableTls[slot]))
        sysrnwfnetTlsServerName[slot].setLabel("Server Name")
        sysrnwfnetTlsServerName[slot].setHelp(net_helpkeyword)
        sysrnwfnetTlsServerName[slot].setVisible(False)
        sysrnwfnetTlsServerName[slot].setDescription("Enter the Server NAme")
        sysrnwfnetTlsServerName[slot].setDefaultValue("")
        sysrnwfnetTlsServerName[slot].setDependencies(sysnetSubMenuVisible, ["SYS_RNWF_NET_ENABLE_TLS"+str(slot)])

        sysrnwfnetTlsDomainNameverify.append(sysrnwfNetComponent.createBooleanSymbol("SYS_RNWF_NET_DOMAIN_NAME_VERIFY"+str(slot), sysrnwfnetEnableTls[slot]))
        sysrnwfnetTlsDomainNameverify[slot].setLabel("Domain Name Verify")
        sysrnwfnetTlsDomainNameverify[slot].setHelp(net_helpkeyword)
        sysrnwfnetTlsDomainNameverify[slot].setVisible(False)
        sysrnwfnetTlsDomainNameverify[slot].setDescription("Domain Name Verify")
        sysrnwfnetTlsDomainNameverify[slot].setDefaultValue(False)
        sysrnwfnetTlsDomainNameverify[slot].setDependencies(sysnetSubMenuVisible, ["SYS_RNWF_NET_ENABLE_TLS"+str(slot)])

        sysrnwfnetTlsDomainName.append(sysrnwfNetComponent.createStringSymbol("SYS_RNWF_NET_DOMAIN_NAME"+str(slot), sysrnwfnetTlsDomainNameverify[slot]))
        sysrnwfnetTlsDomainName[slot].setLabel("Domain Name")
        sysrnwfnetTlsDomainName[slot].setHelp(net_helpkeyword)
        sysrnwfnetTlsDomainName[slot].setVisible(False)
        sysrnwfnetTlsDomainName[slot].setDescription("Domain Name")
        sysrnwfnetTlsDomainName[slot].setDefaultValue("")
        sysrnwfnetTlsDomainName[slot].setDependencies(sysnetSubMenuVisible, ["SYS_RNWF_NET_DOMAIN_NAME_VERIFY"+str(slot)])
        
        if (slot < sysrnwfnetNoOfSocks.getValue()):
            sysrnwfnetSocketInstance[slot].setVisible(True)
        else:
            sysrnwfnetSocketInstance[slot].setVisible(False)
        sysrnwfnetSocketInstance[slot].setDependencies(sysrnwfnetSlotInstanceEnable,["SYS_RNWF_NET_SOCK_CONF","SYS_RNWF_NET_NO_OF_SOCKS"])


    sysrnwfnetadvancedconfigurations = sysrnwfNetComponent.createCommentSymbol("SYS_RNWF_NET_ADV_CONF", None)
    sysrnwfnetadvancedconfigurations.setLabel("Advanced Configurations ")
    sysrnwfnetadvancedconfigurations.setHelp(net_helpkeyword)

    sysrnwfnetdebuglogs = sysrnwfNetComponent.createBooleanSymbol("SYS_RNWF_NET_DEBUG_LOGS", sysrnwfnetadvancedconfigurations)
    sysrnwfnetdebuglogs.setLabel("NET Debug logs")
    sysrnwfnetdebuglogs.setHelp(net_helpkeyword)
    sysrnwfnetdebuglogs.setDefaultValue(False)
    sysrnwfnetdebuglogs.setDescription("Select to enable net service debug logs ")

    sysrnwfnetSocketCallbackHandler = sysrnwfNetComponent.createStringSymbol("SYS_RNWF_NET_SOCKET_CALLBACK_HANDLER", None)
    sysrnwfnetSocketCallbackHandler.setLabel("Net Socket Callback handler")
    sysrnwfnetSocketCallbackHandler.setHelp(net_helpkeyword)
    sysrnwfnetSocketCallbackHandler.setVisible(True)
    sysrnwfnetSocketCallbackHandler.setDescription("Enter the name of net socket callback handler")
    sysrnwfnetSocketCallbackHandler.setDefaultValue("APP_SOCKET_Callback")

    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    sysrnwfnetHeaderFile = sysrnwfNetComponent.createFileSymbol("SYS_RNWF_NET_HEADER", None)
    sysrnwfnetHeaderFile.setSourcePath("system/Net/templates/sys_rnwf02_net_service.h.ftl")
    sysrnwfnetHeaderFile.setOutputName("sys_rnwf_net_service.h")
    sysrnwfnetHeaderFile.setDestPath("system/net/")
    sysrnwfnetHeaderFile.setProjectPath("config/" + configName + "/system/net/")
    sysrnwfnetHeaderFile.setType("HEADER")
    sysrnwfnetHeaderFile.setOverwrite(True)
    sysrnwfnetHeaderFile.setEnabled(False)
    sysrnwfnetHeaderFile.setDependencies(sysrnwfnetRnwf02FilesEnable, ["sysWifiRNWF.SYS_RNWF_NET_SER_ENABLE"])

    print("Network Service Component Header Path %s", sysrnwfnetHeaderFile.getProjectPath())
	
    sysrnwfnetSourceFile = sysrnwfNetComponent.createFileSymbol("SYS_RNWF_NET_SOURCE", None)
    sysrnwfnetSourceFile.setSourcePath("system/Net/templates/src/sys_rnwf02_net_service.c.ftl")
    sysrnwfnetSourceFile.setOutputName("sys_rnwf_net_service.c")
    sysrnwfnetSourceFile.setDestPath("system/net/src")
    sysrnwfnetSourceFile.setProjectPath("config/" + configName + "/system/net/")
    sysrnwfnetSourceFile.setType("SOURCE")
    sysrnwfnetSourceFile.setOverwrite(True)
    sysrnwfnetSourceFile.setEnabled(False)
    sysrnwfnetSourceFile.setDependencies(sysrnwfnetRnwf02FilesEnable, ["sysWifiRNWF.SYS_RNWF_NET_SER_ENABLE"])


    sysrnwfnetSystemConfigFile = sysrnwfNetComponent.createFileSymbol("SYS_RNWF_CONSOLE_SYS_CONFIG", None)
    sysrnwfnetSystemConfigFile.setType("STRING")
    sysrnwfnetSystemConfigFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION")
    sysrnwfnetSystemConfigFile.setSourcePath("system/Net/templates/system/system_config_rnwf02.h.ftl")
    sysrnwfnetSystemConfigFile.setMarkup(True)
    sysrnwfnetSystemConfigFile.setOverwrite(True)
    sysrnwfnetSystemConfigFile.setEnabled(False)
    sysrnwfnetSystemConfigFile.setDependencies(sysrnwfnetRnwf02FilesEnable, ["sysWifiRNWF.SYS_RNWF_NET_SER_ENABLE"])

    ### WINCS02 Code #######

    sysrnwfWincs02NetSourceFile = sysrnwfNetComponent.createFileSymbol("SYS_RNWF_WINCS02_NET_SOURCE", None)
    sysrnwfWincs02NetSourceFile.setSourcePath("system/Net/templates/src/sys_wincs02_net_service.c.ftl")
    sysrnwfWincs02NetSourceFile.setOutputName("sys_wincs_net_service.c")
    sysrnwfWincs02NetSourceFile.setDestPath("system/net/src")
    sysrnwfWincs02NetSourceFile.setProjectPath("config/" + configName + "/system/net/")
    sysrnwfWincs02NetSourceFile.setType("SOURCE")
    sysrnwfWincs02NetSourceFile.setMarkup(True)
    sysrnwfWincs02NetSourceFile.setEnabled(False)
    sysrnwfWincs02NetSourceFile.setOverwrite(True)
    sysrnwfWincs02NetSourceFile.setDependencies(sysrnwfnetWincs02FilesEnable, ["sysWifiRNWF.SYS_RNWF_NET_SER_ENABLE"])


    sysrnwfWincs02NetHeaderFile = sysrnwfNetComponent.createFileSymbol("SYS_RNWF_WINCS02_NET_HEADER", None)
    sysrnwfWincs02NetHeaderFile.setSourcePath("system/Net/templates/sys_wincs02_net_service.h.ftl")
    sysrnwfWincs02NetHeaderFile.setOutputName("sys_wincs_net_service.h")
    sysrnwfWincs02NetHeaderFile.setDestPath("system/net/")
    sysrnwfWincs02NetHeaderFile.setProjectPath("config/" + configName + "/system/net/")
    sysrnwfWincs02NetHeaderFile.setType("HEADER")
    sysrnwfWincs02NetHeaderFile.setMarkup(True)
    sysrnwfWincs02NetHeaderFile.setOverwrite(True)
    sysrnwfWincs02NetHeaderFile.setEnabled(False)
    sysrnwfWincs02NetHeaderFile.setDependencies(sysrnwfnetWincs02FilesEnable, ["sysWifiRNWF.SYS_RNWF_NET_SER_ENABLE"])

    syswincs02netSystemConfigFile = sysrnwfNetComponent.createFileSymbol("SYS_WINCS02_CONSOLE_SYS_CONFIG", None)
    syswincs02netSystemConfigFile.setType("STRING")
    syswincs02netSystemConfigFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION")
    syswincs02netSystemConfigFile.setSourcePath("system/Net/templates/system/system_config_wincs02.h.ftl")
    syswincs02netSystemConfigFile.setMarkup(True)
    syswincs02netSystemConfigFile.setOverwrite(True)
    syswincs02netSystemConfigFile.setEnabled(False)
    syswincs02netSystemConfigFile.setDependencies(sysrnwfnetWincs02FilesEnable, ["sysWifiRNWF.SYS_RNWF_NET_SER_ENABLE"])


    #####RNWF11 Code generation ####################
    sysrnwf11netHeaderFile = sysrnwfNetComponent.createFileSymbol("SYS_RNWF11_NET_HEADER", None)
    sysrnwf11netHeaderFile.setSourcePath("system/Net/templates/sys_rnwf11_net_service.h.ftl")
    sysrnwf11netHeaderFile.setOutputName("sys_rnwf_net_service.h")
    sysrnwf11netHeaderFile.setDestPath("system/net/")
    sysrnwf11netHeaderFile.setProjectPath("config/" + configName + "/system/net/")
    sysrnwf11netHeaderFile.setType("HEADER")
    sysrnwf11netHeaderFile.setOverwrite(True)
    sysrnwf11netHeaderFile.setEnabled(False)
    sysrnwf11netHeaderFile.setDependencies(sysrnwfnetRnwf11FilesEnable, ["sysWifiRNWF.SYS_RNWF_NET_SER_ENABLE"])

    sysrnwf11netSourceFile = sysrnwfNetComponent.createFileSymbol("SYS_RNWF11_NET_SOURCE", None)
    sysrnwf11netSourceFile.setSourcePath("system/Net/templates/src/sys_rnwf11_net_service.c.ftl")
    sysrnwf11netSourceFile.setOutputName("sys_rnwf_net_service.c")
    sysrnwf11netSourceFile.setDestPath("system/net/src")
    sysrnwf11netSourceFile.setProjectPath("config/" + configName + "/system/net/")
    sysrnwf11netSourceFile.setType("SOURCE")
    sysrnwf11netSourceFile.setOverwrite(True)
    sysrnwf11netSourceFile.setEnabled(False)
    sysrnwf11netSourceFile.setDependencies(sysrnwfnetRnwf11FilesEnable, ["sysWifiRNWF.SYS_RNWF_NET_SER_ENABLE"])
	
	
############################################################################
#### Dependency ####
############################################################################
#Set symbols of other components

def sysrnwfnetRnwf02FilesEnable(symbol, event):
    print("Net sysrnwfwifirnwf02FilesEnable")
    if(Database.getComponentByID("sysWifiRNWF") == None):
        print("Net1 NONE  sysrnwfwifirnwf02FilesEnable")

    host = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_HOST")
    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    if ((host == "SAME54X-pro") and (device == "RNWF02") and (interface== "UART")):
        print("Net File : Host and Device are SUPPORTED - RN")
        symbol.setEnabled(True)
    else:
        print("Net File : Host and Device are NOT SUPPORTED")


def sysrnwfnetWincs02FilesEnable(symbol, event):
    print("Net1 sysrnwfnetWincs02FilesEnable")
    # data = Database.getComponentByID("sysWifiRNWFComponent")
    if(Database.getComponentByID("sysWifiRNWF") == None):
        print("Net1 NONE  sysrnwfnetWincs02FilesEnable")

    host = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_HOST")
    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    print("net host      : "+str(host))
    print("net device    : "+str(device))
    print("net interface : "+str(interface))

    if ((host == "SAME54X-pro") and (device == "WINCS02") and (interface == "SPI")):
        print("File : Host and Device are SUPPORTED - NC")
        symbol.setEnabled(True)
    else:
        print("File : Host and Device are NOT SUPPORTED")

def sysrnwfnetRnwf11FilesEnable(symbol, event):
    print("Net sysrnwfnetrnwf11FilesEnable")
    if(Database.getComponentByID("sysWifiRNWF") == None):
        print("Net1 NONE  sysrnwfnetrnwf11FilesEnable")

    host = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_HOST")
    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    print("net host      : "+str(host))
    print("net device    : "+str(device))
    print("net interface : "+str(interface))

    if ((host == "SAME54X-pro") and (device == "RNWF11") and (interface == "UART")):
        print("File : Host and Device are SUPPORTED - RN")
        symbol.setEnabled(True)
    else:
        print("File : Host and Device are NOT SUPPORTED")


def sysrnwfnetSlotInstanceEnable(symbol, event):
    global sysrnwfnetSocketPrev
    print("Start sysotaFileInstanceEnable")
    if(event["id"] == "SYS_RNWF_NET_SOCK_CONF"):
        otafileEnable = Database.getSymbolValue("sysrnwfnetSocketEnable","SYS_RNWF_NET_SOCK_CONF")
        fileIndex = int(filesymbol.getID().strip("SYS_RNWF_SOCKET"))
        print("File Slot " + str(fileIndex))
        print(sysrnwfnetSocketPrev)
        # print(tcpipDhcpsInstancesNumPrev)
        if(otafileEnable == True):
            if(fileIndex < sysrnwfnetSocketPrev ):
                symbol.setVisible(True)
        else:
            symbol.setVisible(False)

    else:
        print(symbol.getID())
        print(event["id"])
        sysotaFileNumValue = event["value"]
        print(sysotaFileNumValue)
        print(sysrnwfnetSocketPrev)
        if (sysotaFileNumValue > sysrnwfnetSocketPrev):
            sysrnwfnetSocketInstance[sysrnwfnetSocketPrev].setVisible(True)
            sysrnwfnetSocketPrev = sysrnwfnetSocketPrev + 1
        else:
            if(sysotaFileNumValue < sysrnwfnetSocketPrev):
                sysrnwfnetSocketPrev = sysrnwfnetSocketPrev - 1
                sysrnwfnetSocketInstance[sysrnwfnetSocketPrev].setVisible(False)
                print("Set False " + str(sysrnwfnetSocketPrev))

            else:
                print("Do Nothing "+ str(sysrnwfnetSocketPrev))
    
    print("END sysotaFileInstanceEnable")

def setVisible_OnValueChanged(symbol, event):
    print("setVisible_OnValueChanged.")
    if (event["value"] == "CLIENT"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)
def sysnetSubMenuVisible(symbol, event):
    print("sysnetSubMenuVisible.")
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def finalizeComponent(sysrnwfNetComponent):
    print("finalizeComponent sysrnwfNetComponent.")
    if(Database.getSymbolValue("sysWifiRNWF", "SYS_RNWF_NET_SER_ENABLE") == False):
        print("Setting SYS_RNWF_NET_SER_ENABLE.")
        Database.setSymbolValue("sysWifiRNWF", "SYS_RNWF_NET_SER_ENABLE", True)

    
