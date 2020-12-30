import os
import binascii
import base58
import hashlib

privateKeyByte = binascii.hexlify(os.urandom(32))

privateKey = str(privateKeyByte)[2:-1] 

print("Your private key is:                            " + privateKey)

extendedPrivateKey = ("80" + privateKey)
print("Your extended private key is:                   " + extendedPrivateKey)

extendedPrivateKeyByte = bytearray.fromhex(extendedPrivateKey) 
firstHash = hashlib.sha256()
firstHash.update(extendedPrivateKeyByte)
print ("Your private key hashed using SHA256 is:        " + firstHash.hexdigest())

secondHash = hashlib.sha256()
firstHashFromHex = bytearray.fromhex(firstHash.hexdigest())
secondHash.update(firstHashFromHex)
print("Your private key hashed using SHA256 again is:  " + secondHash.hexdigest())

checksum = secondHash.hexdigest()[0:8]

finalPrivateKey = extendedPrivateKey + checksum

encodedKey = bytes.fromhex(finalPrivateKey)

finalKey = base58.b58encode(encodedKey)

finalKeyString = str(finalKey)[2:-1]

print("Your final private key in WIF is:               " + finalKeyString)
