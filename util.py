def list_check(array=None):
    return array is not None and type(array) == list


# taken from https://stackoverflow.com/a/1267145/6013366
def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
