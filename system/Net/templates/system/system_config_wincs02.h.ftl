/*----------------- WINCS Net System Service Configuration -----------------*/
<#list 0..(SYS_RNWF_NET_NO_OF_SOCKS - 1) as i>
<#assign mode = ("SYS_RNWF_NET_MODE" + i)?eval>
<#assign sockType = ("SYS_RNWF_NET_SOCK_TYPE" + i)?eval>
<#assign sockIpType = ("SYS_RNWF_NET_SOCK_IP_TYPE" + i)?eval>
<#assign sockIpAddr = ("SYS_RNWF_NET_SOCK_IP_ADDR" + i)?eval>
<#assign sockPort = ("SYS_RNWF_NET_SOCK_PORT" + i)?eval>
<#assign enableTls = ("SYS_RNWF_NET_ENABLE_TLS" + i)?eval>
<#assign peerAuth = ("SYS_RNWF_NET_PEER_AUTH" + i)?eval>
<#assign rootCert = ("SYS_RNWF_NET_ROOT_CERT" + i)?eval>
<#assign deviceCert = ("SYS_RNWF_NET_DEVICE_CERTIFICATE" + i)?eval>
<#assign deviceKey = ("SYS_RNWF_NET_DEVICE_KEY" + i)?eval>
<#assign deviceKeyPwd = ("SYS_RNWF_NET_DEVICE_KEY_PWD" + i)?eval>
<#assign serverName = ("SYS_RNWF_NET_SERVER_NAME" + i)?eval>
<#assign domainNameVerify = ("SYS_RNWF_NET_DOMAIN_NAME_VERIFY" + i)?eval>
<#assign domainName = ("SYS_RNWF_NET_DOMAIN_NAME" + i)?eval>
<#if mode == "SERVER">
#define SYS_WINCS_NET_BIND_TYPE${i}                SYS_WINCS_NET_BIND_LOCAL
<#elseif mode == "CLIENT">
#define SYS_WINCS_NET_BIND_TYPE${i}                SYS_WINCS_NET_BIND_REMOTE 
</#if>
<#if sockType == "UDP">
#define SYS_WINCS_NET_SOCK_TYPE${i}                SYS_WINCS_NET_SOCK_TYPE_UDP
<#elseif sockType == "TCP">
#define SYS_WINCS_NET_SOCK_TYPE${i}                SYS_WINCS_NET_SOCK_TYPE_TCP 
</#if>
<#if sockIpType == "IPv4">
#define SYS_WINCS_NET_SOCK_TYPE_IPv4_${i}          4
#define SYS_WINCS_NET_SOCK_TYPE_IPv6_LOCAL${i}     0
#define SYS_WINCS_NET_SOCK_TYPE_IPv6_GLOBAL${i}    0
<#elseif sockIpType == "IPv6 Local">
#define SYS_WINCS_NET_SOCK_TYPE_IPv4_${i}          0
#define SYS_WINCS_NET_SOCK_TYPE_IPv6_LOCAL${i}     6
#define SYS_WINCS_NET_SOCK_TYPE_IPv6_GLOBAL${i}    0
<#elseif sockIpType == "IPv6 Global">
#define SYS_WINCS_NET_SOCK_TYPE_IPv4_${i}          0
#define SYS_WINCS_NET_SOCK_TYPE_IPv6_LOCAL${i}     0
#define SYS_WINCS_NET_SOCK_TYPE_IPv6_GLOBAL${i}    6
</#if>
<#if mode == "CLIENT">
#define SYS_WINCS_NET_SOCK_SERVER_ADDR${i}         "${sockIpAddr}"
</#if>
#define SYS_WINCS_NET_SOCK_PORT${i}                ${sockPort}
<#if enableTls == true>
#define SYS_WINCS_TLS_ENABLE${i}                   1
<#if peerAuth == true>
#define SYS_WINCS_NET_PEER_AUTH${i}                true
#define SYS_WINCS_NET_ROOT_CERT${i}                "${rootCert}"
</#if>
<#if deviceCert == "">
#define SYS_WINCS_NET_DEVICE_CERTIFICATE${i}       NULL
<#else>
#define SYS_WINCS_NET_DEVICE_CERTIFICATE${i}       "${deviceCert}"
</#if>
<#if deviceKey == "">
#define SYS_WINCS_NET_DEVICE_KEY${i}               NULL
<#else>
#define SYS_WINCS_NET_DEVICE_KEY${i}               "${deviceKey}"
</#if>
<#if deviceKeyPwd == "">
#define SYS_WINCS_NET_DEVICE_KEY_PWD${i}           NULL
<#else>
#define SYS_WINCS_NET_DEVICE_KEY_PWD${i}           "${deviceKeyPwd}"
</#if>
<#if serverName == "">
#define SYS_WINCS_NET_SERVER_NAME${i}              NULL
<#else>
#define SYS_WINCS_NET_SERVER_NAME${i}              "${serverName}"
</#if>
<#if domainNameVerify == true>
#define SYS_WINCS_NET_DOMAIN_NAME_VERIFY${i}       1
#define SYS_WINCS_NET_DOMAIN_NAME${i}              "${domainName}"
<#else>
#define SYS_WINCS_NET_DOMAIN_NAME_VERIFY${i}       0
#define SYS_WINCS_NET_DOMAIN_NAME${i}              ""
</#if>
<#else>
#define SYS_WINCS_TLS_ENABLE${i}                   0
</#if>
</#list>
<#if SYS_RNWF_NET_DEBUG_LOGS == true>
#define SYS_WINCS_NET_DEBUG_LOGS                 1
</#if>
/*----------------------------------------------------------------------------*/