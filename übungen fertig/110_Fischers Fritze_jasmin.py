
# Fischers Fritze

# Es steht folgender String zur Verfügung:
satz = 'Fischers Fritz fischt frische Fische'

# Gib durch String-Slicing des Strings 'satz' die folgenden Strings aus
# 1. ihsrzihf
# 2. sifhrhi
# 3. sche (mit möglichst wenig Zeichen)
# 4. eci hsr hsfziFseci
# 5. ii i


satz = 'Fischers Fritz fischt frische Fische'


print(f"Länge des Strings: {len(satz)}")  


result1 = satz[21:27][::-1]
print("1.", result1)


indizes = [0, 9, 16, 22, 28, 35]  
result2 = "".join([satz[i] for i in indizes])
print("2.", result2)


result3 = satz[22:26]  
print("3.", result3)


result4 = satz[::-1]
print("4.", result4)


result5 = " ".join([c for c in satz if c.lower() == 'i'])
print("5.", result5)
