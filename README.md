# Python Bitcoin Private/Public Keygen
Bitcoin Private/Public Key Generator
![Console Output V1](https://siasky.net/IAAUVxMPHmQjyubF8sGpRuoSQFg0bpKqxgB83quECbESmQ)

# Objective
Develop a client-side Bitcoin wallet address generator.

# Usage
Install required packages and run either in CMD or by opening either of the .py files.

keygen.py runs once, while keygenloop.py allows user input to dictate the amount of addresses to generate. 

vanitykeygen.py generates addresses until a specified prefix in a generated address is found. 

# Use cases
In applications that an individual wants to generate a Bitcoin address on the fly, completely random (uses urandom) while not requiring a network connection.

# Requires
Base58 (pip install base58)

Bitcoin (pip install bitcoin)
