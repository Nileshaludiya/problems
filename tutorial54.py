def full_number_pyramid(N):
    for i in range(N):
        for j in range(2*N-1):
            if j < (N-i-1) or j >(N+i-1):
                print(0, end=" ")
            else:
                num = (i+2)-abs(N-j-i)
                print(num,end=" ")
        print()     
N = 5
full_number_pyramid(N)
