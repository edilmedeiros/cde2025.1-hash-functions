def xor32_hash(s: str) -> str:
    h = 0
    for i, c in enumerate(s):
        shift = (i % 4) * 8
        h ^= (ord(c) << shift)
    return f"{h & 0xFFFFFFFF:08x}"  # Lower 32 bits as hex

# Example usage:
print(xor32_hash("bitcoin"))
print(xor32_hash("oitcbin"))  # Likely different, but many collisions exist!

s1 = "abcd1234"
s2 = "1bcda234"  # swapped s[0] and s[4]
print(xor32_hash(s1))  # e.g., 'f8e4e4e4'
print(xor32_hash(s2))  # should be the same!

print(xor32_hash("aaaa1111"))
