test_list = [1,[2,3],4,[5,[7,8],6,7,[8,[0,[2,8],1],9,[9,[0,[5,5,[7,8,9],5],1],4]],5,[7,9,8]]]
def recursion_list_fun(i):
    final = []

    for item in i:
        if isinstance(item, list):
            list1 = recursion_list_fun(item)
            if list1 != []:
                if final is None or len(list1) > len(final):
                    final = list1
    return final if final != [] else i
deepest_list = recursion_list_fun(test_list)
def add_one(i):
    x=0
    while x < len(final):
        final[x] = final[x]+1
        x+=1
    return final
final = add_one(test_list)
print(final)
