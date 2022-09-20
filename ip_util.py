import string


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
            listNet[i] = int(listIp[i]) & int(listMask[i])
            x = 8 - str(bin(int(listMask[i]))).count('1')
            print(x)
            broadOk = 0
            for j in range(x):
                if j == 0:
                    broadOk += 1
                else:
                    broadOk += 2 ** j
            broadOk += listNet[i]
            listBroad[i] = str(broadOk)

            maxNodesCount = 2 ** (32 - i * 8 - str(bin(int(listMask[i]))).count('1')) - 2
        else:
            listNet[i] = int(listIp[i]) & int(listMask[i])
            listBroad[i] = int(listIp[i]) & int(listMask[i])
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

def get_bin_array(ok: int):
    okStrC = str(bin(ok))[2:]
    print(okStrC)
    resList = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(okStrC)):
        resList[7-i] = int(okStrC[len(okStrC)-(i+1)])
    return resList

def get_min_mask_duo(node1, node2):
    listNode1 = node1.split(".")
    listNode2 = node2.split(".")
    listMinMask = [255, 255, 255, 255]
    okDec = 0
    i = 3
    while i != -1:
        if listNode1[i] != listNode2[i]:
            ok1 = get_bin_array(int(listNode1[i]))
            ok2 = get_bin_array(int(listNode2[i]))
            print(ok1)
            print(ok2)
            j = 0
            while ok1[j] == ok2[j]:
                j += 1
                okDec += 2 ** (8 - j)
            listMinMask[i] = okDec
            break
        else:
            listMinMask[i] = 0

        i -= 1

    return listMinMask


def get_min_mask(nodes_list: list) -> str:
    min_mask = [-1, -1, -1, -1]
    for i in range(len(nodes_list) - 1):
        for j in range(len(nodes_list) - 1):
            j += i + 1
            mask = get_min_mask_duo(nodes_list[i], nodes_list[j])
            for k in range(4):
                if mask[i] > min_mask[i]:
                    min_mask = mask
                    break

    min_mask_res = ""
    for i in range(4):
        min_mask_res += str(min_mask[i])
        if i != 3:
            min_mask_res += "."

    return "Минимальная маска: " + min_mask_res
