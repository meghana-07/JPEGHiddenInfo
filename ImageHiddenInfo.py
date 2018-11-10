import binascii 
fname=input("\nEnter image file name\n") 
with open(fname,'rb') as imgFile:#opening jpeg file in binary mode.
    f=imgFile.read()
size=len(f)
print('Size of file is', size, 'bytes')
f1=f.find(b'\xff\xd8')#Start of Image Marker identifier
f2=f.find(b'\xff\xd9')#End of Image Marker Identifier
f3=f.find(b'\xff\xe0')#JFIF Application Segment identifier
f4=f.find(b'\xff\xe1')#Other Application Segment identifier
f5=f.find(b'\xff\xdb')#Quantization Table identifier
f6=f.find(b'\xff\xc0')#Start of Frame identifier
f7=f.find(b'\xff\xc4')#Huffman Table identifier
f8=f.find(b'\xff\xda')#Start of Scan identifier

def checkJpeg():
    if f1==0 and f2==(size-2):
        print("This is a jpeg file as SOI(Start of Image) and EOI(End of Image) match that of jpeg file")
        return 1
    else:
        print("Not a jpeg image")
        return 0
def JFIFSegment():
    if f3==2:
        print("Start of first JFIF Application Segment")
    if f4==-1:
        print("This image has only JFIF Application Segment, no other optional application segments.")
    #Describing the APP0 Marker(First JFIF Segment)
    j1=int(binascii.hexlify(f[f3+2:f3+4]),16)
    print("Length of APP0 segment is",j1,)#4th and 5th byte give the length of the APP0 marker in bytes
    j2=f[f3+4:f3+9]
    print("Identifier(should be JFIF followed by a null byte) is ",j2) #Identifies the JFIF marker
    j3=f[f3+9:f3+11]
    print("JFIF major version", j3[0], "minor version", j3[1] , "==> JFIF version",j3[0],".",j3[1])
    j4=f[f3+11]#Density unit for X and Y
    print("Density Unit(0-No unit,1-Pixels per inch,2-Pixels per centimeter)",j4)
    j5=int(binascii.hexlify(f[f3+12:f3+14]),16)
    print("Horizontal pixel density is",j5 )
    j6=int(binascii.hexlify(f[f3+14:f3+16]),16)
    print("Vertical pixel density is",j6)
    j7=f[f3+16]
    j8=f[f3+17]
    if j7==0 and j8==0:
        print("Thumbnail image doesn't exist.")#If thumnail exists, next few bytes represent thumnail information.
    else:
        print("Thumbnail horizontal pixels is",j7)
        print("Thumnail vertical pixels is",j8)

    #Next few bytes will be for application specific segments if they exist.

#Quantization tables
def QuantizationTable():
    if f5 is not -1:
        print("DQT(Define Quantization Table) found at index",f5)
    #Jpeg images have one or more quantizaion tables consisting of 3 things , 1.Quantization table length 2. Quantization table number 3. Quantization table.
    q1=int(binascii.hexlify(f[f5+2:f5+4]),16)
    print("Length of QT is",q1)
    print("Quantization data in decimal form is:")
    for i in range(f5+4,f6):
        print(f[i],end=" ")
#SOF0(Start of Frame 0)   
def SOFO():    


    if f6 is not -1:
        print("\nSOF0(Start of Frame 0) found at index",f6)
    sf1=int(binascii.hexlify(f[f6+2:f6+4]),16)
    print("Length of SOF0 is ",sf1)
    sf2=f[f6+4]
    print("Data precision(Bits per pixel per color component) is",sf2)
    sf3=int(binascii.hexlify(f[f6+5:f6+7]),16)
    print("Image height is",sf3,"pixels")
    sf4=int(binascii.hexlify(f[f6+7:f6+9]),16)
    print("Image width is",sf4,"pixels")
    sf5=f[f6+9]
    print("No. of components in image is",sf5)
    if(sf5==3):
        print("RGB image(3 = color YcbCr or YIQ)")
    elif(st5==1):
        print("GreyScaled image")
    #Next few bytes read each component data of 3 bytes. 
    for i in range (f6+10,f7):
        print(f[i],end=" ")#Reading each component data of 3 bytes. It contains,(component Id(1byte)(1 = Y, 2 = Cb, 3 = Cr, 4 = I, 5 = Q),sampling factors (1byte) (bit 0-3 vertical., 4-7 horizontal.),quantization table number (1 byte)).
#Checking whether SOF1, SOF2, SOF3 are present or not(usually not present).
def otherSOF():

    f6a=f.find(b'\xff\xc1')
    if f6a is -1:
        print("\nSOF1 not found")
    f6b=f.find(b'\xff\xc2')
    if f6b is -1:
        print("SOF2 not found")
    f6c=f.find(b'\xff\xc3')
    if f6c is -1:
        print("SOF3 not found")

#Huffman Table
def HuffmanTable():
    if f7 is not -1:
        print("Huffman Table found at index", f7)
        h1=int(binascii.hexlify(f[f7+2:f7+4]),16)
        print("Length of huffman Table is",h1,"bytes")
        h2=f[f7+4]
        print("Huffman Information(type of HT, 0 = DC table, 1 = AC table) =",h2)
        h3=h3=f[f7+5:f8]
        print("Huffman coding info",h3)

#Star of Scan(SOS)
def StartOfScan():
    if f8 is not -1:
        print("Start of Scan marker found at index",f8)
        s1=int(binascii.hexlify(f[f8+2:f8+4]),16)
        print("Length of SOS marker is",s1,"bytes")#This must be equal to 6+2*(number of components in scan).==> 6+2*3=12
        s2=f[f8+4]
        #For each component, read 2 bytes ==> next 6 bytes.
        #This will be folllowed by image data scans information.
#Last marker after SOS is EOI marker which has already been detected in the start.
#Calling all the functions
if checkJpeg()==1:
    JFIFSegment()
    QuantizationTable()
    SOFO()
    otherSOF()
    HuffmanTable()
    StartOfScan()
else:
    print("Please enter jpeg image")

