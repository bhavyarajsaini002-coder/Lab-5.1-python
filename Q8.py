sentence = input("Enter a sentence: ")

capitals = 0
smalls = 0
digits = 0
specials = 0

i = 0
while i < len(sentence):
    char = sentence[i]

    if 'A' <= char <= 'Z':
        capitals += 1
    elif 'a' <= char <= 'z':
        smalls += 1
    elif '0' <= char <= '9':
        digits += 1
    else:
        specials += 1
    i += 1

print("Capital letters:",capitals)
print("Small letters:",smalls)
print("Digits:",digits)
print("Special characters:",specials)