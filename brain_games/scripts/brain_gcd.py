#!/usr/bin/env python3

from brain_games.games import games_
from brain_games.nod import game


def main():
    rules = 'Find the greatest common divisor of given numbers.'
    games_(rules, game)


if __name__ == '__main__':
    main()
