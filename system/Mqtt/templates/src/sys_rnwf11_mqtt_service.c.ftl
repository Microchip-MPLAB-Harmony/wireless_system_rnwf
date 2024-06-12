/*******************************************************************************
  RNWF Host Assisted MQTT Service Implementation

  File Name:
    sys_rnwf_mqtt_service.c

  Summary:
    Source code for the RNWF Host Assisted MQTT Service implementation.

  Description:
    This file contains the source code for the RNWF Host Assisted MQTT Service
    implementation.
 *******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
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
 *******************************************************************************/
//DOM-IGNORE-END


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
 */
#include <stdio.h>
#include <string.h>

/* This section lists the other files that are included in this file.
 */
#include "system/inf/sys_rnwf_interface.h"
#include "system/mqtt/sys_rnwf_mqtt_service.h"
#include "system/net/sys_rnwf_net_service.h"
#include "system/sys_rnwf_system_service.h"


#define SYS_RNWF_MQTT_DPS_TOP_SET_REG        "$dps/registrations/PUT/iotdps-register/?$rid=1"
#define SYS_RNWF_MQTT_DPS_MSG_SET_REQ        "{\\\"payload\\\": {\\\"modelId\\\": \\\"dtmi:com:Microchip:AVR128DB48_CNANO;1\\\"}}"


#define SYS_RNWF_MQTT_DPS_TOP_DPS_GET_STAT   "$dps/registrations/GET/iotdps-get-operationstatus/?$rid=2&operationId=%s"
#define SYS_RNWF_MQTT_DPS_MSG_DPS_GET_STAT   ""

//#define SYS_RNWF_MQTT_DPS_SUBSCRIBE_TOPIC    "$dps/registrations/res/#"


#define SYS_RNWF_MQTT_DPS_HUB_ID_STR         "\\\"assignedHub\\\":\\"""
#define SYS_RNWF_MQTT_DPS_DEV_ID_STR         "\\\"deviceId\\\":\\"""        
#define SYS_RNWF_MQTT_DPS_OP_ID_STR          "\\\"operationId\\\":\\"""
#define SYS_RNWF_MQTT_DPS_END_ID_STR         "\\\" \\\""


#define SYS_RNWF_MQTT_IOT_HUB_USERNAME       "%s/%s/?api-version=2021-04-12"

/* ************************************************************************** */
/* ************************************************************************** */
/* Section: File Scope or Global Data                                         */
/* ************************************************************************** */
/* ************************************************************************** */

SYS_RNWF_MQTT_CALLBACK_t g_MqttCallBackHandler[SYS_RNWF_MQTT_SERVICE_CB_MAX] = {NULL, NULL};
    

/* ************************************************************************** */
/* ************************************************************************** */
// Section: Local Functions                                                   */
/* ************************************************************************** */
/* ************************************************************************** */

