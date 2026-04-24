"""a=[{"name":["a","b","c"],"id":[1,2,3]},{"name":["b","d","f"],"id":[2,5,6]}]
b=[]
for i in a:
    b.extend(i["name"])
print(sorted(set(b)))
"""
"""students = {
    1: {"name": "Vishal", "marks": 90},
    2: {"name": "Arun", "marks": 85}
}
print(students[1].keys())"""

"""a={"name":"vishal" , "age":21,"city":"covai"}
a.update({"marks":59})
a["age"]=25
print(a)
del a["city"]
print(a)"""

"""arr=[1,2,3,2,4,3]
d={}
count=0
element=""
elements=""
for i in arr:
    d[i]=d.get(i,0)+1




    for key,value in d.items():
        if value>count:
            count=value
            element=key
print(element)
for j in arr:
    d[j]=1
a=list(d.keys())
print(a)"""

"""a="listen","silent"
c={}
for i in a:
    for j in i:
        c[j]=c.get(j,0)+1
if len(set(c.values()))==1:
    print("anagram")            
else:
    print("not anagram")"""

"""d1={"a":1,"b":2}
d2={"b":3,"c":4}
d3={}
for i in set(d1.keys()).union(set(d2.keys())):
    d3[i]=d1.get(i,0)+d2.get(i,0)
print(d3)"""

"""words = ["apple", "ant", "bat", "ball"]

d = {}

for word in words:
    key = word[0]   # first letter
    
    if key not in d:
        d[key] = []
    
    d[key].append(word)

print(d)"""

"""from datetime import datetime,timedelta
start=datetime.now()
end=start+timedelta(seconds=1
                    0)
if datetime.now()>end:
    print("session expired")
else:
    print("session active")"""


"""a={"A":"Visha","age":21}
for key, value in a.items():
    print(key, a["age"])
"""
"""
a=["apple","ant","bat","ball"]
b={}
for i in a:
    key=i[0]
    if key not in b:
        b[key]=[]
        b[key].append(i)
    print(b)"""
"""
students = [
    {"name": "Surya", "marks": [33, 48, 44]},
    {"name": "Kumar", "marks": [10, 0, 20]},
    {"name": "Priya", "marks": [26, 50, 45]},
    {"name": "Arun", "marks": [0, 0, 0]}
]
for i in students:
    b=0
    for j in i["marks"]:
        b+=j
        avg=b/3
        c=0
        d=""
    for k in range(len(i["marks"])):
        if c<i["marks"][k]:
            c=i["marks"][k]
    print("highest",c)
    if c>c[j]:
       d=i["name"]
    print(d)

    print("name : ",i["name"])
    print("total",b)
    print()
"""
"""student = {"a":10,"b":20,"c":30}
for k,v in student.items():
    print(k)
print(student.get("d",0))
""""""
marks = {"math": 90, "science": 85, "english": 95}

max_key = max(marks, key=marks.get)
print(max_key) """  # english

"""a=[1,2,2,3,1,1,4]
d={}
for i in a:
    d[i]=d.get(i,0)+1
print(d)
max=max(d,key=d.get)
print(max)
"""
"""students = {
    "s1": {"name": "Vishal", "marks": 80},
    "s2": {"name": "Kumar", "marks": 90},
    "s3":{"name":"agi","marks":100}
}
total=0
for i in students:
    if students[i]["marks"]>total:
        total+=students[i]["marks"]
print(total,i["name"])
"""
"""students = [
    {"name": "Vishal", "marks": [80, 90, 85]},
    {"name": "Kumar", "marks": [60, 70, 75]}
]
c=0
for i in students:
    total=0
    avg=0
    for j in i["marks"]:
        total+=j
        avg=total//len(i["marks"])
    if avg>70:
        print(i["name"])
    if total>c:
        c=total
print(c)"""
"""
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
n=5
print(fact(n))"""

"""a=1234
b=0
while a>0:
    b=b*10+a%10
    a=a//10
print(b)
"""
"""
a=[2,7,11,12,2,7]
k=9
b=[]
a=list(set(a))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        b=a[i]+a[j]
    if b==k:
        b=a[i],a[j]
        print(b)"""
"""
a=[2,7,11,12,2,7]
k=9
a=set(a)
c=[]
for i in a:
    b=k-i
    if b in a:
        if (sorted((i,b))) not in c:
            c.append(sorted((i,b)))
print(c)"""    

