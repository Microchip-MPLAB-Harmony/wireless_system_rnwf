/* WINCS02  WIFIPROV System Service Configuration Options */

#define SYS_WINCS_WIFIPROV_CallbackHandler		${SYS_RNWF_WIFIPROV_CALLBACK_HANDLER}
<#if SYS_RNWF_PROV_DEBUG_LOGS == true>
#define SYS_WINCS_PROV_DEBUG_LOGS                1
</#if>
