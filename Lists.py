list1 = ["elma", "armut", "muz", "erik"]
list2 = ["domates", "salatalık", "biber", "patlıcan"]

print(list1)
print(list2)

list1[0]
list2[2]

for oge in list1:
    print(oge)

list2.append("brokoli")
print(list2)

list3 = list1 + list2
print(list3)

del list3[-1]
list3.pop(3)
list3.remove("domates")
print(list3)

list3[2] = "çilek"
print(list3)

list3[:] = "kiraz", "şeftali", "karpuz"
print(list3)

del list1
print(list1)

cift_sayi = [i for i in range(100) if i % 2 == 0]
print(cift_sayi)
