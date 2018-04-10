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

  #BUILD THE LISTS OF THE ATTRIBUTE
  self.attribute_list = []
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

  attribute_list = self.attribute_list
  outcome_list = self.outcome_list
  x=2
  #CONTINUE TILL THE THERE ARE NO OUTCOMES LEFT
  while x != 1: #SINCE THE FIRST ELEMENT IF THE COL NAME len(outcome_list)
   #LOOP THROUGH THE ATTRIBUTE LIST
   gains = {}
   for attr in attribute_list:
    #print(attr)
    # print(i)
    # print(self.outcome_list)
    # print("")
    #print(self.calculate_gain(attr,self.outcome_list))
    #STORE THE ATTRIBUTE GAINS IN A SEPARATE LIST
    gains[str(attr[0])] = self.calculate_gain(attr,self.outcome_list)
    x=1
   # print(gains)

   node_attr = None
   #CHECK WHICH GAIN IS BIGGER
   count = 0
   for gain in gains:
    # print("Count : "+str(count))
    if count == 0:
     node_attr =gain
     # print("First attr : "+str(node_attr))
    else:
     
     if gains[node_attr] <= gains[gain]:
      # print("node attr value: "+str(gains[node_attr]))
      # print("gain attr value: "+str(gains[gain]))
      node_attr = gain
    count+=1

   #Check the gains
   # print("gains : "+str(gains))
   # print("Highest gain : "+str(node_attr))

   #THE HIGHEST GAIN IS NOW RESERVED IN NODE ATTR


 #THIS METHOD WILL CALCULATE THE ENTROPY
 def calculate_entropy(self,num_positive_outcomes,num_negative_outcomes):
  #FOR TEST
  # print("+ve : "+str(num_positive_outcomes)+" -ve : "+str(num_negative_outcomes))

  #DEFINE ENTROPY AS 0
  S = 0

  #DEFINE THE PROPORTIONS
  pos_proportion = 0.0
  neg_proportion = 0.0
  #CALCULATE THE PROPORTIONS OF POSITIVE AND NEGATIVE
  pos_proportion = num_positive_outcomes/(num_positive_outcomes+num_negative_outcomes)
  neg_proportion = num_negative_outcomes/(num_positive_outcomes+num_negative_outcomes)
  #FOR TEST
  # print("+ve pro : "+str(pos_proportion)+", -ve pro : "+str(neg_proportion))

  #MATH.LOG FAILS IF ANYONE IS 0 HENCE MAKE CHECK BEFORE ADDING CORR VALUES
  if pos_proportion != 0:
   S-= (pos_proportion*(math.log(pos_proportion,2)))
  if neg_proportion != 0:
   S-=(neg_proportion*(math.log(neg_proportion,2)))
  
  return(S)

 #THIS METHOD WILL CALCULATE THE GAIN
 #IT TAKES THREE ARGUMENTS - len_training_set, attribute_list,outcome_list
 #IT CALCULATES THE GAIN FOR THE SET AND RETURNS THE VALUE
 def calculate_gain(self,attribute_list,outcome_list):
  #GET THE UNIQUE ATTRIBUTES
  attribute_values = []
  #CHECK THE UNIQUE ATTRIBUTE_LIST BARRING THE FIRST ONE WHICH IS THE COLUMN NAME
  for attr in set(attribute_list[1:]):
   attribute_values.append(attr)

  # #TEST
  # print(attribute_values)


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

  # #TEST
  # print("pos attribute value dict : "+ str(pos_attribute_value_dict))
  # print("pos attribute value dict : "+ str(neg_attribute_value_dict))

  #INITIALIIZE GAIN WITH total_entropy
  gain = self.entropy

  # #TEST
  # print('gain should be actual entropy: '+str(gain))
  # print('')

  #LOOP LENGHT OF ATTRIBUTE VALUES TO SUBTRACT THE CORR SV/S
  for attribute_value in attribute_values:
   # #TEST
   # print(attribute_value)
   # print("pos attr dict value")
   # print(pos_attribute_value_dict[attribute_value])
   # print("neg attr dict value")
   # print(neg_attribute_value_dict[attribute_value])
   # print("entropy")
   # print(self.calculate_entropy(pos_attribute_value_dict[attribute_value],neg_attribute_value_dict[attribute_value]))

   gain -= ((pos_attribute_value_dict[attribute_value]+
   	neg_attribute_value_dict[attribute_value])/self.training_set_len)*self.calculate_entropy(pos_attribute_value_dict[attribute_value],
   	neg_attribute_value_dict[attribute_value])

  # #TEST
  # print('final gain : '+str(gain))
  # print("")

  return(gain)

training_list = [
['Outlook','Temperature','Humidity','Wind','outcome'],
['Sunny','Hot','High','Weak','No'],
['Sunny','Hot','High','Strong','No'],
['Overcast','Hot','High','Weak','Yes'],
['Rain','Mild','High','Weak','Yes'],
['Rain','Cool','Normal','Weak','Yes'],
['Rain','Cool','Normal','Strong','No'],
['Overcast','Cool','Normal','Strong','Yes'],
['Sunny','Mild','High','Weak','No'],
['Sunny','Cool','Normal','Weak','Yes'],
['Rain','Mild','Normal','Weak','Yes'],
['Sunny','Mild','Normal','Strong','Yes'],
['Overcast','Mild','High','Strong','Yes'],
['Overcast','Hot','Normal','Weak','Yes'],
['Rain','Mild','High','Strong','No']
]
x = training_list
y = ID3(x,'Yes')
y.make_tree()

#TESTS
# j = y.attribute_list[1]
# k = y.outcome_list
# l=y.calculate_gain(j,k)
