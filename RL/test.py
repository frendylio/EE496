all_items = []
for i in range(0,5):
    new_item = {}
    new_item['a'] = i
    new_item['b'] = i

    all_items.append(new_item)
    print (id(new_item))


 print all_items