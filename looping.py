def looping():
    a=int(input())
    k=int(input())
    added_value=a
    for i in range(k):
        if(str(added_value)==str(added_value)[::-1]):
            return i,added_value
        else:
            added_value=a+int(str(added_value)[::-1])
            a=added_value
print(looping())