def high(x):
    alpha_rank = {}
    word_value = {}
    counter = 0
    for i in range(ord('a'), ord('z')+1):
        alpha_rank[chr(i)] = i-96
    word_list = x.split()
    for word in word_list:
        chars = list(word)
        for i in chars:
            if i in alpha_rank.keys():
                counter += int(alpha_rank.get(i))
        word_value[word] = counter
        counter = 0
    sortedWords = (sorted(word_value.items(), key = lambda x:x[1]))
    sw2 = [list(i) for i in sortedWords]
    #if len(sortedWords) > 1:
    for i in sw2:
        if sw2[-1][1] == sw2[-2][1]:                 
            sw2.pop()                                               
    return sw2[-1][0]
