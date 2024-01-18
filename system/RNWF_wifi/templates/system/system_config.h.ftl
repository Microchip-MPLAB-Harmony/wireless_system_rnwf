/* RN WIFI System Service Configuration Options */

<#if SYS_RNWF_WIFI_MODE == "STA">
#define RNWF_WIFI_DEVMODE        			SYS_RNWF_WIFI_MODE_STA
<#elseif SYS_RNWF_WIFI_MODE == "AP">
#define RNWF_WIFI_DEVMODE        			SYS_RNWF_WIFI_MODE_AP
</#if>

<#if SYS_RNWF_WIFI_MODE_STA == true>
#define SYS_RNWF_WIFI_STA_SSID				"${SYS_RNWF_WIFI_STA_SSID_NAME}"
#define SYS_RNWF_WIFI_STA_PWD        			"${SYS_RNWF_WIFI_STA_PWD_NAME}"
<#if SYS_RNWF_WIFI_STA_SECURITY == "OPEN">
#define SYS_RNWF_STA_SECURITY				SYS_RNWF_OPEN
<#elseif SYS_RNWF_WIFI_STA_SECURITY == "WPA2">
#define SYS_RNWF_STA_SECURITY				SYS_RNWF_WPA2 
<#elseif SYS_RNWF_WIFI_STA_SECURITY == "RSVD">
#define SYS_RNWF_STA_SECURITY				SYS_RNWF_RSVD
<#elseif SYS_RNWF_WIFI_STA_SECURITY == "WPA3">
#define SYS_RNWF_STA_SECURITY				SYS_RNWF_WPA3
<#elseif SYS_RNWF_WIFI_STA_SECURITY == "WPA2-MIXED">
#define SYS_RNWF_STA_SECURITY				SYS_RNWF_WPA2_MIXED
<#elseif SYS_RNWF_WIFI_STA_SECURITY == "WPA3-TRANS">
#define SYS_RNWF_STA_SECURITY				SYS_RNWF_WPA3_TRANS
</#if>
<#if SYS_RNWF_WIFI_STA_AUTOCONNECT == true>
#define SYS_RNWF_WIFI_STA_AUTOCONNECT   		true
<#else>
#define SYS_RNWF_WIFI_STA_AUTOCONNECT   		false
</#if>
</#if>

<#if SYS_RNWF_WIFI_MODE_AP == true>
#define SYS_RNWF_WIFI_AP_SSID				"${SYS_RNWF_WIFI_AP_SSID_NAME}"
#define SYS_RNWF_WIFI_AP_PWD        			"${SYS_WIFI_AP_PWD_NAME}"
<#if SYS_RNWF_WIFI_AP_SECURITY == "OPEN">
#define SYS_RNWF_SOFT_AP_SECURITY			SYS_RNWF_OPEN
<#elseif SYS_RNWF_WIFI_AP_SECURITY == "WPA2">
#define SYS_RNWF_SOFT_AP_SECURITY			SYS_RNWF_WPA2
<#elseif SYS_RNWF_WIFI_AP_SECURITY == "RSVD">
#define SYS_RNWF_SOFT_AP_SECURITY			SYS_RNWF_RSVD
<#elseif SYS_RNWF_WIFI_AP_SECURITY == "WPA2_MIXED">
#define SYS_RNWF_SOFT_AP_SECURITY			SYS_RNWF_WPA2_MIXED
<#elseif SYS_RNWF_WIFI_AP_SECURITY == "WPA3">
#define SYS_RNWF_SOFT_AP_SECURITY			SYS_RNWF_WPA3
<#elseif SYS_RNWF_WIFI_AP_SECURITY == "WPA3_TRANS">
#define SYS_RNWF_SOFT_AP_SECURITY			SYS_RNWF_WPA3_TRANS
</#if>
<#if SYS_RNWF_WIFI_AP_AUTOCONNECT == true>
#define SYS_RNWF_WIFI_AP_AUTOCONNECT			1
<#else>
#define SYS_RNWF_WIFI_AP_AUTOCONNECT			0
</#if>
</#if>

<#if SYS_RNWF_WIFI_MODE_PROV == true>
#define SYS_RNWF_WIFI_PROV_SSID				"${SYS_RNWF_WIFI_PROV_SSID_NAME}"
#define SYS_RNWF_WIFI_PROV_PWD        			"${SYS_WIFI_PROV_PWD_NAME}"
<#if SYS_RNWF_WIFI_PROV_SECURITY == "OPEN">
#define SYS_RNWF_PROV_SECURITY				SYS_RNWF_OPEN
<#elseif SYS_RNWF_WIFI_PROV_SECURITY == "WPA2">
#define SYS_RNWF_PROV_SECURITY				SYS_RNWF_WPA2
<#elseif SYS_RNWF_WIFI_PROV_SECURITY == "RSVD">
#define SYS_RNWF_PROV_SECURITY				SYS_RNWF_RSVD
<#elseif SYS_RNWF_WIFI_PROV_SECURITY == "WPA2_MIXED">
#define SYS_RNWF_PROV_SECURITY				SYS_RNWF_WPA2_MIXED
<#elseif SYS_RNWF_WIFI_PROV_SECURITY == "WPA3">
#define SYS_RNWF_PROV_SECURITY				SYS_RNWF_WPA3
<#elseif SYS_RNWF_WIFI_PROV_SECURITY == "WPA3_TRANS">
#define SYS_RNWF_PROV_SECURITY				SYS_RNWF_WPA3_TRANS
</#if>
<#if SYS_RNWF_WIFI_PROV_AUTOCONNECT == true>
#define SYS_RNWF_WIFI_PROV_AUTOCONNECT			1
<#else>
#define SYS_RNWF_WIFI_PROV_AUTOCONNECT			0
</#if>
<#if SYS_RNWF_WIFI_PROV_METHOD == "PROV_WEB_SERVER">
#define SYS_RNWF_PROVI_WEB_SERVER			1
<#elseif SYS_RNWF_WIFI_PROV_METHOD == "PROV_MOBILE_APP">
#define SYS_RNWF_PROVI_MOBILE_APP			1
</#if>
</#if>
#define SYS_RNWF_WIFI_CallbackHandler			        ${SYS_RNWF_WIFI_CALLBACK_HANDLER}
