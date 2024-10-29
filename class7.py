def sqr(x):
    return x * x
print(sqr(44))

def avg(lis):
    return sum(lis)/len(lis)
print(avg([1,2,3,4,5]))

def reverse (list):
    print(list[::-1])
    return
reverse([1,2,23,6])

def cap(word):
    word = input('enter a word')
    print(word.upper())
    return

def dup_removal(list_1): #dont use keywords like "list" as a variable
    set1 = set(list_1)
    print(list(set1))
    return

dup_removal([1,2,3,4,5,6,6,8,4])

def combinator(list1, list2):
    print(set(list1)| set(list2))
    return

combinator([1,2,4,6,6], [3,5,67,8])