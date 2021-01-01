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
    print("\nYour final private key in WIF is:               " + wifKeyString)
    publicKey = privtopub(privateKey)
    btcAddress = pubtoaddr(publicKey)
    print ("Your Bitcoin address is:                        " + btcAddress)