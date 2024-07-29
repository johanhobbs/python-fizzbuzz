# Run through the numbers between 1 and 100 and print the number, BUT
# For multiples of 3, print Fizz
# For multiples of 5, print Buzz
# For multiples of both, print FizzBuzz

def fizz_buzz(up_to_number):
    answer = ""
    for i in range(up_to_number):
        if i % 3 == 0 and i % 5 == 0 :
            answer = "FizzBuzz"
        elif i % 3 == 0 :
            answer = "Fizz"
        elif i % 5 == 0 :
            answer = "Buzz"
        else:
            answer = str(i)
        print(answer)

if __name__ == "__main__":
    fizz_buzz(25)