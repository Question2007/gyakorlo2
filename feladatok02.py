f = open("kutyusok.txt", "r", encoding="UTF-8")
kutyusok = []
for sor in f:
    kutyusok.append(sor.capitalize().strip())
f.close()
print(*kutyusok)

print(f"1. Hány név szerepel: {len(kutyusok)}")

print("2. Kutyák i-re végződő nevei: ")
for i in kutyusok:
    if  i[-1] == "i":
        print(i)

nevek = {}
for i in kutyusok:
    if not i in nevek:
        nevek[i] = 0
    nevek[i] += 1

print("3. Ismétlődő nevek")
for i in nevek:
    v = nevek[i]
    if v == 2:
        print(i)

print("4. ABC rendezés: ")


with open("kutyusok_nagy.txt", "a") as f:
  kutyusok.sort()
  for i in kutyusok:
      f.write(i)
      f.write("\n")