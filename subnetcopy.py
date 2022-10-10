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
    rangeValidHosts = []
    lockedOctets = 0
    blockSize = []


#OCTET CREATION
#x equals input from standard list
#y equals output to octets list
def octetCreate(x, y):
    if len(x) != 4:
        print("Invalid: IP Length - {} octets".format(str(len(x))))
    else:
        for i in x:
            if i < "0" or i > "255":
                invalidOctet = x.index(i) + 1
                print("Invalid: Octet {}".format(invalidOctet))
                y.clear()
                break
            else:
                y.append(int(i))
    # print(y)


#CLASS ASSIGNMENT
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
def slashNot(x, y):
    slashNotValue = (int(x[0].count('1')))
    y.append(slashNotValue)


#FINDS WHICH OCTET THE SUBNET WILL BEGIN ON AND DETERMINES
#THE BLOCK SIZE
#x provSubMask.slashNot
#y defSubMask.slashNot
def findOutputOctet(x, y):
    if x < y:
        print("Incorrect Subnet Mask")
    else:
        slashNotValue = x[0] - y[0]
        addLockedOctet, tempBlockSize = divmod(slashNotValue, 8)
        outputAddresses.lockedOctets = outputAddresses.lockedOctets + addLockedOctet
        outputAddresses.blockSize = binaryValues[tempBlockSize - 1]


octetCreate(provIPaddress.value, provIPaddress.octets)
octetCreate(provSubMask.value, provSubMask.octets)    
classAssign(provIPaddress.octets)

binaryConvert(provIPaddress.octets, provIPaddress.bits)
binaryConvert(provSubMask.octets, provSubMask.bits)
binaryConvert(defSubMask.octets, defSubMask.bits)

slashNot(provSubMask.bits, provSubMask.slashNot)

findOutputOctet(provSubMask.slashNot, defSubMask.slashNot)

print('Locked octets = ', outputAddresses.lockedOctets)
print('Block size = ', outputAddresses.blockSize)

def networkAddress():
    

networkAddress()