

# def greeting():
#     print('Hello welcome to the world')


# greeting()


# def polarity(num):
#     if num >=0:
#         return 'Its is positve'
#     else:
#         return 'It is negative'


# print(polarity(-10))




# def  personal_info(name, surname, gender, age):
#     print('Name of the boy is: ',name)
#     print('His surname is: ',surname)
#     print('Gender: ', gender  )
#     print('His age is: ',age)
   


# personal_info(name='Julian',age = 90,surname = 'Mayson', gender= 'Male')


def names(*args):
    for i in args:
        print(i)
names('Raul','Sham','Male')
