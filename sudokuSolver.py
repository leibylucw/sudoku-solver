def createSudokuBoard(filePath):
	with open(filePath, 'r') as sudokuFile:
		sudokuBoard = [line.strip() for line in sudokuFile.readlines()]

	return sudokuBoard

def validateSudokuBoard(sudokuBoard):
	for row in sudokuBoard:
		if not all(character.isdigit() or character == '_' for character in row):
			return False

	return True
