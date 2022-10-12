binaryValues = [128, 64, 32, 16, 8 , 4, 2, 1]

class provIPaddress():
    value = input("IP Address: ").split('.')
    octets = []
    bits = []

class provSubMask():
    value = input("Subnet Mask: ").split('.')
    octets = []
    bits = []
    slashNot = []

class defSubMask():
    value = []
    octets = []
    bits = []
    slashNot = []

class outputAddresses():
    network = []
    broadcast = []
    rangeValidHostsFirst = []
    rangeValidHostsLast = []
    lockedOctets = 0
    blockSize = []
    blockSizePlace =[]


#OCTET CREATION
#x equals input from standard list
#y equals output to octets list
def octetCreate(x, y):
    if len(x) != 4:
        print("Invalid: IP Length - {} octets".format(str(len(x))))
    else:
        for i in x:
            tempInt = int(i)
            if tempInt < 0 or tempInt > 255:
                invalidOctet = x.index(i) + 1
                print("Invalid: Octet {}".format(invalidOctet)) #GETTING ERROR WITH SINGLE DIGIT VALUES
                y.clear()
                break
            else:
                y.append(int(i))
    # print(y)


#CLASS ASSIGNMENT
#x provIPaddress.octets
def classAssign(x):
    if len(x) == 0:
        print("Unable to define class")
    elif x[0] > 0 and x[0] < 127:
        print("Class A")
        (defSubMask.value).extend(["255", "0", "0", "0"])
        octetCreate(defSubMask.value, defSubMask.octets)
        defSubMask.slashNot.append(8)
        outputAddresses.lockedOctets += 1
    elif x[0] > 127 and x[0] < 192:
        print("Class B")
        (defSubMask.value).extend(["255", "255", "0", "0"])
        octetCreate(defSubMask.value, defSubMask.octets)
        defSubMask.slashNot.append(16)
        outputAddresses.lockedOctets += 2
    elif x[0] > 191 and x[0] < 224:
        print("Class C")
        (defSubMask.value).extend(["255", "255", "255", "0"])
        octetCreate(defSubMask.value, defSubMask.octets)
        defSubMask.slashNot.append(24)
        outputAddresses.lockedOctets += 3
    elif x[0] == 127:
        print("Feedback Loop")
    else: 
        print("This IP Address does not have a valid class.")


#DECIMAL TO BINARY BITS CONVERSION
#x is input from octets list
#y is output to bits list
def binaryConvert(x, y):
    tempList = []
    for i in x:
        for b in binaryValues:
            if i >= b:
                tempList.append('1')
                i = i - b
            else:
                tempList.append('0')
    y.append(tempList)
    # y.append(''.join(tempList)) IF JOIN NEEDED ?


#NEED TO VERIFY THAT PROVSUBMASK IS A CONTINUOUS STRING OF 1S AND NO 1S ARE 
#PRESENT AFTER THE FIRST 0. 
# def verifySubMask(x):
#     tempVerifyOctets = []
#     tempVerifyBits = []
#     octetCreate(x, tempVerifyOctets)
#     binaryConvert(tempVerifyOctets, tempVerifyBits)
#     for x,y in zip(arr2,arr2[1:]):
#     if x == y == 2:
#         print('BROKEN!!!!')
    # for i in tempVerifyBits[0]:
    #     if i == '0':
    #         nextBit = tempVerifyBits[0].index(i) + 1
    #         if tempVerifyBits[0][nextBit] == '1':
    #             print('FUCK!!!!!')
            # print(nextBit)
            # print('0')
        # else:
        #     print('1')
    # print(tempVerifyBits[0])

# verifySubMask(provSubMask)


#SLASH NOTATION
#input x is from provSubMask_bits[0]
#y is output to slashNot list attribute
def slashNot(x, y):
    slashNotValue = (int(x[0].count('1')))
    y.append(slashNotValue)


