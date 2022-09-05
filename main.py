import ip_util

print(ip_util.get_ip_attributes("10.216.1.93", "255.0.0.0"))

print(ip_util.same_network('192.168.1.0', "255.0.0.0", '192.32.45.7', "255.0.0.0"))

print(ip_util.same_network("17.53.128.0", "255.255.240.0", "17.53.127.0", "255.255.240.0"))

print(ip_util.get_min_mask("17.53.128.0", "17.53.127.0"))