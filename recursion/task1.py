def sum_of_numbers(n):
    #base solution
    if n == 1:
        result = 1
    #genral solution
    else:
        result = n + sum_of_numbers(n-1)
    return result

def user_input():
    n = int(input("please input an interger"))
    return n

def display(result):
    print("the sum of the numbers is",result)

def main():
    n = user_input()
    result = sum_of_numbers(n)
    display(result)

if __name__ == "__main__":
    main()
