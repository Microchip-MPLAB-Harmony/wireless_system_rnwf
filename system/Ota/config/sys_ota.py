# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
global ota_helpkeyword

ota_helpkeyword = "mcc_h3_RNWF_ota_system_service_configurations"

sysrnwfnetMaxSockets = 2
################################################################################
#### Business Logic ####
################################################################################

################################################################################
#### Component ####
################################################################################


def instantiateComponent(sysrnwfOTARNWFComponent):
    
    
    global ota_helpkeyword
    #-------------------------------------------------------------------------#
    #                           OTA main menu                        #
    #-------------------------------------------------------------------------#
 
 ################################# RNWF02 DFU Configurations
    sysrnwfwifiotaDevice = sysrnwfOTARNWFComponent.createComboSymbol("SYS_RN_NC_OTA_DEVICE", None , ["None","RNWF02","WINCS02"])
    sysrnwfwifiotaDevice.setLabel("Select device ")
    sysrnwfwifiotaDevice.setHelp(ota_helpkeyword)
    sysrnwfwifiotaDevice.setVisible(True)
    sysrnwfwifiotaDevice.setDescription("Select the Device")
    sysrnwfwifiotaDevice.setDefaultValue("None")
    
    sysrnwfotadfuEnable = sysrnwfOTARNWFComponent.createBooleanSymbol("SYS_RNWF_OTA_DFU_ENABLE", None)
    sysrnwfotadfuEnable.setLabel("RNWF02")
    sysrnwfotadfuEnable.setHelp(ota_helpkeyword)
    sysrnwfotadfuEnable.setDefaultValue(False)
    sysrnwfotadfuEnable.setVisible(False)
    sysrnwfotadfuEnable.setDescription("Enable DFU mode Configuration ")
    sysrnwfotadfuEnable.setDependencies(sysOtarnwfMenuEnable, ["SYS_RN_NC_OTA_DEVICE"])

    sysrnwfOtaConfSoc = sysrnwfOTARNWFComponent.createIntegerSymbol("SYS_RNWF_OTA_CONF_SOC", None)
    sysrnwfOtaConfSoc.setLabel("OTA Configuration Socket ")
    sysrnwfOtaConfSoc.setHelp(ota_helpkeyword)
    sysrnwfOtaConfSoc.setDescription("Socket to receive the OTA server and Image details")
    sysrnwfOtaConfSoc.setVisible(False)
    sysrnwfOtaConfSoc.setMin(0)
    sysrnwfOtaConfSoc.setMax(sysrnwfnetMaxSockets)
    sysrnwfOtaConfSoc.setDefaultValue(0)
    sysrnwfOtaConfSoc.setDependencies(sysotaDFUautoMenu, ["SYS_RNWF_OTA_DFU_ENABLE"])

    sysrnwfOtaServerSoc = sysrnwfOTARNWFComponent.createIntegerSymbol("SYS_RNWF_OTA_SERVER_SOC", None)
    sysrnwfOtaServerSoc.setLabel("OTA Server Socket ")
    sysrnwfOtaServerSoc.setHelp(ota_helpkeyword)
    sysrnwfOtaServerSoc.setVisible(False)
    sysrnwfOtaServerSoc.setMin(0)
    sysrnwfOtaServerSoc.setMax(sysrnwfnetMaxSockets)
    sysrnwfOtaServerSoc.setDescription("OTA Server Socket ")
    sysrnwfOtaServerSoc.setDefaultValue(1)
    sysrnwfOtaServerSoc.setDependencies(sysotaDFUautoMenu, ["SYS_RNWF_OTA_DFU_ENABLE"])

    sysrnwfOtaFlashAddr = sysrnwfOTARNWFComponent.createStringSymbol("SYS_RNWF_OTA_FLASH_ADDR", None)
    sysrnwfOtaFlashAddr.setLabel("OTA FW Flash Address ")
    sysrnwfOtaFlashAddr.setHelp(ota_helpkeyword)
    sysrnwfOtaFlashAddr.setVisible(False)
    sysrnwfOtaFlashAddr.setDescription("Enter the Flash Address of OTA image in device low : 0x60000000, high : 0x600F0000")
    sysrnwfOtaFlashAddr.setDefaultValue("0x600F0000")
    sysrnwfOtaFlashAddr.setDependencies(sysotaDFUautoMenu, ["SYS_RNWF_OTA_DFU_ENABLE"])

