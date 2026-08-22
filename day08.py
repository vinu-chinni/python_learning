#link:https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
# if __name__ == '__main__':
#     n = int(input().strip())
# if n % 2 == 1:
#     print("Weird")
# elif 2 <= n <= 5:
#     print("Not Weird")
# elif 6 <= n <= 20:
#     print("Weird")
# else:
#     print("Not Weird")



#Link:https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

#take n,if n from 1 to 7 print dayname else print invalid day number

n = int(input("Enter day number: "))

match n:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")
