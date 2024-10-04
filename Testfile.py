#1
# (x → (y ≡ w)) ∧ (y ≡ (w → z))     1   2   3w   4x
#(x <= (y == w)) amd (y == (w <=z))

print ("x y z w F")
for x in range (0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                F = int(x <= (y == w) and (y == (w <= z)))
                if F == 0:
                    print (x, y, z, w, F)

#2(x ≡ ¬y) → ((x ∧ w) ≡ (z ∧ ¬w))
#(x == not y) <= ((x and w) == (z and not w))

"""print ("x y z w F")
for x in range (0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                F = int((x == not y) <= ((x and w) == (z and not w)))
                #if F == 0:
                print (x, y, z, w, F)

#3((x → y) ≡ (w → x)) ∧ (z → w)
#((x <= y) == (w <= x)) and (z <= w)

for x in range (0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                F = int((x <= y) == (w <= x)) and (z <= w)
                # if F == 0:
                print(x, y, z, w, F)

#4(¬z ≡ y) → ((w ∧ ¬x) ≡ (y ∧ x))
#(not z == y) <= ((w and not x) == (y and x))

for x in range (0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                F = int(not z == y) <= ((w and not x) == (y and x))
                # if F == 0:
                print(x, y, z, w, F)

#5(¬x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w
#(not x and not y) or (y -- z) or not w)

for x in range (0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                F = int((not x and not y) or (y -- z) or not w)
                # if F == 0:
                print(x, y, z, w, F)"""