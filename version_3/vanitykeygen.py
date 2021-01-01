import os
import binascii
import base58
import hashlib
from bitcoin import privtopub, pubtoaddr

vanity = "1" + input("Enter a word you want your BTC address to start with(case sensitive): ")
print("\nSearching for address starting with the word " + vanity + "\n")

btcAddress = ""

while btcAddress[:len(vanity)] != vanity:
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
    print(btcAddress)

f = open("SavedKeys/vanityKeysGenerated.txt", "a")
f.write("Your private key is:                            " + privateKey + "\n")
f.write("Your extended private key is:                   " + extendedPrivateKey + "\n")
f.write("Your private key hashed using SHA256 is:        " + firstHash.hexdigest() + "\n")
f.write("Your private key hashed using SHA256 again is:  " + secondHash.hexdigest() + "\n")
f.write("Your private key in WIF is:                     " + wifKeyString + "\n")
f.write("Your Bitcoin address is:                        " + btcAddress + "\n")
f.write("View address on the blockchain:                 " + keyURL + "\n")
f.write("\n")
f.close()

print("\nYour private key is:                            " + privateKey)
print("Your extended private key is:                   " + extendedPrivateKey)
print ("Your private key hashed using SHA256 is:        " + firstHash.hexdigest())
print("Your private key hashed using SHA256 again is:  " + secondHash.hexdigest())    
print("Your private key in WIF is:                     " + wifKeyString)
print ("Your Bitcoin address is:                        " + btcAddress)
print("View address on the blockchain:                 " + keyURL)
print("\nBitcoin Key information saved to /SavedKeys/vanityKeysGenerated.txt")

keyPairCount = input("")