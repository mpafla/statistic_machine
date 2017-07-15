from views.InputTerminalView import*
import os
from pathlib import Path


class InputController:

	file_path_prefix = Path(os.path.abspath("")).parent / "data" 
	file_path = None

	def __init__(self):
		self.view = InputTerminalView() 
		
	def getInput(self, model):
		valid_filename = False
		while (valid_filename == False):
			filename = self.view.getFilename()
			self.file_path = self.file_path_prefix / filename
			if os.path.isfile(str(self.file_path)):
				valid_filename = True
			else:
				print ("File could not be found.\n")
		model.setFilePath(str(self.file_path))
		try:
			model.loadDataFrame()
		except : 
			print("Data file could not be loaded.")
			return False
		else: 
			return True