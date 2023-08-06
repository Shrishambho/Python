list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = []

min_length = min(len(list1), len(list2))

for i in range(min_length):
    result.append(list1[i] + list2[i])

if len(list1) > min_length:
    result.extend(list1[min_length:])
elif len(list2) > min_length:
    result.extend(list2[min_length:])

print(result)
