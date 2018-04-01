import math
class ID3():
 #INITIALIZE THE CLASS WITH THE INPUT OF OUTCOME AND TRAINING ATTRIBUTE LIST
 def __init__(self,training_list):
  #FIND OUT WHAT IS LISTED AS AN POSITIVE OUTCOME
  self.positive_outcome = positive_outcome
  #INITIALIZE THE RESULT LIST, ATTRIBUTE LIST AND THE LENGTH OF THE DATASET TO BE TRAINED UPON
  self.result_list = result_list
  self.attribute_list = attribute_list
  self.training_set_len = len(result_list)
  self.attribute_len = no_of_attributes


 #THIS METHOD WILL CALCULATE THE ENTROPY
 def entropy(no_of_positive_outcomes,no_of_negative_outcomes):

  #CALCULATE THE PROPORTIONS OF POSITIVE AND NEGATIVE
  pos_proportion = no_of_positive_outcomes/(no_of_positive_outcomes+no_of_negative_outcomes)
  neg_proportion = no_of_negative_outcomes/(no_of_positive_outcomes+no_of_negative_outcomes)

  #ENTROPY CALCULATION
  s = - pos_proportion*(math.log(pos_proportion,2)) - neg_proportion*(math.log(neg_proportion,2))
  return(s)

 #THIS METHOD WILL CALCULATE THE GAIN	
 def gain(entropy):
  




