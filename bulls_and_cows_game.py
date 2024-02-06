#!/usr/bin/env python

# Normally these classes would have been all in separate files.

import re
import random
from typing import List


class Credits:
    TITLE: str = "BULLS AND COWS GAME"
    AUTHOR: str = "Evgueni Antonov"
    DATE: str = "2024-02-06"
    VERSION: str = "1.0"
    APPURL: str = "https://github.com/StrayFeral/python_exercises"
    AUTHORMAIL: str = "Evgueni.Antonov@gmail.com"

    def __repr__(self) -> str:
        return f"{self.TITLE} {self.VERSION}\n{self.DATE} {self.AUTHOR} ({self.AUTHORMAIL})\n{self.APPURL}"


class Rules:
    RULES: str = """
RULES
=====================================================
Find the secret 4-digit number!
The number cannot contain same digits!
BULL: Found correct digit on the correct position.
COW: Found correct digit on a different position.

EXAMPLE:
Secret number = 1234
User guess = 0243
BULLS = 1, COWS = 2
because 2 is on the same position, 
but 3 and 4 are on different positions.

For reference:
https://en.wikipedia.org/wiki/Bulls_and_cows
"""

    def __repr__(self) -> str:
        return self.RULES


class BCNumber:
    """Bulls and Cows Number class.

    REQUIREMENTS:
    1) Must contain exactly four digits
    2) All symbols must be digits
    3) All digits must be unique
    (no digit can repeat twice in the number)
    """

    def __init__(self, num: str) -> None:
        self._value: List[int] = []
        self._value_str: str = num

    def valid(self) -> bool:
        if len(str(self)) != 4 or not re.search(r"^[0-9]+$", str(self)):
            return False

        # After ensuring all symbols are digits,
        # we can convert them to a list of integers
        self._value = [int(x) for x in str(self)]
        if len(set(self.value)) != 4:
            return False

        return True

    @property
    def value(self) -> List[int]:
        return self._value

    def __repr__(self) -> str:
        return self._value_str


class NewNumberPicker:
    """Generates a new random four digit integer."""

    def __init__(self) -> None:
        self._value: int = self._pick()

    def _pick(self) -> int:
        """Picks and returns a random number.

        It may look weird I seeded 101 as a start of the set, but
        this is to eliminate the numbers of 100 and smaller, which
        would mean we already have two zeroes on the right or two
        zeroes on the left padding. May not be the best decision,
        but seems good to me.
        """
        return random.randint(101, 9999)

    def __repr__(self) -> str:
        return f"{self._value:04}"

    @property
    def value(self) -> str:
        return str(self)


class UserInput:
    """Gets the user input and applies very basic string formatting."""

    def __init__(self, retries_count: int) -> None:
        self._value: str = ""
        self._retries_count = retries_count
        if retries_count < 1:
            raise ValueError(
                "retries_count must be a positive integer, greater than zero!"
            )

    def get(self) -> str:
        self._value = input(f"[{self._retries_count}] Your guess: ")
        self._value.strip()

        if len(self._value) and self._value[0].upper() == "Q":
            self._value = "Q"  # Regardless if there are other symbols

        return str(self)

    def __repr__(self) -> str:
        return self._value.upper()


class InputAnalyzer:
    def __init__(self, number: BCNumber, guess: BCNumber) -> None:
        self._value: str = self._analize(number, guess)

    def _analize(self, number: BCNumber, guess: BCNumber) -> str:
        bulls: int = 0
        cows: int = 0

        for i in range(4):
            if guess.value[i] == number.value[i]:
                bulls += 1
            elif guess.value[i] in number.value:
                cows += 1

        return f"BULLS: {bulls}; COWS: {cows}"

    def __repr__(self) -> str:
        return self._value


class Game:
    """Main class."""

    def run(self) -> None:
        secret_number: BCNumber = BCNumber(NewNumberPicker().value)
        while not secret_number.valid():
            secret_number = BCNumber(NewNumberPicker().value)

        print(
            "Game start.\nWe got a new secret number. Now you must guess it!\nEnter a four-digit number or Q to quit!"
        )

        retries: int = 0
        win: bool = False
        user_quit = False
        while not win:
            retries += 1

            user_input: str = UserInput(retries).get()
            if user_input == "Q":
                user_quit = True
                retries -= 1
                break

            user_guess: BCNumber = BCNumber(user_input)
            while not user_guess.valid():
                print("ERROR: Invalid number! See the rules!")

                user_input = UserInput(retries).get()
                if user_input == "Q":
                    user_quit = True
                    break

                user_guess = BCNumber(user_input)

            if user_quit:
                retries -= 1
                break
            else:
                analysis: str = str(InputAnalyzer(secret_number, user_guess))
                print(analysis)

                if str(secret_number) == str(user_guess):
                    win = True

        status: str = "lost."
        if win:
            status = "WON!"

        print(f"\nGame end. Total retries: {retries}. Game status: You {status}")


if __name__ == "__main__":
    print(Credits())
    print(Rules())

    game: Game = Game()
    game.run()
