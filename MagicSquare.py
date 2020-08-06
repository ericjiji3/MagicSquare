#  File: MagicSquare.py

#  Description:

#  Student's Name: Eric Ji

#  Student's UT EID: ej6638

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 9/2/19

#  Date Last Modified: 9/6/19

def main():
    x = int(input("Enter an odd number 1 or greater: "))
    #checks whether user input is odd number 1 or greater
    while x < 1 or x % 2 == 0:
        if x < 1:
            x = int(input("That is less than 1, try again: "))
        if x % 2 == 0:
            x = int(input("That is not an odd number, try again: "))
    array = make_square(x)
    print_square(array)
    check_square(array)

def make_square(n):
    num = 1
    row = n - 1
    col = n//2
    #creates 2D list that has a dimension of n x n
    a = [[0 for i in range(n)] for j in range(n)]
    #places a 1 in the middle of the bottom row
    a[row][col] = num
    #places value to the right and down of the square
    while num < n*n:
        num = num + 1
        row = row + 1
        col = col + 1
        if row>=n:
            row=0
        if col >= n:
            col = 0
        if a[row][col] != 0:
            row = row - 2
            col = col - 1
        a[row][col] = num
    return a

def check_square(magic_square):
    sum = 0
    tow1 = 0
    sum1 = 0
    sum2 = 0
    size = len(magic_square)
    tow2 = size - 1
    right = True
    total = size * (size * size + 1) / 2
    #checks the sum of the column
    for c in range(size):
        for r in range(size):
            sum += magic_square[r][c]
        if sum != total:
            right = False
        sum = 0
    #checks the sum of the row
    for x in range(size):
        for y in range(size):
            sum += magic_square[x][y]
        if sum != total:
            right = False
        sum = 0
    #checks sum of first diagonal
    for a in range(size):
        sum1 += magic_square[tow1][a]
        tow1 += 1
    if sum1 != total:
            right = False
    #checks sum of second diagonal
    for b in range(size):
        sum2 += magic_square[tow2][b]
        tow2 -= 1
    if sum2 != total:
            right = False


    #Checks that the sum is in every row, column, and diagonal
    if right == True:
        print("This is a magical square and the canonical sum is ",total)
    if right == False:
        print("This is not a magical square")



def print_square(magic_square):
    y = len(magic_square)
    #Creates a space in between each number in the list
    for i in range(y):
        for j in range(y):
            print(magic_square[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()








