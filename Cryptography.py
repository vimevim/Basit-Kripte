import string
lettersDigitsPanctuations = list(string.ascii_letters + string.digits + string.punctuation+ " ") #sorted alphabet, symbolls, digits, punctuations
alpha =''.join(lettersDigitsPanctuations)#declare list to the string without seperations
key = "J6pN<\" {XcO!tZQ5]f-+M\`v%,_idL/&S'l(~HyzF#w20|xbIT?R.e>CYD^4*AnKjG[B97Us=uEag}ro3W;h)P18mk:@V$q"
def encode(encrypted):# Parametre
    encrypted = encrypted.strip()
    crypted = ""
    for i in encrypted:#encrypted boyunca dön
        crypted += str(key[alpha.find(i)])
        """For example, our password is "kask" and the "i" variable loops while "kask" and gives us the character which 0-1-2-3 indexes holds
        Our first character is "k". "alpha.find(i)" = "alpha.find("k") which gives us the index of "k" in the "alpha" and lets say "k" letter stands in 13th index
        "key[alpha.find(i)]" is equal with "key[13]" which it gives us the 13th index of "key" and lets say 13th index of key holds "S" letter so "kask" turns into "Sask"
        Our second character is "a". "alpha.find(i)" = "alpha.find("a") which gives us the index of "a" in the "alpha" and lets say "a" letter stands in 24th index
        "key[alpha.find(i)]" is equal with "key[24]" which it gives us the 24th index of "key" and lets say 24th index of key holds "j" letter so "Sask" turns into "Sjsk"
        """
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
