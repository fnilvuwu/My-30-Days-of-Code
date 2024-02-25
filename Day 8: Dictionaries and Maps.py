n = int(input())
my_dict = dict()

for i in range(n):
    key, value = input().split()
    my_dict[key] = value
        
    
queries = str(input())

while queries:
    if queries in my_dict:
        print(queries + "=" + my_dict.get(queries))
    else:
        print("Not found")
    try:
        queries = input()
    except EOFError:
        break
