# Wi-Fi OTA Service Interface

The OTA service role is to enable the module firmware update over the network link. The OTA service has the HTTP based file download and RNWF02 Device Firmware Update \(DFU\) implementation. The OTA service open ups a TCP tunnel to receive the OTA server and firmware image details. Any device \(say PC or Mobile\) in the network can initiate the firmware download process. Once the OTA service receives all the necessary details, it starts downloading the firmware image and reports each downloaded chunk to user application over the callback. The user application needs to store the firmware in the local memory. After the successful download the user application can use the OTA service API's to flash new image into the RNWF02 module. The OTA service API call syntax is provided below:

``` {#CODEBLOCK_AJF_DVC_PYB .language-c}
SYS_RNWF_RESULT_t SYS_RNWF_OTA_SrvCtrl( SYS_RNWF_OTA_SERVICE_t request, void *input)
```

**OTA System Service Configuration in MCC**

![](images/GUID-5EE6F82C-875B-4001-8938-DF15D00F2406-low.png)

-   **OTA Configuration Socket :** Select the socket as per net service socket number to recieve the OTA server and image details.
-   **OTA Server Socket :**  Configure the OTA Server socket as per net service socket number.
-   **OTA FW Flash Address :** Enter the address of OTA image in device. for low partition : 0x60000000 and for high partition : 0x600F0000
-   **OTA Callback Handler:** Configure callback function name to handle OTA service events \(for example, downloading firmware binary from OTA server, erasing RNWF Flash before programming it with newly downloaded firmware image from server and perform RNWF Reset/Reboot with new firmware image\)

The following table provides the list of OTA services available:

<br />

|Option/Command|Input|Description|
|:-------------|:----|:----------|
|`SYS_RNWF_OTA_ENABLE`|Buffer of 4096 \(to align with DFU max write size\) bytes|Enable OTA service and opens a TCP tunnel to receive the OTA server and Image details|
|`SYS_RNWF_OTA_SET_CALLBACK`|Callback handler|Register callback function for the OTA service to report the status|
|`SYS_RNWF_OTA_DFU_INIT`|None|Generates the DFU pattern and places the RNWF module in firmware update mode|
|`SYS_RNWF_OTA_DFU_WRITE`|[chunk\_addr, chunk\_size, chunk\_ptr](GUID-D3C86805-5A5C-477E-9794-C8E14969C96D.md)|Writes the given chunk into the RNWF module. Max chunk size can be 4096 bytes.|
|`SYS_RNWF_OTA_DFU_ERASE`|[chunk\_addr, chunk\_size, chunk\_ptr](GUID-D3C86805-5A5C-477E-9794-C8E14969C96D.md)|Erases the provided size of memory \(chunk\_ptr can be<br /> NULL\)|

<br />

The following table captures the OTA Callback event codes and event data:

|Event|Response Component|Description|
|:----|:-----------------|:----------|
|`SYS_RNWF_EVENT_DWLD_START`|Total size of the image file to be downloaded|Given image file download has started|
|`SYS_RNWF_EVENT_DWLD_DONE`|Total size of downloaded Image file|Firmware download process completed, the application can initialize the DFU and start flle|
|`SYS_RNWF_EVENT_FILE_CHUNK`|[chunk\_addr, chunk\_size, chunk\_ptr](GUID-D3C86805-5A5C-477E-9794-C8E14969C96D.md)|Received image file chunk, the received data chunk should be saved in non-volatile memory|
|`SYS_RNWF_EVENT_DWLD_FAIL`|None|Firmware download failed|

The sequence chart for the OTA process is provided below:

<br />

![](images/GUID-554F7FCC-9DD8-4FDF-B1BB-E6F2D02FB03E-low.png "OTA Process")

<br />

The example code for OTA DFU is provided below:

