 



class User():
    first_name = ''
    last_name = ''
    email_address = ''
    phone_number = ''
    alergies = ''
    food_diet = ''
    user_type = ''
    is_active = False
    
    def get_full_name(self):
        return "{},{}".format (self.first_name,self.last_name)


class MealItem():
    meal_name= ''
    description = ''
    serving_size = ''
    allergens = ''

class Admin():
    name = ''
    number = ''
    


class Kitchen():
    pass 



user = User()
user.first_name = 'Max'
user.last_name  = 'Arhur'
user.phone_number  = '0204875759'
user.email_address = 'max@gmail.com'




class Order():
    pass


class Price():
    pass



print('My name is {} and we are Fuudia'.format(user.get_full_name()))


class Father():
    last_name = ''
    company = ''
    wife = ''

class Son(Father):
    first_name =''


# Admin
# upload Menu
# delete menu
# delete users


# kitchen staff 
# upload menu 
# delete menu


# EIT/ FACULTY/ OTHERS
# Order menu 