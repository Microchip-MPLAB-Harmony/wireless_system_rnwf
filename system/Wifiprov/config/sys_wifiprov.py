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
global wifi_prov_helpkeyword

wifi_prov_helpkeyword = "mcc_h3_pic32mzw1_wifi_prov_system_service_configurations"
################################################################################
#### Business Logic ####
################################################################################

################################################################################
#### Component ####
################################################################################
def instantiateComponent(syswifiprovComponent):

    global wifi_prov_helpkeyword

    # Enable dependent Harmony core components

    syswifiprovNvmAdd = syswifiprovComponent.createStringSymbol("SYS_RNWF_WIFIPROV_CALLBACK_HANDLER", None )
    syswifiprovNvmAdd.setLabel("Provision Callback Handler")
    syswifiprovNvmAdd.setHelp(wifi_prov_helpkeyword)
    syswifiprovNvmAdd.setVisible(True)
    syswifiprovNvmAdd.setDescription("Enterthe provision callback function")
    syswifiprovNvmAdd.setDefaultValue("APP_WIFIPROV_Callback")

    sysrnwfprovadvancedconfigurations = syswifiprovComponent.createCommentSymbol("SYS_RNWF_PROV_ADV_CONF", None)
    sysrnwfprovadvancedconfigurations.setLabel("Advanced Configurations ")
    sysrnwfprovadvancedconfigurations.setHelp(wifi_prov_helpkeyword)

    sysrnwfwifiprovdebuglogs = syswifiprovComponent.createBooleanSymbol("SYS_RNWF_PROV_DEBUG_LOGS", sysrnwfprovadvancedconfigurations)
    sysrnwfwifiprovdebuglogs.setLabel("Provision Debug logs")
    sysrnwfwifiprovdebuglogs.setHelp(wifi_prov_helpkeyword)
    sysrnwfwifiprovdebuglogs.setDefaultValue(False)
    sysrnwfwifiprovdebuglogs.setDescription("Select to enable Provision service debug logs ")

    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    syswifiprovHeaderFile = syswifiprovComponent.createFileSymbol("SYS_WIFIPROV_SOURCE", None)
    syswifiprovHeaderFile.setSourcePath("system/Wifiprov/templates/src/sys_rnwf02_provision_service.c.ftl")
    syswifiprovHeaderFile.setOutputName("sys_rnwf_provision_service.c")
    syswifiprovHeaderFile.setDestPath("system/wifiprov/src")
    syswifiprovHeaderFile.setProjectPath("config/" + configName + "/system/wifiprov/")
    syswifiprovHeaderFile.setType("SOURCE")
    syswifiprovHeaderFile.setMarkup(True)
    syswifiprovHeaderFile.setEnabled(False)
    syswifiprovHeaderFile.setDependencies(sysrnwfprovRnwf02FilesEnable, ["sysWifiRNWF.SYS_RNWF_WIFI_SER_PROV_ENABLE"])

    syswifiprovSourceFile = syswifiprovComponent.createFileSymbol("SYS_WIFIPROV_HEADER", None)
    syswifiprovSourceFile.setSourcePath("system/Wifiprov/templates/sys_rnwf02_provision_service.h.ftl")
    syswifiprovSourceFile.setOutputName("sys_rnwf_provision_service.h")
    syswifiprovSourceFile.setDestPath("system/wifiprov/")
    syswifiprovSourceFile.setProjectPath("config/" + configName + "/system/wifiprov/")
    syswifiprovSourceFile.setType("HEADER")
    syswifiprovSourceFile.setMarkup(True)
    syswifiprovSourceFile.setEnabled(False)
    syswifiprovSourceFile.setDependencies(sysrnwfprovRnwf02FilesEnable, ["sysWifiRNWF.SYS_RNWF_WIFI_SER_PROV_ENABLE"])

    syswifiprovSystemConfFile = syswifiprovComponent.createFileSymbol("SYS_RNWF_WIFIPROV_CONFIGURATION_H", None)
    syswifiprovSystemConfFile.setType("STRING")
    syswifiprovSystemConfFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
    syswifiprovSystemConfFile.setSourcePath("system/Wifiprov/templates/system/system_config_rnwf02.h.ftl")
    syswifiprovSystemConfFile.setMarkup(True)
    syswifiprovSystemConfFile.setEnabled(False)
    syswifiprovSystemConfFile.setDependencies(sysrnwfprovRnwf02FilesEnable, ["sysWifiRNWF.SYS_RNWF_WIFI_SER_PROV_ENABLE"])

    ## WINCS02 Code Generation ######

    syswifiWincso2provHeaderFile = syswifiprovComponent.createFileSymbol("SYS_WIFI_WINCS02_PROV_SOURCE", None)
    syswifiWincso2provHeaderFile.setSourcePath("system/Wifiprov/templates/src/sys_wincs02_provision_service.c.ftl")
    syswifiWincso2provHeaderFile.setOutputName("sys_wincs_provision_service.c")
    syswifiWincso2provHeaderFile.setDestPath("system/wifiprov/src")
    syswifiWincso2provHeaderFile.setProjectPath("config/" + configName + "/system/wifiprov/")
    syswifiWincso2provHeaderFile.setType("SOURCE")
    syswifiWincso2provHeaderFile.setMarkup(True)
    syswifiWincso2provHeaderFile.setEnabled(False)
    syswifiWincso2provHeaderFile.setDependencies(sysrnwfprovWincs02FilesEnable, ["sysWifiRNWF.SYS_RNWF_WIFI_SER_PROV_ENABLE"])

    syswifiWincs02provSourceFile = syswifiprovComponent.createFileSymbol("SYS_WIFI_WINCS02_PROV_HEADER", None)
    syswifiWincs02provSourceFile.setSourcePath("system/Wifiprov/templates/sys_wincs02_provision_service.h.ftl")
    syswifiWincs02provSourceFile.setOutputName("sys_wincs_provision_service.h")
    syswifiWincs02provSourceFile.setDestPath("system/wifiprov/")
    syswifiWincs02provSourceFile.setProjectPath("config/" + configName + "/system/wifiprov/")
    syswifiWincs02provSourceFile.setType("HEADER")
    syswifiWincs02provSourceFile.setMarkup(True)
    syswifiWincs02provSourceFile.setEnabled(False)
    syswifiWincs02provSourceFile.setDependencies(sysrnwfprovWincs02FilesEnable, ["sysWifiRNWF.SYS_RNWF_WIFI_SER_PROV_ENABLE"])

    syswincs02wifiprovSystemConfFile = syswifiprovComponent.createFileSymbol("SYS_WINCS02_WIFIPROV_CONFIGURATION_H", None)
    syswincs02wifiprovSystemConfFile.setType("STRING")
    syswincs02wifiprovSystemConfFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
    syswincs02wifiprovSystemConfFile.setSourcePath("system/Wifiprov/templates/system/system_config_wincs02.h.ftl")
    syswincs02wifiprovSystemConfFile.setMarkup(True)
    syswincs02wifiprovSystemConfFile.setEnabled(False)
    syswincs02wifiprovSystemConfFile.setDependencies(sysrnwfprovWincs02FilesEnable, ["sysWifiRNWF.SYS_RNWF_WIFI_SER_PROV_ENABLE"])


