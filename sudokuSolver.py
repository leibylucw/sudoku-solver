def createSudokuBoard(filePath):
	with open(filePath, 'r') as sudokuFile:
		sudokuBoard = [line.strip() for line in sudokuFile.readlines()]

	return sudokuBoard
