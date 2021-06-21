# class RiverGraph:
#     def __init__(self):
#         self.checkRiverSize = []
#         self.visited = [ [False] * len(self.checkRiverSize[0]) ] * len( self.checkRiverSize )
#         self.sizes = []
#         for i in range(len(self.checkRiverSize)-1):
#             for j in range(len(self.checkRiverSize[i])-1):
#                 self.visited[i][j]

    
#     def find(self):
#         for i in range(len(self.checkRiverSize)-1):
#             for j in range(len(self.checkRiverSize[i])-1):
#                 if self.visited[i][j]:
#                     continue
#                 else:
#                     pass

#     def traverseThroughRiver(self, i,j):
#         self.checkRiverSize = 0;

class RiverSize:

    def __init__(self):
        self.checkRiverSize = []
        self.visited = []
        
        
    def riverSizes(self, matrix):
        self.visited = [[False for value in matrix] for row in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if self.visited[i][j]:   
                    continue
                self.traverseThroughRiver(i, j, matrix)
        return self.checkRiverSize


    def traverseThroughRiver(self, i, j, matrix):
        currentRiverSize = 0
        nodesToExplore = [[i, j]]
        while len(nodesToExplore):
            currentNode = nodesToExplore.pop()
            i = currentNode[0]
            j = currentNode[1]
            if self.visited[i][j]:
                continue
            self.visited[i][j] = True
            if matrix[i][j] == 0:
                continue
            currentRiverSize += 1
            unvisitedNeighbors = self.getUnvisitedNeighbors(i,j,matrix)
            for neighbor in unvisitedNeighbors:
                nodesToExplore.append(neighbor)
        if currentRiverSize > 0:
            self.checkRiverSize.append(currentRiverSize)


    def getUnvisitedNeighbors(self, i, j, matrix):

        unvisitedNeighbors = []
        if i > 0 and not self.visited[i - 1][j]:
            unvisitedNeighbors.append([i-1,j])

        if i < len(matrix) - 1 and not self.visited[i + 1][j]:
            unvisitedNeighbors.append([i+1, j])

        if j > 0 and not self.visited[i][j -1 ]:
            unvisitedNeighbors.append([i,j-1])
        
        if j < len(matrix[0]) - 1 and not self.visited[i][j+1]:
            unvisitedNeighbors.append([i,j+1])
        return unvisitedNeighbors




island =[
  [1, 1, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]


riv = RiverSize()
adjectestRiver = riv.riverSizes(island)
print(adjectestRiver)
  