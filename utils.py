def read_textfile(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.readlines()]
		return lines

def raw_textfile(filename):
	with open(filename) as f:
		lines = [line for line in f.readlines()]
		return lines


class Directory:
	def __init__(self, name, parent):
		self.name = name
		self.parent = parent
		self.content = {}
		self.size = 0
	
	def addFile(self, name, size):
		self.content[name] = size

	def addDirectory(self, name, parent):
		self.content[name] = Directory(name, parent)

	def calculateSize(self):
		size = 0
		for value in self.content.values():
			if isinstance(value, int):
				size += value
			else:
				size += value.calculateSize()
		self.size = size
		return size
