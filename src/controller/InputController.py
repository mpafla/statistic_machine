from views.InputTerminalView import*

class InputController:

	def __init__(self):
		self.view = InputTerminalView() 
		
	def getInput(self, model):
		filename = self.view.getFilename()
		model.setFilename(filename)
		if (model.loadDataFrame()):
			return True
		else:
			self.view.error("loadDataFrame")
			return False