k = int(input("k: "))

if k > 5000 or k < 1:
    print("enter the correct number!")
    exit()
else: pass


a = []
i = 13
fib1 = 1
fib2 = 1
a.append(1)
while i > 0:
    fib1 = fib2
    fib2 = fib1 + fib1
    a.append(fib2)
    i -= 1

print(a)

for j in range(len(a)):
    if k > a[j] and k < a[j+1]:
        print(j+1)
    if k == a[j]:
        print(j+1)



