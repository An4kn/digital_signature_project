import rsa


print("Napisz plik który chcesz zweryfikowac")

path = 'dokumenty/'
path += input()

with open(path, 'rb') as plik_otwarty:
        message = plik_otwarty.read()

with open("signature.pem","rb") as f:
    signature = f.read()

with open("public.pem","rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

try:
    rsa.verify(message, signature, public_key)
    print("Podpis został zweryfikowany.")
except rsa.VerificationError:
    print("Błąd weryfikacji podpisu.")