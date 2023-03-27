#!/usr/bin/env python3

from brain_games.games import games_
from brain_games.calc import game


def main():
    rules = 'What is the result of the expression'
    games_(rules, game)


if __name__ == '__main__':
    main()
