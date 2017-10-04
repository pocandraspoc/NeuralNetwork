#Nowdays usually in the new literature this one is used:
#ReLu anctivation function (3 implementation)
import numpy as np

x = np.random.random((5000, 5000)) - 0.5
print("max method:")
%timeit -n10 np.maximum(x, 0)

print("multiplication method:")
%timeit -n10 x * (x > 0)

print("abs method:")
%timeit -n10 (abs(x) + x) / 2
###################################################################################

#OR
# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation

#I left the original code but the terms are bit confusing.
#Usually "Activation" is used in the sence how "Transfer" is used here!!!
# Transfer "Activation function" neuron activation
#SO THe "Old" Sigmoid
def sigmoid(activation): #I changed the name!
	return 1.0 / (1.0 + exp(-activation))
  
  

####################################################################################

#TANH function:
def tanh(activation):
  np.sinh(activation)/np.cosh(activation)

  
