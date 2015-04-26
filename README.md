pyTcpTran
=========

> ###基于ip_relay的tcp/udp端口转发小工具

> pyTcpTran可用来为Burpsuite的Intruder模块做http代理切换

> Burpuite需要做两处设置：

> 1. options -> upstream proxy server -> add

>         destination host: *
>         proxy host: 127.0.0.1
>         proxy port: 5551(默认）

> 2. Intruder模块，payload中的url写全路径

>     例如：     
> 
>         GET /ic.asp HTTP/1.1
>         Host: 1111.ip138.com
>         ......
>     
>     修改为 
>
>         GET http://1111.ip138.com/ic.asp HTTP/1.1
>         Host: 1111.ip138.com
>         ......

> ###usage:  
>     python pyTcpTran proxy.txt 5551

 
> https://github.com/retanoj/BurpMultiProxy Burpsuite插件版代理工具
