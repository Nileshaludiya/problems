def full_number_pyramid(N):
    for i in range(1,N+1):
        for _ in range(N-i):
            print("0",end="  ")
        for j in range(i,2*i):
            print(j,end="  ")
        for k in range(2*i-2,i-1,-1):
            print(k,end="  ")
        for _ in range(N-i):
            print("0",end="  ")
        print()
N = int(input("Enter a number: "))
full_number_pyramid(N)                        