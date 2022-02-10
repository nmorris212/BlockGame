import numpy as np
class GameBoard:
    def __init__(self):
        self.board = np.zeros((10, 10))
        self.score = 0
    def __str__(self):
        fullString = ""
        fLine = "Score: " + str(self.score)+'\n'+"-\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t\n"
        fullString += fLine
        for i in range(len(self.board)):
            tempString = str(i)+"\t"
            for j in range(len(self.board[0])):
                tempString += str(int(self.board[i][j]))+"\t"
            tempString += "\n"
            fullString += tempString
        return fullString
    def getTest(self,x,y):
        return self.board[x][y]
    def __getitem__(self, point):
        x = point[0]
        y = point[1]
        return self.board[x][y]
    def __setitem__(self, key, value):
        x,y = key
        self.board[x,y] = value
    def printBoard(self):
        print(str(self))
    def checkBoard(self):
        count = 0
        # Check rows
        for i in range(10):
            for j in range(10):
                if self.board[i][j] != 1.0:
                    break
                elif j == 9:
                    count += 1
        # Columns
        for i in range(10):
            for j in range(10):
                if self.board[j][i] != 1.0:
                    break
                elif j == 9:
                    count += 1
        if count == 5:
            self.score += count * 10 + 200
        elif count == 6:
            self.score += count * 10 + 300
        else:
            self.score += count * 10
        return self.score
    def updateBoard(self):
        count = 0
        # Check rows
        fullRows = []
        for i in range(10):
            for j in range(10):
                if self.board[i][j] != 1.0:
                    break
                elif j == 9:
                    count += 1
                    fullRows.append(i)
        # Columns
        fullColumns = []
        for i in range(10):
            for j in range(10):
                if self.board[j][i] != 1.0:
                    break
                elif j == 9:
                    count += 1
                    fullColumns.append(i)
        if count == 5:
            self.score += count * 10 + 200
        elif count == 6:
            self.score += count * 10 + 300
        else:
            self.score += count * 10
        # Removes the entries from the rows after scoring
        if len(fullRows) != 0:
            for i in fullRows:
                for j in range(10):
                    self.board[i][j] = 0
        if len(fullColumns) != 0:
            for i in fullColumns:
                for j in range(10):
                    self.board[j][i] = 0
        return self
    def getBoard(self):
        return self.board
    def getScore(self):
        return self.score
    def setScore(self, score):
        self.score = score
    def placeBlock(self, id, middle):
        if id == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i + middle[0] not in range(0, 10) or j + middle[1] not in range(0, 10):
                        return False
                    if self.board[i + middle[0]][j + middle[1]] != 0.0:
                        return False
                    else:
                        continue
            for i in range(-1, 2):
                for j in range(-1, 2):
                    self.board[i + middle[0]][j + middle[1]] = 1.0
            self.score += 9
            self.updateBoard()
            return self.board

        if id == 1:
            for i in range(-1, 1):
                for j in range(-1, 1):
                    if i + middle[0] not in range(0, 10) or j + middle[1] not in range(0, 10):
                        return False
                    if self.board[i + middle[0]][j + middle[1]] != 0.0:
                        return False
                    else:
                        continue
            for i in range(-1, 1):
                for j in range(-1, 1):
                    self.board[i + middle[0]][j + middle[1]] = 1.0
            self.score += 4
            self.updateBoard()
            return self.board

        if id == 2:
            for i in range(-1, 1):
                if middle[0] + i not in range(0, 10):
                    return False
                if self.board[middle[0] + i][middle[1]] != 0.0:
                    return False
                else:
                    continue
            for i in range(-1, 1):
                self.board[middle[0] + i][middle[1]] = 1.0
            self.score += 2
            self.updateBoard()
            return self.board

        if id == 3:
            for i in range(-1, 2):
                if middle[0] + i not in range(0, 10):
                    return False
                if self.board[middle[0] + i][middle[1]] != 0.0:
                    return False
                else:
                    continue
            for i in range(-1, 2):
                self.board[middle[0] + i][middle[1]] = 1.0
            self.score += 3
            self.updateBoard()
            return self.board

        if id == 4:
            for i in range(-2, 2):
                if middle[0] + i not in range(0, 10):
                    return False
                if self.board[middle[0] + i][middle[1]] != 0.0:
                    return False
                else:
                    continue
            for i in range(-2, 2):
                self.board[middle[0] + i][middle[1]] = 1.0
            self.score += 4
            self.updateBoard()
            return self.board

        if id == 5:
            for i in range(-2, 3):
                if middle[0] + i not in range(0, 10):
                    return False
                if self.board[middle[0] + i][middle[1]] != 0.0:
                    return False
                else:
                    continue
            for i in range(-2, 3):
                self.board[middle[0] + i][middle[1]] = 1.0
            self.score += 5
            self.updateBoard()
            return self.board

        if id == 6:
            if self.board[middle[0]][middle[1]] != 0.0:
                return False
            self.board[middle[0]][middle[1]] = 1.0
            self.score += 1
            self.updateBoard()
            return self.board

        if id == 7:
            for i in range(-1, 1):
                if middle[1] + i not in range(0, 10):
                    return False
                if self.board[middle[0]][middle[1] + i] != 0.0:
                    return False
                else:
                    continue
            for i in range(-1, 1):
                self.board[middle[0]][middle[1] + i] = 1.0
            self.score += 2
            self.updateBoard()
            return self.board

        if id == 8:
            for i in range(-1, 2):
                if middle[1] + i not in range(0, 10):
                    return False
                if self.board[middle[0]][middle[1] + i] != 0.0:
                    return False
                else:
                    continue
            for i in range(-1, 2):
                self.board[middle[0]][middle[1] + i] = 1.0
            self.score += 3
            self.updateBoard()
            return self.board

        if id == 9:
            for i in range(-2, 2):
                if middle[1] + i not in range(0, 10):
                    return False
                if self.board[middle[0]][middle[1] + i] != 0.0:
                    return False
                else:
                    continue
            for i in range(-2, 2):
                self.board[middle[0]][middle[1] + i] = 1.0
            self.score += 4
            self.updateBoard()
            return self.board

        if id == 10:
            for i in range(-2, 3):
                if middle[1] + i not in range(0, 10):
                    return False
                if self.board[middle[0]][middle[1] + i] != 0.0:
                    return False
                else:
                    continue
            for i in range(-2, 3):
                self.board[middle[0]][middle[1] + i] = 1.0
            self.score += 5
            self.updateBoard()
            return self.board

        if id == 11:
            """
            Creates a "step" shape with the middle point at the center of the step
            1. 1.
            1. 0.
            :param self.board: Some gameself.board
            :param middle: Center of the step
            :return: Gameself.board or False if cannot be placed
            """
            x, y = middle
            if x > 8 or y > 8:
                return False
            if self.board[x][y] != 0.0 or self.board[x + 1][y] != 0.0 or self.board[x][y + 1] != 0.0:
                return False
            else:
                self.board[x][y] = 1.0
                self.board[x + 1][y] = 1.0
                self.board[x][y + 1] = 1.0
            self.score += 3
            self.updateBoard()
            return self.board

        if id == 12:
            """
            Creates a "step" shape with the middle point at the center of the step
            1. 0.
            1. 1.
            :param self.board: Some gameself.board
            :param middle: Center of the step
            :return: Gameself.board or False if cannot be placed
            """
            x, y = middle
            if x < 1 or y > 8:
                return False
            if self.board[x][y] != 0.0 or self.board[x - 1][y] != 0.0 or self.board[x][y + 1] != 0.0:
                return False
            else:
                self.board[x][y] = 1.0
                self.board[x - 1][y] = 1.0
                self.board[x][y + 1] = 1.0
            self.score += 3
            self.updateBoard()
            return self.board

        if id == 13:
            """
            Creates a "step" shape with the middle point at the center of the step
            1. 1.
            0. 1.
            :param self.board: Some gameself.board
            :param middle: Center of the step
            :return: Gameself.board or False if cannot be placed
            """
            x, y = middle
            if x > 8 or y < 1:
                return False
            if self.board[x][y] != 0.0 or self.board[x + 1][y] != 0.0 or self.board[x][y - 1] != 0.0:
                return False
            else:
                self.board[x][y] = 1.0
                self.board[x + 1][y] = 1.0
                self.board[x][y - 1] = 1.0
            self.score += 3
            self.updateBoard()
            return self.board

        if id == 14:
            """
            Creates a "step" shape with the middle point at the center of the step
            0. 1.
            1. 1.
            :param self.board: Some gameself.board
            :param middle: Center of the step
            :return: Gameself.board or False if cannot be placed
            """
            x, y = middle
            if x < 1 or y < 1:
                return False
            if self.board[x][y] != 0.0 or self.board[x - 1][y] != 0.0 or self.board[x][y - 1] != 0.0:
                return False
            else:
                self.board[x][y] = 1.0
                self.board[x - 1][y] = 1.0
                self.board[x][y - 1] = 1.0
            self.score += 3
            self.updateBoard()
            return self.board

        if id == 14:
            """
            Creates an "L" with the middle point at the center of the L
            1. 1. 1.
            1. 0. 0.
            1. 0. 0.
            :param self.board: Some gameself.board
            :param middle: Center of the L
            :return: Gameself.board or False if cannot be placed
            """
            x, y = middle
            if x > 7 or y > 7:
                return False
            if self.board[x][y] != 0.0 or self.board[x + 1][y] != 0.0 or self.board[x][y + 1] != 0.0 or \
                    self.board[x + 2][y] != 0.0 or self.board[x][y + 2] != 0.0:
                return False
            else:
                self.board[x][y] = 1.0
                self.board[x + 1][y] = 1.0
                self.board[x][y + 1] = 1.0
                self.board[x + 2][y] = 1.0
                self.board[x][y + 2] = 1.0
            self.score += 5
            self.updateBoard()
            return self.board

        if id == 15:
            """
            Creates an "L" with the middle point at the center of the L
            1. 0. 0.
            1. 0. 0.
            1. 1. 1.
            :param self.board: Some gameself.board
            :param middle: Center of the L
            :return: Gameself.board or False if cannot be placed
            """
            x, y = middle
            if x < 2 or y > 8:
                return False
            if self.board[x][y] != 0.0 or self.board[x - 1][y] != 0.0 or self.board[x][y + 1] != 0.0 or \
                    self.board[x - 2][y] != 0.0 or self.board[x][y + 2] != 0.0:
                return False
            else:
                self.board[x][y] = 1.0
                self.board[x - 1][y] = 1.0
                self.board[x][y + 1] = 1.0
                self.board[x - 2][y] = 1.0
                self.board[x][y + 2] = 1.0
            self.score += 5
            self.updateBoard()
            return self.board

        if id == 16:
            """
            Creates an "L" with the middle point at the center of the L
            1. 1. 1.
            0. 0. 1.
            0. 0. 1.
            :param self.board: Some gameself.board
            :param middle: Center of the L
            :return: Gameself.board or False if cannot be placed
            """
            x, y = middle
            if x > 7 or y < 2:
                return False
            if self.board[x][y] != 0.0 or self.board[x + 1][y] != 0.0 or self.board[x][y - 1] != 0.0 or \
                    self.board[x + 2][y] != 0.0 or self.board[x][y - 2] != 0.0:
                return False
            else:
                self.board[x][y] = 1.0
                self.board[x + 1][y] = 1.0
                self.board[x][y - 1] = 1.0
                self.board[x + 2][y] = 1.0
                self.board[x][y - 2] = 1.0
            self.score += 5
            self.updateBoard()
            return self.board

        if id == 17:
            """
            Creates an "L" with the middle point at the center of the L
            0. 0. 1.
            0. 0. 1.
            1. 1. 1.
            :param self.board: Some gameself.board
            :param middle: Center of the L
            :return: Gameself.board or False if cannot be placed
            """
            x, y = middle
            if x < 2 or y < 2:
                return False
            if self.board[x][y] != 0.0 or self.board[x - 1][y] != 0.0 or self.board[x][y - 1] != 0.0 or \
                    self.board[x - 2][y] != 0.0 or self.board[x][y - 2] != 0.0:
                return False
            else:
                self.board[x][y] = 1.0
                self.board[x - 1][y] = 1.0
                self.board[x][y - 1] = 1.0
                self.board[x - 2][y] = 1.0
                self.board[x][y - 2] = 1.0
            self.score += 5
            self.updateBoard()
            return self.board









    def threeByThree(self, middle):
        for i in range(-1,2):
            for j in range(-1,2):
                if i + middle[0] not in range(0,10) or j + middle[1] not in range(0,10):
                    return False
                if self.board[i+middle[0]][j+middle[1]] != 0.0:
                    return False
                else:
                    continue
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.board[i+middle[0]][j+middle[1]] = 1.0
        self.score +=9
        self.updateBoard()
        return True
    def twoByTwo(self, middle):
        for i in range(-1,1):
            for j in range(-1,1):
                if i + middle[0] not in range(0,10) or j + middle[1] not in range(0,10):
                    return False
                if self.board[i+middle[0]][j+middle[1]] != 0.0:
                    return False
                else:
                    continue
        for i in range(-1, 1):
            for j in range(-1, 1):
                self.board[i+middle[0]][j+middle[1]] = 1.0
        self.score +=4
        self.updateBoard()
        return True
    def twoByOne(self, middle):
        for i in range(-1,1):
            if middle[0] + i not in range(0,10):
                return False
            if self.board[middle[0]+i][middle[1]] != 0.0:
                return False
            else:
                continue
        for i in range(-1, 1):
            self.board[middle[0] + i][middle[1]] = 1.0
        self.score += 2
        self.updateBoard()
        return True
    def threeByOne(self, middle):
        for i in range(-1,2):
            if middle[0] + i not in range(0,10):
                return False
            if self.board[middle[0]+i][middle[1]] != 0.0:
                return False
            else:
                continue
        for i in range(-1, 2):
            self.board[middle[0] + i][middle[1]] = 1.0
        self.score += 3
        self.updateBoard()
        return True
    def fourByOne(self, middle):
        for i in range(-2,2):
            if middle[0] + i not in range(0,10):
                return False
            if self.board[middle[0]+i][middle[1]] != 0.0:
                return False
            else:
                continue
        for i in range(-2, 2):
            self.board[middle[0] + i][middle[1]] = 1.0
        self.score += 4
        self.updateBoard()
        return True
    def fiveByOne(self, middle):
        for i in range(-2,3):
            if middle[0] + i not in range(0,10):
                return False
            if self.board[middle[0]+i][middle[1]] != 0.0:
                return False
            else:
                continue
        for i in range(-2, 3):
            self.board[middle[0] + i][middle[1]] = 1.0
        self.score += 5
        self.updateBoard()
        return True
    def oneByOne(self, middle):
        if self.board[middle[0]][middle[1]] != 0.0:
            return False
        self.board[middle[0]][middle[1]] = 1.0
        self.score += 1
        self.updateBoard()
        return True
    def oneByTwo(self, middle):
        for i in range(-1,1):
            if middle[1] + i not in range(0,10):
                return False
            if self.board[middle[0]][middle[1]+i] != 0.0:
                return False
            else:
                continue
        for i in range(-1, 1):
            self.board[middle[0]][middle[1]+i] = 1.0
        self.score += 2
        self.updateBoard()
        return True
    def oneByThree(self, middle):
        for i in range(-1,2):
            if middle[1] + i not in range(0,10):
                return False
            if self.board[middle[0]][middle[1]+i] != 0.0:
                return False
            else:
                continue
        for i in range(-1, 2):
            self.board[middle[0]][middle[1]+i] = 1.0
        self.score += 3
        self.updateBoard()
        return True
    def oneByFour(self, middle):
        for i in range(-2,2):
            if middle[1] + i not in range(0,10):
                return False
            if self.board[middle[0]][middle[1]+i] != 0.0:
                return False
            else:
                continue
        for i in range(-2, 2):
            self.board[middle[0]][middle[1]+i] = 1.0
        self.score += 4
        self.updateBoard()
        return True
    def oneByFive(self, middle):
        for i in range(-2,3):
            if middle[1] + i not in range(0,10):
                return False
            if self.board[middle[0]][middle[1]+i] != 0.0:
                return False
            else:
                continue
        for i in range(-2,3):
            self.board[middle[0]][middle[1]+i] = 1.0
        self.score += 5
        self.updateBoard()
        return True
    def step1(self, middle):
        """
        Creates a "step" shape with the middle point at the center of the step
        1. 1.
        1. 0.
        :param self.board: Some gameself.board
        :param middle: Center of the step
        :return: Gameself.board or False if cannot be placed
        """
        x,y = middle
        if x > 8 or y > 8:
            return False
        if self.board[x][y] != 0.0 or self.board[x+1][y] != 0.0 or self.board[x][y+1] != 0.0:
            return False
        else:
            self.board[x][y] = 1.0
            self.board[x + 1][y] = 1.0
            self.board[x][y + 1] = 1.0
        self.score += 3
        self.updateBoard()
        return True
    def step2(self, middle):
        """
        Creates a "step" shape with the middle point at the center of the step
        1. 0.
        1. 1.
        :param self.board: Some gameself.board
        :param middle: Center of the step
        :return: Gameself.board or False if cannot be placed
        """
        x,y = middle
        if x < 1 or y > 8:
            return False
        if self.board[x][y] != 0.0 or self.board[x-1][y] != 0.0 or self.board[x][y+1] != 0.0:
            return False
        else:
            self.board[x][y] = 1.0
            self.board[x -1][y] = 1.0
            self.board[x][y + 1] = 1.0
        self.score += 3
        self.updateBoard()
        return True
    def step3(self, middle):
        """
        Creates a "step" shape with the middle point at the center of the step
        1. 1.
        0. 1.
        :param self.board: Some gameself.board
        :param middle: Center of the step
        :return: Gameself.board or False if cannot be placed
        """
        x,y = middle
        if x > 8 or y < 1:
            return False
        if self.board[x][y] != 0.0 or self.board[x+1][y] != 0.0 or self.board[x][y-1] != 0.0:
            return False
        else:
            self.board[x][y] = 1.0
            self.board[x + 1][y] = 1.0
            self.board[x][y - 1] = 1.0
        self.score += 3
        self.updateBoard()
        return True
    def step4(self, middle):
        """
        Creates a "step" shape with the middle point at the center of the step
        0. 1.
        1. 1.
        :param self.board: Some gameself.board
        :param middle: Center of the step
        :return: Gameself.board or False if cannot be placed
        """
        x,y = middle
        if x < 1 or y < 1:
            return False
        if self.board[x][y] != 0.0 or self.board[x-1][y] != 0.0 or self.board[x][y-1] != 0.0:
            return False
        else:
            self.board[x][y] = 1.0
            self.board[x - 1][y] = 1.0
            self.board[x][y - 1] = 1.0
        self.score += 3
        self.updateBoard()
        return True
    def l1(self, middle):
        """
        Creates an "L" with the middle point at the center of the L
        1. 1. 1.
        1. 0. 0.
        1. 0. 0.
        :param self.board: Some gameself.board
        :param middle: Center of the L
        :return: Gameself.board or False if cannot be placed
        """
        x, y = middle
        if x > 7 or y > 7:
            return False
        if self.board[x][y] != 0.0 or self.board[x + 1][y] != 0.0 or self.board[x][y + 1] != 0.0 or self.board[x + 2][y] != 0.0 or self.board[x][y + 2] != 0.0:
            return False
        else:
            self.board[x][y] = 1.0
            self.board[x + 1][y] = 1.0
            self.board[x][y + 1] = 1.0
            self.board[x + 2][y] = 1.0
            self.board[x][y + 2] = 1.0
        self.score += 5
        self.updateBoard()
        return True
    def l2(self, middle):
        """
        Creates an "L" with the middle point at the center of the L
        1. 0. 0.
        1. 0. 0.
        1. 1. 1.
        :param self.board: Some gameself.board
        :param middle: Center of the L
        :return: Gameself.board or False if cannot be placed
        """
        x, y = middle
        if x < 2 or y > 8:
            return False
        if self.board[x][y] != 0.0 or self.board[x - 1][y] != 0.0 or self.board[x][y + 1] != 0.0 or self.board[x - 2][y] != 0.0 or self.board[x][y + 2] != 0.0:
            return False
        else:
            self.board[x][y] = 1.0
            self.board[x - 1][y] = 1.0
            self.board[x][y + 1] = 1.0
            self.board[x - 2][y] = 1.0
            self.board[x][y + 2] = 1.0
        self.score += 5
        self.updateBoard()
        return True
    def l3(self, middle):
        """
        Creates an "L" with the middle point at the center of the L
        1. 1. 1.
        0. 0. 1.
        0. 0. 1.
        :param self.board: Some gameself.board
        :param middle: Center of the L
        :return: Gameself.board or False if cannot be placed
        """
        x, y = middle
        if x > 7 or y < 2:
            return False
        if self.board[x][y] != 0.0 or self.board[x + 1][y] != 0.0 or self.board[x][y - 1] != 0.0 or self.board[x + 2][y] != 0.0 or self.board[x][y - 2] != 0.0:
            return False
        else:
            self.board[x][y] = 1.0
            self.board[x + 1][y] = 1.0
            self.board[x][y - 1] = 1.0
            self.board[x + 2][y] = 1.0
            self.board[x][y - 2] = 1.0
        self.score += 5
        self.updateBoard()
        return True
    def l4(self, middle):
        """
        Creates an "L" with the middle point at the center of the L
        0. 0. 1.
        0. 0. 1.
        1. 1. 1.
        :param self.board: Some gameself.board
        :param middle: Center of the L
        :return: Gameself.board or False if cannot be placed
        """
        x, y = middle
        if x < 2 or y < 2:
            return False
        if self.board[x][y] != 0.0 or self.board[x - 1][y] != 0.0 or self.board[x][y - 1] != 0.0 or self.board[x - 2][y] != 0.0 or self.board[x][y - 2] != 0.0:
            return False
        else:
            self.board[x][y] = 1.0
            self.board[x - 1][y] = 1.0
            self.board[x][y - 1] = 1.0
            self.board[x - 2][y] = 1.0
            self.board[x][y - 2] = 1.0
        self.score += 5
        self.updateBoard()
        return True









    # Checking functions will be below. These will be used as a part of an evaluation function
    def checkThreeByThree(self, middle):
        try:
            for i in range(-1,2):
                for j in range(-1,2):
                    if self.board[i+middle[0]][j+middle[1]] != 0.0:
                        return False
                    else:
                        return True
        except IndexError:
            return
    def checkTwoByTwo(self, middle):
        try:
            for i in range(-1,1):
                for j in range(-1,1):
                    if self.board[i+middle[0]][j+middle[1]] != 0.0:
                        return False
                    else:
                        return True
        except IndexError:
            return
    def checkTwoByOne(self, middle):
        try:
            for i in range(-1,1):
                if self.board[middle[0]+i][middle[1]] != 0.0:
                    return False
                else:
                    return True
        except IndexError:
            return
    def checkThreeByOne(self, middle):
        try:
            for i in range(-1,2):
                if self.board[middle[0]+i][middle[1]] != 0.0:
                    return False
                else:
                    return True
        except IndexError:
            return
    def checkFourByOne(self, middle):
        try:
            for i in range(-2,2):
                if self.board[middle[0]+i][middle[1]] != 0.0:
                    return False
                else:
                    return True
        except IndexError:
            return
    def checkFiveByOne(self, middle):
        try:
            for i in range(-2,3):
                if self.board[middle[0]+i][middle[1]] != 0.0:
                    return False
                else:
                    return True
        except IndexError:
            return
    def checkOneByOne(self, middle):
        try:
            if self.board[middle[0]][middle[1]] != 0.0:
                return False
            else:
                return True
        except IndexError:
            return
    def checkOneByTwo(self, middle):
        try:
            for i in range(-1,1):
                if self.board[middle[0]][middle[1]+i] != 0.0:
                    return False
                else:
                    return True
        except IndexError:
            return
    def checkOneByThree(self, middle):
        try:
            for i in range(-1,2):
                if self.board[middle[0]][middle[1]+i] != 0.0:
                    return False
                else:
                    return True
        except IndexError:
            return
    def checkOneByFour(self, middle):
        try:
            for i in range(-2,2):
                if self.board[middle[0]][middle[1]+i] != 0.0:
                    return False
                else:
                    return True
        except IndexError:
            return
    def checkOneByFive(self, middle):
        try:
            for i in range(-2,3):
                if self.board[middle[0]][middle[1]+i] != 0.0:
                    return False
                else:
                    return True
        except IndexError:
            return
    def checkStep1(self, middle):
        """
        Creates a "step" shape with the middle point at the center of the step
        1. 1.
        1. 0.
        :param self.board: Some gameself.board
        :param middle: Center of the step
        :return: Gameself.board or False if cannot be placed
        """
        try:
            x,y = middle
            if self.board[x][y] != 0.0 or self.board[x+1][y] != 0.0 or self.board[x][y+1] != 0.0:
                return False
            else:
                return True
        except IndexError:
            return
    def checkStep2(self, middle):
        """
        Creates a "step" shape with the middle point at the center of the step
        1. 0.
        1. 1.
        :param self.board: Some gameself.board
        :param middle: Center of the step
        :return: Gameself.board or False if cannot be placed
        """
        try:
            x,y = middle
            if self.board[x][y] != 0.0 or self.board[x-1][y] != 0.0 or self.board[x][y+1] != 0.0:
                return False
            else:
                return True
        except IndexError:
            return
    def checkStep3(self, middle):
        """
        Creates a "step" shape with the middle point at the center of the step
        1. 1.
        0. 1.
        :param self.board: Some gameself.board
        :param middle: Center of the step
        :return: Gameself.board or False if cannot be placed
        """
        try:
            x,y = middle
            if self.board[x][y] != 0.0 or self.board[x+1][y] != 0.0 or self.board[x][y-1] != 0.0:
                return False
            else:
                return True
        except IndexError:
            return
    def checkStep4(self, middle):
        """
        Creates a "step" shape with the middle point at the center of the step
        0. 1.
        1. 1.
        :param self.board: Some gameself.board
        :param middle: Center of the step
        :return: Gameself.board or False if cannot be placed
        """
        try:
            x,y = middle
            if self.board[x][y] != 0.0 or self.board[x-1][y] != 0.0 or self.board[x][y-1] != 0.0:
                return False
            else:
                return True
        except IndexError:
            return
    def checkl1(self, middle):
        """
        Creates an "L" with the middle point at the center of the L
        1. 1. 1.
        1. 0. 0.
        1. 0. 0.
        :param self.board: Some gameself.board
        :param middle: Center of the L
        :return: Gameself.board or False if cannot be placed
        """
        try:
            x, y = middle
            if self.board[x][y] != 0.0 or self.board[x + 1][y] != 0.0 or self.board[x][y + 1] != 0.0 or self.board[x + 2][y] != 0.0 or self.board[x][y + 2] != 0.0:
                return False
            else:
                return True
        except IndexError:
            return
    def checkl2(self, middle):
        """
        Creates an "L" with the middle point at the center of the L
        1. 0. 0.
        1. 0. 0.
        1. 1. 1.
        :param self.board: Some gameself.board
        :param middle: Center of the L
        :return: Gameself.board or False if cannot be placed
        """
        try:
            x, y = middle
            if self.board[x][y] != 0.0 or self.board[x - 1][y] != 0.0 or self.board[x][y + 1] != 0.0 or self.board[x - 2][y] != 0.0 or self.board[x][y + 2] != 0.0:
                return False
            else:
                return True
        except IndexError:
            return
    def checkl3(self, middle):
        """
        Creates an "L" with the middle point at the center of the L
        1. 1. 1.
        0. 0. 1.
        0. 0. 1.
        :param self.board: Some gameself.board
        :param middle: Center of the L
        :return: Gameself.board or False if cannot be placed
        """
        try:
            x, y = middle
            if self.board[x][y] != 0.0 or self.board[x + 1][y] != 0.0 or self.board[x][y - 1] != 0.0 or self.board[x + 2][y] != 0.0 or self.board[x][y - 2] != 0.0:
                return False
            else:
                return True
        except IndexError:
            return
    def checkl4(self, middle):
        """
        Creates an "L" with the middle point at the center of the L
        0. 0. 1.
        0. 0. 1.
        1. 1. 1.
        :param self.board: Some gameself.board
        :param middle: Center of the L
        :return: Gameself.board or False if cannot be placed
        """
        try:
            x, y = middle
            if self.board[x][y] != 0.0 or self.board[x - 1][y] != 0.0 or self.board[x][y - 1] != 0.0 or self.board[x - 2][y] != 0.0 or self.board[x][y - 2] != 0.0:
                return False
            else:
                return True
        except IndexError:
            return

    # Features are below
    def orphanSquares(self):
        count = 0
        for i in range(10):
            for j in range(10):
                rightSide = False
                leftSide = False
                top = False
                bottom = False
                if i-1 < 0:
                    top = True
                if i+1 > 9:
                    bottom = True
                if j - 1 < 0:
                    leftSide = True
                if j + 1 > 9:
                    rightSide = True
                if top and leftSide:
                    if self.board[i+1][j] == 1.0 and self.board[i][j+1] == 1.0:
                        count+=1
                elif top and rightSide:
                    if self.board[i + 1][j] == 1.0 and self.board[i][j - 1] == 1.0:
                        count+=1
                elif bottom and leftSide:
                    if self.board[i - 1][j] == 1.0 and self.board[i][j + 1] == 1.0:
                        count+=1
                elif bottom and rightSide:
                    if self.board[i - 1][j] == 1.0 and self.board[i][j - 1] == 1.0:
                        count+=1
                else:
                    if self.board[i - 1][j] == 1.0 and self.board[i][j - 1] == 1.0 and self.board[i+1][j] == 1.0 and self.board[i][j+1] == 1.0:
                        count+=1
        return count
    def maxHorizontal(self):
        max = 0
        for i in range(10):
            counter = 0
            for j in range(10):
                if self.board[i][j] == 0.0:
                    counter+=1
                else:
                    if counter > max:
                        max = counter
                    counter = 0
                if j == 9:
                    if counter > max:
                        max = counter
        return max
    def maxVertical(self):
        max = 0
        for i in range(10):
            counter = 0
            for j in range(10):
                if self.board[j][i] == 0.0:
                    counter+=1
                else:
                    if counter > max:
                        max = counter
                    counter = 0
                if j == 9:
                    if counter > max:
                        max = counter
        return max
    def totalSquares(self):
        return int(self.board.sum())
    def emptyRows(self):
        count = 0
        for i in range(10):
            for j in range(10):
                if self.board[i][j] == 1.0:
                    break
                elif j == 9:
                    count+=1
        return count
    def emptyColumns(self):
        count = 0
        for i in range(10):
            for j in range(10):
                if self.board[j][i] == 1.0:
                    break
                elif j == 9:
                    count+=1
        return count
def main():
    board = GameBoard()
    board.twoByTwo((4,5))
    board.threeByThree((1,1))
    board.threeByThree((1,4))
    board.threeByThree((1, 7))
    board.threeByOne((1,9))
    board.step4((1,1))
    board.step3((8,1))
    board.step2((1,8))
    board.oneByFive((5,2))
    board.oneByFive((6,7))
    print(board)
    print(board.getScore())
    board.updateBoard()
    print(board)
    print("Total orphan squares:",board.orphanSquares())
    print("Maximum horizontal space:",board.maxHorizontal())
    print("Maximum vertical space:",board.maxVertical())
    print("Total squares:",board.totalSquares())
    print("Empty rows:",board.emptyRows())
    print("Empty columns:",board.emptyColumns())

if __name__ == "__main__":
    main()