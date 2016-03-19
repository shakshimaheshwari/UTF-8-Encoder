import sys
def byte2int(bstr, width=32):
    """
    Convert a byte string into a signed integer value of specified width.
    """
    val = sum(ord(b) << 8*n for (n, b) in enumerate(reversed(bstr)))
    if val >= (1 << (width - 1)):
        val = val - (1 << width)
    return val

filename = sys.argv[1]
f = open(filename,"rb")
f1 = open("utf8encoder_out.txt",'wb')
try:
    byte = f.read(2)
    while byte != "":
        hexValue = hex(byte2int(byte))
        integervalue = int(hexValue,16);
        binary = bin(int(hexValue, 16))[2:]
        
        if(len(binary)<16):
            k = 16-len(binary)
            while(k!=0):
                binary = "0"+binary
                k=k-1

        if(integervalue >= (int('0000',16)) and integervalue <= (int('007f',16))):
            binarychunkneeded= binary[9:]
            finalbinaryvalue="0"+binarychunkneeded
        elif(integervalue >= (int('0080',16))and integervalue <= (int('07ff',16))):
            binarychunkneeded = binary[5:10]
            binarychunk1 = binary[10:]
            finalbinaryvalue = "110"+binarychunkneeded+"10"+binarychunk1
        else:
            binarychunk1 = binary[0:4]
            binarychunk2 = binary[4:10]
            binarychunk3 = binary[10:]
            finalbinaryvalue = "1110"+binarychunk1+"10"+binarychunk2+"10"+binarychunk3
        while(len(finalbinaryvalue)!=0):
            newfinalbinaryvalue = finalbinaryvalue[0:8]
            finalbinaryvalue = finalbinaryvalue[8:]
            n = int(newfinalbinaryvalue,2)
            data = chr(n)
            f1.write(data)
        
        byte = f.read(2)
finally:
    f1.close()
    f.close()
