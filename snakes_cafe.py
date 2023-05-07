print(
    '''
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    

    ***********************************
    ** What would you like to order? **
    ***********************************
    ''')

menu=["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"]


def user_insertion():
    user_input=input(">")
    return user_input

user_input=user_insertion()
orders=[]
while user_input != "quit":
    if user_input.lower().title() in menu:
        orders.append(user_input.lower().title())
        quantitiy=orders.count(user_input.lower().title())
        print(f"** {quantitiy} order of {user_input.lower().title()} has been added to your meal **")
        user_input=user_insertion()
    else:
        print("please choose order from the menu")
        user_input=user_insertion()
else:
    if (len(orders)!=0):
        print('your order is:',orders)
        print("Thank you for visiting my app")
    else:
        print("Thank you for visiting my app")

    
    



