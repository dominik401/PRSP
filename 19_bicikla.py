n = int(input("broj zupcanika na pedali: "))
pedal_axel= list(map(int, input().split()))

m = int(input("broj zupcanika na straznjem kotacu: "))
rear_axel = list(map(int, input().split()))

max_ratio = 0
max_ratio_count = 0

for i in range(n):
    for j in range(m):

        ratio = rear_axel[j] / pedal_axel[i]

        if ratio.is_integer():
            if ratio > max_ratio:
                max_ratio=ratio
                max_ratio = 1
            elif ratio == max_ratio:
                max_ratio_count+=1
print(max_ratio)
print(max_ratio_count)
