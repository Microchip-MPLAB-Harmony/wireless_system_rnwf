# RNWF System Service

The system service provides API's to set and get the system level details. The following table lists all the services exposed by the system service layer. The system service API prototype is as follows:

``` {#CODEBLOCK_FLJ_FNJ_MYB .language-c}
SYS_RNWF_RESULT_t SYS_RNWF_SYSTEM_SrvCtrl(SYS_RNWF_SYSTEM_SERVICE_t request, uint8_t *input)
```

The table below shows the various commands and options available for system service.

|Option/Command|Input|Remarks|
|--------------|-----|-------|
|`SYS_RNWF_SYSTEM_RESET`|None|Request/Trigger Reset the system|
|`SYS_RNWF_SYSTEM_ECHO_OFF`|None|Turn OFF the AT command Echo|
|`SYS_RNWF_SYSTEM_GET_MAN_ID`|Buffer array to read Manufacturer<br /> ID|Get the manufacturing ID|
|`SYS_RNWF_SYSTEM_SET_TIME_UNIX`|Time \(String\) in UNIX format|Set the sytem time in UNIX format|
|`SYS_RNWF_SYSTEM_SET_TIME_NTP`|Time \(String\) in NTP format|Set the system time in NTP format|
|`SYS_RNWF_SYSTEM_SET_TIME_STRING`|Time \(String\)|Set the system time in string<br /> \(YYYY-MM-DDTHH:MM:SS.00Z\) format|
|`SYS_RNWF_SYSTEM_SW_REV`|Buffer array to read Software<br /> Revision|Request Software Revision|
|`SYS_RNWF_SYSTEM_DEV_INFO`|Buffer array to read Device Info|Request Device Info|
|`SYS_RNWF_SYSTEM_SET_SNTP`|Server name \(String\)|Enable SNTP with given server URL|
|`SYS_RNWF_SYSTEM_GET_TIME`|Buffer array to read Time|Get the system time|
|`SYS_RNWF_SYSTEM_GET_CERT_LIST`|Buffer array to read Certification<br /> list|Get the available certificate list|
|`SYS_RNWF_SYSTEM_GET_KEY_LIST`|Buffer array to read Key list|Get the available private key list|
|`SYS_RNWF_SYSTEM_GET_WIFI_INFO`|Buffer array to read Wi-Fi Info|Get Wi-Fi configuration information|
|`SYS_RNWF_SYSTEM_GET_MQTT_INFO`|Buffer array to read MQTT Config<br /> Info|Get MQTT configuration Information|

Following are few examples to use the system service API's

``` {#CODEBLOCK_N1X_ZZW_XYB .language-c}
/*
    System Service application
*/

/* Application buffer */
uint8_t app_buf[SYS_RNWF_BUF_LEN_MAX];

void APP_Initialize ( void )
{
    /* Place the App state machine in its initial state. */
    appData.state = APP_STATE_INITIALIZE;
}

void APP_Tasks ( void )
{
    switch(appData.state)
    {
        case APP_STATE_INITIALIZE:
        {
            SYS_RNWF_IF_Init();
            appData.state = APP_STATE_REGISTER_CALLBACK;
            SYS_CONSOLE_PRINT("APP_STATE_INITIALIZE\r\n");
            break;
        }
        case APP_STATE_REGISTER_CALLBACK:
        {              
            SYS_RNWF_SYSTEM_SrvCtrl(SYS_RWWF_SYSTEM_GET_WIFI_INFO, app_buf);    
            SYS_CONSOLE_PRINT("Wi-Fi Info:- \r\n%s\n", app_buf);   
    
            SYS_RNWF_SYSTEM_SrvCtrl(SYS_RNWF_SYSTEM_GET_CERT_LIST, app_buf);    
            SYS_CONSOLE_PRINT("Certs on RNWF02:- \r\n%s\n", app_buf);
    
            SYS_RNWF_SYSTEM_SrvCtrl(SYS_RNWF_SYSTEM_GET_KEY_LIST, app_buf);    
            SYS_CONSOLE_PRINT("Keys on RNWF02:- \r\n%s\n", app_buf);
                                                                                
            SYS_RNWF_SYSTEM_SrvCtrl(SYS_RNWF_SYSTEM_SW_REV, app_buf);    
            SYS_CONSOLE_PRINT("%s\n", app_buf);
    
            SYS_RNWF_SYSTEM_SrvCtrl(SYS_RNWF_SYSTEM_DEV_INFO, app_buf);    
            SYS_CONSOLE_PRINT("%s\n", app_buf);  
              
            appData.state = APP_STATE_TASK;
            break;
        }
        case APP_STATE_TASK:
        {
            if(g_AppState == APP_CLOUD_UP)
            {
                CLOUD_STATE_MACHINE();
            }
            RNWF_EVENT_Handler();
            break;
        }
        default:
        {
            break;
        }
    }
}
```

**Parent topic:**[RNWF02 Service Layer](GUID-CF733F9F-D5DE-4262-A3E0-C236C1531575.md)

