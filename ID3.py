import math
class ID3():
 #INITIALIZE THE CLASS WITH THE INPUT OF OUTCOME AND TRAINING ATTRIBUTE LIST
 def __init__(self,training_list,positive_outcome):
  #FIND OUT WHAT IS LISTED AS AN POSITIVE OUTCOME
  self.positive_outcome = positive_outcome
  #INITIALIZE THE TRAINING LIST
  self.training_list = training_list
  self.attribute_names = training_list[0][:-1] #All the elements of the first list save the last
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
  pass

training_list = [['Outlook','Temperature','outcome'],['Sunny','Hot','Yes'],['Rain','Warm','Yes'],['Sunny','Cool','No']]
y = ID3(training_list,'Yes')