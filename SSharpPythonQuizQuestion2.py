# Python Quiz Question 2
# author: SSharp

keepGoing = "yes"

while keepGoing == "yes":
    mag = float(input("Enter the magnitude of an earthquake: "))

    if mag < 0:
        print("Impossible. All earthquakes have a magnitude between 0 and 10.")
    elif mag <= 2.5:
        print("Usually not felt, but can be recorded through seismograph.")
    elif 2.6 <= mag <= 5.4:
        print("Often felt, but only causes minor damage.")
    elif 5.5 <= mag <= 6.0:
        print("Slight damage to buildings and other structures.")
    elif 6.1 <= mag <= 6.9:
        print("May cause lots of damage in very populated areas.")
    elif 7.0 <= mag <= 7.9:
        print("Major earthquake. Serious damage.")
    elif 8.0 <= mag <= 10:
        print("Great earthquake. Can totally destroy communities near the epicenter.")
    else:
        print("Impossible. All earthquakes have a magnitude between 0 and 10.")

    print()
    keepGoing = input("Do you want to keep going? Enter yes or no. ")
    print()
