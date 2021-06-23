balance=100000
print("1.English\n"
      "2.Hindi")
language=int(input("Enter your Language"))
if language==1:
    pin=int(input("Enter your 4 digit number\n"))
    if pin==3456:
        print(
        "1. balance\n"
        "2. withdraw\n"
        "3. quit")
        option = int(input("What you want to do"))
        if option==1:
            print(balance)
        elif option==2:
            print("1.Savings\n"
                  "2.Current\n"
                  "3.Quit")
            withdraw=int(input("Enter Type "))
            Amt=int(input("Enter Amount"))
            if withdraw==1 or withdraw==2:
                if Amt<balance and Amt%100==0:
                    print("Your Transaction is successful")
                else:
                    print("You are unable to process transaction")
            else:
                print("Quit\n")
                print("Thankyou!")
    else:
        print("Invalid pin")
else:
    pin=int(input("Apna 4 ankh ka pin dabaye\n"))
    if pin==3456:
        print(
        "1. khaate mein shesh\n"
        "2. paise nikaalna\n"
        "3. vaapas")
        option = int(input("aapko kya karna hain"))
        if option==1:
            print(balance)
        elif option==2:
            print("1.bachat khaata\n"
                  "2.Chaalu khaata\n"
                  "3.vaapis")
            withdraw=int(input("Apne khaate ke prakar choose kare"))
            Amt=int(input("Rashi Daale"))
            if withdraw==1 or withdraw==2:
                if Amt<balance and Amt%100==0:
                    print("Aapka Transaction safal hua")
                else:
                    print("Aapka Transaction asamarth raha")
            else:
                print("process asamarth hone ke liye maafi\n")
                print("Dhanyawaad")
    else:
        print("Amanaya pin")

