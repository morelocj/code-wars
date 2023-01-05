# Implement the function unique_in_order which takes as argument a sequence 
# and returns a list of items without any elements with the same value next to each other 
# and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    if len(iterable) == 1:
        return list(iterable)
    result = [iterable[0]]
    dummy = result
    for i in iterable[1:]:
        if type(i) == str:
            if i != dummy[0]:
                result.append(i) 
                dummy = i
        if type(i) == int:
            if i != dummy:
                result.append(i) 
                dummy = i
    return result