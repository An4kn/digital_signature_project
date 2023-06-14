import shutil
import rsa

public_key, private_key = rsa.newkeys(1024)

with open("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

print("Napisz nazwę pliku, który chcesz podpisać:")
extension = input()
path = 'dokumenty/' + extension

with open(path, 'rb') as plik_otwarty:
    message = plik_otwarty.read()

target = 'dokumenty/copy_' + extension

shutil.copyfile(path, target)

signature = rsa.sign(message, private_key, "SHA-256")

with open("signature.pem", "wb") as f:
    f.write(signature)
