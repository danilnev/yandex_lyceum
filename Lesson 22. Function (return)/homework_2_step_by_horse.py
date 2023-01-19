def cell_to_word(cell):
    letters = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'
    }
    return letters[cell[0]] + str(cell[1])


def word_to_cell(word):
    letters = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8
    }
    return letters[word[0]], int(word[1])


def in_field(cell):
    if 1 <= cell[0] <= 8 and 1 <= cell[1] <= 8:
        return True
    else:
        return False


def possible_turns(cell: str) -> list[str]:
    tuple_cell = word_to_cell(cell)
    steps = []
    if in_field((tuple_cell[0] - 1, tuple_cell[1] + 2)):
        steps.append(cell_to_word((tuple_cell[0] - 1, tuple_cell[1] + 2)))
    if in_field((tuple_cell[0] + 1, tuple_cell[1] + 2)):
        steps.append(cell_to_word((tuple_cell[0] + 1, tuple_cell[1] + 2)))
    if in_field((tuple_cell[0] + 2, tuple_cell[1] + 2)):
        steps.append(cell_to_word((tuple_cell[0] + 2, tuple_cell[1] + 1)))
    if in_field((tuple_cell[0] + 2, tuple_cell[1] - 1)):
        steps.append(cell_to_word((tuple_cell[0] + 2, tuple_cell[1] - 1)))
    if in_field((tuple_cell[0] + 1, tuple_cell[1] - 2)):
        steps.append(cell_to_word((tuple_cell[0] + 1, tuple_cell[1] - 2)))
    if in_field((tuple_cell[0] - 1, tuple_cell[1] - 2)):
        steps.append(cell_to_word((tuple_cell[0] - 1, tuple_cell[1] - 2)))
    if in_field((tuple_cell[0] - 2, tuple_cell[1] - 1)):
        steps.append(cell_to_word((tuple_cell[0] - 2, tuple_cell[1] - 1)))
    if in_field((tuple_cell[0] - 2, tuple_cell[1] + 1)):
        steps.append(cell_to_word((tuple_cell[0] - 2, tuple_cell[1] + 1)))
    steps.sort()
    return steps


# print(possible_turns("B1"))
# print(possible_turns("H8"))
