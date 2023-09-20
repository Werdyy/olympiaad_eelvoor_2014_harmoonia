import itertools

f = open("hargsis.txt", "r")
lines = f.readlines()

info = lines[0].split()

N = info[0]
K = int(info[1])

with open("hargsis.txt", "r") as f:
    next(f)
    prev_line = next(f).split()

    lineCount = -1

    for line in f:
        
        lineCount = lineCount + 1

        line = line.strip().split()
        print(prev_line)
        print(line)

        

        for index2 in range (0, K):
            match = []
            index1 = 0
            index2 = 1
            if int(prev_line[index1]) - int(prev_line[index2]) == int(line[index1]) - int(line[index2]):
                print("chomp")
                match.append(lineCount)
                match.append(index1 + 1)
                match.append(index2 + 1)
                print(match)

            index1 = index1 + 1
            index2 = index2 + 1


        prev_line = line  



