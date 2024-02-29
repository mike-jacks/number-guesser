import pytest

class NumberGuesser:

    def __init__(self, begin_range, end_range):
        self.left = begin_range
        self.right = end_range
        self.mid = (self.left + self.right) // 2
        self.is_correct_answer = False

    def is_too_high_or_too_low(self):
        while True:
            user_input = input("Is the number too high or too low? (too high or too low): ")
            if user_input.lower() == "too high":
                self.right = self.mid - 1
                self.mid = (self.left + self.right) // 2
                return self.mid
            elif user_input.lower() == "too low":
                self.left = self.mid + 1
                self.mid = (self.left + self.right) // 2
                return self.mid
            else:
                print("Invalid input. Please enter 'too high' or 'too low'.")

    def is_guess_correct(self) -> bool:
        while True:
            user_input = input(f"Is it {self.mid}? (yes or no): ")
            if user_input.lower().strip() == "yes" or user_input.lower() == "y":
                self.is_correct_answer = True
                return True
            elif user_input.lower().strip() == "no" or user_input.lower() == "n":
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    while True:
        range = input("Enter the range of numbers you want the computer to guess using binary search?(num1 - num2): ")
        begin_range = range.split("-")[0].strip()
        end_range = range.split("-")[1].strip()
        try:
            begin_range = int(begin_range)
            end_range = int(end_range)
        except ValueError:
            print("Invalid input. Please enter a valid range.")
            continue
        break
    print(f"Think of a number between {begin_range} and {end_range} and I'll try and guess it!")

    while True:
        answer = input("Are you ready (yes or no): ")
        if answer.lower() == "no":
            print("Okay, let me know when you're ready.")
            continue
        elif answer.lower() == "yes":
            print("Great!")
            break
        else:
            print("Invalid input. Please enter yes or no.")

    number_guesser = NumberGuesser(begin_range, end_range)
    
    while not number_guesser.is_correct_answer:
        if number_guesser.left > number_guesser.right:
            print("You're cheating! I give up.")
            break
        if number_guesser.left == number_guesser.right:
            print(f"Your number must be {number_guesser.left}.", end=" ")
        if number_guesser.is_guess_correct():
            print("I got it! Awesome! Thanks for playing!")
            break
        number_guesser.is_too_high_or_too_low()




if __name__ == "__main__":
    main()
