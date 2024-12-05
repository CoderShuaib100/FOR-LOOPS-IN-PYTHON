# creating the algorithm
num = int(input("Enter a last term: "))
ans = 0
for i in range(0, num + 1):
    ans = ans + i
print(ans)