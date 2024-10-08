#2(x ≡ ¬y) → ((x ∧ w) ≡ (z ∧ ¬w))
#(x == not y) <= ((x and w) == (z and not w))

print ("x y z w F")
for x in range (0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                F = int((x == (not y)) <= ((x and w) == (z and not w)))
                #if F == 0:
                print (x, y, z, w, F)