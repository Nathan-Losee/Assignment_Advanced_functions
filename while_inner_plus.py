test_list =  [1,[2,3],4,[5,[7,8],6,7,[8,[0,[2,8],1],9,[9,[0,[5,5,[7,8,9],5],1],4]],5,[7,9,8]]]

def list_of_lists(i):
    x = 0
    lists = []
    while x < len(i):
        if type(i[x]) == list:
            lists.append(i[x])
        x+=1
    return lists

def list_boy(i):
    x = 0
    y = 0
    lists = []
    while x < len(i):
        while y < len(i[x]):
            if type(i[x][y]) == list:
                lists.append(i[x][y])
            y += 1
        y=0
        x+=1
    return lists

def check(i):
    final = list_of_lists(i)
    while len(final[0]) != 1:
        final = list_of_lists(final)
        if len(final) == 1:
            final = final[0]
            break
        final = list_boy(final)
        if len(final) == 1:
            if len(final[0]) != 1:
                final = list_boy(final)
            final  = final[0]
            break
    x=0
    while x < len(final):
        final[x] = final[x]+1
        x+=1
    return final

print(check(test_list))
