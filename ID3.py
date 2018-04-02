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

  #Set the tree length
  self.tree_length = self.num_attributes-1
  #INITIALIZE AN EMPTY TREE
  self.tree = {}


 #THIS METHOD STARTS TO MAKE THE DECISION TREE
 def make_tree():
  #LOOP TREE LENGTH
  for i in range(0,self.tree_length):
   #CALCULATE GAIN FOR ALL ATTRIBUTES
   gains = []
   for attr in self.attribute_lists:
    gains.append(gain(attr))
 
 #THIS METHOD WILL CALCULATE THE ENTROPY
 def entropy(no_of_positive_outcomes,no_of_negative_outcomes):

  #CALCULATE THE PROPORTIONS OF POSITIVE AND NEGATIVE
  pos_proportion = no_of_positive_outcomes/(no_of_positive_outcomes+no_of_negative_outcomes)
  neg_proportion = no_of_negative_outcomes/(no_of_positive_outcomes+no_of_negative_outcomes)

  #ENTROPY CALCULATION
  s = - pos_proportion*(math.log(pos_proportion,2)) - neg_proportion*(math.log(neg_proportion,2))
  return(s)

 #THIS METHOD WILL CALCULATE THE GAIN	
 def gain(total_entropy, len_training_set, attribute_list,outcome_list):
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


training_list = [['Outlook','Temperature','outcome'],['Sunny','Hot','Yes'],['Rain','Warm','Yes'],['Sunny','Cool','No']]
x = training_list
y = ID3(training_list,'Yes')