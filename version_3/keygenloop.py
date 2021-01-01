import os
import binascii
import base58
import hashlib
from bitcoin import privtopub, pubtoaddr

keyPairCount = int(input("Enter the number of addresses you want to generate:"))

for x in range(keyPairCount):
    privateKeyByte = binascii.hexlify(os.urandom(32))
    privateKey = str(privateKeyByte)[2:-1]
    extendedPrivateKey = ("80" + privateKey)
    extendedPrivateKeyByte = bytearray.fromhex(extendedPrivateKey)
    firstHash = hashlib.sha256()
    firstHash.update(extendedPrivateKeyByte)
    secondHash = hashlib.sha256()
    firstHashFromHex = bytearray.fromhex(firstHash.hexdigest())
    secondHash.update(firstHashFromHex)
    checksum = secondHash.hexdigest()[0:8]
    finalPrivateKey = extendedPrivateKey + checksum
    encodedKey = bytes.fromhex(finalPrivateKey)
    wifKey = base58.b58encode(encodedKey)
    wifKeyString = str(wifKey)[2:-1]
    publicKey = privtopub(privateKey)
    btcAddress = pubtoaddr(publicKey)
    keyURL = "https://www.blockchain.com/btc/address/" + btcAddress
    print("... Writing keys to keysGenerated.txt ...")
    print(".. Writing keys to keysGenerated.txt ..")
    print(". Writing keys to keysGenerated.txt .")
    print(".. Writing keys to keysGenerated.txt ..")

    f = open("SavedKeys/keysGenerated.txt", "a")
    f.write("Your private key is:                            " + privateKey + "\n")
    f.write("Your extended private key is:                   " + extendedPrivateKey + "\n")
    f.write("Your private key hashed using SHA256 is:        " + firstHash.hexdigest() + "\n")
    f.write("Your private key hashed using SHA256 again is:  " + secondHash.hexdigest() + "\n")
    f.write("Your private key in WIF is:                     " + wifKeyString + "\n")
    f.write("Your Bitcoin address is:                        " + btcAddress + "\n")
    f.write("View address on the blockchain:                 " + keyURL + "\n")
    f.write("\n")
    f.close()

    #page = urllib.request.urlopen(keyURL)
    #soup = BeautifulSoup(page, 'html.parser')
    #transaction = str(soup.find('span', {"class":"sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"}))[81:-7]
    #print(transaction)
    #work on getting web implementation to work

print("\nBitcoin Key information saved to /SavedKeys/keysGenerated.txt")\

keyPairCount = int(input(""))