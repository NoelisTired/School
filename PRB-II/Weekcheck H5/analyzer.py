line_count = 0
word_count = 0
for line in open("recording.txt", "r").readlines():
    line_count += 1
    word_count += len(line.split())

open('report.txt', 'w').write(f"Aantal regels: {line_count}\nAantal woorden: {word_count}")