``` {#CODEBLOCK_MKZ_CVS_CYB .language-c}


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include <string.h>
#include <stdio.h>
#include <stdio.h>
#include <stddef.h>                     
#include <stdbool.h>                   
#include <stdlib.h>                
#include <string.h>

/* This section lists the other files that are included in this file.
 */
#include "app_rnwf02.h"
#include "user.h"
#include "definitions.h" 
#include "configuration.h"
#include "system/debug/sys_debug.h"
#include "system/inf/sys_rnwf_interface.h"
#include "system/sys_rnwf_system_service.h"
#include "system/net/sys_rnwf_net_service.h"
#include "system/ota/sys_rnwf_ota_service.h"
#include "system/wifi/sys_rnwf_wifi_service.h"
#include "peripheral/sercom/spi_master/plib_sercom6_spi_master.h"


// *****************************************************************************
// *****************************************************************************
// Section: Global Data Definitions
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Application Buffer

  Summary:
    Application Buffer array 

  Description:
    This array holds the application's buffer.

  Remarks:
    None
*/

static uint8_t g_appBuf[SYS_RNWF_OTA_BUF_LEN_MAX];

// *****************************************************************************
/* Application Data

  Summary:
    Holds application data

  Description:
    This structure holds the application's data.

  Remarks:
    This structure should be initialized by the APP_Initialize function.

    Application strings and buffers are be defined outside this structure.
*/

static APP_DATA g_appData;

// *****************************************************************************
/* Application Image size

  Summary:
    Holds size of the Image downloaded by Ota 

  Description:
    This variable size of the Image downloaded by Ota 

  Remarks:
    This structure should be initialized by the APP_Initialize function.

    Application strings and buffers are be defined outside this structure.
*/

static uint32_t g_appImgSize;


// *****************************************************************************
// *****************************************************************************
// Section: Application Callback Functions
// *****************************************************************************
// *****************************************************************************

/**
 * Callback handler for WiFi events.
 *
 * This function is called whenever a WiFi event occurs. It processes the event
 * and performs the necessary actions based on the event type.
 *
 * parameter : event - The WiFi event that triggered the callback.
 * parameter : p_str - Pointer to a string associated with the event, if any.
 */

static void SYS_RNWF_WIFI_CallbackHandler
(
    SYS_RNWF_WIFI_EVENT_t event, 
    uint8_t *p_str
)
{
    switch(event)
    {
        /* Wifi Connected */
        case SYS_RNWF_WIFI_CONNECTED:
        {
            SYS_CONSOLE_PRINT(TERM_GREEN"[APP] : Wi-Fi Connected    \r\n"TERM_RESET);
            break;
        }
        
        /* Wifi Disconnected */
        case SYS_RNWF_WIFI_DISCONNECTED:
        {    
            SYS_CONSOLE_PRINT(TERM_RED"[APP] : Wi-Fi Disconnected\nReconnecting... \r\n"TERM_RESET);
            SYS_RNWF_WIFI_SrvCtrl(SYS_RNWF_WIFI_STA_CONNECT, NULL);
            break;
        }
            
        /* DHCP IP allocated */
        case SYS_RNWF_WIFI_DHCP_IPV4_COMPLETE:
        {
            SYS_CONSOLE_PRINT("[APP] : DHCP IPv4 : %s\r\n",  &p_str[2]); 
            
            /* Enable OTA by passing the OTA buffer space */
            if(SYS_RNWF_OTA_SrvCtrl(SYS_RNWF_OTA_ENABLE, (void *)g_appBuf) == SYS_RNWF_PASS)
            {
                SYS_RNWF_OTA_DBG_MSG(TERM_GREEN"Successfully Enabled the OTA. Waiting for OTA Server Details...\r\n"TERM_RESET);
            }
            else
            {
                SYS_RNWF_OTA_DBG_MSG(TERM_RED"ERROR!!! Failed to enable the OTA\r\n"TERM_RESET);
            }
            break;
        }
        
        default:
        {
            break;
        }
    }    
}

/**
 * Callback handler for OTA (Over-The-Air) update events.
 *
 * This function is called whenever an OTA event occurs. It processes the event
 * and performs the necessary actions based on the event type.
 *
 * parameter : event - The OTA event that triggered the callback.
 * parameter : p_str - Pointer to a string or data associated with the event, if any.
 */

static void SYS_RNWF_OTA_CallbackHandler
(
    SYS_RNWF_OTA_EVENT_t event,
    void *p_str
)
{
    static uint32_t flash_addr = SYS_RNWF_OTA_FLASH_IMAGE_START;
    
    switch(event)
    {
        /* Change to UART mode */
        case SYS_RNWF_OTA_EVENT_MAKE_UART:
        {
            break;
        }
            
        /* FW Download start */
        case SYS_RNWF_OTA_EVENT_DWLD_START:
        {
            SYS_CONSOLE_PRINT(TERM_CYAN"Total Size = %lu\r\n"TERM_RESET, *(uint32_t *)p_str); 
            SYS_CONSOLE_PRINT("Erasing the SPI Flash\r\n");
            
            SYS_RNWF_OTA_FlashErase();
            SYS_CONSOLE_PRINT(TERM_GREEN"Erasing Complete!\r\n"TERM_RESET); 
            break;
        }
        
        /* FW Download done */
        case SYS_RNWF_OTA_EVENT_DWLD_DONE:
        {       
            g_appImgSize = *(uint32_t *)p_str;  
            SYS_CONSOLE_PRINT(TERM_GREEN"Download Success!= %lu bytes 100%\r\n"TERM_RESET, g_appImgSize);  
            break; 
        }
              
        /* Write to SST26 */
        case SYS_RNWF_OTA_EVENT_FILE_CHUNK://15212
        {
            volatile SYS_RNWF_OTA_CHUNK_t *ota_chunk = (SYS_RNWF_OTA_CHUNK_t *)p_str;               
            SYS_RNWF_OTA_FlashWrite(flash_addr,ota_chunk->chunk_size ,ota_chunk->chunk_ptr);
            flash_addr += ota_chunk->chunk_size;
            break; 
        }    
        
        case SYS_RNWF_OTA_EVENT_DWLD_FAIL:
        {
            SYS_CONSOLE_PRINT(TERM_RED"[APP ERROR] : OTA image Download Failed\r\n"TERM_RESET);
            break;
        }
                           
        default:
        {
            break;
        }
    }
    
}

// *****************************************************************************
// *****************************************************************************
// Section: Application Initialization and State Machine Functions
// *****************************************************************************
// *****************************************************************************

/*******************************************************************************
  Function:
    void APP_Initialize ( void )

  Remarks:
    See prototype in app_wincs02.h.
 */

void APP_RNWF02_Initialize 
( 
    void 
)
{
    /* Place the App state machine in its initial state. */
    g_appData.state = APP_STATE_INITIALIZE;
}

// *****************************************************************************
// *****************************************************************************
// Section: Application Local Functions
// *****************************************************************************
// *****************************************************************************


/**
 * Software reset handler.
 *
 * This function is responsible for handling software reset events. It performs
 * the necessary actions to reset the system or specific components.
 *
 * parameter : None.
 */

void APP_RNWF_SwResetHandler
(
    void
)
{
    /* RNWF Reset */
    SYS_RNWF_OTA_DfuReset();
    
    /* Manual Delay to synchronise host reset. 
     * User can change according to their Host reset timing*/
    for(int i=0; i< 0xFFFFF; i++)
    {
        SYS_CONSOLE_PRINT("");
    }
    
    /* Host Reset */
    SYS_RESET_SoftwareReset();
}


/**
 * Application tasks handler.
 *
 * This function is responsible for handling the main tasks of the application.
 * It is typically called in the main loop and performs periodic checks and operations.
 *
 * parameter : None.
 */

void APP_RNWF02_Tasks 
( 
    void 
)
{
    switch(g_appData.state)
    {
        /* Initialize Flash and RNWF device */
        case APP_STATE_INITIALIZE:
        {
            SYS_CONSOLE_PRINT(TERM_YELLOW"%s"TERM_RESET, "##############################################\r\n");
            SYS_CONSOLE_PRINT(TERM_CYAN"%s"TERM_RESET, "  Welcome RNWF02 WiFi Host Assisted OTA Demo  \r\n");
            SYS_CONSOLE_PRINT(TERM_YELLOW"%s"TERM_RESET, "##############################################\r\n\r\n"); 
            
            if(false == SYS_RNWF_OTA_FlashInitialize())
            {
                SYS_CONSOLE_PRINT(TERM_RED"[APP ERROR] : No valid SPI Flash found!\r\n\tConnect SPI MikroBus(SST26) to EXT2 and reset!\r\n"TERM_RESET);
                g_appData.state = APP_STATE_ERROR;
                break;
            }
            
            /* Initialize RNWF Module */
            SYS_RNWF_IF_Init();
            
            g_appData.state = APP_STATE_GET_DEV_INFO;
            break;
        }
        
        /* Get RNWF device Information */
        case APP_STATE_GET_DEV_INFO:
        {
            
            if (SYS_RNWF_SYSTEM_SrvCtrl( SYS_RNWF_SYSTEM_SW_REV, g_appBuf) != SYS_RNWF_PASS)
            {
                /* Check if Flash has the New FW pre loaded in it */
                SYS_RNWF_OTA_HDR_t otaHdr;
                SYS_RNWF_OTA_FlashRead(SYS_RNWF_OTA_FLASH_IMAGE_START, sizeof(SYS_RNWF_OTA_HDR_t), (uint8_t *)&otaHdr.seq_num);
                
                SYS_CONSOLE_PRINT("Image details in the Flash\r\n");
                SYS_CONSOLE_PRINT("Sequence Number 0x%X\r\n", (unsigned int)otaHdr.seq_num);
                SYS_CONSOLE_PRINT("Start Address 0x%X\r\n", (unsigned int)otaHdr.start_addr);
                SYS_CONSOLE_PRINT("Image Length 0x%X\r\n", (unsigned int)otaHdr.img_len);
                
                if(otaHdr.seq_num != 0xFFFFFFFF && otaHdr.start_addr != 0xFFFFFFFF && otaHdr.img_len != 0xFFFFFFFF)               
                {        
                    g_appImgSize = otaHdr.img_len;
                    /* Program RNWF with pre loaded FW in Flash*/
                    g_appData.state = APP_STATE_PROGRAM_DFU;
                    break;
                }
                SYS_CONSOLE_PRINT(TERM_RED"[APP ERROR] : Module is Bricked!"TERM_RESET);
                
                g_appData.state = APP_STATE_ERROR;
                break;
            }
            else
            {
                if(g_appBuf[0] == '\0')
                {
                    SYS_CONSOLE_PRINT(TERM_RED"[APP ERROR] : No RNWF02 module found\r\n\tConnect RNWF02 module to EXT1 and reset\r\n"TERM_RESET);
                    g_appData.state = APP_STATE_ERROR;
                    break;
                }
                
                SYS_CONSOLE_PRINT(TERM_CYAN"[APP] : Software Revision: %s\r\n"TERM_RESET,g_appBuf);
            }
            
            /* Get RNWF device Information */
            SYS_RNWF_SYSTEM_SrvCtrl(SYS_RNWF_SYSTEM_DEV_INFO, g_appBuf);
            SYS_CONSOLE_PRINT("[APP] : Device Info: %s\r\n", g_appBuf);
            
            /* Get RNWF device Wi-Fi Information*/
            SYS_RNWF_SYSTEM_SrvCtrl(SYS_RWWF_SYSTEM_GET_WIFI_INFO, g_appBuf);
            SYS_CONSOLE_PRINT("[APP] : Network Configuration : %s\r\n\n", g_appBuf);
            
            g_appData.state = APP_STATE_REGISTER_CALLBACK;
            break;
        }
        
        /* Register the Callbacks with Services */
        case APP_STATE_REGISTER_CALLBACK:
        {
            /* Configure SSID and Password for STA mode */
            SYS_RNWF_WIFI_PARAM_t wifi_sta_cfg = {SYS_RNWF_WIFI_MODE_STA, SYS_RNWF_WIFI_STA_SSID, SYS_RNWF_WIFI_STA_PWD, SYS_RNWF_STA_SECURITY, 1};
            SYS_CONSOLE_PRINT("[APP] : Connecting to AP : %s\r\n",SYS_RNWF_WIFI_STA_SSID);
            
            /* Register Callback with Wifi Service */
            SYS_RNWF_WIFI_SrvCtrl(SYS_RNWF_WIFI_SET_CALLBACK, SYS_RNWF_WIFI_CallbackHandler);
            SYS_RNWF_WIFI_SrvCtrl(SYS_RNWF_SET_WIFI_PARAMS, &wifi_sta_cfg);
    
            /* Register Callback with OTA Service */
            SYS_RNWF_OTA_SrvCtrl(SYS_RNWF_OTA_SET_CALLBACK, (void *)SYS_RNWF_OTA_CallbackHandler);
            
            g_appData.state = APP_STATE_WAIT_FOR_DOWNLOAD;
            break;
        }
        
        /* Wait for Download to complete */
        case APP_STATE_WAIT_FOR_DOWNLOAD:
        {
            bool isDownloadDone = false;
            SYS_RNWF_OTA_SrvCtrl(SYS_RNWF_OTA_CHECK_DWLD_DONE,(void *)&isDownloadDone);
            
            if (isDownloadDone == true)
            {
                SYS_CONSOLE_PRINT(TERM_GREEN"[APP] : Download Completed !!!\r\n"TERM_RESET);
                g_appData.state = APP_STATE_PROGRAM_DFU;
            }
            break;
        }
        
        /* Program the RNWF device with New FW */
        case APP_STATE_PROGRAM_DFU:
        {
            bool OtaDfuComplete = false;
            
            SYS_RNWF_OTA_ProgramDfu(); 
            SYS_RNWF_OTA_SrvCtrl ( SYS_RNWF_OTA_CHECK_DFU_DONE, (void *)&OtaDfuComplete);
            
            if(OtaDfuComplete == true )
            {
                g_appData.state = APP_STATE_RESET_DEVICE;
            }
            break;
        }
        
        /* Reset RNWF device and Host */
        case APP_STATE_RESET_DEVICE:
        {
            APP_RNWF_SwResetHandler();
            
            break;
        }
        
        /* Application Error State */
        case APP_STATE_ERROR:
        {
            SYS_CONSOLE_PRINT(TERM_RED"[APP ERROR] : Error in Application\r\n"TERM_RESET);
            g_appData.state = APP_STATE_IDLE;
            break;
        }
        
        /* Application Idle state */
        case APP_STATE_IDLE:
        {
            break;
        }
        
        /* Default state */
        default:
        {
            break;
        }
    }
    
    /* Console Tasks */
    SYS_CONSOLE_Tasks(sysObj.sysConsole0);
    
    /* Interface Event Handler */
    SYS_RNWF_IF_EventHandler();
}

/*******************************************************************************
 End of File
 */

```

The data types used for the OTA service are provided below:

-   [OTA Modes Enum](GUID-D3C86805-5A5C-477E-9794-C8E14969C96D.md#GUID-EA13EBB2-7D50-44B9-96EA-60C931285A12)
-   [OTA Service Enum](GUID-D3C86805-5A5C-477E-9794-C8E14969C96D.md)
-   [OTA Event Enum](GUID-D3C86805-5A5C-477E-9794-C8E14969C96D.md)
-   [OTA Chunk Header Struct](GUID-D3C86805-5A5C-477E-9794-C8E14969C96D.md#GUID-ED2A0620-6B66-4906-A029-D4B3BA9C024D)


