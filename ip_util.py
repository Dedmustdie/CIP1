def get_ip_attributes(ip: str, mask: str) -> str:
    listIp = ip.split(".")
    listMask = mask.split(".")
    listNode = ["0", "0", "0", "0"]
    listBroad = ["0", "0", "0", "0"]
    listNet = ["0", "0", "0", "0"]
    maxNodesCount = 0

    listNodeRes = ""
    listBroadRes = ""
    listNetRes = ""

    for i in range(4):
        if listMask[i] == "0":
            listNode[i] = listIp[i]
            listBroad[i] = 255
            if maxNodesCount == 0:
                maxNodesCount = 2 ** (32 - i * 8 - str(bin(int(listMask[i]))).count('1')) - 2
        elif listMask[i] != "255":
            listNode[i] = (int(listIp[i]) & (255 - int(listMask[i])))
            listBroad[i] = listNode[i]
            listNet[i] = int(listIp[i]) & int(listMask[i])
            maxNodesCount = 2 ** (32 - i * 8 - str(bin(int(listMask[i]))).count('1')) - 2
        else:
            listNet[i] = int(listIp[i]) & int(listMask[i])
        listNodeRes += str(listNode[i])
        listBroadRes += str(listBroad[i])
        listNetRes += str(listNet[i])
        if i != 3:
            listNodeRes += "."
            listBroadRes += "."
            listNetRes += "."

    return ("Узел: " + listNodeRes + "\n" +
            "Широковещательный: " + listBroadRes + "\n" +
            "Сеть: " + listNetRes + "\n" +
            "Макс. узлы: " + str(maxNodesCount))


def get_net_address(ip: str, mask: str) -> str:
    listIp = ip.split(".")
    listMask = mask.split(".")
    listNet = ["0", "0", "0", "0"]

    listNetRes = ""

    for i in range(4):
        if listMask[i] != "0":
            listNet[i] = int(listIp[i]) & int(listMask[i])
        listNetRes += str(listNet[i])
        if i != 3:
            listNetRes += "."

    return listNetRes


def same_network(ip1: str, m1: str, ip2: str, m2: str) -> str:
    if get_net_address(ip1, m1) == get_net_address(ip2, m2):
        return "Узлы находятся в одной сети"
    else:
        return "Узлы находятся в разных сетях"


def get_min_mask(node1: str, node2: str) -> str:
    listNode1 = node1.split(".")
    listNode2 = node2.split(".")
    maskRes = ""
    okDec = 0
    for i in range(4):
        if listNode1[i] != listNode2[i]:
            ok1 = bytearray(listNode1[i], 'utf-8')
            ok2 = bytearray(listNode2[i], 'utf-8')
            j = 0
            while ok1[j] == ok2[j]:
                j += 1
                okDec += 2 ** (8 - j)
            maskRes += str(okDec)
            if i != 3:
                maskRes += "."
        else:
            if okDec == 0:
                maskRes += "255"
            else:
                maskRes += "0"
            if i != 3:
                maskRes += "."
    return "Минимальная маска: " + maskRes


