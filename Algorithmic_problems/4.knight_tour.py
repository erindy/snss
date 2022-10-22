class KnightTourProblem:
    def __init__(self, board_size):
        # self.chess_board = [[None]*col for i in range(row)]
        self.board_size = board_size
        self.x_moves = [2, 1, -1, -2, -2, -1,  1,  2]
        self.y_moves = [1, 2,  2,  1, -1, -2, -2, -1]
        self.solution_matrix = [[-1 for x in range(board_size)] for x in range(board_size)]


    def solve_knight_tour_problem(self):
        self.solution_matrix[0][0] = 0

        if self.solve_problem(1,0,0):
            self.show_solution()
        else:
            print("No feasible solution")

    def solve_problem(self, step_count, x, y):
        # base case
        # if the step count is equal to the total number of boardsize then you have seen all solutions
        if step_count == self.board_size * self.board_size:
            return True

        for i in range(8):
            next_x = x + self.x_moves[i]
            next_y = y + self.y_moves[i]

            if self.is_valid_move(next_x, next_y):
                self.solution_matrix[next_x][next_y] = step_count
                if self.solve_problem(step_count+1, next_x, next_y):
                    return True

                self.solution_matrix[next_x][next_y] = -1

        return False




    def show_solution(self):
        print(self.solution_matrix)
        print(True)

    def is_valid_move(self, next_x, next_y):
        if next_x >= self.board_size or next_x < 0:
            return False

        if next_y >= self.board_size or next_y < 0:
            return False

        if self.solution_matrix[next_x][next_y] > -1:
            return False

        return True



if __name__=="__main__":
    knight = KnightTourProblem(8)
    knight.solve_knight_tour_problem()


