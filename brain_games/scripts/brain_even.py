#!/usr/bin/env python3

from brain_games.games import games_
from brain_games.even import game


def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    games_(rules, game)


if __name__ == '__main__':
    main()
