import datetime

def get_current_age():
    age = raw_input("What is your current age? ")
    return int(age)

def get_retirement_age():
    age = raw_input("At what age would you like to retire? ")
    return int(age)

def calculate_retirement_year(current_age, retirement_age):
    current_year = datetime.datetime.now().year
    how_many_years_left = retirement_age - current_age
    retirement_year = current_year + how_many_years_left
    if how_many_years_left > 0:
        print "You have {} years left until you can retire.".format(how_many_years_left)
        print "It's {}, so you can retire in {}.".format(str(current_year), str(current_year + how_many_years_left))
    else:
        if how_many_years_left == 0:
            print "You can retire this year!"
        else:
            print "You should have retired {} years ago.".format(abs(how_many_years_left))
    return retirement_year

def main():
    current_age = get_current_age()
    retirement_age = get_retirement_age()
    calculate_retirement_year(current_age, retirement_age)

if __name__ == '__main__':
    main()
