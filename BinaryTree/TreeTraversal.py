import Queue

class Graph:
	def __init__(self, number_of_vertices):
		self.number_of_vertices = number_of_vertices
		self.vertex_details = {}
		self.visited = {}
		
	def add_edge(self, vertex_label, edge):
		if self.vertex_details.has_key(vertex_label):
			self.vertex_details[vertex_label].append(edge)
		else:
			self.vertex_details[vertex_label] = []
			self.vertex_details[vertex_label].append(edge)
			self.visited[vertex_label] = 0
			
	def bfs(self, starting_vertex):
		print "Starting breath first search from vertex: ", starting_vertex
		bfs_queue = Queue.Queue()

		bfs_trace = []
		bfs_queue.put(starting_vertex)
		self.visited[starting_vertex] = 1

		while(not bfs_queue.empty()):
			current_vertex = bfs_queue.get()
			bfs_trace.append(current_vertex)
			adjacent_vertices = self.vertex_details[current_vertex]
			for adjacent_vertex in adjacent_vertices:
				if self.visited[adjacent_vertex] == 0:
					bfs_queue.put(adjacent_vertex)
					self.visited[adjacent_vertex] = 1

		return bfs_trace

	def dfs(self, vertex):
		self.visited[vertex] = 1
		print vertex," ",
		adjacent_vertices = self.vertex_details[vertex]
		for adjacent_vertex in adjacent_vertices:
			if self.visited[adjacent_vertex] == 0:
				self.dfs(adjacent_vertex)

	def print_bfs(self, bfs_trace):
		print bfs_trace

def main():
	g = Graph(4)
	g.add_edge(0, 1);
	g.add_edge(0, 2);
	g.add_edge(1, 2);
	g.add_edge(2, 0);
	g.add_edge(2, 3);
	g.add_edge(3, 3);

	# bfs_trace = g.bfs(2)
	# g.print_bfs(bfs_trace)
	g.dfs(2)

if __name__ == '__main__':
	main()


