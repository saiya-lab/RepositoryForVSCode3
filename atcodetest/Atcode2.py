#a = int(input("a_num:"))
#a_num:3
#print(a)
#b = int(input("b_num:"))
#b_num:4
#if a * b % 2 == 0:
    #print("Even")
#else:
    #print("Odd")

a, b = map(int, input().split())

if a*b%2==0:
    print("Even")
else:
    print("Odd")
