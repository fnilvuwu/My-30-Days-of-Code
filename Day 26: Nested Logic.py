# Enter your code here. Read input from STDIN. Print output to STDOUT
d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())

if y2 > y1 or y2 == y1 and m2 > m1 or y2 == y1 and m2 == m1 and d2 >= d1:
    print(0)
elif (y1) > (y2):
    print(10000)
else:
    if (m1) > (m2):
        print(500 * (m1 - m2))
    elif (d1) > (d2):
        print(15 * (d1 - d2))
        
    
        