/*MQTT Service control function*/
SYS_RNWF_RESULT_t SYS_RNWF_MQTT_SrvCtrl( SYS_RNWF_MQTT_SERVICE_t request, void *input)  
{
    SYS_RNWF_RESULT_t result = SYS_RNWF_FAIL;

    switch(request)
    {
        /**<Configure the MQTT Broker parameters*/
        case SYS_RNWF_MQTT_CONFIG:
        {
            uint8_t device_temp[sizeof(SYS_RNWF_MQTT_DPS_MSG_SET_REQ)];
            const char *begin;
            char *token;

            SYS_RNWF_MQTT_CFG_t *mqtt_cfg = (SYS_RNWF_MQTT_CFG_t *)input;  
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_SET_PROTO_VER, 3);

            if(mqtt_cfg->tls_idx != 0)
            {

                if(mqtt_cfg->tls_use_ecc608)
                {
                    if(mqtt_cfg->tls_idx == SYS_RNWF_NET_TLS_CONFIG_1)
                        result = SYS_RNWF_NET_SockSrvCtrl(SYS_RNWF_NET_TLS_ECC608_CONFIG_1, mqtt_cfg->tls_conf);
                    else
                        result = SYS_RNWF_NET_SockSrvCtrl(SYS_RNWF_NET_TLS_ECC608_CONFIG_2, mqtt_cfg->tls_conf);
                }
                else
                {

                result = SYS_RNWF_NET_SockSrvCtrl(mqtt_cfg->tls_idx, mqtt_cfg->tls_conf);

                }

                result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_SET_TLS_CONF, mqtt_cfg->tls_idx);                             
            }

            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_SET_BROKER_URL, mqtt_cfg->url);
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_SET_BROKER_PORT, mqtt_cfg->port);
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_SET_CLIENT_ID, mqtt_cfg->clientid);
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_SET_USERNAME, mqtt_cfg->username);
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_SET_PASSWORD, mqtt_cfg->password);
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_SET_KEEPALIVE, 60);
            
            if(mqtt_cfg->azure_dps)
            {

				result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_SET_SERVER_SEL, NULL);
				result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_SET_READ_LENGTH, 600);
				strcpy((char *)device_temp, SYS_RNWF_MQTT_DPS_MSG_SET_REQ);
				begin = strstr((char *)device_temp, "dtmi:");
				if(begin != NULL) {
					token = strtok((char *)begin, "\\");
					result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_SET_AZURE_DTMI, token);
				}
				else
					printf("Error in parsing modelID\r\n");

            }
            break;
        }    

        /**<Connect to the MQTT Broker */  
        case SYS_RNWF_MQTT_CONNECT:
        {
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_CMD_DISCONNECT);
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_CMD_CONNECT);     
        }
        break;

        /**<Request reconnect to the MQTT Cloud*/ 
        case SYS_RNWF_MQTT_RECONNECT:
	    {
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_CMD_RECONNECT);     
            break;
        }

        /**<Trigger Disconnect from MQTT Broker*/        
        case SYS_RNWF_MQTT_DISCONNECT:
	    {	
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_CMD_DISCONNECT);     
            break;
        }
        
        /**<Publis to MQTT Broker*/
        case SYS_RNWF_MQTT_PUBLISH:
        {
            SYS_RNWF_MQTT_FRAME_t *mqtt_frame = (SYS_RNWF_MQTT_FRAME_t *)input;
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_CMD_PUBLISH, mqtt_frame->isNew, mqtt_frame->qos, mqtt_frame->isRetain, mqtt_frame->topic, mqtt_frame->message);     
        }
        break;            
        
        /**<Subscribe to QoS0 Topics */
        case SYS_RNWF_MQTT_SUBSCRIBE_QOS0:
        {
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_CMD_SUBSCRIBE_QOS0, (const char *)input);
        }
        break;
	
        /**<Subscribe to QoS1 Topics */
        case SYS_RNWF_MQTT_SUBSCRIBE_QOS1:
        {
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_CMD_SUBSCRIBE_QOS1, (const char *)input);
        }
        break;
	
        /**<Subscribe to QoS2 Topics */
        case SYS_RNWF_MQTT_SUBSCRIBE_QOS2:
        {            
            result = SYS_RNWF_CMD_SEND_OK_WAIT(NULL, NULL, SYS_RNWF_MQTT_CMD_SUBSCRIBE_QOS2, (const char *)input);     
        }        
        break;            
        
        /**<Configure the MQTT Application Callback*/ 
        case SYS_RNWF_MQTT_SET_CALLBACK:
        {
            g_MqttCallBackHandler[1] = (SYS_RNWF_MQTT_CALLBACK_t)(input);
            result = SYS_RNWF_PASS;
        }
        break;

        /**<Configure the MQTT Application Callback*/     
        case SYS_RNWF_MQTT_SET_SRVC_CALLBACK:        
        {
            g_MqttCallBackHandler[0] = (SYS_RNWF_MQTT_CALLBACK_t)(input);            
            result = SYS_RNWF_PASS;
        }
        break;
        
        case SYS_RNWF_MQTT_GET_CALLBACK:
        {
            SYS_RNWF_MQTT_CALLBACK_t *mqttCallBackHandler;
            mqttCallBackHandler = (SYS_RNWF_MQTT_CALLBACK_t *)input;
            
            mqttCallBackHandler[0] = g_MqttCallBackHandler[0];
            mqttCallBackHandler[1] = g_MqttCallBackHandler[1];
            break;
        }
            
        default:
            break;    
    }

    return result;
}


/* *****************************************************************************
 End of File
 */