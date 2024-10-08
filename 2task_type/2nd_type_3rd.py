#3((x → y) ≡ (w → x)) ∧ (z → w)
#((x <= y) == (w <= x)) and (z <= w)

print ('x y z w  F')
for x in range (0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                F = int((x <= y) == (w <= x)) and (z <= w)
                if F == 1:
                    print(x, y, z, w, F)
# ответ: yxwx