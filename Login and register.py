def register():
    db = open("User_Details.txt", "r")
    a = input("Please enter your Email ID ")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])

    if a in d:
        print("User Already Exists. Please Enter new Email ID for Registration")
        register()

    elif a.count('@') == 0 or a.count('.') == 0:
        print("Email ID is not in a proper format. Please check the following examples and Try Again")
        print("sherlock@gmail.com nothing123@yahoo.in")
        register()

    elif ((a.index('@')) - (a.index('.'))) == -1:
        print("The Email ID should start with a character.Please check the following examples and Try Again")
        print("sherlock@gmail.com nothing123@yahoo.in")
        register()

    elif a[0].isdigit():
        print("The Email ID should start with a character.Please check the following examples and Try Again")
        print("sherlock@gmail.com nothing123@yahoo.in")
        register()

    elif (a[0] == '@' or a[0] == '$' or a[0] == '_' or a[0] == '%' or a[0] == '!' or a[0] == '#' or a[0] == '*' or a[
        0] == '&'):
        print("The Email ID should start with a character.Please check the following examples and Try Again")
        print("sherlock@gmail.com nothing123@yahoo.in")
        register()

    else:
        print("Username created")

    b = input("Create your password with atleast one capital letter one integer and one special character: ")
    s = False

    if len(b) < 5 or len(b) > 16:
        print("Create Password with length between 5 an 16, Try Again")
        register()

    if len(b) > 5 and len(b) < 16:
        l, u, p, d = 0, 0, 0, 0
        for i in b:
            if i.isdigit():
                d += 1
            if i.islower():
                l += 1
            if i.isupper():
                u += 1
            if (i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                p += 1
            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(b)):
                s = True

    if s:
        c = input("Confirm Password: ")
        while (c != b):
            print("Password not match, Try Again")
            c = input("Try Again: ")

    else:
        print("Try again")
        register()

    file = open("User_Details.txt", "a")
    file.write(a + "," + b + "\n")
    file.close()
    login()

def login():
    X=input("Enter your username to login: ")
    X = X.strip()
    db = open("User_Details.txt", "r")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])

    if X in d:
        Y=input("Please Enter your password: ")
        Y=Y.strip()
        file1=open("User_Details.txt","r").readlines()
        for x in file1:
            x=x.strip()
            info=x.split(",")
            if X==info[0] and Y==info[1]:
                print("Welcome to GUVI Home Page")
                exit()
            else:
                F = input("Forgot Password [Y/N] : ")

                if F == "N":
                    print("try")
                    login()

                if F == "Y":
                    b = input("Create your new password with atleast one capital letter one integer and one special character: ")
                    s = False

                    if len(b) < 5 and len(b) > 16:
                        print("Create Password with length between 5 an 16, Try Again")
                        register()

                    if len(b) > 5 and len(b) < 16:
                        l, u, p, d = 0, 0, 0, 0
                        for i in b:
                            if i.isdigit():
                                d += 1
                            if i.islower():
                                l += 1
                            if i.isupper():
                                u += 1
                            if (
                                    i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                                p += 1
                            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(b)):
                                s = True

                    if s:
                        c = input("Confirm Password: ")
                        while (c != b):
                            print("Password not match")
                            c = input("Try Again: ")

                    else:
                        print("Sorry,Try again to login")
                        login()

                    file = open("User_Details.txt", "w")
                    file.write(X + "," + b + "\n")
                    file.close()

    else:
        print("Unregister user you need to register first")
        register()

def homepage():
    print("Welcome to the GUVI Login Page ")
    print("For Existing user continue with Login. For new user, Please Register")
    print("1.Login"+"\n"+"2.Register ")
    W=int(input("Enter your Choice"))
    if W==1:
        login()
    elif W==2:
        register()
    else:
        print("Enter the Right choice and Try Again")
        homepage()
homepage()
