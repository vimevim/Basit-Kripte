import string
import random
#random key generator
lettersDigitsPanctuations = list(string.ascii_letters + string.digits + string.punctuation+ " ") #sorted alphabet, symbolls, digits, punctuations
alpha =''.join(lettersDigitsPanctuations)#declare list to the string without seperations
random.shuffle(lettersDigitsPanctuations)#shuffle alphabet, symbolls, digits, punctuations
key=''.join(lettersDigitsPanctuations)#declare shuffled list to the string without seperations
#random key generator
keepGoing = True#loop forever
def encode(encrypted):# encode method
    encrypted = encrypted.strip()
    crypted = ""
    for i in encrypted:#loop while encrypted
        crypted += str(key[key.find(key[alpha.find(i)])])#this line needs a good explanation 
    return "Encode edilmiş şifreniz: " + crypted

def decode(crypted):#decode method
    crypted = crypted.strip()
    encrypted = ""
    for a in crypted:
        encrypted += str(alpha[alpha.find(alpha[key.find(a)])])
    return "Decode edilmiş şifreniz: " + encrypted

def menu():
    print("---MENU---\n1 - Encode.\n2 - Decode.\n3 - Mesaj.")
    response = input("Menü indeksi giriniz: ")
    if response == "1":
        plain = input("Encode yapılacak kelimeyi gir: ")
        print(encode(plain))
    elif response == "2":
        coded = input("Decode yapılacak kelimeyi gir: ")
        print(decode(coded))
    elif response == "3":
        print("Thanks for doing secret spy stuff with me")
    else:
        print("Gecersiz input")
def main():
    while (keepGoing):
        menu()
main()
