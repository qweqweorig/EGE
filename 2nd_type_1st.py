# (x → (y ≡ w)) ∧ (y ≡ (w → z))     1y   2x   3w   4z
#(x <= (y == w)) amd (y == (w <=z))

print ("x y z w F")
for x in range (0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                F = int(x <= (y == w) and (y == (w <= z)))
                if F == 0:
                    print (x, y, z, w, F)
# ответ:yxwz