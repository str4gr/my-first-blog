import webbrowser
user={}
while True:
#регистрация 
    print("REGISTRATION")
    name=input("Name:")
    sername=input("Sername:")
    password=str(input("Password:"))
    #удаление пробелов в name, sernme, password
    name=name.replace(" ",'')
    sername=sername.replace(" ",'')
    password=password.replace(" ",'')
    a={"name"+name:name}
    b={"sername"+name:sername}
    c={"password"+name:password}
    user.update(a)
    user.update(b)
    user.update(c)
    #регистрация другого пользователя 
    print("to regist another print OK")
    s=input()
    step=s.upper()
    if step=="OK":
        continue
    else:
        print("")
        break
#вход
print('''
''')
print("Log in")

while True:
    try:
#сдалать обработку исключений 
        name=input("Name:")
        sername=input("Sername:")
        password=str(input("Password:"))
        if user["name"+name]==name and user["sername"+name]==sername and user["password"+name]==password:
            print("autification complete")
            break
        else:
            print("something wrong, try again") 
            print('''
            	''')
            continue 

    except KeyError as error:
        print("something wrong, try again")
        continue 

#страница
f = open ("index1.html", 'r')
result = f.read()
webbrowser.open("index1.html")
