def displayTextFile():
    words = dict()
    try:
        with open("theHungryCaterpillar.txt", "r") as files:
            reader = files.readlines()
            for line in reader:
                for word in line.split(" "):
                    word = word.lower()
                    while not word[-1].isalpha():
                        word = word[:-1]
                    if word not in words.keys():
                        words[word] = 1
                    else:
                        words[word] += 1
        print(words)
    except:
        print("File not found")
displayTextFile()