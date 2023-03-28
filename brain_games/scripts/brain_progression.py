#!/usr/bin/env python3

from brain_games.games import games_
from brain_games.progress import game


def main():
    rules = 'What number is missing in the progression?'
    games_(rules, game)


if __name__ == '__main__':
    main()
