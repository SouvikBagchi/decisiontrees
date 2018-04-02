from __future__ import division
import math

class ID3():
 #INITIALIZE THE CLASS WITH THE INPUT OF OUTCOME AND TRAINING ATTRIBUTE LIST
 def __init__(self,training_list,positive_outcome):
  #FIND OUT WHAT IS LISTED AS AN POSITIVE OUTCOME
  self.positive_outcome = positive_outcome
  #INITIALIZE THE TRAINING LIST
  self.training_list = training_list
  self.attribute_names = training_list[0][:] #include outcome which will be removed later
  self.num_attributes = len(self.attribute_names)
  self.training_set_len = len(self.training_list) - 1 #first list is the row names
  self.attribute_list = []
  #BUILD THE LISTS OF THE ATTRIBUTE
  for attr in self.attribute_names :
  	self.attribute_list.append([attr])

  #COLUMN TRAVERSAL
  for i in range(0,self.num_attributes):
   #ROW TRAVERSAL
   temp_list = self.attribute_list[i]
   for j in range(0,self.training_set_len):
    temp_list.append(self.training_list[j+1][i]) #rowsxcolumns
   #CHANGE THE OLD ATTRIBUTE LIST 
   self.attribute_list[i] = temp_list
  #STORE OUTCOME IN A SEPARATE LIST AND REMOVE FROM ATTRIBUTE LIST
  self.outcome_list = self.attribute_list[-1]
  del self.attribute_list[-1]
  #CREATE VARIABLES WHICH HOLD THE NUMBER OF POSITIVE AND NEGATIVE OUTCOMES
  self.no_of_positive_outcomes = 0
  self.no_of_negative_outcomes = 0
  #COUNT THE POSITIVE OUTCOMES AND SET IT
  for item in self.outcome_list:
   if item == self.positive_outcome :
    self.no_of_positive_outcomes+=1
  #SET THE NEGATIVE OUTCOMES
  self.no_of_negative_outcomes = self.training_set_len-self.no_of_positive_outcomes
  #DECLARE THE ENTROPY VARIABLE OF THE LIST
  self.entropy = self.calculate_entropy(self.no_of_positive_outcomes,self.no_of_negative_outcomes)

  #Set the tree length
  self.tree_length = self.num_attributes-1
  #INITIALIZE AN EMPTY TREE
  self.tree = {}

 #THIS METHOD STARTS TO MAKE THE DECISION TREE
 def make_tree(self):
  

 def test(self):
  print("TEST RUNNING")
  self.entropy = 9
  print("END TEST")

 #THIS METHOD WILL CALCULATE THE ENTROPY
 def calculate_entropy(self,num_positive_outcomes,num_negative_outcomes):
  print("+ve : "+str(num_positive_outcomes)+" -ve : "+str(num_negative_outcomes))
  #DEFINE THE PROPORTIONS
  pos_proportion = 0.0
  neg_proportion = 0.0
  #CALCULATE THE PROPORTIONS OF POSITIVE AND NEGATIVE
  pos_proportion = num_positive_outcomes/(num_positive_outcomes+num_negative_outcomes)
  neg_proportion = num_negative_outcomes/(num_positive_outcomes+num_negative_outcomes)
  #COMMENT ON PRODUCTION
  print("+ve pro : "+str(pos_proportion)+", -ve ro : "+str(neg_proportion))

  #ENTROPY CALCULATION
  s = -(pos_proportion*(math.log(pos_proportion,2))) -(neg_proportion*(math.log(neg_proportion,2)))
  
  return(s)

 #THIS METHOD WILL CALCULATE THE GAIN
 #IT TAKES THREE ARGUMENTS - len_training_set, attribute_list,outcome_list
 #IT CALCULATES THE GAIN FOR THE SET AND RETURNS THE VALUE
 def calculate_gain(self,attribute_list,outcome_list):
  #GET THE UNIQUE ATTRIBUTES
  attribute_values = []
  for attr in set(attribute_list):
  	attribute_values.append(attr)
  #CREATE A DICT OF ATTRIBUTE WHICH HOLDS NO OF POSITIVE AND NEGATIVE OUTCOME
  pos_attribute_value_dict = {}
  neg_attribute_value_dict = {}
  for i in attribute_values :
   pos_attribute_value_dict[str(i)] = 0
   neg_attribute_value_dict[str(i)] = 0
  #LOOP THROUGH THE OUTCOME
  for i in range(1,len(outcome_list)):
   #START CHECKING FROM THE 2ND ELEMENT SINCE THE FIRST ELEMENT IS THE COLUMN NAME
   if outcome_list[i] == self.positive_outcome : 
    #CHECK THE NAME OF THE ATTRIBUTE AT THAT INDEX IN THE ATTRIBUTE LIST AND APPEND IN THE DICT
    pos_attribute_value_dict[str(attribute_list[i])]+=1
   #ELSE NEGATIVE, INCREMENT THE NEGATIVE DICT
   else :
   	neg_attribute_value_dict[str(attribute_list[i])]+=1

  #INITIALIIZE GAIN WITH total_entropy
  gain = self.entropy
  #LOOP LENGHT OF ATTRIBUTE VALUES TO SUBTRACT THE CORR SV/S
  for attribute_value in attribute_values:
   gain -= (pos_attribute_value_dict[attribute_value]+
   	neg_attribute_value_dict[attribute_value])*self.calculate_entropy(pos_attribute_value_dict[attribute_value],
   	neg_attribute_value_dict[attribute_value])

  return(gain)


 

training_list = [
['Outlook','Temperature','outcome'],
['Sunny','Hot','Yes'],
['Rain','Warm','Yes'],
['Sunny','Cool','No'],
['Cloudy','Cool','Yes'],
['Rain','Cool','No']
]
x = training_list
y = ID3(x,'Yes')
y.make_tree()