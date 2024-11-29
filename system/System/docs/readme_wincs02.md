# System Service

The system service provides API's to set and get the system level details. The following<br /> table lists all the services exposed by the system service layer. The system service API<br /> prototype is as<br /> follows:

``` {#GUID-681D8313-B33A-4C96-8FC1-3232AA4A3BD2_CODEBLOCK_FLJ_FNJ_MYB}
SYS_WINCS_RESULT_t SYS_WINCS_SYSTEM_SrvCtrl(SYS_WINCS_SYSTEM_SERVICE_t request, SYS_WINCS_SYSTEM_HANDLE_t systemHandle);
```

The<br /> table below shows the various commands and options available for system service.

|Option/Command|Input|Remarks|
|--------------|-----|-------|
|`SYS_WINCS_SYSTEM_RESET`|None|Request/Trigger Reset the system|
|`SYS_WINCS_SYSTEM_SW_REV`|FIRMWARE_VERSION_INFO structure|Request Software Revision|
|`SYS_WINCS_SYSTEM_DEV_INFO`|DEVICE_INFO structure|Request Device Info|
|`SYS_WINCS_SYSTEM_GET_CERT_LIST`|None|Get the available Certificate list|
|`SYS_WINCS_SYSTEM_GET_KEY_LIST`|Buffer array to read Key list|Get the available private key list|
|`SYS_WINCS_SYSTEM_DRIVER_VER`| DRIVER_VERSION_INFO structure |Request Driver version|
|`SYS_WINCS_SYSTEM_SET_SYS_EVENT_CALLBACK`|  Callback Handler |Set Driver system event callback|
|`SYS_WINCS_SYSTEM_DEBUG_UART_SET`|Null|Debug firmware logs|
|`SYS_WINCS_SYSTEM_SET_DEBUG_REG_CLBK`|Null|User defined printf|

Following are few examples to use the system service API's

```  {#GUID-681D8313-B33A-4C96-8FC1-3232AA4A3BD2_CODEBLOCK_N1X_ZZW_XYB}
*/\*
    System Service application
    void APP_WINCS02_Tasks ( void )
{

    /* Check the application's current state. */
    switch ( g_appData.state )
    {
       /* Application's initial state. */
        case APP_STATE_WINCS_INIT:
        {
            SYS_STATUS status;
            SYS_WINCS_WIFI_SrvCtrl(SYS_WINCS_WIFI_GET_DRV_STATUS, &status);

            if (SYS_STATUS_READY == status)
            {
                g_appData.state = APP_STATE_WINCS_OPEN_DRIVER;
            }
            
            break;
        }
        
        case APP_STATE_WINCS_OPEN_DRIVER:
        {
            DRV_HANDLE wdrvHandle = DRV_HANDLE_INVALID;
            // Open the Wi-Fi driver
            if (SYS_WINCS_FAIL == SYS_WINCS_WIFI_SrvCtrl(SYS_WINCS_WIFI_OPEN_DRIVER, &wdrvHandle))
            {
                g_appData.state = APP_STATE_WINCS_ERROR;
                break;
            }

            // Get the driver handle
            SYS_WINCS_WIFI_SrvCtrl(SYS_WINCS_WIFI_GET_DRV_HANDLE, &wdrvHandle);
            
            SYS_WINCS_SYSTEM_SrvCtrl(SYS_WINCS_SYSTEM_DEBUG_UART_SET, NULL);
            
            EIC_CallbackRegister(EIC_PIN_15,APP_RNWF_eicUserHandler, 0);
            g_appData.state = APP_STATE_WINCS_DEVICE_INFO;
            break;
        }
        
        case APP_STATE_WINCS_DEVICE_INFO:
        {
            APP_DRIVER_VERSION_INFO drvVersion;
            APP_FIRMWARE_VERSION_INFO fwVersion;
            APP_DEVICE_INFO devInfo;
            SYS_WINCS_RESULT_t status = SYS_WINCS_BUSY;

            // Get the firmware version
            status = SYS_WINCS_SYSTEM_SrvCtrl(SYS_WINCS_SYSTEM_SW_REV, &fwVersion);

            if(status == SYS_WINCS_PASS)
            {
                // Get the device information
                status = SYS_WINCS_SYSTEM_SrvCtrl(SYS_WINCS_SYSTEM_DEV_INFO, &devInfo);
            }

            if(status == SYS_WINCS_PASS)
            {
                // Get the driver version
                status = SYS_WINCS_SYSTEM_SrvCtrl(SYS_WINCS_SYSTEM_DRIVER_VER, &drvVersion);
            }

            if(status == SYS_WINCS_PASS)
            {
                char buff[30];
                // Print device information
                SYS_CONSOLE_PRINT("WINC: Device ID = %08x\r\n", devInfo.id);
                for (int i = 0; i < devInfo.numImages; i++)
                {
                    SYS_CONSOLE_PRINT("%d: Seq No = %08x, Version = %08x, Source Address = %08x\r\n", 
                            i, devInfo.image[i].seqNum, devInfo.image[i].version, devInfo.image[i].srcAddr);
                }

                // Print firmware version
                SYS_CONSOLE_PRINT(TERM_CYAN "Firmware Version: %d.%d.%d ", fwVersion.version.major,
                        fwVersion.version.minor, fwVersion.version.patch);
                strftime(buff, sizeof(buff), "%X %b %d %Y", localtime((time_t*)&fwVersion.build.timeUTC));
                SYS_CONSOLE_PRINT(" [%s]\r\n", buff);

                // Print driver version
                SYS_CONSOLE_PRINT("Driver Version: %d.%d.%d\r\n"TERM_RESET, drvVersion.version.major, 
                        drvVersion.version.minor, drvVersion.version.patch);
                
                g_appData.state = APP_STATE_WINCS_SET_REG_DOMAIN;
            }
            break;
        }

        case APP_STATE_WINCS_SET_REG_DOMAIN:
        {
            
            // Set the callback handler for Wi-Fi events
            SYS_WINCS_WIFI_SrvCtrl(SYS_WINCS_WIFI_SET_CALLBACK, SYS_WINCS_WIFI_CallbackHandler);

            SYS_CONSOLE_PRINT(TERM_YELLOW"[APP] : Setting REG domain to " TERM_UL "%s\r\n"TERM_RESET ,SYS_WINCS_WIFI_COUNTRYCODE);
            // Set the regulatory domain
            if (SYS_WINCS_FAIL == SYS_WINCS_WIFI_SrvCtrl(SYS_WINCS_WIFI_SET_REG_DOMAIN, SYS_WINCS_WIFI_COUNTRYCODE))
            {
                g_appData.state = APP_STATE_WINCS_ERROR;
                break;
            }
            g_appData.state = APP_STATE_WINCS_SERVICE_TASKS;
            break;
        }
        
        case APP_STATE_WINCS_PRINT_CERTS_KEYS:
        {
            SYS_CONSOLE_PRINT("[APP] : Certificates on Device :-\r\n"TERM_YELLOW);
            if (SYS_WINCS_FAIL == SYS_WINCS_SYSTEM_SrvCtrl(SYS_WINCS_SYSTEM_GET_CERT_LIST,NULL))
            {
                g_appData.state = APP_STATE_WINCS_ERROR;
                break;
            }
            g_appData.state = APP_STATE_WINCS_SET_WIFI_PARAMS;
            break;
        }
        
        case APP_STATE_WINCS_SERVICE_TASKS:
        { 

            break;
        }
        

    }
}
\*/*
