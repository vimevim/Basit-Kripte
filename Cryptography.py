import string
lettersDigitsPanctuations = list(string.ascii_letters + string.digits + string.punctuation+ " ") #sorted alphabet, symbolls, digits, punctuations
alpha =''.join(lettersDigitsPanctuations)#declare list to the string without seperations
key = "J6pN<\" {XcO!tZQ5]f-+M\`v%,_idL/&S'l(~HyzF#w20|xbIT?R.e>CYD^4*AnKjG[B97Us=uEag}ro3W;h)P18mk:@V$q"
def encode(encrypted):# Parametre
    encrypted = encrypted.strip()
    crypted = ""
    for i in encrypted:#encrypted boyunca dön
        crypted += str(key[alpha.find(i)])
    return "Encode edilmiş şifreniz: " + crypted + "\nKey: \""+ key+"\""
def decode(crypted):  # Parametre
    encrypted = ""
    for a in crypted:
        encrypted += str(alpha[key.find(a)])#reverse engineering of method called "encode"
    return "Decode edilmiş şifreniz: " + encrypted
def menu():
    print("---MENU---\n1 - Encode.\n2 - Decode.\n3 - Mesaj.\n4 - Çıkış")
    response = input("Menü indeksi giriniz: ")
    if response == "1":
        plain = input("Encode yapılacak kelimeyi gir: ")
        print(encode(plain.strip()))
    elif response == "2":
        coded = input("Decode yapılacak kelimeyi gir: ")
        print(decode(coded.strip()))
    elif response == "3":
        print("Thanks for doing secret spy stuff with me")
    elif response == "4":
        exit()
    else:
        print("Gecersiz input")
def main():
    while (True):
        menu()
main()
