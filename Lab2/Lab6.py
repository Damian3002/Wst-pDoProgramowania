# 1
#
# int_numbers = [10,20,33]
# str_numbers = ["ten", "twenty" , "thirty"]
#
# dictionary = dict(zip(str_numbers , int_numbers ))
#
# print(dictionary)
#
# dict_1 = {}
#
# for i in range(len(int_numbers)):
#     dict_1[str_numbers[i]] = int_numbers[i]
# print(dict_1)
#
# dict_2 = dict(thirty=30 , fourty=40, fifty=50)
# dict_3 = dict_1.copy()
# dict_3.update(dict_2)
# print(dict_3)
#
# 2
#
# sample_dict = {
#  "name": "Kelly",
#  "surname": "Jones",
#  "age": 25,
#  "salary": 8000,
#  "city": "New york"}
#
#
# for k, v in sample_dict.items():
#     print(f'{k:<10} = {v:>10}')
# list = ["name", "age"]
#
# D = {}
# for k in list:
#     for k2 in sample_dict.keys():
#         if k == k2:
#             D[k] = sample_dict[k]
#
# print(D)
# for k in list:
#     sample_dict.pop(k, None)
# print(sample_dict)
#
# for k in sample_dict.values():
#     if k == "jones":
#         print("istnieje")
#         break
# else:
#     print("nie istnieje")

# 3
# slowniki = {x: x * x for x in range(1,16)}
# print(slowniki)
#
# slownik2 = {x: 2**x for x in range(0, 11)}
# print(slownik2)