######################### WINCS02 Inbuild OTA Configirations
    syswincsdirectotaEnable = sysrnwfOTARNWFComponent.createBooleanSymbol("SYS_WINCS_DIRECT_OTA_ENABLE", None)
    syswincsdirectotaEnable.setLabel("WINCS02")
    syswincsdirectotaEnable.setHelp(ota_helpkeyword)
    syswincsdirectotaEnable.setVisible(False)
    syswincsdirectotaEnable.setDescription("Enable WINCS02 inbuilt OTA Configuration ")
    syswincsdirectotaEnable.setDependencies(sysOtawincsMenuEnable, ["SYS_RN_NC_OTA_DEVICE"])

    syswincsOtaServerSoc = sysrnwfOTARNWFComponent.createIntegerSymbol("SYS_WINCS_OTA_SERVER_SOC", syswincsdirectotaEnable)
    syswincsOtaServerSoc.setLabel("OTA Server Socket ")
    syswincsOtaServerSoc.setHelp(ota_helpkeyword)
    syswincsOtaServerSoc.setVisible(False)
    syswincsOtaServerSoc.setMin(0)
    syswincsOtaServerSoc.setMax(sysrnwfnetMaxSockets)
    syswincsOtaServerSoc.setDescription("OTA Server Socket ")
    syswincsOtaServerSoc.setDefaultValue(0)
    syswincsOtaServerSoc.setDependencies(syswincsdirectotaautoMenu, ["SYS_WINCS_DIRECT_OTA_ENABLE"])

    syswincsOtasfile = sysrnwfOTARNWFComponent.createStringSymbol("SYS_WINCS_OTA_FILE_NAME", syswincsdirectotaEnable)
    syswincsOtasfile.setLabel("File Name")
    syswincsOtasfile.setHelp(ota_helpkeyword)
    syswincsOtasfile.setVisible(False)
    syswincsOtasfile.setDescription("Enter the file name")
    syswincsOtasfile.setDependencies(syswincsdirectotaautoMenu, ["SYS_WINCS_DIRECT_OTA_ENABLE"])

    syswincsOtatimeout = sysrnwfOTARNWFComponent.createIntegerSymbol("SYS_WINCS_OTA_TIME_OUT", syswincsdirectotaEnable)
    syswincsOtatimeout.setLabel("OTA Time out ")
    syswincsOtatimeout.setHelp(ota_helpkeyword)
    syswincsOtatimeout.setVisible(False)
    syswincsOtatimeout.setMin(0)
    syswincsOtatimeout.setMax(200)
    syswincsOtatimeout.setDescription("Ota Time out ")
    syswincsOtatimeout.setDefaultValue(20)
    syswincsOtatimeout.setDependencies(syswincsdirectotaautoMenu, ["SYS_WINCS_DIRECT_OTA_ENABLE"])

######################### Advanced Configurations
    sysrnwfotaadvancedconfigurations = sysrnwfOTARNWFComponent.createCommentSymbol("SYS_RNWF_OTA_ADV_CONF", None)
    sysrnwfotaadvancedconfigurations.setLabel("Advanced Configurations ")
    sysrnwfotaadvancedconfigurations.setHelp(ota_helpkeyword)

    sysrnwfotadebuglogs = sysrnwfOTARNWFComponent.createBooleanSymbol("SYS_RNWF_OTA_DEBUG_LOGS", sysrnwfotaadvancedconfigurations)
    sysrnwfotadebuglogs.setLabel("OTA Debug logs")
    sysrnwfotadebuglogs.setHelp(ota_helpkeyword)
    sysrnwfotadebuglogs.setDefaultValue(False)
    sysrnwfotadebuglogs.setDescription("Select to enable OTA service debug logs ")

    sysrnwfOtaCallbackHandler = sysrnwfOTARNWFComponent.createStringSymbol("SYS_RNWF_OTA_CALLBACK_HANDLER", sysrnwfotaadvancedconfigurations)
    sysrnwfOtaCallbackHandler.setLabel("OTA Callback Handler")
    sysrnwfOtaCallbackHandler.setVisible(True)
    sysrnwfOtaCallbackHandler.setDescription("Configure callback function name to handle OTA service events")
    sysrnwfOtaCallbackHandler.setDefaultValue("APP_OTA_Callback")


    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")
    
    sysrnwfotaSourceFile = sysrnwfOTARNWFComponent.createFileSymbol("SYS_RNWF_OTA_SOURCE", None)
    sysrnwfotaSourceFile.setSourcePath("system/Ota/templates/src/sys_rnwf02_ota_service.c.ftl")
    sysrnwfotaSourceFile.setOutputName("sys_rnwf_ota_service.c")
    sysrnwfotaSourceFile.setDestPath("system/ota/src")
    sysrnwfotaSourceFile.setProjectPath("config/" + configName + "/system/ota/")
    sysrnwfotaSourceFile.setType("SOURCE")
    sysrnwfotaSourceFile.setMarkup(True)
    sysrnwfotaSourceFile.setEnabled(False)
    sysrnwfotaSourceFile.setDependencies(sysotaRnwf02FilesEnable,["sysWifiRNWF.SYS_RNWF_OTA_SER_ENABLE"])


    sysrnwfotaHeaderFile = sysrnwfOTARNWFComponent.createFileSymbol("SYS_RNWF_OTA_HEADER", None)
    sysrnwfotaHeaderFile.setSourcePath("system/Ota/templates/sys_rnwf02_ota_service.h.ftl")
    sysrnwfotaHeaderFile.setOutputName("sys_rnwf_ota_service.h")
    sysrnwfotaHeaderFile.setDestPath("system/ota/")
    sysrnwfotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/")
    sysrnwfotaHeaderFile.setType("HEADER")
    sysrnwfotaHeaderFile.setMarkup(True)
    sysrnwfotaHeaderFile.setOverwrite(True)
    sysrnwfotaHeaderFile.setEnabled(False)
    sysrnwfotaHeaderFile.setDependencies(sysotaRnwf02FilesEnable, ["sysWifiRNWF.SYS_RNWF_OTA_SER_ENABLE"])

