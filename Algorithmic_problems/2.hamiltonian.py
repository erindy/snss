class HamiltonianProblem:
    def __init__(self, adjacencyMatrix):
        self.num_of_vertexes = len(adjacencyMatrix)
        self.hamiltonian_path = [None]*self.num_of_vertexes # path to be constructed
        self.adjacencyMatrix = adjacencyMatrix


    def hamiltonian_cycle(self):
        self.hamiltonian_path[0] = 0

        if not self.find_feasible_solution(1):
            print("No feasible solution found...")
        else:
            self.showHamiltonianPath()

    def find_feasible_solution(self, position):
        # base case
        # if position is same as num of vertexes means that recursion has run its course and we need to check
        if position==self.num_of_vertexes:
            first_vertex = self.hamiltonian_path[0]
            last_vertex = self.hamiltonian_path[self.num_of_vertexes-1]
            if self.adjacencyMatrix[first_vertex][last_vertex] == 1:
                return True
            else:
                return False


        for vertex_index in range(1, self.num_of_vertexes):
            if self.is_feasible(vertex_index, position):
                self.hamiltonian_path[position] = vertex_index
                if self.find_feasible_solution(position+1):
                    return True
                
                # Backtrack, backtracking happens here since if it gets at this point it means it did not return
                # true and the next backwards cycle will start
        
        return False

    def is_feasible(self, vertex, actual_position):
        # first criteria: whether the two nodes are connected?
        if self.adjacencyMatrix[self.hamiltonian_path[actual_position-1]][vertex] == 0:
            return False

        # second criteria: whether we have already added the given node
        if vertex in self.hamiltonian_path:
            return False

        return True

    def showHamiltonianPath(self):
        print("Hamiltonian cycle exists: ")
        for i in range(self.num_of_vertexes):
            print(self.hamiltonian_path[i]),

        print(self.hamiltonian_path[0])


if __name__=="__main__":
    adjacency_matrix = [
        [0,1,1],
        [1,0,1],
        [1,1,0]
    ]

    hamiltonian = HamiltonianProblem(adjacency_matrix)
    hamiltonian.hamiltonian_cycle()