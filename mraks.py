def percent(x):
    return x / 200 * 100  # function to get percentage. You can change the total marks from 200 to your preferred number.

# Asking students to enter their obtained marks out of 200.
x = int(input("\nPlease enter the obtain marks out of 200? "))
while True:
    if x > 200:
        x = int(input("\nPlease enter the obtain marks out of 200? "))
        print("\nObtain Marks should not be greater than 200!")
    else:
        if round(x) >= 180:
            print("\nCongratulations. You got A+. Your percentage is", round(percent(x)), "%")
            break
        elif round(x) >= 150:
            print("\nCongratulations. You got A. Your percentage is ", round(percent(x)), "%")
            break
        elif round(x) >= 120:
            print("\nCongratulations. You got B. Your percentage is ", round(percent(x)), "%")
            break
        elif round(x) >= 110:
            print("\nYou got C. Your percentage is ", round(percent(x)), "%")
            break
        elif round(x) >= 90:
            print("\nYou got D. You need to improve yourself. Your percentage is ", round(percent(x)), "%")
            break
        elif round(x) < 90:
            print("\nCongratulations. You got F. Study more you retard. Your percentage is too funny",
                  round(percent(x)), "%") # This is intentional.
            break

