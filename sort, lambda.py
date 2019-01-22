#SORTING BASICS
sorted(alist)
alist.sort
(sorted({1:'E', 2:'K', 6: 'A', 0:'B'}))
    # result : [0,1,2,6]


#KEY FUNCTIONS
print(sorted('a AAA aa AA'.split(), key = str.lower))
    #result : ['a', 'aa', 'AA', 'AAA']
print(sorted('a AAA aa AA'.split()))
    #result = ['AA', 'AAA', 'a', 'aa']


#LAMBDA
f = lambda x,y : x+y
f(1,1) #result : 2

a = [(1,2), (4,9), (0,6)]
a.sort(key = lambda x:x[1])
print(a)
    #result : [(1, 2), (0, 6), (4, 9)]
a.sort(key = lambda x:x[0])
print(a)
    #result : [(0, 6), (1, 2), (4, 9)]


#ZIP
a = [1,2,3,4]
b = [0,10,20,30]
data = zip(a,b)
data.sort()
a,b = map(lambda t: list(t), zip(*data))
print(a)
print(b)

numlist = [1,2,3]
strlist = ['one', 'two', 'three']
result = zip(numlist, strlist)
resultList = list(result)
print(resultList) #[(1, 'one'), (2, 'two'), (3, 'three')]
result = zip(numlist, strlist)
resultSet = set(result)
print(resultSet) #{(2, 'two'), (1, 'one'), (3, 'three')}
#order of resultList is alwasy same as 1,2,3 bue order of resultSet is chane


numList = [1,2,3]
strList = ['one', 'two']
strTuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip(numList,strTuple)
resultSet = set(result)
print(resultSet)
#{(2, 'TWO'), (1, 'ONE'), (3, 'THREE')}

result = zip(numList,strList,strTuple)
resultSet = set(result)
print(resultSet) #{(2, 'two', 'TWO'), (1, 'one', 'ONE')}


#UNZIPPING
coordinate = ['x', 'y', 'z']
value = [1,2,3,4,5]
result = zip(coordinate, value)
resultList = list(result)
print(resultList)
#[('x', 1), ('y', 2), ('z', 3)]
c,v = zip(*resultList)
print('c = ', c) #c =  ('x', 'y', 'z')
print('v = ', v) #v =  (1, 2, 3)