###WINCS02 Code generation #####################
    syswincsotaSourceFile = sysrnwfOTARNWFComponent.createFileSymbol("SYS_WINCS_OTA_SOURCE", None)
    syswincsotaSourceFile.setSourcePath("system/Ota/templates/src/sys_wincs02_ota_service.c.ftl")
    syswincsotaSourceFile.setOutputName("sys_wincs_ota_service.c")
    syswincsotaSourceFile.setDestPath("system/ota/src")
    syswincsotaSourceFile.setProjectPath("config/" + configName + "/system/ota/")
    syswincsotaSourceFile.setType("SOURCE")
    syswincsotaSourceFile.setMarkup(True)
    syswincsotaSourceFile.setEnabled(False)
    syswincsotaSourceFile.setDependencies(sysotaWincs02FilesEnable,["sysWifiRNWF.SYS_RNWF_OTA_SER_ENABLE"])


    syswincsotaHeaderFile = sysrnwfOTARNWFComponent.createFileSymbol("SYS_WINCS_OTA_HEADER", None)
    syswincsotaHeaderFile.setSourcePath("system/Ota/templates/sys_wincs02_ota_service.h.ftl")
    syswincsotaHeaderFile.setOutputName("sys_wincs_ota_service.h")
    syswincsotaHeaderFile.setDestPath("system/ota/")
    syswincsotaHeaderFile.setProjectPath("config/" + configName + "/system/ota/")
    syswincsotaHeaderFile.setType("HEADER")
    syswincsotaHeaderFile.setMarkup(True)
    syswincsotaHeaderFile.setOverwrite(True)
    syswincsotaHeaderFile.setEnabled(False)
    syswincsotaHeaderFile.setDependencies(sysotaWincs02FilesEnable, ["sysWifiRNWF.SYS_RNWF_OTA_SER_ENABLE"])

    ###########WINCS02 system header #################
    syswincsotaSystemConfFile = sysrnwfOTARNWFComponent.createFileSymbol("SYS_WINCS_OTA_CONFIGURATION_H", None)
    syswincsotaSystemConfFile.setType("STRING")
    syswincsotaSystemConfFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION")
    syswincsotaSystemConfFile.setSourcePath("system/Ota/templates/system/system_config_wincs02.h.ftl")
    syswincsotaSystemConfFile.setMarkup(True)
    syswincsotaSystemConfFile.setOverwrite(True)
    syswincsotaSystemConfFile.setEnabled(False)
    syswincsotaSystemConfFile.setDependencies(sysotaWincs02FilesEnable, ["sysWifiRNWF.SYS_RNWF_OTA_SER_ENABLE"])

    ###RNWF11 Code generation #####################
    sysrnwf11otaSourceFile = sysrnwfOTARNWFComponent.createFileSymbol("SYS_RNWF11_OTA_SOURCE", None)
    sysrnwf11otaSourceFile.setSourcePath("system/Ota/templates/src/sys_rnwf11_ota_service.c.ftl")
    sysrnwf11otaSourceFile.setOutputName("sys_rnwf_ota_service.c")
    sysrnwf11otaSourceFile.setDestPath("system/ota/src")
    sysrnwf11otaSourceFile.setProjectPath("config/" + configName + "/system/ota/")
    sysrnwf11otaSourceFile.setType("SOURCE")
    sysrnwf11otaSourceFile.setMarkup(True)
    sysrnwf11otaSourceFile.setEnabled(False)
    sysrnwf11otaSourceFile.setDependencies(sysrnwfotaRnwf11FilesEnable, ["sysWifiRNWF.SYS_RNWF_OTA_SER_ENABLE"])

    sysrnwf11otaHeaderFile = sysrnwfOTARNWFComponent.createFileSymbol("SYS_RNWF11_OTA_HEADER", None)
    sysrnwf11otaHeaderFile.setSourcePath("system/Ota/templates/sys_rnwf11_ota_service.h.ftl")
    sysrnwf11otaHeaderFile.setOutputName("sys_rnwf_ota_service.h")
    sysrnwf11otaHeaderFile.setDestPath("system/ota/")
    sysrnwf11otaHeaderFile.setProjectPath("config/" + configName + "/system/ota/")
    sysrnwf11otaHeaderFile.setType("HEADER")
    sysrnwf11otaHeaderFile.setMarkup(True)
    sysrnwf11otaHeaderFile.setEnabled(False)
    sysrnwf11otaHeaderFile.setDependencies(sysrnwfotaRnwf11FilesEnable, ["sysWifiRNWF.SYS_RNWF_OTA_SER_ENABLE"])

    ########### system header #################
    sysrnwfotaSystemConfFile = sysrnwfOTARNWFComponent.createFileSymbol("SYS_RNWF_OTA_CONFIGURATION_H", None)
    sysrnwfotaSystemConfFile.setType("STRING")
    sysrnwfotaSystemConfFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION")
    sysrnwfotaSystemConfFile.setSourcePath("system/Ota/templates/system/system_config_rnwf02.h.ftl")
    sysrnwfotaSystemConfFile.setMarkup(True)
    sysrnwfotaSystemConfFile.setOverwrite(True)
    sysrnwfotaSystemConfFile.setEnabled(False)
    sysrnwfotaSystemConfFile.setDependencies(sysotaRnwf02FilesEnable, ["sysWifiRNWF.SYS_RNWF_OTA_SER_ENABLE"])


    ########### system header end #################

