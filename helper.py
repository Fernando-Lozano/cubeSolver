# cube template
solvedCube = {
    "top":    [["y","y"],
               ["y","y"]],
    "front":  [["r","r"],
               ["r","r"]],
    "bottom": [["w","w"], 
               ["w","w"]],
    "back":   [["o","o"],
               ["o","o"]],
    "right":  [["g","g"],
               ["g","g"]],
    "left":   [["b","b"],
               ["b","b"]]
}


# prints cube to screen
def printCube(cube):
    for row in cube["top"]:
        print("      ", end="")
        for square in row:
            print(square, end="  ")
        print()
    for i in range(2):
        for square in cube["left"][i]:
            print(square, end="  ")
        for square in cube["front"][i]:
            print(square, end="  ")
        for square in cube["right"][i]:
            print(square, end="  ")
        print()
    for row in cube["bottom"]:
        print("      ", end="")
        for square in row:
            print(square, end="  ")
        print()
    for row in cube["back"]:
        print("      ", end="")
        for square in row:
            print(square, end="  ")
        print()


# shifts the rotating face
def face(top, bottom, clockWise):
    temp = top[1]
    
    if clockWise:
        top[1] = top[0]
        top[0] = bottom[0]
        bottom[0] = bottom[1]
        bottom[1] = temp
    else:
        top[1] = bottom[1]
        bottom[1] = bottom[0]
        bottom[0] = top[0]
        top[0] = temp


def rightTurn(cube, clockwise=True):
    # re-assign for easier read
    top = cube["top"]
    bottom = cube["bottom"]
    front = cube["front"]
    back = cube["back"]
    right = cube["right"]

    # move rotating face colors
    face(right[0], right[1], clockwise)

    # move edge colors
    temp1 = front[0][1]
    temp2 = front[1][1]
    if clockwise:
        # move in cube notation
        move = "r"

        # move first set of relative squares
        front[0][1] = bottom[0][1]
        bottom[0][1] = back[0][1]
        back[0][1] = top[0][1]
        top[0][1] = temp1
        # move second set of relative squares
        front[1][1] = bottom[1][1]
        bottom[1][1] = back[1][1]
        back[1][1] = top[1][1]
        top[1][1] = temp2
    else:
        # move in cube notation
        move = "R"

        # move first set of relative squares
        front[0][1] = top[0][1]
        top[0][1] = back[0][1]
        back[0][1] = bottom[0][1]
        bottom[0][1] = temp1
        # move second set of relative squares
        front[1][1] = top[1][1]
        top[1][1] = back[1][1]
        back[1][1] = bottom[1][1]
        bottom[1][1] = temp2
        # return move in cube notation
    return move

def bottomTurn(cube, clockwise = True):
    # re-assign for easier read
    bottom = cube["bottom"]
    front = cube["front"]
    back = cube["back"]
    left = cube["left"]
    right = cube["right"]

    # move rotating face colors
    face(bottom[0], bottom[1], clockwise)

    # move edge colors
    temp1 = front[1][0]
    temp2 = front[1][1]
    if clockwise:
        # move in cube notation
        move = "d"

        # move first set of relative squares
        front[1][0] = left[1][0]
        left[1][0] = back[0][1]
        back[0][1] = right[1][0]
        right[1][0] = temp1
        # move second set of relative squares
        front[1][1] = left[1][1]
        left[1][1] = back[0][0]
        back[0][0] = right[1][1]
        right[1][1] = temp2
    else:
        # move in cube notation
        move = "D"

        # move first set of relative squares
        front[1][0] = right[1][0]
        right[1][0] = back[0][1]
        back[0][1] = left[1][0]
        left[1][0] = temp1
        # move second set of relative squares
        front[1][1] = right[1][1]
        right[1][1] = back[0][0]
        back[0][0] = left[1][1]
        left[1][1] = temp2
    # return move in cube notation
    return move

def backTurn(cube, clockwise = True):
    # re-assign for easier read
    top = cube["top"]
    bottom = cube["bottom"]
    back = cube["back"]
    left = cube["left"]
    right = cube["right"]

    # move rotating face colors
    face(back[0], back[1], clockwise)

    # move edge colors
    temp1 = top[0][0]
    temp2 = top[0][1]
    if clockwise:
        # move in cube notation
        move = "b"

        # move first set of relative squares
        top[0][0] = right[0][1]
        right[0][1] = bottom[1][1]
        bottom[1][1] = left[1][0]
        left[1][0] = temp1
        # move second set of relative squares
        top[0][1] = right[1][1]
        right[1][1] = bottom[1][0]
        bottom[1][0] = left[0][0]
        left[0][0] = temp2
    else:
        # move in cube notation
        move = "B"

        # move first set of relative squares
        top[0][0] = left[1][0]
        left[1][0] = bottom[1][1]
        bottom[1][1] = right[0][1]
        right[0][1] = temp1
        # move second set of relative squares
        top[0][1] = left[0][0]
        left[0][0] = bottom[1][0]
        bottom[1][0] = right[1][1]
        right[1][1] = temp2
        # return move in cube notation
    return move

# checks if two cubes are match
def isMatch(cube1, cube2):
    for face in cube1:
        for i, row in enumerate(cube1[face]):
            for j, color in enumerate(row):
                if color != cube2[face][i][j]:
                    return False
    return True

# scrambles cube
def scrambler(cube, algorithm):
    for letter in algorithm:
        if letter == "r":
            rightTurn(cube)
        elif letter == "R":
            rightTurn(cube, False)
        elif letter == "d":
            bottomTurn(cube)
        elif letter == "D":
            bottomTurn(cube, False)
        elif letter == "b":
            backTurn(cube)
        else:
            backTurn(cube, False)
