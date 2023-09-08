inputFile = input('Enter the name of file: ')
lines = []
with open(inputFile, 'r') as a:
	for line in a :
		lines.append(line.strip())

while True:
	print("The file has", len(lines), "lines.")
	if len(lines) == 0:
		break
	numberLine = int(input("Enter a line number [0 to quit]: "))
	if numberLine == 0:
		break
	elif numberLine > len(lines):
		print ("ERROR: line must be less than or equal to", len(lines))
	else:
		print(numberLine, ": ", lines[numberLine -1])
