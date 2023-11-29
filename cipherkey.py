def getCipherkey():
    while True:
        try:
            sa = input("Please enter a key (whole number from 1-25): ")
            sa = int(sa)
            if 1<= sa <=25:
                return sa
            else:
                print("enter Numeric value")
        except ValueError:
            print("You have entered Non-numeric")