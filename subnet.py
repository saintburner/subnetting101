binaryValues = [128, 64, 32, 16, 8 , 4, 2, 1]


#Need to create primary variables with sub attributes
#I.E provIPaddress will be the primary variable and provIPaddress_octet will 
#instead becomes a sub attribute of "Octets = []", the same goes for bits and 
#slash notation values (for submasks)

class provIPaddress():
    octets = []
    bits = []

class provSubMask():
    octets = []
    bits = []
    slashNot = 0

class defSubMask():
    octets = []
    bits = []
    slashNot = 0


provIPaddress = input("IP Address: ").split('.')
provSubMask = input("Subnet Mask: ").split('.')
defSubMask = []

provIPaddress_octets = []
provSubMask_octets = []
defSubMask_octets = []

provIPaddress_bits = []
provSubMask_bits = []
defSubMask_bits = []

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
        defSubMask.extend(["255", "0", "0", "0"])
        octetCreate(defSubMask, defSubMask_octets)
        #Assign slash notation value 8 to defSubMask property
    elif x[0] > 127 and x[0] < 192:
        print("Class B")
        defSubMask.extend(["255", "255", "0", "0"])
        octetCreate(defSubMask, defSubMask_octets)
        #Assign slash notation value 16 to defSubMask property
    elif x[0] > 191 and x[0] < 224:
        print("Class C")
        defSubMask.extend(["255", "255", "255", "0"])
        octetCreate(defSubMask, defSubMask_octets)
        #Assign slash notation value 24 to defSubMask property
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
def slashNot(x):
    slashNotValue = (str(x[0].count('1')))
    print(slashNotValue)


octetCreate(provIPaddress, provIPaddress_octets)
octetCreate(provSubMask, provSubMask_octets)    
classAssign(provIPaddress_octets)

binaryConvert(provSubMask_octets, provSubMask_bits)
binaryConvert(defSubMask_octets, defSubMask_bits)

# print(provIPaddress_bits)
# print(provSubMask_bits)
# print(defSubMask_bits)

slashNot(provSubMask_bits)