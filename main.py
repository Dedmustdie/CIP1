import ip_util
print(str(ip_util.get_ip_attributes("128.43.0.1", "255.224.0.0")))
print("Выберете задание: \n"
      "1)\n"
      "2)\n"
      "3)\n")
task_number = input()


if task_number == "1":
    print("Введите ip-адрес: ")
    ip = input()
    print("Введите маску: ")
    mask = input()
    print(ip_util.get_ip_attributes(ip, mask))
elif task_number == "2":
    print("Введите адресс первого узла: ")
    ip1 = input()
    print("Введите маску первого узла: ")
    m1 = input()
    print("Введите адресс второго узла: ")
    ip2 = input()
    print("Введите адресс третьего узла: ")
    m2 = input()
    print(ip_util.same_network(ip1, m1, ip2, m2))
elif task_number == "3":
    a = ""
    nodesList = []
    while a != "s":
        print("Введите адрес узла (s - stop): ")
        a = input()
        if a == "s":
            break
        nodesList.append(a)
    print(str(ip_util.get_min_mask(nodesList)))


#print(ip_util.same_network("17.53.128.0", "255.255.240.0", "17.53.127.0", "255.255.240.0"))

# print(str(ip_util.get_min_mask_duo("17.53.128.0", "17.53.127.0")))

# print(str(ip_util.get_min_mask_duo("17.53.128.0", "17.53.128.0")))

#print(str(ip_util.get_min_mask(["17.53.128.0", "17.53.127.0"])))

