def add_edge(adj, src, dest):

	adj[src].append(dest);
	adj[dest].append(src);
v = int(input("Enter number of vertices :"));
visited = [False for i in range(v)];
def BFS(adj, src, dest, v, pred, dist):


	queue = []

	for i in range(v):

		dist[i] = 1000000
		pred[i] = -1;

	visited[src] = True;
	dist[src] = 0;
	queue.append(src);

	# standard BFS algorithm
	while (len(queue) != 0):
		u = queue[0];
		queue.pop(0);
		for i in range(len(adj[u])):
		
			if (visited[adj[u][i]] == False):
				visited[adj[u][i]] = True;
				dist[adj[u][i]] = dist[u] + 1;
				pred[adj[u][i]] = u;
				queue.append(adj[u][i]);

			
				if (adj[u][i] == dest):
					return True;


	return False;


def printShortestDistance(adj, s, dest, v):
	

	pred=[0 for i in range(v)]
	dist=[0 for i in range(v)];

	if (BFS(adj, s, dest, v, pred, dist) == False):
		print("Given source and destination are not connected")

	path = []
	crawl = dest;
	crawl = dest;
	path.append(crawl);
	
	while (pred[crawl] != -1):
	    path.append(pred[crawl]);
	    crawl = pred[crawl];
	

	print("Shortest path length is : " + str(dist[dest]), end = '')
	print("\nPath is : : ")
	
	for i in range(len(path)-1, -1, -1):
	    print(path[i], end=' ');
	    
	print("\nVisited nodes : ");
	for i in range(v):
		if(visited[i]):
			print(" ",i),
if __name__=='__main__':
	
	

	adj = [[] for i in range(v)];

	e = int(input("Enter number of edges :"));
	i = 0;
	while(i < e):
	   x = int(input("Enter x : "));
	   y = int(input("Enter y : "));
	   add_edge(adj, x , y);
	   i = i + 1;
	source = int(input("Enter source :"));
	dest = int(input("Enter destination :"));
	
	printShortestDistance(adj, source, dest, v);
	
	       #    0----1
            #   |    |\
            #   |    | \
            #   |    |  \          
            #   2----3---4
