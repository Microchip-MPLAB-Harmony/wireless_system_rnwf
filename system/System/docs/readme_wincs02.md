# System Service

The system service provides API's to set and get the system level details. The following<br /> table lists all the services exposed by the system service layer. The system service API<br /> prototype is as<br /> follows:

``` {#GUID-681D8313-B33A-4C96-8FC1-3232AA4A3BD2_CODEBLOCK_FLJ_FNJ_MYB}
SYS_WINCS_RESULT_t SYS_WINCS_SYSTEM_SrvCtrl(SYS_WINCS_SYSTEM_SERVICE_t request, void *input);
```

The<br /> table below shows the various commands and options available for system service.

|Option/Command|Input|Remarks|
|--------------|-----|-------|
|`SYS_WINCS_SYSTEM_RESET`|None|Request/Trigger Reset the system|
|`SYS_WINCS_SYSTEM_ECHO_OFF`|None|Turn OFF the AT command Echo|
|`SYS_WINCS_SYSTEM_GET_MAN_ID`|Buffer array to read Manufacturer ID|Get the manufacturing ID|
|`SYS_WINCS_SYSTEM_SET_TIME_UNIX`|Time \(String\) in UNIX format|Set the sytem time in UNIX format|
|`SYS_WINCS_SYSTEM_SET_TIME_NTP`|Time \(String\) in NTP format|Set the system time in NTP format|
|`SYS_WINCS_SYSTEM_SET_TIME_STRING`|Time \(String\)|Set the system time in string \(YYYY-MM-DDTHH:MM:SS.00Z\)<br /> format|
|`SYS_WINCS_SYSTEM_SW_REV`|Buffer array to read Software Revision|Request Software Revision|
|`SYS_WINCS_SYSTEM_DEV_INFO`|Buffer array to read Device Info|Request Device Info|
|`SYS_WINCS_SYSTEM_SET_SNTP`|Server name \(String\)|Enable SNTP with given server URL|
|`SYS_WINCS_SYSTEM_GET_TIME`|Buffer array to read Time|Get the system time|
|`SYS_WINCS_SYSTEM_GET_CERT_LIST`|Buffer array to read Certification list|Get the available certificate list|
|`SYS_WINCS_SYSTEM_GET_KEY_LIST`|Buffer array to read Key list|Get the available private key list|
|`SYS_WINCS_SYSTEM_GET_WIFI_INFO`|Buffer array to read Wi-Fi Info|Get Wi-Fi configuration information|
|`SYS_WINCS_SYSTEM_GET_MQTT_INFO`|Buffer array to read MQTT Config Info|Get MQTT configuration Information|
|`SYS_WINCS_SYSTEM_DRIVER_VER`| |Request Driver version|
|`SYS_WINCS_SYSTEM_SET_SYS_EVENT_CALLBACK`| |Set Driver system event callback|
|`SYS_WINCS_SYSTEM_DEBUG_UART_SET`| |Debug UART Set|
|`SYS_WINCS_SYSTEM_SET_DEBUG_REG_CLBK`| |Debug UART Register callback|

Following are few examples to use the system service<br /> API's

``` {#GUID-681D8313-B33A-4C96-8FC1-3232AA4A3BD2_CODEBLOCK_N1X_ZZW_XYB}
*/\*
    System Service application
\*/*
```


