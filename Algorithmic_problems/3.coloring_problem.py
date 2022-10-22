class ColoringProblem:

    """
    Validity check
    1. check the adjacent vertex has same color


    """

    def __init__(self, num_of_verteces, num_of_colors, graph_matrix):
        self.num_vertices = num_of_verteces
        self.color_vertex_graph = [None]*num_of_verteces # index of the list represents the vertex
        self.color_list = [i for i in range(1, num_of_colors+1)]
        self.graph_matrix = graph_matrix


    def solve_coloring_problem(self, color=1):
        self.color_vertex_graph[0] = color
        if self.solve_c_util(1):
            print(self.color_vertex_graph)
            return True
        else:
            print("sorry no solution")
            return False

    def solve_c_util(self, current_vertex):
        # base case
        # when you have run out of verteces to color
        if self.num_vertices == current_vertex:
            # possible other checks
            return True

        for color in self.color_list:
            if self.is_valid(color, current_vertex):
                self.color_vertex_graph[current_vertex] = color
                if self.solve_c_util(current_vertex+1):
                    return True

                # backtrack
                self.color_vertex_graph[current_vertex] = None

        return False

    def is_valid(self, current_color, current_vertex):

        # check the neighbors of the current vertex whether they have same color, exclude the uncolored ones

        for vertex in range(0, current_vertex):
            # check if it is connected
            # if yes then compare colors
            # if not skip

            if self.color_vertex_graph[vertex] == current_color and  self.graph_matrix[vertex][current_vertex] == 1:
                return False

        return True



if __name__=="__main__":
    adjacency_matrix = [
        [0,1,0,1,0],
        [1,0,1,1,1],
        [0,1,0,1,0],
        [1,1,1,0,1],
        [0,0,0,1,0]
    ]

    coloring_problem = ColoringProblem(len(adjacency_matrix), 3, adjacency_matrix)
    print(coloring_problem.solve_coloring_problem())




