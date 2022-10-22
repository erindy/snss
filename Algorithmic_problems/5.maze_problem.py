
class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.max_len = len(self.maze)
        self.x_moves = [0, 1]
        self.y_moves = [1, 0]

    def solve_maze(self):
        self.maze[0][0] = 1
        if self.solve(2, 0, 0):
            print("there is a solution")
            print(self.maze)
        else:
            print("no solution found")

    def solve(self, step, x, y):
        # base case
        if x>=self.max_len-1 and y>=self.max_len-1:
            return True


        for i in range(len(self.x_moves)):

            x_next = x + self.x_moves[i]
            y_next = y + self.y_moves[i]


            if self.is_valid(x_next, y_next):

                self.maze[x_next][y_next]=step
                if self.solve(step+1, x_next, y_next):
                    return True
                self.maze[x_next][y_next]=0

    def is_valid(self, x_next, y_next):
        if x_next < 0 or x_next >= self.max_len:
            return False

        if y_next < 0 or y_next >= self.max_len:
            return False

        if self.maze[x_next][y_next]==-1:
            return False

        return True


if __name__=="__main__":
    maze = [
        [ 0,  0,  0,  0,  0],
        [-1, -1, -1,  0, -1],
        [ 0,  0,  1,  0,  0],
        [ 0, -1,  0, -1,  0],
        [-1,  0,  0,  0,  0]
    ]

    maze_solver = MazeSolver(maze)
    maze_solver.solve_maze()