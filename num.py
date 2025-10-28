import numpy as np

# a=np.array([2 , 4, 5 ,2,   4, 0])
# b=a[:3]
# b[1]=200
# print(b)
# print(a.dtype)

# a=np.zeros((2, 3))
# print(a)

# a=np.full((2, 3) , 6)
# print(a)

# a=np.eye(5)
# print(a)

# arr_3d=np.array([[[1,2,3] , [4 , 5,6] , [2,3, 4]]])
# print(arr_3d.ndim)

# a=np.array(["yukti" , "kashvi" , "saatvik"])
# print(a.dtype)

# a=np.array(["1"  ,"2"])
# print(a.astype(float))

# a=np.array([2, 4, 8])
# print(a**3)

# a=np.array([4, 8, 12])
# print(np.std(a))

# a=np.array([3 , 4, 5,6, 9 , 8])
# print(a[0:7:-1])

# print(a.reshape(2,3))


# arr=np.array([10 , 20 , 30   ,40 , 50 ])
# new_arr1=np.insert(arr , 0, 5  , axis=None)
# print(new_arr1)



# arr_2d=np.array([[1, 2,3] , [4, 5, 6]])
# new_arr2=np.insert(arr_2d , 0 , [3, 6, 8]  , axis=0)
# print(new_arr2)
#       OR.....
# print(np.insert(arr_2d , 1 , [3, 4, 5] , axis=0))


# arr_2d=np.array([[1, 2,3] , [4, 5, 6]])
# new_arr2=np.insert(arr_2d , 0 , 3, axis=1)
# print(new_arr2)


# arr=np.array([10 , 20 , 30])
# print(np.append(arr , [40 , 50 , 60]))


# arr_1=np.array([1,2,3])
# arr_2=np.array([4, 5, 6])

# print(np.concatenate((arr_2 , arr_1) ,axis=0))



# arr1=np.array([1,23,5])

# arr2=np.array([3,56,8])
# print(np.vstack((arr1 , arr2)))

# print(np.hstack((arr1 , arr2)))


# arr1=np.array([10,20, 30, 40 ,50 ,60])

# print(np.split(arr1 , 6))


prices=np.array([100 , 200 , 300 , 400])
discount=10
final_prices=prices-(prices*discount/100)
print(final_prices)