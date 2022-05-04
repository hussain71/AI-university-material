graph = {}

all_nodes = input('Enter All Nodes Availaible - ').split(' ')
for i in all_nodes:
    tmp = input(f'{i} : ')
    if (tmp):
        graph[i] = tmp.split(' ')
    else:
        graph[i] = []

print()
start_node = input('Enter Start Node :- ')
end_node = input('Enter Goal Node :- ')
print()
 
visited = []
stack = []
 
def dfs(visited, graph, node):
    visited.append(node)
    stack.append(node)
   
    nodes_explored = 0
   
    while stack:
      nodes_explored += 1
      m = stack.pop()
      print (m, end = " ")
     
      if (m == end_node):
        print()
        print('Node Found !!')
        print()
        print('Total Nodes Explored =', nodes_explored)
        print()
        break
 
      for neighbor in graph[m]:
        if neighbor not in visited:
          visited.append(neighbor)
          stack.append(neighbor)

print("____DFS____\n")
dfs(visited, graph, list(graph.keys())[0])
 
print()

    #            0-------1
 	#            |       |
	#            |       |
	#            2       3
	#           / \      
	#          /   \      
	#         4-----5   
	#         | \   |
	#         |  \  |    
	#         |   \ |      
	#         |    \|    
	#         7-----6
