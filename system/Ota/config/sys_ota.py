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
 
    sysrnwfOtaTunnel = sysrnwfOTARNWFComponent.createComboSymbol("SYS_RNWF_OTA_TUNNEL", None, ["TCP"])
    sysrnwfOtaTunnel.setLabel("OTA Tunnel Selection ")
    sysrnwfOtaTunnel.setHelp(ota_helpkeyword)
    sysrnwfOtaTunnel.setDescription("Tunnel to receive the OTA server and Image details. Drop-down to select OTA Tunnel. Currently supports TCP only")
    sysrnwfOtaTunnel.setVisible(True)
    sysrnwfOtaTunnel.setDefaultValue("TCP")

    sysrnwfOtaTunnelPort = sysrnwfOTARNWFComponent.createIntegerSymbol("SYS_RNWF_OTA_TUNNEL_PORT", None)
    sysrnwfOtaTunnelPort.setLabel("OTA Tunnel Port")
    sysrnwfOtaTunnelPort.setHelp(ota_helpkeyword)
    sysrnwfOtaTunnelPort.setVisible(True)
    sysrnwfOtaTunnelPort.setMin(1)
    sysrnwfOtaTunnelPort.setMax(65535)
    sysrnwfOtaTunnelPort.setDescription("OTA tunnel Port to receive OTA server details")
    sysrnwfOtaTunnelPort.setDefaultValue(6666)

    sysrnwfotaadvancedconfigurations = sysrnwfOTARNWFComponent.createCommentSymbol("SYS_RNWF_OTA_ADV_CONF", None)
    sysrnwfotaadvancedconfigurations.setLabel("Advanced Configurations ")
    sysrnwfotaadvancedconfigurations.setHelp(ota_helpkeyword)

    sysrnwfotadebuglogs = sysrnwfOTARNWFComponent.createBooleanSymbol("SYS_RNWF_OTA_DEBUG_LOGS", sysrnwfotaadvancedconfigurations)
    sysrnwfotadebuglogs.setLabel("OTA Debug logs")
    sysrnwfotadebuglogs.setHelp(ota_helpkeyword)
    sysrnwfotadebuglogs.setDefaultValue(False)
    sysrnwfotadebuglogs.setDescription("Select to enable OTA service debug logs ")

    sysrnwfOtaCallbackHandler = sysrnwfOTARNWFComponent.createStringSymbol("SYS_RNWF_OTA_CALLBACK_HANDLER", None)
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
    sysrnwfotaHeaderFile.setEnabled(False)
    sysrnwfotaHeaderFile.setDependencies(sysotaRnwf02FilesEnable, ["sysWifiRNWF.SYS_RNWF_OTA_SER_ENABLE"])

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
    sysrnwfotaSystemConfFile.setDependencies(sysotaRnwf02FilesEnable, ["sysWifiRNWF.SYS_RNWF_NET_SER_ENABLE"])
    ########### system header end #################

#-----------------------------------------------------------------------------# 
def sysotaRnwf02FilesEnable(symbol, event):
    print("ota sysrnwfwifirnwf02FilesEnable")
    if(Database.getComponentByID("sysWifiRNWF") == None):
        print("OTA NONE  sysrnwfwifiRnwf02FilesEnable1")

    host = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_HOST")
    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    if ((host == "SAME54X-pro") and (device == "RNWF02") and (interface== "UART")):
        print("OTA File : Host and Device are SUPPORTED - RN")
        symbol.setEnabled(True)
    else:
        print("OTA File : Host and Device are NOT SUPPORTED")

def sysrnwfotaRnwf11FilesEnable(symbol, event):
    print("ota sysrnwfotarnwf11FilesEnable")
    if(Database.getComponentByID("sysWifiRNWF") == None):
        print("OTA NONE  sysrnwfotarnwf11FilesEnable")

    host = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_HOST")
    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    if ((host == "SAME54X-pro") and (device == "RNWF11") and (interface== "UART")):
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

    if ((host == "SAME54X-pro") and (device == "RNWF02") and (interface== "UART")):

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

        

def destroyComponent(sysrnwfOTARNWFComponent):
    res = Database.deactivateComponents(["sercom6"])
    res = Database.deactivateComponents(["drv_sst26"])
    res = Database.deactivateComponents(["tc0"])
    res = Database.deactivateComponents(["sys_time"])
    res = Database.deactivateComponents(["sysOtaRNWF"])

    
#-----------------------------------------------------------------------------#
    
