from util import represents_int
import math


class FloorSearch:
    def __init__(self, floor: str = None):
        self.goal_floor = int(floor) if represents_int(floor) else 0
        print("Goal floor is: {}".format(self.goal_floor))

    def search_highest_egg_protector_floor(self, floor: int = None):
        goal_floor_ = floor if type(floor) is int else self.goal_floor
        # print("Goal floor for search: {}".format(goal_floor_))
        it_count = 1
        pick = 2
        if goal_floor_ < 2:
            return 2

        while pick <= goal_floor_:
            # print(pick)
            it_count += 1
            pick = pick * 2
        # have 1 more egg
        # print("it_count: ", it_count)
        # print("goal_floor_: ", goal_floor_)
        # print("pick: ", pick)
        exact = type(math.floor(pick / goal_floor_)) is int
        # print("exact: ", exact)
        return int(it_count + (goal_floor_ - pick / 2)) + (1 if exact else 0)
