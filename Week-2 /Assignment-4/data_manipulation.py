def count(input):
    mydict = dict()
    for i in input:
        if i in mydict:
            mydict[i] += 1 
        else: 
            mydict[i] = 1
    return mydict

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) 

def group_by_key(input):
    new_keys = list()
    new_values = list()
    for d in input:
        new_keys.append(d.values()[1]) 
        new_values.append(d.values()[0]) 

    mydict = dict()
    count = 0
    for i in new_keys:
        if i in mydict:
            mydict[i] += new_values[count]
        else:
            mydict[i] = new_values[count]
        count += 1
    return mydict

input2 = [
{'key': 'a', 'value': 3}, 
{'key': 'b', 'value': 1}, 
{'key': 'c', 'value': 2}, 
{'key': 'a', 'value': 3}, 
{'key': 'c', 'value': 5}
]
print(group_by_key(input2))