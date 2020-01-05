from util import list_check


class DuplicateFinder:
    def __init__(self, array=None):
        if not list_check(array) or len(array) == 0:
            print("Object is initialized with empty array.")
            self.array = []
        else:
            self.array = array
            print("Object is initialized with predefined array.")

    def find_duplicates_in_list(self, array=None):
        case_list = array if list_check(array) else self.array
        element_dict = {}
        duplicate_dict = {}
        for element in case_list:
            if element in element_dict:
                duplicate_dict[element] = True
            element_dict[element] = True
        return [*duplicate_dict]
