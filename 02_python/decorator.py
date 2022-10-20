def announce(f):
	def wrapper():
		print("++++++++++++++++++++++++++++")
		f()
		print("++++++++++++++++++++++++++++")
	return wrapper

@announce
def hello():
	print("Hello, World!")

hello()


def incomplete(lost_piece):
	def falacy():
		print("GOD IS")
		lost_piece()
		print("DEAD")
	return falacy

@incomplete
def truth():
	print("NOT")

truth()
