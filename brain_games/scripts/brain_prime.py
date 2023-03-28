#!/usr/bin/env python3

from brain_games.games import games_
from brain_games.prime import game


def main():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    games_(rules, game)


if __name__ == '__main__':
    main()