#FINDS WHICH OCTET THE SUBNET WILL BEGIN ON AND DETERMINES
#THE BLOCK SIZE
#x provSubMask.slashNot
#y defSubMask.slashNot
def findBlockSize(x, y):
    if x < y:
        print("Incorrect Subnet Mask")
    else:
        slashNotValue = x[0] - y[0]
        addLockedOctet, tempBlockSize = divmod(slashNotValue, 8)
        outputAddresses.lockedOctets = outputAddresses.lockedOctets + addLockedOctet
        outputAddresses.blockSizePlace = tempBlockSize
        if tempBlockSize == 0:
            outputAddresses.blockSize = 256 
        else:
            outputAddresses.blockSize = binaryValues[tempBlockSize - 1]


#x provIPaddress.octets
#z outputAddress.network
def networkAddress(x, z):
    for i in x:
        if x.index(i) < outputAddresses.lockedOctets:
            z.append(i)
    #VARIABLE OCTET WILL CHANGE ACCORDING TO BLOCK SIZE AND CORRESPONDING OCTET FROM
    #PROVIDED IP ADDRESS
    #IF VARIABLE OCTET IN PROVIDED SUBMASK IS 0, IMMEDIATELY
    #SET BLOCK SIZE 
    # outputAddresses.network.append
    variableOctet = (int(provIPaddress.octets[int(outputAddresses.lockedOctets)]/(outputAddresses.blockSize))) * outputAddresses.blockSize
    z.append(variableOctet)
    while True:
        if len(z) != 4:
            z.append(0)
        if len(z) == 4:
            break
    outputAddresses.network = '.'.join(map(str, z)) 


def broadcastAddress(x, z):
    for i in x:
        if x.index(i) < outputAddresses.lockedOctets:
            z.append(i)
    variableOctet = (((int(provIPaddress.octets[int(outputAddresses.lockedOctets)]/(outputAddresses.blockSize))) * outputAddresses.blockSize) + outputAddresses.blockSize) - 1
    z.append(variableOctet)
    while True:
        if len(z) != 4:
            z.append(255)
        if len(z) == 4:
            break
    outputAddresses.broadcast = '.'.join(map(str, z)) 


#x provIPaddress.octets
#y outputAddresses.rangeValidHostsFirst
#z outputAddresses.rangeValidHostsLast
def rangeValidHosts(x, y, z):
    for i in x:
        if x.index(i) < outputAddresses.lockedOctets:
            y.append(i)
            z.append(i)
    variableOctet = ((int(provIPaddress.octets[int(outputAddresses.lockedOctets)]/(outputAddresses.blockSize))) * outputAddresses.blockSize)
    y.append(variableOctet)
    z.append(variableOctet + (outputAddresses.blockSize - 1))
    while True:
        if len(y) != 4:
            y.append(0)
        if len(y) == 4:
            break
    while True:
        if len(z) != 4:
            z.append(255)
        if len(z) == 4:
            break
    outputAddresses.rangeValidHostsFirst[3] =  outputAddresses.rangeValidHostsFirst[3] + 1
    outputAddresses.rangeValidHostsLast[3] = outputAddresses.rangeValidHostsLast[3] - 1
    outputAddresses.rangeValidHostsFirst = '.'.join(map(str, y)) 
    outputAddresses.rangeValidHostsLast = '.'.join(map(str, z)) 


octetCreate(provIPaddress.value, provIPaddress.octets)
octetCreate(provSubMask.value, provSubMask.octets)    
classAssign(provIPaddress.octets)

binaryConvert(provIPaddress.octets, provIPaddress.bits)
binaryConvert(provSubMask.octets, provSubMask.bits)
binaryConvert(defSubMask.octets, defSubMask.bits)

slashNot(provSubMask.bits, provSubMask.slashNot)

findBlockSize(provSubMask.slashNot, defSubMask.slashNot)

# print('Locked octets = ', outputAddresses.lockedOctets)
print('Block size:', outputAddresses.blockSize)

networkAddress(provIPaddress.octets, outputAddresses.network)
broadcastAddress(provIPaddress.octets, outputAddresses.broadcast)

rangeValidHosts(provIPaddress.octets, outputAddresses.rangeValidHostsFirst, outputAddresses.rangeValidHostsLast)

print("Network Address:", outputAddresses.network)
print("Broadcast Address:", outputAddresses.broadcast)
print("Range of Valid Host Addresses: {0} - {1}".format(outputAddresses.rangeValidHostsFirst, outputAddresses.rangeValidHostsLast))