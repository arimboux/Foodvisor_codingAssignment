#!usr-/bin/python
# -*- coding: utf-8 -*-

from node import Node

class Database(object):

	def __init__(self):
		self.nodes = {"core": Node(None)}
		self.extracts = {}

	def add_nodes(self, new_nodes):

		for node_pair in new_nodes:
			node_parent = node_pair[1]
			node_child = node_pair[0]

			if node_parent in self.nodes:
				self.nodes[node_child] = Node(self.nodes[node_parent])
				self.nodes[node_parent].new_child = True
			else:
				if node_parent == None:
					# New root node replace the abstract one created in constructor
					self.nodes[node_child] = self.nodes.pop("core")
				else:
					print("This node does not exist and can't be a parent for a new node")

	def add_extract(self, extract_dict):

		self.extracts = extract_dict
		for nodeId in self.nodes:
			self.nodes[nodeId].new_child = False

	def get_extract_status(self):

		status = ['valid', 'granularity_staged', 'coverage_staged', 'invalid']
		result_dict = {}

		for extract in self.extracts:
			results = []
			for nodeId in self.extracts[extract]:
				if nodeId not in self.nodes:
					results.append(3)
				#Check coverage change
				elif self.nodes[nodeId].query_parent():
					results.append(2)
				#Check granularity change
				elif self.nodes[nodeId].new_child:
					results.append(1)
				elif nodeId in self.nodes:
					results.append(0)

			if len(results) > 0:
				result_dict[extract] = status[max(results)]
			else:
				result_dict[extract] = status[0]

		return result_dict
