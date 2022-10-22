class QueensProblem:
    def __init__(self, num_of_queens):
        self.num_of_queens = num_of_queens
        self.chess_table = [[None for i in range(num_of_queens)] for j in range(num_of_queens)]


    def solve_queens_problem(self):
        if self.solve(0):
            self.print_queens()
        else:
            print("There is no solution")


    def solve(self, col_index):
        if col_index == self.num_of_queens:
            return True
        
        
        # traversing the rows
        for row_index in range(self.num_of_queens):
            if self.is_valid(row_index, col_index):
                self.chess_table[row_index][col_index] = 1
                # self.print_queens()
                if self.solve(col_index+1):
                    return True

                # backtrack
                self.chess_table[row_index][col_index] = 0
                # self.print_queens()

        return False
            

    def print_queens(self):
        for i in range(self.num_of_queens):
            for j in range(self.num_of_queens):
                if self.chess_table[i][j] == 1:
                    print("*", end="")
                else:
                    print("0", end="")
            print("\t")


    def is_valid(self, row_index, col_index):

        # horizontal check
        for item in range(col_index, -1, -1):
            if self.chess_table[row_index][item] == 1:
                return False


        # bottom right -> top left
        for i, j in zip(range(row_index, -1, -1), range(col_index, -1, -1)):
            if self.chess_table[i][j] == 1:
                return False


        # top right -> bottom left
        for i, j in zip(range(row_index, self.num_of_queens), range(col_index, -1, -1)):
            if self.chess_table[i][j] == 1:
                return False



        return True




if __name__ == "__main__":
    queensProblem = QueensProblem(4)
    queensProblem.solve_queens_problem()
