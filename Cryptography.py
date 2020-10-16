alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
key ="XPMGTDHLYONZBWEARKJUFSCIQV,"
keepGoing = True

def encode(encrypted):# Parametre
    encrypted = encrypted.strip()
    encrypted = encrypted.upper()
    crypted = ""
    alphaKeyIndex = 0  # alpha ve key için harf basamağı
    cryptedEncryptedIndex = 0  # crypted ve encrypted için harf basamağı
    while alphaKeyIndex < len(key):  # alpha ve key basamağı tamamlama döngüsü
        while cryptedEncryptedIndex < len(encrypted):  # şifrelenecek basamağı tamamlama döngüsü
            if encrypted[cryptedEncryptedIndex] in alpha[
                alphaKeyIndex]:  # eğer encrypted'ın indeksi alpha'nın indexi ile çakışırsa
                crypted += key[alphaKeyIndex]  # çakışma olduğu durumda gerçekleşen, crypted değişkenini düzenleyen kod
                if(len(encrypted)==len(crypted)):
                    return "Encode edilmiş şifreniz: " + crypted
                #print(crypted)  # her harf eklendiğinde ekrana crypted değişkenini yazdır
                cryptedEncryptedIndex += 1  # her harf eklendiğinde  encrypted harf basamağını bir arttır
                alphaKeyIndex = 0  # harf eklendiğinde alpha ve key harf basamağını sıfırla
            alphaKeyIndex += 1  # encrypted'ın indeksi alpha'nın indexi ile çakışsa da çakışmasa da alpha ve key harf basamağını arttır

def decode(crypted):  # Parametre
    crypted = crypted.strip()
    crypted = crypted.upper()
    encrypted = ""
    alphaKeyIndex = 0  # alpha ve key için harf basamağı
    cryptedEncryptedIndex = 0  # crypted ve encrypted için harf basamağı
    while alphaKeyIndex < len(alpha):  # alpha ve key basamağı tamamlama döngüsü
        while cryptedEncryptedIndex < len(crypted):  # şifrelenecek basamağı tamamlama döngüsü
            if crypted[cryptedEncryptedIndex] in key[
                alphaKeyIndex]:  # eğer encrypted'ın indeksi alpha'nın indexi ile çakışırsa
                encrypted += alpha[alphaKeyIndex]  # çakışma olduğu durumda gerçekleşen, crypted değişkenini düzenleyen kod
                if (len(encrypted) == len(crypted)):
                    return "Decode edilmiş şifreniz: " + encrypted
                #print(encrypted)  # her harf eklendiğinde ekrana crypted değişkenini yazdır
                cryptedEncryptedIndex += 1  # her harf eklendiğinde  encrypted harf basamağını bir arttır
                alphaKeyIndex = 0  # harf eklendiğinde alpha ve key harf basamağını sıfırla
            alphaKeyIndex += 1  # encrypted'ın indeksi alpha'nın indexi ile çakışsa da çakışmasa da alpha ve key harf basamağını arttır

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
