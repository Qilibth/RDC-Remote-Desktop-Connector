import json

class backendClass:

	def __init__(self):
		self.userState = self.returnData('logState')

	# RETURNS DATA FROM THE JSON FILE
	def returnData(self, pwId):
		with open('LogF/logData.json', 'r') as dataFile:
			self.data = json.load(dataFile)

			if self.data['isLogged'] == True:
				if pwId == 'id':
					return self.data['userID']
				elif pwId == 'pw':
					return self.data['userPW']
				elif pwId == 'idPw':
					return self.data['userID'], self.data['userPW']
				elif pwId == 'logState':
					return self.data['isLogged']
			else:
				return False
