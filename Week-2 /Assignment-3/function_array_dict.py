# -*- coding: utf-8 -*-

def avg(data):
    p = data.values()
    products = p[0]
    d1 = products[0]
    d2 = products[1]
    d3 = products[2]

    p1 = d1["price"]
    p2 = d2["price"]
    p3 = d3["price"]
    newlist = [p1,p2,p3]

    total = 0
    for p in newlist:
        total +=p
    avgp = total/len(newlist)
    return avgp

print( avg({
"products": [ {
"name": "Product 1",
"price": 100 },
{
"name": "Product 2", "price": 700
}, {
"price": 300 }
] })
)