#-----------------------------------------------------------------------------# 
def sysotaRnwf02FilesEnable(symbol, event):
    print("RNWF02 Files : OTA  sysrnwfwifirnwf02FilesEnable")

    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    if device == "RNWF02" and interface== "UART":
        symbol.setEnabled(True)
    else:
        symbol.setEnabled(False)

def sysotaWincs02FilesEnable(symbol, event):
    print("WINCS02 Files : OTA  syswincswifiwincs02FilesEnable")

    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    if ((device == "WINCS02") and (interface == "SPI")):
        symbol.setEnabled(True)
        print("sysotaWincs02FilesEnable")
    else:
        symbol.setEnabled(False)
        print("sysotaWincs02FilesDisable")

def sysrnwfotaRnwf11FilesEnable(symbol, event):
    print("ota sysrnwfotarnwf11FilesEnable")
    if(Database.getComponentByID("sysWifiRNWF") == None):
        print("OTA NONE  sysrnwfotarnwf11FilesEnable")

    host = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_HOST")
    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    if ((host == "SAME54X-pro") and (device == "RNWF11") and (interface == "UART")):
        print("OTA File : Host and Device are SUPPORTED - RN")
        symbol.setEnabled(True)
    else:
        print("OTA File : Host and Device are NOT SUPPORTED")
		
		
