with open("recording.txt", "r") as f:
    for lines in f.read():
        if lines != "\n":
            print(lines)
            
