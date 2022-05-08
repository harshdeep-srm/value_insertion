value = int(input('Enter a value\t'))
index = int(input('Enter the index at which you want the value to be inserted\t'))

list = [1,2,3,4,5,6]
updated_list = list.insert(index,value)

print(list)