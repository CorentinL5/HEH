grp = ["johan", "denis", "yoan"]
for i in range(2):
    grp.append(input("Entrez le nom:\n=>"))
del grp[1], grp[3]
grp.insert(0, "erwin")
print(grp)
