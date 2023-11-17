message = input('Encoding or decoding?\n')

if message == 'encoding':
    message = input('Enter the message\n')
    cipher = ''
    for character in message:
        if (character == 'A') or (character == 'a'):
            cipher = cipher + 'D'
        elif (character == 'B') or (character == 'b'):
            cipher = cipher + 'E'
        elif (character == 'C') or (character == 'c'):
            cipher = cipher + 'F'
        elif (character == 'D') or (character == 'd'):
            cipher = cipher + 'G'
        elif (character == 'E') or (character == 'e'):
            cipher = cipher + 'H'
        elif (character == 'F') or (character == 'f'):
            cipher = cipher + 'I'
        elif (character == 'G') or (character == 'g'):
            cipher = cipher + 'J'
        elif (character == 'H') or (character == 'h'):
            cipher = cipher + 'K'
        elif (character == 'I') or (character == 'i'):
            cipher = cipher + 'L'
        elif (character == 'J') or (character == 'J'):
            cipher += 'M'
        elif (character == 'K') or (character == 'k'):
            cipher = cipher + 'N'
        elif (character == 'L') or (character == 'l'):
            cipher = cipher + 'O'
        elif (character == 'M') or (character == 'm'):
            cipher += 'P'
        elif (character == 'N') or (character == 'n'):
            cipher = cipher + 'Q'
        elif (character == 'O') or (character == 'o'):
            cipher = cipher + 'R'
        elif (character == 'P') or (character == 'p'):
            cipher = cipher + 'S'
        elif (character == 'Q') or (character == 'q'):
            cipher = cipher + 'T'
        elif (character == 'R') or (character == 'r'):
            cipher = cipher + 'U'
        elif (character == 'S') or (character == 's'):
            cipher = cipher + 'V'
        elif (character == 'T') or (character == 't'):
            cipher = cipher + 'W'
        elif (character == 'U') or (character == 'u'):
            cipher = cipher + 'X'
        elif (character == 'V') or (character == 'v'):
            cipher = cipher + 'Y'
        elif (character == 'W') or (character == 'w'):
            cipher = cipher + 'Z'
        elif (character == 'X') or (character == 'x'):
            cipher = cipher + 'A'
        elif (character == 'Y') or (character == 'y'):
            cipher = cipher + 'B'
        elif (character == 'Z') or (character == 'z'):
            cipher = cipher + 'C'
        else:
            cipher = cipher +character
    print(cipher)

else:
    message = input('Enter the message\n')
    cipher = ''
    for character in message:
        if (character == 'A') or (character == 'a'):
            cipher = cipher + 'X'
        elif (character == 'B') or (character == 'b'):
            cipher = cipher + 'Y'
        elif (character == 'C') or (character == 'c'):
            cipher = cipher + 'Z'
        elif (character == 'D') or (character == 'd'):
            cipher = cipher + 'A'
        elif (character == 'E') or (character == 'e'):
            cipher = cipher + 'B'
        elif (character == 'F') or (character == 'f'):
            cipher = cipher + 'C'
        elif (character == 'G') or (character == 'g'):
            cipher = cipher + 'D'
        elif (character == 'H') or (character == 'h'):
            cipher = cipher + 'E'
        elif (character == 'I') or (character == 'i'):
            cipher = cipher + 'F'
        elif (character == 'J') or (character == 'J'):
            cipher = cipher + 'G'
        elif (character == 'K') or (character == 'k'):
            cipher = cipher + 'H'
        elif (character == 'L') or (character == 'l'):
            cipher = cipher + 'I'
        elif (character == 'M') or (character == 'm'):
            cipher = cipher + 'J'
        elif (character == 'N') or (character == 'n'):
            cipher = cipher + 'K'
        elif (character == 'O') or (character == 'o'):
            cipher = cipher + 'L'
        elif (character == 'P') or (character == 'p'):
            cipher = cipher + 'M'
        elif (character == 'Q') or (character == 'q'):
            cipher = cipher + 'N'
        elif (character == 'R') or (character == 'r'):
            cipher = cipher + 'O'
        elif (character == 'S') or (character == 's'):
            cipher = cipher + 'P'
        elif (character == 'T') or (character == 't'):
            cipher = cipher + 'Q'
        elif (character == 'U') or (character == 'u'):
            cipher = cipher + 'R'
        elif (character == 'V') or (character == 'v'):
            cipher = cipher + 'S'
        elif (character == 'W') or (character == 'w'):
            cipher = cipher + 'T'
        elif (character == 'X') or (character == 'x'):
            cipher = cipher + 'U'
        elif (character == 'Y') or (character == 'y'):
            cipher = cipher + 'V'
        elif (character == 'Z') or (character == 'z'):
            cipher = cipher + 'W'
        else:
            cipher = cipher + character
    print(cipher)