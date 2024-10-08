#5  (¬x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w
#   ((not x and not y) or (y == z) or not w)
print ("x y z w F")
for x in range (0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                F = int((not x and not y) or (y == z) or not w)
                if F == 0:
                    print(x, y, z, w, F)
                if F == 2:
                    print(x, y, z, w, F)
# ответ:zwxy