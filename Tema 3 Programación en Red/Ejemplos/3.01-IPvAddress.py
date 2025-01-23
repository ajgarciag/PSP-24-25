import ipaddress

ip = ipaddress.IPv4Address('172.19.27.91')

print("Bits en la IP:", ip.max_prefixlen)
print("Multicast:", ip.is_multicast) #rango 224.0.0.0 a 239.255.255.255
print("Privada:", ip.is_private) 
#rangos privados: 0.0.0.0 a 10.255.255.255 , 172.16.0.0 a 172.31.255.255, 192.168.0.0 a 192.168.255.255
print("Pública:", ip.is_global)
print("No es específica:", ip.is_unspecified)
print("Reservada:", ip.is_reserved)
print("Loopback:", ip.is_loopback) #rango 127.0.0.0 a 127.255.255.255
print("Uso local:", ip.is_link_local) #rango 169.254.0.0 a 169.254.255.255
ip1 = ip + 1
print("IP siguiente:", ip1)
ip2 = ip - 1
print("IP anterior:", ip2)
print(ip1 , "mayor que", ip2, ":", ip1 > ip2) #se pueden comparar