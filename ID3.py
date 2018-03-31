class ID3():
	#INITIALIZE THE CLASS WITH THE INPUT OF OUTCOME AND TRAINING ATTRIBUTE LIST
	def __init__(self,positive_outcome,no_of_attributes,result_list,attribute_list):
		#FIND OUT WHAT IS LISTED AS AN POSITIVE OUTCOME
		self.positive_outcome = positive_outcome
		#INITIALIZE THE RESULT LIST, ATTRIBUTE LIST AND THE LENGTH OF THE DATASET TO BE TRAINED UPON
		self.result_list = result_list
		self.attribute_list = attribute_list
		self.training_set_len = len(result_list)
		self.attribute_len = no_of_attributes
		