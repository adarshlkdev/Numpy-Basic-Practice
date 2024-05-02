import numpy as np

'''
list = [1 , 2 , 4 , 6]
print(list)

print('1 D Array')

a = np.array([1 , 2 , 4, 5])
print(a)

print('2 D Array')

b = np.array([[1.2 , 2 , 4, 5] ,
              [2 , 5 , 8 , 3]])
print(b)

print('3 D Array')

c = np.array([[[2+2j , 8 , 4, 5] ,
              [2 , 5.5 , 8 , 3] ,
              [3 , 6 ,7 , "Hello"]]])
print(c)

print(type(c))  #<class 'numpy.ndarray'>

print(a.size) #4
print(b.size) #8
print(c.size) #12

#shape = (rows , col)

print(a.shape)
print(b.shape)  #(2 , 4)
print(c.shape)

#datatype

print(a.dtype)
print(b.dtype)
print(c.dtype)
 
c = c.transpose()

print(c)



a = np.arange(1 , 100 , 2)
print(a)

a = a.reshape((10 , 5))
print(a)

a = a.flatten()  # It is just opposite of reshape function {a.ravel() is also used}
print(a)         # ravel() is faster than flatten as it doesn;t occuipy memory. It works on original array
'''

#<=================Numpy array Slicing operation=============>
'''
a = np.arange(1 , 51)
a = a.reshape(10 , 5)
print(a)
print(a[0])  #[ 1  2  3  4  5]

print(a[3, 4]) # 20

print(a[: , 2])  #all the rows of 2nd column

print(a[2:6 , 4])

print(a[2:5]) 

print(a[2:7:2])

print(a[2:7:2].dtype)

'''

#Numpy mathematical operation
'''
a = np.arange(0 , 18).reshape(6 , 3)
b = np.arange(20, 38).reshape(6 , 3)
print(a)
print(b)

print('\n' ,a+b)
print('\n' ,np.add(a , b))
print('\n' ,a-b)
print('\n' ,np.subtract(a , b))
print('\n' ,a*b)
print('\n',np.multiply(a , b))
print('\n',a/b)
print('\n',np.divide(a , b))

#Matrix multiplication

b = b.reshape(3 , 6)
print('\n')
c = a@b #print(a.dot(b))
print(c)
print(c.min())
print(c.max())
print(c.argmax())  #argmax() is index of that maximum value

'''

#Numpy random operations
'''

print(np.random.random(1))
print(np.random.random(2))
print(np.random.random((2 , 2)))
print(np.random.randint(1 , 10))

print(np.random.randint(1, 10 , (2 , 3)))

print(np.random.rand(2 , 2))
print(np.random.randn(2 , 2))  #n for negative

a = np.arange(1 , 10)
print(a)
print(np.random.choice(a))

'''
#Numpy string operations

s1 = 'Adarsh is my name'
s2 = ' I am a full stack developer'

print(np.char.add(s1 , s2))
print(np.char.upper(s1))
print(np.char.lower(s2))

print(np.char.split(s1))

s3 = 'Adarsh is my \n name'
print(np.char.splitlines(s3))

print(np.char.replace(s3 , 'Adarsh', 'Aman'))

print(np.char.center(' Good Morning ' , 80 , '#'))
