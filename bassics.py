"""a = [5, 2, 9, 1, 5, 6]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
"""
"""a = ["apple", "bat", "banana", "cat"]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if len(a[i])>len(a[j]):
            a[i],a[j]=a[j],a[i]
print(a)

marks = {"ram": 80, "sam": 50, "john": 90}

items = list(marks.items())

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:
            items[i], items[j] = items[j], items[i]

# convert back to dict
sorted_marks = {}
for key, value in items:
    sorted_marks[key] = value

print(sorted_marks)
""""""
a = [4, 6, 2, 6, 4, 4, 1]

# count frequency manually
freq = {}
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
# sort based on frequency
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if freq[a[i]] > freq[a[j]]:
            a[i], a[j] = a[j], a[i]

print(a)"""
a = [0, 1, 0, 3, 12]

result = []

# add non-zero
for i in a:
    if i != 0:
        result.append(i)
zeros = len(a) - len(result)
for i in range(zeros):
    result.append(0)

print(result)