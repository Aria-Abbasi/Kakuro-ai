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

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.is_valid(row, col, i):
                self.field[row][col] = i

                if self.solve():
                    return True

                self.field[row][col] = Kakuro.EMPTY

        return False

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
    
