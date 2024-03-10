T = int(input())

for _ in range(T):
    n = int(input())
    prime = True
    if n <= 1:
        prime = False
    else:
        for j in range(2, int(n**0.5) + 1):  # Only need to check until square root of n, time limit fix
            if n % j == 0:
                prime = False
                break

    if prime:
        print("Prime")
    else:
        print("Not prime")