###RNWF11 code generation ################
    syswifiprovRnwf11SourceFile = syswifiprovComponent.createFileSymbol("SYS_WIFIPROV_RNWF11_HEADER", None)
    syswifiprovRnwf11SourceFile.setSourcePath("system/Wifiprov/templates/sys_rnwf11_provision_service.h.ftl")
    syswifiprovRnwf11SourceFile.setOutputName("sys_rnwf_provision_service.h")
    syswifiprovRnwf11SourceFile.setDestPath("system/wifiprov/")
    syswifiprovRnwf11SourceFile.setProjectPath("config/" + configName + "/system/wifiprov/")
    syswifiprovRnwf11SourceFile.setType("HEADER")
    syswifiprovRnwf11SourceFile.setMarkup(True)
    syswifiprovRnwf11SourceFile.setEnabled(False)
    syswifiprovRnwf11SourceFile.setDependencies(sysrnwfprovRnwf11FilesEnable, ["sysWifiRNWF.SYS_RNWF_WIFI_SER_PROV_ENABLE"])

    syswifiprovRnwf11HeaderFile = syswifiprovComponent.createFileSymbol("SYS_WIFIPROV_RNWF11_SOURCE", None)
    syswifiprovRnwf11HeaderFile.setSourcePath("system/Wifiprov/templates/src/sys_rnwf11_provision_service.c.ftl")
    syswifiprovRnwf11HeaderFile.setOutputName("sys_rnwf_provision_service.c")
    syswifiprovRnwf11HeaderFile.setDestPath("system/wifiprov/src")
    syswifiprovRnwf11HeaderFile.setProjectPath("config/" + configName + "/system/wifiprov/")
    syswifiprovRnwf11HeaderFile.setType("SOURCE")
    syswifiprovRnwf11HeaderFile.setMarkup(True)
    syswifiprovRnwf11HeaderFile.setEnabled(False)
    syswifiprovRnwf11HeaderFile.setDependencies(sysrnwfprovRnwf11FilesEnable, ["sysWifiRNWF.SYS_RNWF_WIFI_SER_PROV_ENABLE"])