"""
from datetime import datetime,date,time
a = [
    {
        -
        "Ram": {
            "login": "2026-3-1 00:00:00",
            "logout": "2026-3-1 00:03:00"
        },
        "Prem": {
            "login": "2026-3-1 00:04:00",
            "logout": "nil"
        }
    }
]
duration=""
for i in a:
    for j in i:
        print(i[j]["login"])
        login = datetime.strptime(i[j]["login"], "%Y-%m-%d %H:%M:%S")
        logout = i[j]["logout"]
        if logout != "nil":
            logout = datetime.strptime(logout, "%Y-%m-%d %H:%M:%S")
        
        else:
            logout=datetime.now()
            
        duration=logout-login
        print(j,"\nlogin:",login,"\nlogout:",logout)
        print(j,"duration:",duration.seconds)"""
"""def flatten_dict(d, parent_key=""):
    result = {}

    for key, value in d.items():
        # create new key
        new_key = f"{parent_key}.{key}" if parent_key else key

        # if value is dictionary → go inside (recursion)
        if isinstance(value, dict):
            result.update(flatten_dict(value, new_key))
        else:
            # store final value
            result[new_key] = value

    return result


# Input
data = {
    "user": {
        "id": 1,
        "details": {
            "name": "John",
            "address": {
                "city": "NY",
                "zip": 10001
            }
        }
    }
}

# Output
print(flatten_dict(data))"""

"""words = ["eat", "tea", "tan", "ate", "nat", "bat"] 
result={}

for i in words:
    key="".join(sorted(i))

    if key not in result:
        result[key]=[]
    result[key].append(i)

print(result)
"""
"""
dict1 = {"a": 1, "b": {"x": 10, "y": 20}} 
dict2 = {"b": {"y": 200, "z": 300}, "c": 3}
c={}

for key,value in dict1.items():
    print(key,value)
    c[key]=dict1[key]
    if key in c:
     """   

"""data = {"a": 1, "b": {"x": 10, "y": 20}}
sum=0
for key,value in data.items():
    if isinstance(value,dict):
        for key,value in value.items():
            print(value)
            sum+=value
    else:
        print(value)
        sum+=value
print(sum)
""""""
def maximum(d):
    max_2=0
    for key,value in d.items():
    
        if isinstance(value,dict):
            max_1=maximum(value)
            max_2=max(max_2,max_1)
        else:
            max_2=max(max_2,value)
    return max_2
data = {"a": 5, "b": {"x": 10, "y": 3}}
print(maximum(data))"""

"""
def maximum(d):
    for key,value in d.items():
    
        if isinstance(value,dict):
            maximum(value)
        else:
            d[key]=0
    return d
data = {"a": 5, "b": {"x": 10, "y": 3}}
print(maximum(data))"""
"""def find_depth(d):
    max_depth = 1

    for value in d.values():
        if isinstance(value, dict):
            max_depth = max(max_depth, 1 + find_depth(value))

    return max_depth
""""""
def b(d):
    a=[]
    for key,value in d.items():
        a.append(key)
        if isinstance(value,dict):
            a.extend(b(value))
            
    return a
c={"a":{"b":{"c":1}}}
print(b(c))"""

"""def py(d,target,path=""):
    for key,value in d.items():
        new=f"{path}.{key}"if path else key
        if key==target:
            return new 
        if isinstance(value,dict):
            res=py(value,target,new)

            if res:
                return res
    
    return new

b={"a":{"b":{"c":1}}}
target="c"
print(py(b,target))"""

"""
def a(d):
    sum=0
    for key,value in d.items():
        if isinstance(value,dict):
                sum+=a(value)
        else:
            if value%2==0:
                sum+=value
    return sum
data = {"a": 1, "b": {"x": 10, "y": 7, "z": 4}}
print(a(data))"""
"""
def a(d):
    c={"even":0,"odd":0}
    for key,value in d.items():
        if isinstance(value,dict):
            b=a(value)
            c["even"]+=b["even"]
            c["odd"]+=b["odd"]
        else:
            if value%2==0:
                c["even"]+=1
            else:
                c["odd"]+=1 
    return c       

data = {"a": 1, "b": {"x": 10, "y": 7, "z": 4}}
print(a(data))"""
"""
def addition(d):
    mul=1
    for key,value in d.items():
        if isinstance(value,dict):
            mul*=addition(value)
        else:
            mul*=value
    return mul
b={"a":2,"b":{"x":3,"y":4}}
print(addition(b))"""