def finalizeComponent(sysrnwfOTARNWFComponent):
    print("finalizeComponent")
    if(Database.getComponentByID("sysWifiRNWF") == None):
        print("OTA NONE  finalizeComponent")

    host = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_HOST")
    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    if(Database.getSymbolValue("sysWifiRNWF", "SYS_RNWF_OTA_SER_ENABLE") == False):
        print("Setting SYS_RNWF_OTA_SER_PROV_ENABLE.")
        Database.setSymbolValue("sysWifiRNWF", "SYS_RNWF_OTA_SER_ENABLE", True) 

    if ((device == "RNWF02") and (interface== "UART")):

        if(Database.getComponentByID("sercom6") == None):    
            res = Database.activateComponents(["sercom6"])
            Database.setSymbolValue("sercom6", "SPI_DOPO", 0)
            Database.setSymbolValue("sercom6", "SPI_DIPO", 3)
            Database.setSymbolValue("sercom6", "SPI_BAUD_RATE", 7000000)
            Database.setSymbolValue("sercom6", "SPI_MSSN", False)

        if(Database.getComponentByID("drv_sst26") == None):    
            res = Database.activateComponents(["drv_sst26"])
            res = Database.setSymbolValue("drv_sst26", "SPI_CHIP_SELECT_PIN", 67)
            
        autoConnectTablespi = [["sercom6","SERCOM6_SPI" , "drv_sst26", "drv_sst26_SPI_dependency"]]
        res = Database.connectDependencies(autoConnectTablespi)

        if(Database.getComponentByID("tc0") == None):    
            res = Database.activateComponents(["tc0"])
        
        if(Database.getComponentByID("sys_time") == None):    
            res = Database.activateComponents(["sys_time"])

        autoConnectTabletc0 = [["tc0","TC0_TMR" , "sys_time", "sys_time_TMR_dependency"]]
        res = Database.connectDependencies(autoConnectTabletc0)

        Database.setSymbolValue("core","PIN_30_FUNCTION_TYPE","SERCOM6_PAD3")
        Database.setSymbolValue("core","PIN_27_FUNCTION_TYPE","SERCOM6_PAD0")
        Database.setSymbolValue("core","PIN_28_FUNCTION_TYPE","SERCOM6_PAD1")
        Database.setSymbolValue("core","ENABLE_SYS_RESET",True)

    elif ((host == "SAME54X-pro") and (device == "RNWF11") and (interface== "UART")):

        if(Database.getComponentByID("sercom6") == None):    
            res = Database.activateComponents(["sercom6"])
            Database.setSymbolValue("sercom6", "SPI_DOPO", 0)
            Database.setSymbolValue("sercom6", "SPI_DIPO", 3)
            Database.setSymbolValue("sercom6", "SPI_BAUD_RATE", 7000000)
            Database.setSymbolValue("sercom6", "SPI_MSSN", False)

        if(Database.getComponentByID("drv_sst26") == None):    
            res = Database.activateComponents(["drv_sst26"])
            res = Database.setSymbolValue("drv_sst26", "SPI_CHIP_SELECT_PIN", 67)
            
        autoConnectTablespi = [["sercom6","SERCOM6_SPI" , "drv_sst26", "drv_sst26_SPI_dependency"]]
        res = Database.connectDependencies(autoConnectTablespi)

        if(Database.getComponentByID("tc0") == None):    
            res = Database.activateComponents(["tc0"])
        
        if(Database.getComponentByID("sys_time") == None):    
            res = Database.activateComponents(["sys_time"])

        autoConnectTabletc0 = [["tc0","TC0_TMR" , "sys_time", "sys_time_TMR_dependency"]]
        res = Database.connectDependencies(autoConnectTabletc0)

        Database.setSymbolValue("core","PIN_30_FUNCTION_TYPE","SERCOM6_PAD3")
        Database.setSymbolValue("core","PIN_27_FUNCTION_TYPE","SERCOM6_PAD0")
        Database.setSymbolValue("core","PIN_28_FUNCTION_TYPE","SERCOM6_PAD1")
        Database.setSymbolValue("core","ENABLE_SYS_RESET",True)

    else:
        print("OTA finalize : Host and Device are NOT SUPPORTED")

def sysotaSubMenuVisible(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def sysotaDFUautoMenu(symbol, event):
    if (event["value"] == True):
        print("DFU Menu Visible.")
        symbol.setVisible(True)
    else:
        print("DFU Menu Invisible.")
        symbol.setVisible(False)

def syswincsdirectotaautoMenu(symbol, event):
    if (event["value"] == True):
        print("DFU Menu Visible.")
        symbol.setVisible(True)
    else:
        print("DFU Menu Invisible.")
        symbol.setVisible(False)

def sysOtawincsMenuEnable(symbol, event):
    print("Device OTA Menu Visible.")
    component = symbol.getComponent()
    device = component.getSymbolValue("SYS_RN_NC_OTA_DEVICE")

    if (device == "WINCS02"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)    

def sysOtarnwfMenuEnable(symbol, event):
    print("Device OTA Menu Visible.")
    component = symbol.getComponent()
    device = component.getSymbolValue("SYS_RN_NC_OTA_DEVICE")

    if (device == "RNWF02"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def destroyComponent(sysrnwfOTARNWFComponent):
    Database.setSymbolValue("sysWifiRNWF", "SYS_RNWF_OTA_SER_ENABLE", False)
    res = Database.deactivateComponents(["sysOtaRNWF"])

    
#-----------------------------------------------------------------------------#
    
