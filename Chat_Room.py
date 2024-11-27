s = input().strip()

target = "hello"
i = 0 

for char in s:
    if char == target[i]:
        i += 1  
    
    if i == 5:  
        break

# If i reached 5, then we found all characters of "hello" in order
if i == 5:
    print("YES")
else:
    print("NO")
