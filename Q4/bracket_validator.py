class BracketValidator:
    def __init__(self, string: str = None):
        if type(string) is not str:
            print("Object is initialized with empty string.")
            self.string = ''
        else:
            self.string = string
            print("Object is initialized with predefined array.")

    def validate(self, string: list = None):
        array_ = string if type(string) is str else self.string
        opening_brackets = {
            "{": True,
            "(": True,
            "[": True
        }
        closing_brackets = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        bracket_stack = []
        for idx in range(len(array_)):
            char = array_[idx]
            if char in opening_brackets:
                bracket_stack.append(char)
            else:
                if char in closing_brackets and bracket_stack[len(bracket_stack) - 1] == closing_brackets[char]:
                    bracket_stack = bracket_stack[:len(bracket_stack) - 1]
                else:
                    return False
        return len(bracket_stack) == 0
