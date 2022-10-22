class HamiltonianProblem:
    def __init__(self, adjacencyMatrix):
        self.adjancy_matrix = adjacencyMatrix
        self.num_vertex = len(self.adjancy_matrix)
        self.hamiltonian_graph = [None]*self.num_vertex

    def hamiltonian_cycle(self):
        self.hamiltonian_graph[0] = 0
        if self.find_feasible_solution(1):
            print("Hamiltonian cycle exists!")
            self.showHamiltonianPath()
        else:
            print("Hamiltonian cycle does not exist!")

    def find_feasible_solution(self, position):
        # base case
        # if we have exhausted the list
        if position == self.num_vertex:
            last_position = self.hamiltonian_graph[position-1]
            first_position = self.hamiltonian_graph[0]
            if self.adjancy_matrix[first_position][last_position] == 1:
                return True
            else:
                return False

        for vertex in range(1, self.num_vertex):
            if self.is_feasible(vertex, position):
                self.hamiltonian_graph[position] = vertex
                if self.find_feasible_solution(position+1):
                    return True

                # backtrack
                self.hamiltonian_graph[position] = None

        return False

    def is_feasible(self, vertex, actual_position):
        # to be feasible the vertex being investigated should be have a connection to the vertex being chosen (actual_position)

        if self.adjancy_matrix[vertex][actual_position-1] == 0:
            return False

        if vertex in self.hamiltonian_graph:
            return False

        return True

    def showHamiltonianPath(self):
        print(self.hamiltonian_graph)


if __name__=="__main__":
    adjacency_matrix = [
        [0,1,1],
        [1,0,1],
        [1,1,0]
    ]

    hamiltonian = HamiltonianProblem(adjacency_matrix)
    hamiltonian.hamiltonian_cycle()