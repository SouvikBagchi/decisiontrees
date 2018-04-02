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
  #GET THE ENTROPY OF THE LIST
  self.entropy = 0

  #Set the tree length
  self.tree_length = self.num_attributes-1
  #INITIALIZE AN EMPTY TREE
  self.tree = {}

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
 def calculate_gain(self,total_entropy, len_training_set, attribute_list,outcome_list):
  #GET THE UNIQUE ATTRIBUTES
  attributes = []
  for attr in set(attribute_list):
  	attributes.append(attr)
  #CREATE A DICT OF ATTRIBUTE
  attribute_dict = {}
  for i in attributes :
  	attribute_dict[str(i)] = []
  #LOOP THROUGH THE OUTCOME
  
  #INITIALIIZE GAIN WITH total_entropy
  gain = total_entropy
  #LOOP LENGHT OF ATTRIBUTE VALUES TO SUBTRACT THE CORR SV/S
  for i in range(0,len_training_set):
   gain -= 1

 #THIS METHOD STARTS TO MAKE THE DECISION TREE
 def make_tree(self):
  self.entropy = self.calculate_entropy(self.no_of_positive_outcomes,self.no_of_negative_outcomes)
  #LOOP TREE LENGTH
  for i in range(0,self.tree_length):
   #CALCULATE GAIN FOR ALL ATTRIBUTES
   gains = []
 

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