ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# () - tuple
# A tuple is a sequence of items that can't be changed (immutable).

# [] - list
# A list is a sequence of items that can be changed (mutable).

# {} - dictionary or set
# A dictionary is a list of key-value pairs, with unique keys (mutable).

#your code here

ft_list[1] = 'World!'

converted_list = list(ft_tuple)
converted_list[1] = 'France!'
ft_tuple = tuple(converted_list)

ft_set.remove('tutu!')
ft_set.add('Paris!')

ft_dict['Hello'] = '42Paris!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)