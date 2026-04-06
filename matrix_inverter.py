from fractions import Fraction

def get_matrix():
    """This fucniton lets the user input their own matrices"""
    n = int(input("Enter size of matrix n (nxn): "))
    matrix = []
    for i in range(n):
        while True:
            row_input = input(f"Enter row {i+1} (space-separated): ")
            parts = row_input.split()

            if len(parts) != n:
                print("Incorrect number of elements. Try again.")
                continue

            try:
                row = [Fraction(x) for x in parts]
                matrix.append(row)
                break
            except:
                print("Invalid input. Use numbers or fractions like 1/2.")
    return matrix

def print_matrix(matrix):
    """This function takes a matrix, cleans it up, and displays"""
    
    for row in matrix:
        for num in row:
            print(Fraction(num).limit_denominator(), end=" ")
        print()

def identity_matrix(n):
    """this function creates an nxn identity matrix"""
    
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix
    
def swap_rows(matrix, i, j):
    """This function swaps rows in matrices"""
    
    matrix[i], matrix[j] = matrix[j], matrix[i]

def scale_row(matrix, i, scalar):
    """this function multiplies a row bya  scalar"""
    
    for j in range(len(matrix[i])):
        matrix[i][j] = scalar * matrix[i][j]

def add_rows(matrix, i, j, factor):
    """replaces row i with row i + scalar * row j"""
    
    for k in range(len(matrix[i])):
        matrix[i][k] += factor * matrix[j][k]

def augment_matrix(matrix):
    """This function takes an nxn coeffecient amtrix and augments it by matching it with
    its corresponding identity matrix"""
    
    n = len(matrix)
    I = identity_matrix(n)
    augmented = []
    for i in range(len(matrix)):
        augmented.append(matrix[i] + I[i])
    return augmented

def extract_inverse(aug_matrix):
    n = len(aug_matrix)
    inverse = []
    for row in aug_matrix:
        inverse.append(row[n:])
    return inverse

def invert_matrix(matrix):
    """This fuction uses all elementary row operations on the auugmented
    matrix to produce the inverse (applicable for all nxn matrices)"""
    
    aug_matrix = augment_matrix(matrix)
    n = len(matrix)
    
    # makes pivot = 1
    for i in range(n):
        pivot = aug_matrix[i][i]
        
        if pivot == 0:
            for k in range(i+1, n):
                if aug_matrix[k][i] != 0:
                    swap_rows(aug_matrix, i, k)
                    break
            pivot = aug_matrix[i][i]
            
            if pivot == 0:
                raise ValueError("Matrix is not invertible")
        scale_row(aug_matrix, i, 1 / pivot)
        
        # uses pivot to eliminate other columns
        for j in range(n):
            if j != i:
                factor = -aug_matrix[j][i]
                add_rows(aug_matrix, j, i, factor)
    inverse = extract_inverse(aug_matrix)
    return inverse



def main():
    matrix = get_matrix()
    print_matrix(invert_matrix(matrix))

    
main()