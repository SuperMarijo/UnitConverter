print("Welcome to the unit conversion software. This software allows you to convert kilometers "
      "into miles.")

while True:
    km = int(input("Please enter the number of kilometers you wish to convert. "))

    mile = km * 0.6213712

    print(str(km) + " kilometers equals " + str(mile) + " miles.")

    retry = input("Would you like to make another conversion? (Y/N) ")

    if retry != "Y" and retry != "y" and retry != "Yes" and retry != "YES" and retry != "yes":
        break
