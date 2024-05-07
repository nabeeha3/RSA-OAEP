import hashlib

def trace(seed, maskLenth):
    T = b""
    digestLength = 2
    count = (maskLenth + digestLength - 1) // digestLength
    
    print("Initialization:")
    print("Seed:", " ".join(format(byte, '08b') for byte in seed))
    print("T   :", T)
    print("-----------------------------------------------------------------------------")
  
    for i in range(count):
        print("Counter:", i)
        seedCount = seed + i.to_bytes(4, 'big')
        print("  seed|counter           : ", "".join(format(byte, '08b') for byte in seedCount))
        hashVal = hashlib.blake2b(seedCount, digest_size = digestLength).digest()
        print("  hash(seed|counter)     : ", "".join(format(byte, '08b') for byte in hashVal))
        T += hashVal
        print("  T <- T | hash          : ", "".join(format(byte, '08b') for byte in T))

    print("-----------------------------------------------------------------------------")
    return T[:maskLenth]

# mgfSeed: 0x0608, maskLen: 5
seed = bytes.fromhex('0608')
maskLenth = 5

output = trace(seed, maskLenth)
outputFormat = " ".join([format(byte, '08b') for byte in output])

print("Output: T =", outputFormat)
