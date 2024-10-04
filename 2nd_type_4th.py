#4(¬z ≡ y) → ((w ∧ ¬x) ≡ (y ∧ x))
#(not z == y) <= ((w and not x) == (y and x))

print ("x y z w F")
for x in range (0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                F = int(not z == y) <= ((w and not x) == (y and x))
                if F == 0:
                    print(x, y, z, w, F)
# ответ:zwxy