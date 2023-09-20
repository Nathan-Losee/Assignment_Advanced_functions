test_list = [1,2,3,4,5,6,7,8,9]
def cut_off_list(list1, arg):
    final = []
    list2 = list1
    filter1 = arg
    for i in range(filter1):
        final.append(list2[i])
    return final
final = cut_off_list(test_list, 6)
print(final)
