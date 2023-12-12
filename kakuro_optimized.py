import numpy as np

class Kakuro:
    WALL = 'W'
    EMPTY = ' '

    def __init__(self, field):
        self.field = field

    def get_segments(self, row, col):
        vertical_list = []
        horizontal_list = []
        vertical_target = None
        horizontal_target = None

        for r in range(row - 1, -1, -1):
            if self.field[r, col] == Kakuro.WALL or (isinstance(self.field[r, col], dict)):
                if isinstance(self.field[r, col], dict) and self.field[r, col]['top'] != None:
                    vertical_target = self.field[r, col]['top']
                break
            vertical_list.append(self.field[r, col])

        for r in range(row + 1, len(self.field)):
            if self.field[r, col] == Kakuro.WALL or (isinstance(self.field[r, col], dict)):
                break
            vertical_list.append(self.field[r, col])

        for c in range(col - 1, -1, -1):
            if self.field[row, c] == Kakuro.WALL or (isinstance(self.field[row, c], dict)):
                if isinstance(self.field[row, c], dict) and self.field[row, c]['left'] != None:
                    horizontal_target = self.field[row, c]['left']
                break
            horizontal_list.append(self.field[row, c])

        for c in range(col + 1, len(self.field[row])):
            if self.field[row, c] == Kakuro.WALL or (isinstance(self.field[row, c], dict)):
                break
            horizontal_list.append(self.field[row, c])

        return vertical_list, vertical_target, horizontal_list, horizontal_target


    def is_valid(self, row, col, num):
        vertical_list, vertical_target, horizontal_list, horizontal_target = self.get_segments(
            row, col)
        vertical_sum, horizontal_sum = 0, 0
        for item in vertical_list:
            if type(item) == int:
                vertical_sum += item

        for item in horizontal_list:
            if type(item) == int:
                horizontal_sum += item

        if vertical_target and ((num in vertical_list) or (vertical_list.count(Kakuro.EMPTY) == 0 and vertical_sum + num != vertical_target) or (vertical_sum + num > vertical_target)):
            return False
        if horizontal_target and ((num in horizontal_list) or (horizontal_list.count(Kakuro.EMPTY) == 0 and horizontal_sum + num != horizontal_target) or (horizontal_sum + num > horizontal_target)):
            return False
        
        return True

    def find_empty(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i, j] == Kakuro.EMPTY:
                    return i, j
        return None
    
    def find_most_constrained_empty(self):
        min_legal_values = 10
        most_constrained_cell = None

        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i, j] == Kakuro.EMPTY:
                    legal_values_count = self.count_legal_values(i, j)
                    if legal_values_count < min_legal_values:
                        min_legal_values = legal_values_count
                        most_constrained_cell = (i, j)

        return most_constrained_cell

    def count_legal_values(self, row, col):
        count = 0
        for value in range(1, 10):
            if self.is_valid(row, col, value):
                count += 1
        return count
    
    def get_legal_values(self, row, col):
        legal_values = []
        for value in range(1, 10):
            if self.is_valid(row, col, value):
                legal_values.append(value)
        return legal_values



    def solve(self):
        find = self.find_most_constrained_empty()
        if not find:
            return True
        else:
            row, col = find

        legal_values = self.get_legal_values(row, col)
        legal_values_sorted = self.sort_by_least_constraining_value(legal_values, row, col)

        for i in legal_values_sorted:
            self.field[row][col] = i
            if self.solve():
                return True
            self.field[row][col] = Kakuro.EMPTY

        return False

    def sort_by_least_constraining_value(self, legal_values, row, col):
        constraint_count = []

        for value in legal_values:
            count = self.count_constraints_for_value(row, col, value)
            constraint_count.append((value, count))

        constraint_count.sort(key=lambda x: x[1])
        sorted_values = [val for val, count in constraint_count]

        return sorted_values

    def count_constraints_for_value(self, row, col, value):
        count = 0

        original_value = self.field[row, col]
        self.field[row, col] = value

        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if (i != row or j != col) and self.field[i, j] == Kakuro.EMPTY:
                    if not self.get_legal_values(i, j):
                        count += 1

        self.field[row, col] = original_value

        return count


    @staticmethod
    def set_targets(left=None, top=None):
        return {
            'left': left,
            'top': top,
        }
    
    def __str__(self):
        st = ''
        for row in self.field:
            for cell in row:
                st += str(cell) if type(cell) != dict else 'B'
                st += ' '
            st += '\n'
        return st
