<h3>This repository contains the following implementations of a very popular machine learning technique called the Decision Tree :</h3>
<h4>`ID3`</h4>
<h5>The ID3 algorithm uses _information gain_ as a criteria to measure the strength of an attribute for the target classification.</h5>

<h6>To understand information gain we need to define entropy </h6>


<h6>	Entropy (S) = - p<sub>+</sub> log<sub>2</sub> p<sub>+</sub> - p<sub>-</sub> log<sub>2</sub> p<sub>-</sub> </h6>
<h6>	Where p<sub>+</sub> is the proportion of the positive examples and p<sub>-</sub> is the proportion of negative examples </h6>
<h6>	Entropy in a more general form is defined as - </h6>
<h6>	Entropy(S) = Sum ``` - p<sub>i</sub> log<sub>2</sub> p<sub>i</sub> </h6>

<h6>Information Gain is thus - </h6>

<h6>Gain(S,A) = S - Sum (S<sub>v</sub>/S)S<sub>v</sub></h6>

<h6>Where A is the set of all values for attribute A and S<sub>v</sub> is the subset of S for which attribute A has value v</h6>

<h6>Thus Gain is the expected reduction in entropy caused by knowing the value of attribute A</h6>


<h6>Thus the tree is split at every node by the Gain by selecting the attribute with the highest gain. The process is then repeated again </h6>

<h5>The ID3.py file :</h5>

<h6>Classes :</h6>

`ID3` :
<h6>Needs to be initialized with the following values : </h6>

`training_list` :  <h6>a list containing lists starting with the column names which are names of the attributes and the last column is the named 'outcome' (positive/negative). The subsequent lists will contain the rows of the values</h6>
<h6>Example - </h6>
<h6>The following table - </h6>

| Outlook       | Temperature   |Outcome|
| ------------- | ------------- | ----- |
| Sunny      | Hot | Yes |
| Rain     | Warm      |   Yes |
| Sunny | Cool      |    No |

<h6>Should be represented in this form -  [['Outlook','Temperature','outcome'],['Sunny','Hot','Yes'],['Rain','Warm','Yes'],['Sunny','Cool','No']] for initializing thhe class ID3</h6>

`positive_outcome` : <h6>the value of the positive outcome in the above example 'Yes'</h6>