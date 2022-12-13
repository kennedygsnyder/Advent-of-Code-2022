with open('input.txt') as f:
    lines = f.readlines()
    line = lines[0]

    marker_length = 14

    for i in range(len(line)-marker_length):
        chars = []
        for j in range(marker_length):
            chars.append(line[i+j])
        print(chars)

        if len(chars) == len(set(chars)):
            print(i+14)
            break
