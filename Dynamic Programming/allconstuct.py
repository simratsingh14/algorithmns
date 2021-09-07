'''
It takes a target word and we have to return 2-D how we construct it

'''
final = []
def allconstuct(target,wordBank,arr = []):
    if target == '':
        final.append(arr)
        return arr
    lar = list(filter(lambda x:target.startswith(x),wordBank))
    for i in lar:
        allconstuct(target[len(i):],wordBank,arr+[i])

    return final

target = 'enterapotentpot'
wordBank = ['a','p','ent','enter','ot','o','t']
print(allconstuct('',wordBank))
# print(allconstuct('abcdef',['ab','abc','cd','def','abcd','ef','c']))


    
