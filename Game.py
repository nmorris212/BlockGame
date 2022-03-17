import numpy as np, pandas as pd, random, time
from GameBoard import GameBoard
class Game:
    def __init__(self):
        # 19
        self.possibleMoves = [random.randint(0,18), random.randint(0,18), random.randint(0,18)]
        self.board = GameBoard()
        self.moves = self.getMoves()
    def __getitem__(self, tup):
        return self.board[tup]
    def __setitem__(self, key, value):
        x,y = key
        self.board[x,y] = value
    def __str__(self):
        return str(self.board)
    def checkIndex(self, x, y):
        return self.board[x,y]
    def getBoard(self):
        return self.board
    def getMoveIDs(self):
        return self.possibleMoves
    def checkLose(self):
        done = False
        entryResult = False
        breakLoop = False
        while (not entryResult) and (not done):
            for entry in self.possibleMoves:
                if breakLoop:
                    break
                for i in range(10):
                    if breakLoop:
                        break
                    for j in range(10):
                        if entry == 0:
                            tempResult = self.board.checkThreeByThree((i,j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 1:
                            tempResult = self.board.checkTwoByTwo((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 2:
                            tempResult = self.board.checkTwoByOne((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 3:
                            tempResult = self.board.checkThreeByOne((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 4:
                            tempResult = self.board.checkFourByOne((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 5:
                            tempResult = self.board.checkFiveByOne((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 6:
                            tempResult = self.board.checkOneByOne((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 7:
                            tempResult = self.board.checkOneByTwo((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 8:
                            tempResult = self.board.checkOneByThree((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 9:
                            tempResult = self.board.checkOneByFour((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 10:
                            tempResult = self.board.checkOneByFive((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 11:
                            tempResult = self.board.checkStep1((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 12:
                            tempResult = self.board.checkStep2((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 13:
                            tempResult = self.board.checkStep3((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 14:
                            tempResult = self.board.checkStep4((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 15:
                            tempResult = self.board.checkl1((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 16:
                            tempResult = self.board.checkl2((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 17:
                            tempResult = self.board.checkl3((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
                        elif entry == 18:
                            tempResult = self.board.checkl4((i, j))
                            if tempResult:
                                entryResult = True
                                breakLoop = True
            done = True
        return not entryResult
    def printBoard(self):
        print(self.board)


    def getMoves(self):
        Moves = []
        for i in self.possibleMoves:
            if i == 0:
                Moves.append("3x3")
            elif i == 1:
                Moves.append("2x2")
            elif i == 2:
                Moves.append("2x1")
            elif i == 3:
                Moves.append("3x1")
            elif i == 4:
                Moves.append("4x1")
            elif i == 5:
                Moves.append("5x1")
            elif i == 6:
                Moves.append("1x1")
            elif i == 7:
                Moves.append("1x2")
            elif i == 8:
                Moves.append("1x3")
            elif i == 9:
                Moves.append("1x4")
            elif i == 10:
                Moves.append("1x5")
            elif i == 11:
                Moves.append("Step1")
            elif i == 12:
                Moves.append("Step2")
            elif i == 13:
                Moves.append("Step3")
            elif i == 14:
                Moves.append("Step4")
            elif i == 15:
                Moves.append("L1")
            elif i == 16:
                Moves.append("L2")
            elif i == 17:
                Moves.append("L3")
            elif i == 18:
                Moves.append("L4")
        self.moves = Moves
        return self.moves
    def move(self, id, tup):
        x,y = tup
        if self.checkLose() == True:
            print("You have lost!")
            return
        self.board.printBoard()
        if id not in self.possibleMoves:
            return
        if x not in range(0,10) or y not in range(0,10):
            print("\nOut of range! Try again.\n")
        self = self.place(id,tup)
        self.possibleMoves.remove(id)
        if len(self.possibleMoves) == 0:
            self.possibleMoves = [random.randint(0,18), random.randint(0,18), random.randint(0,18)]
        self.board.updateBoard()
        self.getMoves()
    def updateMoves(self):
        self.possibleMoves = [random.randint(0,18), random.randint(0,18), random.randint(0,18)]
    def update(self):
        self.board = self.board.updateBoard()
    def place(self, blockID, location):
        i = blockID
        if i == 0:
            return self.board.threeByThree(location)
        elif i == 1:
            return self.board.twoByTwo(location)
        elif i == 2:
            return self.board.twoByOne(location)
        elif i == 3:
            return self.board.threeByOne(location)
        elif i == 4:
            return self.board.fourByOne(location)
        elif i == 5:
            return self.board.fiveByOne(location)
        elif i == 6:
            return self.board.oneByOne(location)
        elif i == 7:
            return self.board.oneByTwo(location)
        elif i == 8:
            return self.board.oneByThree(location)
        elif i == 9:
            return self.board.oneByFour(location)
        elif i == 10:
            return self.board.oneByFive(location)
        elif i == 11:
            return self.board.step1(location)
        elif i == 12:
            return self.board.step2(location)
        elif i == 13:
            return self.board.step3(location)
        elif i == 14:
            return self.board.step4(location)
        elif i == 15:
            return self.board.l1(location)
        elif i == 16:
            return self.board.l2(location)
        elif i == 17:
            return self.board.l3(location)
        elif i == 18:
            return self.board.l4(location)
    def startGame(self):
        self.move()
    def getPossibleStates(self):
        stateID = []
        location = []
        orphanSquares = []
        maxHorizontal = []
        maxVertical = []
        totalSquares = []
        emptyRows = []
        emptyColumns = []
        longestDFS = []
        eval = []
        moves = []
        scores = []
        possiblePlaces = []
        parentStates = []
        for move in self.possibleMoves:
            for i in range(10):
                for j in range(10):
                    tempBoard = GameBoard()
                    tempBoard.placeBlock(move, (i,j))
                    key = str(move) + str(i) +str(j)
                    stateID.append(key)
                    moves.append(move)
                    location.append((i,j))
                    # orphanNum = tempBoard.getOrphanSquares()
                    # orphanSquares.append(orphanNum)
                    score = tempBoard.getScore()-self.board.getScore()
                    scores.append(score)
                    places = self.board.possiblePlaces()
                    possiblePlaces.append(places)
                    maxHNum = tempBoard.maxHorizontal()
                    maxHorizontal.append(maxHNum)
                    maxVNum = tempBoard.maxVertical()
                    maxVertical.append(maxVNum)
                    numFull = tempBoard.totalSquares()
                    totalSquares.append(numFull)
                    numREmpty = tempBoard.emptyRows()
                    emptyRows.append(numREmpty)
                    numCEmpty = tempBoard.emptyColumns()
                    emptyColumns.append(numCEmpty)
                    # largestSpace = tempBoard.getOpenSpace()
                    # longestDFS.append(largestSpace)
                    # eval.append(score*10 - numFull + (numREmpty * 100)+places**3)
                    eval.append(places*2 + numREmpty + numCEmpty)
                    parentStates.append([])
        df = pd.DataFrame(list(zip(stateID, moves, location, possiblePlaces, scores, maxHorizontal, maxVertical, totalSquares, emptyRows,
                emptyColumns, eval, parentStates)),
                          columns=["StateID", "BlockID", "Location", "PossiblePlaces","Score","MaxHorizontal", "MaxVertical",
                                   "TotalSquares",
                                   "EmptyRows", "EmptyColumns", "eval", "ParentStates"])
        # df = pd.DataFrame(list(zip(stateID, moves, location,orphanSquares,maxHorizontal,maxVertical,totalSquares,emptyRows,emptyColumns,longestDFS,eval)),
        #     columns=["StateID", "BlockID","Location", "OrphanSquares", "MaxHorizontal", "MaxVertical", "TotalSquares",
        #              "EmptyRows", "EmptyColumns", "LongestDFS","eval"])
        return df

    def deepSearch(self, percentage, depth = 3):
        df = self.getPossibleStates()
        print(df)
        depth-=1
        for i in range(depth):
            newdf = pd.DataFrame(columns=["StateID", "BlockID", "Location", "PossiblePlaces","Score","MaxHorizontal", "MaxVertical",
                                   "TotalSquares",
                                   "EmptyRows", "EmptyColumns", "eval", "ParentStates"])
            topPercent = df.iloc[:int(len(df) * percentage)]
            for entry in range(len(topPercent)):
                tempBoard = self
                for state in newdf["ParentStates"]:
                    if len(state) !=0:
                        if tempBoard.place(topPercent.iloc[i]["BlockID"],topPercent.iloc[i]["Location"]):
                            tempBoard.update()
                            tempBoard.possibleMoves.remove(topPercent.iloc[i]["BlockID"])
                            continue
                        else:
                            entry['eval'] = 0
                    else:
                        state.append(entry)
                newPossibleStates = tempBoard.getPossibleStates()
                newdf = pd.concat([newdf, newPossibleStates],axis=0)
                # print(tempBoard.getPossibleStates())
        return newdf


def main():
    newGame = Game()

    board = newGame.board
    board.twoByTwo((4, 5))
    board.threeByThree((1, 1))
    board.threeByThree((1, 4))
    board.threeByThree((1, 7))
    board.threeByOne((1, 9))
    print(newGame.deepSearch(.01))
    # board.step4((1, 1))
    # board.step3((8, 1))
    # board.step2((1, 8))
    # board.oneByFive((5, 2))
    # board.oneByFive((6, 7))
    # print(board)
    # print(board.getScore())
    # board.updateBoard()
    # print(board)
    # print("Total orphan squares:", board.orphanSquares())
    # print("Maximum horizontal space:", board.maxHorizontal())
    # print("Maximum vertical space:", board.maxVertical())
    # print("Total squares:", board.totalSquares())
    # print("Empty rows:", board.emptyRows())
    # print("Empty columns:", board.emptyColumns())
    # print(newGame.checkLose())
    # sampleArr = [False, False]
    # boolArr = np.random.choice(sampleArr, size= (10,10))
    # print(board)
    # for i in range(10):
    #     for j in range(10):
    #         boolArr[i,j] = newGame.board.checkOneByFive((i,j))
    # print(boolArr)
    # newGame.place(1,(3,3))
    # newGame.printBoard()
if __name__ == "__main__":
    main()