"""def p(d,target,path=""):
    b=[]
    for key,value in d.items():
        new=f"{path}.{key}"if path else key
        if key==target:
             b.append(new)
        if isinstance(value,dict):
            b.extend(p(value,target,new))
    return b
data = {"a":{"b":1,"c":{"b":2}}}
target="b"
print(p(data,target))"""

"""def flatten(d,path=""):
    sum=0
    b={}
    for key,value in d.items():
        new=f"{path}.{key}"if path else key
        if isinstance(value,dict):
            e,f=flatten(value,new)
            b.update(e)
            sum+=f
        else:
            b[new]=value
            sum+=b[new]
    
    return b,sum
data={"a":{"b":2,"c":3}}

flat, total = flatten(data)
print(flat)
print("sum:", total)
"""
"""def deep(d):
    for key,value in d.items():
        if isinstance(value,dict):
            deep(value)
        else:
            print(value)

data={"a":{"b":{"c":10}}}
deep(data)
"""        
"""def avg(d):
    sum=0
    count=0
    for key,value in d.items():
        if isinstance(value,dict):
            a,b=avg(value)
            sum+=a
            count+=b
        else:
            sum+=value
            count+=1
    return sum,count
data = {"a": 2, "b": {"x": 4, "y": 6}}
flat,total=avg(data)
print(flat/total)"""

"""def maximum(d):
    a=0
    b=None
    for key,value in d.items():
        if isinstance(value,dict):
            c,e=maximum(value)
            if c > a:
                a,b=c,e
        else:
            if value > a:
                a,b=value,key

    return a,b
data = {"a": 5, "b": {"x": 10, "y": 3}}
f,g=maximum(data)
print((g,f))
"""

"""def keysa(b,target):
    for key,value in b.items():
        if key==target:
            return True
        
        if isinstance(value,dict):
            if keysa(value,target):
                return True
    return False
data = {"a": {"b": {"c": 1}}}
target="c"
print(keysa(data,target))
"""
"""def even(d):
    for key,value in d.items():
        if isinstance(value,dict):
            even(value)
        else:
            if value%2==0:
                d[key]=0

    return d
data={"a":1,"b":{"x":2,"y":3}}
print(even(data))
"""
"""
dict1 = {"a": 1, "b": {"x": 10, "y": 20}} 
dict2 = {"b": {"y": 200, "z": 300}, "c": 3}
{
  "a": 1,
  "b": {"x": 10, "y": 200, "z": 300},
  "c": 3
}
def merge_dicts(d1, d2):
    result = d1.copy()  

    for key, value in d2.items():  
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            
            result[key] = merge_dicts(result[key], value)

        else:
            
            result[key] = value

    return result"""
"""
def flat(d,path=""):
    a={}
    for key,value in d.items():
        new=f"{path}.{key}"if path else key
        if isinstance(value,dict):
            a.update(flat(value,new))
        else:
            a[new]=value
    return a
data = {   "user": {"id": 1, "details": {"name": "John", "address": {"city": "NY", "zip": 10001}}}
}
print(flat(data))
"""
"""def anagram(a):
    new={}
    for i in a:
        b="".join(sorted(i))

        if b not in new:
            new[b]=[]
        new[b].append(i)

    return new
words = ["eat", "tea", "tan", "ate", "nat", "bat"] 
print(anagram(words))
"""
"""def merge(d1,d2):
    di1=d1.copy()
    for key,value in d2.items():
        if key in di1 and isinstance(di1[key],dict) and isinstance(value,dict):
            di1[key]=merge(di1[key],value)
        else:
            di1[key]=value
    return di1

dict1 = {"a": 1, "b": {"x": 10, "y": 20}} 
dict2 = {"b": {"y": 200, "z": 300}, "c": 3}
print(merge(dict1,dict2))
""""""
data = {"a": [1,2,3], "b": [2,3,4], "c": [3,4,5]} 
d={}
for i,j in data.items():
    for k in j:
        d[k]=d.get(k,0)+1
print(d)"""

def count(d):
    c={}
    for i,j in d.items():
        if isinstance(i,list):
            c=count(i)
        else:
            c[i]=c.get(i,0)+1
    return c
data = {"a": [1,2,3], "b": [2,3,4], "c": [3,4,5]}
print(count(data))



