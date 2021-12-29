import os
import requests as req
import socket , time
from colorama import Fore , init
init()

os.system("clear")

print('''\007
\033[0;35m ___  ____     ____
 / _ \|  _ \   / ___| ___ _ __
| | | | |_) | | |  _ / _ \ '_ \
| |_| |  _ <  | |_| |  __/ | | |
 \__\_\_| \_\  \____|\___|_| |_|\033[5;31mv1.0

\033[1;36m ==================================================\033[1;m
\033[1;33m|    [+] By HIRUWA     [+] QR GEN Api              |
\033[1;33m|    [+] DARK CRIME OWNER                          |
\033[1;33m|                                                  |
\033[1;36m ==================================================\033[00m-''')
print()
print('''\033[0;36m[1] සිංහල ''')
print('''\033[0;36m[2] English ''')
print()
print("\033[0;35mඔබගේ භාෂාව තෝරන්න: ")
print("\033[0;35mSelect Your language: ")
ya = input('''\033[0;37m[+] -> ''')
print()

def english():
    try:
        ip = socket.gethostbyname("www.google.com") 
        print('''\033[0;32m[+] Internet : Active\n''')   
    except Exception as e: 
        print('''\033[0;31m[-] Internet : Not Available \nExitting in 5 seconds''')  
        time.sleep(5)
        exit()

    Data = input('''Enter data to store in QR code : ''')

    url = "https://qr-generator.qrcode.studio/qr/custom"

    #data = input("Enter url : ")

    #payload = {"data":"https://www.qrcode-monkey.com","config":{"body":"rounded-pointed","eye":"frame14","eyeBall":"ball16","erf1":[],"erf2":["fh"],"erf3":["fv"],"brf1":[],"brf2":["fh"],"brf3":["fv"],"bodyColor":"#5C8B29","bgColor":"#FFFFFF","eye1Color":"#3F6B2B","eye2Color":"#3F6B2B","eye3Color":"#3F6B2B","eyeBall1Color":"#60A541","eyeBall2Color":"#60A541","eyeBall3Color":"#60A541","gradientColor1":"#5C8B29","gradientColor2":"#25492F","gradientType":"radial","gradientOnEyes":"false","logo":""},"size":"300","download":"false","file":"svg"}
    payload1 = {"data":Data,"config":{"body":"square","eye":"frame13","eyeBall":"ball14","erf1":[],"erf2":[],"erf3":[],"brf1":[],"brf2":[],"brf3":[],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#021326","eye2Color":"#021326","eye3Color":"#021326","eyeBall1Color":"#074f03","eyeBall2Color":"#074f03","eyeBall3Color":"#074f03","gradientColor1":"#12a637","gradientColor2":"#0b509e","gradientType":"linear","gradientOnEyes":"true","logo":"","logoMode":"default"},"size":1000,"download":"imageUrl","file":"png"}
    payload2 = {"data":Data,"config":{"body":"diamond","eye":"frame12","eyeBall":"ball17","erf1":[],"erf2":[],"erf3":[],"brf1":[],"brf2":[],"brf3":[],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#021326","eye2Color":"#021326","eye3Color":"#021326","eyeBall1Color":"#074f03","eyeBall2Color":"#074f03","eyeBall3Color":"#074f03","gradientColor1":"#12a637","gradientColor2":"#0b509e","gradientType":"linear","gradientOnEyes":"true","logo":"","logoMode":"default"},"size":1000,"download":"imageUrl","file":"png"}
    payload3 = {"data":Data,"config":{"body":"circle-zebra-vertical","eye":"frame14","eyeBall":"ball18","erf1":[],"erf2":[],"erf3":[],"brf1":[],"brf2":[],"brf3":[],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#021326","eye2Color":"#021326","eye3Color":"#021326","eyeBall1Color":"#074f03","eyeBall2Color":"#074f03","eyeBall3Color":"#074f03","gradientColor1":"#12a637","gradientColor2":"#0b509e","gradientType":"linear","gradientOnEyes":"true","logo":"","logoMode":"default"},"size":1000,"download":"imageUrl","file":"png"}

    print("\n1. Round Rectangle\n2. Circle\n3. Square\n")
    ptype = int(input("Enter Design Type : "))
    if ptype == 1 :
        payload = payload1
    elif ptype == 2 :
        payload = payload2
    elif ptype == 3 :
        payload = payload3
    else :
        print("invalid option ! \nRedirect to Random Design Type")
        payload = payload1
    
    resp = req.post(url , json=payload)

    if resp.status_code == 200 :
        print("\n[+] Status : Success\n")
        OutPut = resp.json()
        Link = OutPut.get('imageUrl')
        Link = "http:" + Link
        print('''Image Download Link : ''',Link)    
        print()
        #Save = input("Enter name to save (example.png) : ")
        #Loc = "c:/Users/Dimuth De Zoysa/Desktop/" + Save
        response = req.get(Link)
        svnm = input("Name to save (qrgen.png) : ")
        if len(svnm) == 0 :
            svnm = "Sample_qrgen.png"

        file = open(svnm, "wb")
        file.write(response.content)
        file.close()
    #img = req.get(Link)
    #image = open(Loc,'wb')
    #image.write(img.content)
    #image.close()

        print('''\033[0;36m\nImage ''',svnm,''' Saved (current directory)''')
    else:
        print('''\033[0;31m[-] Status : Error ''',resp.status_code)

    input("\nExit >")

def sinhala():
    try:
        ip = socket.gethostbyname("www.google.com") 
        print('''\033[0;32m[+] data ඔන් කර ඇත.\n''')   
    except Exception as e: 
        print('''\033[0;31m[-] data ඔන් කර නැත. \nතත්පර 5 කින් නතර වේ.''')  
        time.sleep(5)
        exit()

    print('''QR කෝඩ් එකක් බවට පත් කල යුතු දේ ඇතුලත් කරන්න: ''')
    Data = input('''[+]======> ''')

    url = "https://qr-generator.qrcode.studio/qr/custom"

    #data = input("Enter url : ")

    #payload = {"data":"https://www.qrcode-monkey.com","config":{"body":"rounded-pointed","eye":"frame14","eyeBall":"ball16","erf1":[],"erf2":["fh"],"erf3":["fv"],"brf1":[],"brf2":["fh"],"brf3":["fv"],"bodyColor":"#5C8B29","bgColor":"#FFFFFF","eye1Color":"#3F6B2B","eye2Color":"#3F6B2B","eye3Color":"#3F6B2B","eyeBall1Color":"#60A541","eyeBall2Color":"#60A541","eyeBall3Color":"#60A541","gradientColor1":"#5C8B29","gradientColor2":"#25492F","gradientType":"radial","gradientOnEyes":"false","logo":""},"size":"300","download":"false","file":"svg"}
    payload1 = {"data":Data,"config":{"body":"square","eye":"frame13","eyeBall":"ball14","erf1":[],"erf2":[],"erf3":[],"brf1":[],"brf2":[],"brf3":[],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#021326","eye2Color":"#021326","eye3Color":"#021326","eyeBall1Color":"#074f03","eyeBall2Color":"#074f03","eyeBall3Color":"#074f03","gradientColor1":"#12a637","gradientColor2":"#0b509e","gradientType":"linear","gradientOnEyes":"true","logo":"","logoMode":"default"},"size":1000,"download":"imageUrl","file":"png"}
    payload2 = {"data":Data,"config":{"body":"diamond","eye":"frame12","eyeBall":"ball17","erf1":[],"erf2":[],"erf3":[],"brf1":[],"brf2":[],"brf3":[],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#021326","eye2Color":"#021326","eye3Color":"#021326","eyeBall1Color":"#074f03","eyeBall2Color":"#074f03","eyeBall3Color":"#074f03","gradientColor1":"#12a637","gradientColor2":"#0b509e","gradientType":"linear","gradientOnEyes":"true","logo":"","logoMode":"default"},"size":1000,"download":"imageUrl","file":"png"}
    payload3 = {"data":Data,"config":{"body":"circle-zebra-vertical","eye":"frame14","eyeBall":"ball18","erf1":[],"erf2":[],"erf3":[],"brf1":[],"brf2":[],"brf3":[],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#021326","eye2Color":"#021326","eye3Color":"#021326","eyeBall1Color":"#074f03","eyeBall2Color":"#074f03","eyeBall3Color":"#074f03","gradientColor1":"#12a637","gradientColor2":"#0b509e","gradientType":"linear","gradientOnEyes":"true","logo":"","logoMode":"default"},"size":1000,"download":"imageUrl","file":"png"}

    print("\n[1] Round Rectangle\n[2] Circle\n[3] Square\n")
    ptype = int(input("ඔබට QR කේතය අවශ්‍ය වන්නේ ඉහත කුමන ආකාරයෙන්ද? : "))
    if ptype == 1 :
        payload = payload1
    elif ptype == 2 :
        payload = payload2
    elif ptype == 3 :
        payload = payload3
    else :
        print("වැරදි ඇතුලත් කිරීමකි. ! \nනැවතත්....!")
        payload = payload1
    
    resp = req.post(url , json=payload)

    if resp.status_code == 200 :
        print("\n[+] සාර්ථකයි...!\n")
        OutPut = resp.json()
        Link = OutPut.get('imageUrl')
        Link = "http:" + Link
        print('''මෙම ලින්ක් එක ඔස්සේ ඔබට මෙම QR කේතය ලබා ගත හැකිය: ''',Link)    
        print()
        #Save = input("Enter name to save (example.png) : ")
        #Loc = "c:/Users/Dimuth De Zoysa/Desktop/" + Save
        response = req.get(Link)
        print("ඔබගේ QR කේතය සැකසී අවසන්...!")
        svnm = input("එය සේව් කල යුතු නම ඇතුලත් කරන්න (qrgen.png) : ")
        if len(svnm) == 0 :
            svnm = "Sample_qrgenpng"

        file = open(svnm, "wb")
        file.write(response.content)
        file.close()
    #img = req.get(Link)
    #image = open(Loc,'wb')
    #image.write(img.content)
    #image.close()

        print('''\033[0;36m\nඔබගේ ''',svnm,''' නමැති QR කෝඩ් එක සේව් වී අවසන්.''')
    else:
        print('''\033[0;31m[-] වැරදීමකි...!''',resp.status_code)

    input("\nඉවත් වන්න>>>")

if ya == "1":
    sinhala();
elif ya == "2":
    english();
else:
    print('''\033[0;31mවැරදි ඇතුලත් කිරීමකි...!''')
    print('''\033[0;31minvalid number...!''')
   
   
   
   
   
   
   
      
