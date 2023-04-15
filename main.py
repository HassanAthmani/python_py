#  Exception handling-events detected during execution that interrupt the flow of the program

try:
    numerator = int(input("enter a number to be divided:"))
    denominator = int(input("enter a number to divide by:"))
    result = numerator/denominator

except ZeroDivisionError:
    print("You cannot divide a number by zero!")
except ValueError:
    print("Enter only numbers!")
except Exception:
    print("Something is wrong:")
else:
    print("the result is"+str(result))
finally:
    print("Thank you ):")


