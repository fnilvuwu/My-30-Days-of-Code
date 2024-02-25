# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    s = list(input())
    even = ""
    odd = ""
    
    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i]
        else:
            odd += s[i]
            
    print(even + " " + odd)
