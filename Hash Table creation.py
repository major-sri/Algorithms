# Suppose you have some alphabets given and you have to keep a record of frequency of it's occurence
# We can do it using Dictionary in python 
// CODE
count={}
a=['a','b','b','a','c','c','c']
for x in a:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1
print(count.keys()[0])
//Output: {'a': 2, 'b': 2, 'c': 3}




