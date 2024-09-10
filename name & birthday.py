
def addFamily(user):
    family=input(f"enter family {user['name']}=  ")
    lastName={'name': user['name'], 'age': user['age'],'family':family}
    return lastName
def main():
    from datetime import datetime

    users=[
        {'name': 'amir', 'birthday': 1990},
        {'name': 'ahmad', 'birthday': 2005},
        {'name': 'asghar', 'birthday': 2000},
        {'name': 'mamad', 'birthday': 1995},
        {'name': 'hossein', 'birthday': 2020}
    ]
    
    currentYear = datetime.now().year
    ages = list(map(lambda user: {'name': user['name'], 'age': currentYear - user['birthday']}, users))
    print(ages)
    
    adultUsers= list(filter(lambda user: user['age']>=18, ages))
    print(adultUsers)

    usersName=list(map(addFamily,ages))
    print(usersName)



main()