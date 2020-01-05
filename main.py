#! /home/safa/Projects/M-Challenge-Solutions/venv/bin/python

import asyncio

from sys import argv, stdin
from Q1.find_duplicates_in_array import DuplicateFinder
from Q2.async_writer import AsyncWriter
from Q4.bracket_validator import BracketValidator
from Q5.floor_search import FloorSearch


def main():
    try:
        if len(argv) == 1:
            message = "Program should be run with at least one argument."
            raise Exception(message)
        q_no = argv[1]

        if len(argv) == 2:
            print("Input will be read from stdin")
            args = stdin.read().split()
        else:
            print("Arguments are considered as input")
            args = argv[2:]

        if q_no == "1":
            dup_finder = DuplicateFinder([*args])
            print(dup_finder.find_duplicates_in_list())
        elif q_no == "2":
            loop = asyncio.get_event_loop()
            async_writer = AsyncWriter([*args])
            res = async_writer.print_async(loop)
            # print("It is unblocking, other functions might be run without blocking.")
            loop.run_until_complete(res)  # this line makes it blocking.
            loop.close()
        elif q_no == "4":
            bracket_validator = BracketValidator(args[0])
            print(bracket_validator.validate())
        elif q_no == "5":
            floor_search = FloorSearch(args[0])
            print(floor_search.search_highest_egg_protector_floor())
        else:
            message = "Program should be run with at least one valid option and one argument."
            raise Exception(message)
    except Exception as e:
        print(e)
        print("Need to help? Read the README.md")


if __name__ == "__main__":
    main()
