'''
Vertex class
'''
class Vertex:
	def __init__(self, node):
		self.id = node
		self.adjacent = {}

	def __str__(self):
		return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

	def add_neighbor(self, neighbor, weight=0):
		self.adjacent[neighbor] = weight
		#add the next node along with the weight of the node 

	def get_connections(self):
		return self.adjacent.keys()
		# ??  check what edges  the current node is connected to

	def get_id(self):
		return self.id
		#getting the name of the node eg: A, B, etc 

	def get_weight(self, neighbor):
		return self.adjacent[neighbour]
		#weight of getting to the adjacent vertex
		# we will get this from our map problem 

'''
Graph class
'''

class Graph(object):
	def __init__(start_node=None):
		self.start = start_node
		self.nodes = []
		self.edges = [] #change?
		#self.weight - how to represent weights?

	def add_node():
		return
		#add a new node to graph

	def add_edge():
		return
		#add a new edge to graph

	def printGraph():
		return
		#print all nodes and edges

	def get_weight():
		return
		#return weight given edge (may change?)

print("Something")
