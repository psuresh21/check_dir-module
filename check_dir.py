class check_dir:	
	def listy(self,item):
		self._listy = item
		listy = [print("list - ✔") for l in dir(list) if (self._listy).__eq__(l)]
		return listy
	
	def dictionary(self,item):
		self._dictionary = item
		dictionary = [print("dictionary - ✔") for l in dir(dict) if (self._dictionary).__eq__(l)]
		return dictionary
	
	def tuples(self,item):
		self._tuples = item
		tuples = [print("tuples - ✔") for l in dir(tuple) if (self._tuples).__eq__(l)]
		return tuples
	
	def strings(self,item):
		self._strings = item
		strings = [print("strings - ✔") for l in dir(str) if (self._strings).__eq__(l)]
		return strings
	
	def numbers(self,item):
		self._numbers = item
		numbers = [print("numbers - ✔") for l in dir(int) if (self._numbers).__eq__(l)]
		return numbers
	
	def floats(self,item):
		self._floats = item
		floats = [print("floats - ✔") for l in dir(float) if (self._floats).__eq__(l)]
		return floats
	
	def checkall(self,item):
		self._checkall = self.listy(item),self.floats(item),self.strings(item)
		self._checkall += self.numbers(item),self.dictionary(item),self.tuples(item)
		return self._checkall

check_dir = check_attr()

