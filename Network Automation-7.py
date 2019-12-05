# Program starts
#Call gns3
#loop n number times where n = the number of routers
for router in range(1,5):
    if router == 1: 
        ip = '192.168.1.101' 
    elif router == 2: 
        ip = '192.168.1.102'
    elif router == 3: 
        ip = '192.168.1.103'
    elif router == 4: 
        ip = '192.168.1.104'
    telnet_gns3(ip,router) 
#--------------------

ip = '192.168.1.101' 
n = 50

for router in range(1,5):
    quad = ip[len(ip)-3:len(ip)]
    quad_int = int(quad)
    quad_int = quad_int + 1
    quads = str(quad_int)

    temp_ip = ip[:len(ip)-3]
    ip = temp_ip + quads
    


















