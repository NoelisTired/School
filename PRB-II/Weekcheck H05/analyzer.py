lineCount = 0
wordCount = 0
with open("recording.txt", "r") as f:
    for line in f:
        lineCount += 1
        wordCount += len(line.split())
    open('report.txt', 'w').write(f"Aantal regels: {lineCount}\nAantal woorden: {wordCount}")
print("einde")