############################################################################
#### Dependency ####
############################################################################

def setVal(component, symbol, value):
    print("setVal")

def sysrnwfprovRnwf02FilesEnable(symbol, event):
    print("prov sysrnwfwifirnwf02FilesEnable")
    if(Database.getComponentByID("sysWifiRNWF") == None):
        print("prov NONE  sysrnwfwifiRnwf02FilesEnable1")

    host = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_HOST")
    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    if ((host == "SAME54X-pro") and (device == "RNWF02") and (interface== "UART")):
        print("prov File : Host and Device are SUPPORTED - RN")
        symbol.setEnabled(True)
    else:
        print("prov File : Host and Device are NOT SUPPORTED")

def sysrnwfprovRnwf11FilesEnable(symbol, event):
    print("prov sysrnwfwifirnwf11FilesEnable")
    if(Database.getComponentByID("sysWifiRNWF") == None):
        print("prov NONE  sysrnwfwifirnwf11FilesEnable")

    host = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_HOST")
    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    if ((host == "SAME54X-pro") and (device == "RNWF11") and (interface== "UART")):
        print("prov File : Host and Device are SUPPORTED - RN")
        symbol.setEnabled(True)
    else:
        print("prov File : Host and Device are NOT SUPPORTED")


def sysrnwfprovWincs02FilesEnable(symbol, event):
    print("prov sysrnwfwifiWincs02FilesEnable")
    # data = Database.getComponentByID("sysWifiRNWFComponent")
    if(Database.getComponentByID("sysWifiRNWF") == None):
        print("prov NONE  sysrnwfwifiWincs02FilesEnable")

    host = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_HOST")
    device = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_WIFI_DEVICE")
    interface = Database.getSymbolValue("sysWifiRNWF","SYS_RNWF_INTERFACE_MODE")

    print("prov host      : "+str(host))
    print("prov device    : "+str(device))
    print("prov interface : "+str(interface))

    if ((host == "SAME54X-pro") and (device == "WINCS02") and (interface == "SPI")):
        print("prov : Host and Device are SUPPORTED - NC")
        symbol.setEnabled(True)
    else:
        print("prov : Host and Device are NOT SUPPORTED")


def finalizeComponent(syswifiprovComponent):
    print("finalizeComponent syswifiprovComponent.")
    if(Database.getSymbolValue("sysWifiRNWF", "SYS_RNWF_WIFI_SER_PROV_ENABLE") == False):
        print("Setting SYS_RNWF_WIFI_SER_PROV_ENABLE.")
        Database.setSymbolValue("sysWifiRNWF", "SYS_RNWF_WIFI_SER_PROV_ENABLE", True)

def destroyComponent(component):
    print("destroyComponent")

