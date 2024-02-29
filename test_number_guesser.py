from number_guesser import NumberGuesser
import pytest

@pytest.fixture
def number_guesser_1_to_100():
    return NumberGuesser(1, 100)

@pytest.fixture
def guess_number():
    return 7

def describe_number_guesser():

    def it_instantiates(number_guesser_1_to_100):
        number_guesser = number_guesser_1_to_100
        assert number_guesser.left == 1
        assert number_guesser.right == 100
        assert number_guesser.mid == 50
        assert number_guesser.is_correct_answer == False
        assert str(number_guesser.left).isdigit()== True
        assert str(number_guesser.right).isdigit() == True
    
    def it_is_too_high_or_too_low(monkeypatch, number_guesser_1_to_100):
        number_guesser = number_guesser_1_to_100
        user_inputs = iter(["too high", "too low", "too high"])
        def mock_input(prompt):
            return next(user_inputs)
        monkeypatch.setattr('builtins.input', mock_input)

        assert number_guesser.is_too_high_or_too_low() == 25 # user input: too high
        assert number_guesser.is_too_high_or_too_low() == 37 # user input: too low
        assert number_guesser.is_too_high_or_too_low() == 31 # user input: too high

    def it_gets_correct_guess(monkeypatch, number_guesser_1_to_100):
        number_guesser = number_guesser_1_to_100
        monkeypatch.setattr('builtins.input',lambda _: "yes")
                            
        assert number_guesser.is_guess_correct() == True # user input: yes

    def it_gets_incorrect_guess(monkeypatch, number_guesser_1_to_100):
        number_guesser = number_guesser_1_to_100
        monkeypatch.setattr('builtins.input',lambda _: "no")
                            
        assert number_guesser.is_guess_correct() == False # user input: no

    def it_gets_invalid_input(monkeypatch, number_guesser_1_to_100):
        number_guesser = number_guesser_1_to_100
        user_inputs = iter(["invalid", "no", "another invalid input", "yes"])
        def mock_input(prompt):
            return next(user_inputs)
        monkeypatch.setattr('builtins.input', mock_input)
        print("\n")

        assert number_guesser.is_guess_correct() == False
        assert number_guesser.is_guess_correct() == True


