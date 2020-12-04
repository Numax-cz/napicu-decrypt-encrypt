import os
import base64
import hashlib
# b'U\xf7+\xe9=4\xbd\xd1\xf3\xd7$\xa2\xa7H\xbe\xc5'
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
print()
print("NapicuCrypt (v1.1.0)")
print("==============================")
print()

# klíč
# file = open('key.key', 'rb')
# klic_us = file.read()
# file.close()



heslo = input('Zadejte heslo: ')


# heslo je 'Jonáš je L'
heslo_en = heslo.encode()
saltA = b'U\xf7+\xe9=4\xbd\xd1\xf3\xd7$\xa2\xa7H\xbe\xc5'
decod = PBKDF2HMAC(
    algorithm=hashes.SHA3_512(),
    length = 32,
    salt = saltA,
    iterations = 10000,
    backend = default_backend()
)
klic_us = base64.urlsafe_b64encode(decod.derive(heslo_en))


print()
print('\033[31m' + 'Varování!!!' + '\033[0m' + ' Tento program vám může trvalo poškodit soubory!')
print('Prosím před použití napište: ' + '"napicucrypt -h"')
print("=============================================================")
funkce = input('Co chceš ? \033[31m' + 'zaheslovat / odheslovat' + '\033[0m  :  ')
if funkce == ('zaheslovat'):
    print("******************************")
    print('Jaký soubor chceš zaheslovat?')
    print()
    soubor_nazev = input('Soubor zadej bez přípony: ')
    soubor_nazev_připona = input('Zadej příponu bez . ')
    print("******************************")
    NazevSouboru = (soubor_nazev + "." + soubor_nazev_připona)
    print("******************************")
    print()
    print("Cílovej soubor: " + NazevSouboru)
    print()
    try:
        with open(NazevSouboru, 'rb') as t:
            data = t.read()
            fernet = Fernet(klic_us)
            encrypted = fernet.encrypt(data)
            t.close()
            souhlas = input('Opravdu si přejete zaheslovat ' + NazevSouboru + "?  ano/ne : ")
            if souhlas == ("ano"):
                f = open (NazevSouboru + ".napicucrypt", 'wb')
                f.write(encrypted)
                os.remove(NazevSouboru)
                print()
                print("******************************")
                print("Soubor byl úspěšně zaheslován!")
                print("******************************")
                print()
            else:
                print("*****************************************************")
                print()                                         
                print()
                os.system('pause')          
    except FileNotFoundError:
        print('Zadaný soubor neexistuje!')
        print('Zadaný název souboru: ' + NazevSouboru)
        print()
        os.system('pause')




elif funkce == ('odheslovat'):
    print("******************************")
    print('Jaký soubor chceš odheslovat?')
    print()
    soubor_nazev = input('Soubor zadej bez přípony: ')
    soubor_nazev_připona = input('Zadej příponu bez . ')
    NazevSouboru = (soubor_nazev + "." + soubor_nazev_připona)
    NazevSouboruPripona = (NazevSouboru + ".napicucrypt")
    print()
    print("Cílovej soubor: " + NazevSouboru)
    print()
    try:
        with open(NazevSouboruPripona, "rb") as t:
            data = t.read()
            fernet = Fernet(klic_us)
            encrypted = fernet.decrypt(data)
            t.close()
            souhlas = input('Opravdu si přejete odheslovat ' + NazevSouboru + "?  ano/ne : ")
            if souhlas == ('ano'):
                f = open (NazevSouboru, 'wb')
                f.write(encrypted)
                f.close()
                os.remove(NazevSouboruPripona)
                print()
                print("******************************")
                print("Soubor byl úspěšně odheslován!")
                print("******************************")
                print()
    except FileNotFoundError:
        print('Zadaný soubor neexistuje!')
        print('Zadaný název souboru: ' + NazevSouboru)
        print()
        os.system('pause')
#help
elif funkce ==('napicucrypt -h'):
    print('\033[33m' + 'napicucrypt -h ' + '\033[0m' + '     help')
    print('\033[33m' + 'napicucrypt -v ' + '\033[0m' + '     verze')
    print('\033[33m' + 'napicucrypt -p ' + '\033[0m' + '     použití')

elif funkce ==('napicucrypt -v'):
    print()
    print("==============================")
    print("NapicuCrypt (v1.1.0)")
    print("==============================")
    print()
elif funkce ==('napicucrypt -p'):
    print()
    print("==============================")
    print('Použití')
    print("==============================")
    print()
    print('1.   Zadejte heslo které chce použít k dešifraci souboru')
    print('2.   Vyberte zda chcete soubor šifrovat nebo dešifrovat')
    print('3.   Zadejte název soubor který chcete šifrovat nebo dešifrovat')
    print('      - Zadaný název nesmí obsahovat koncovku npř. .png .mp4 .txt')
    print('4.   Zadejte koncovku soubor který chcete šifrovat nebo dešifrovat')
    print('      - Zadaná koncovka nesmí být s tečkou!')
    print('5.   Potvrďte souhlas zda chce zašifrovat soubor')
    print('5.   Dešifrace souboru')
    print('      - Zadejte heslo pod kterým jste soubor zašifrovali')


    

    
    









else:
    print()
    print()

    print("******************************")
    print('\033[31m' + '    Špatně zadaný příkaz!   ' + '\033[0m')
    print("******************************")
    print('\033[33m' + 'napicucrypt -h ' + '\033[0m' +  '    Pro více informací')
    print()
    os.system('pause')









# if funkce == ('odheslovat'):
#     print("******************************")
#     print('Jaký soubor chceš odheslovat?')
#     print()
#     soubor_nazev = input('Soubor zadej bez přípony: ')
#     soubor_nazev_připona = input('Zadej příponu bez . ')
#     NazevSouboru = (soubor_nazev + "." + soubor_nazev_připona)
#     NazevSouboruPripona = (NazevSouboru + ".zaheslovano")

    
#     t = open(NazevSouboruPripona,'rb')
#     data = t.read()
#     fernet = Fernet(klic_us)
#     encrypted = fernet.decrypt(data)
#     t.close()
#     f = open (NazevSouboru, 'wb')
#     f.write(encrypted)
#     f.close()
#     os.remove(NazevSouboruPripona)
# else:
#     print()
#     print("******************************")
#     print("Špatně zadaný příkaz!")
#     print("******************************")
#     print()
#     os.system('pause')






# def hesloHash():
#     with open('UDAJE.txt', 'rb') as t:

#         data = t.read()

#         fernet = Fernet(klic_us)
#         encrypted = fernet.encrypt(data)

#     with open ('UDAJE.txt.zaheslovano', 'wb') as f:
#         f.write(encrypted)





# soubor = open('key.key', 'rb')
# klic = soubor.read()
# soubor.close
# key_hlavni =  (b'XmLsoJJ9iCKZHUx_lG2k0vS2A4rL_S8NbQQlqcQ50Tc=')
# while klic == key_hlavni:
#     f = Fernet(klic)
#     soubor_s = open('UDAJE.txt', 'rb')
#     data = soubor_s.read()


#     print(data)
#     break
# else:
#     print('špatne heslo')

        

        






