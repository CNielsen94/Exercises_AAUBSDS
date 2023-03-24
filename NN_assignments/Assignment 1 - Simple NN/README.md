# NN_exercises_AAUBSDS
Repository for assignments from AAUBS Data Science masters programme

# The HR_Attrition_NN.ipynb
This dataset is about predicting whether or not individuals within the organization is prone to leave or stay. This make the prediction binary (0 or 1). Therefore we chose to make use of the Sigmoid activation function as the output function, as this produces an output of either 0 or 1. The data cleaning and preprocessing had for the most part already been done in the last semester, as a part of a RandomForest SML model.
We created the X_tensor based on feature importances from the RandomForest model from the original assignment, which aren't a part of this notebook. For future iterations, we may build the NN into a copy of the original notebook, so that the choices are more clear cut, and comparison can be more easily made. 

We tested a few different variations of the neural network, where we mostly focused on testing different learning_rates, number of layers/neurons and a combination of different activation functions within the hidden layers. Initially we ran into some issues with the network loss score increasing from the first epoch, but after reviewing the code in further detail, we found that we had been backpropagating the prediction output instead of the loss scores between the prediction and true values. After changing this, the neural net started getting better for each epoch consistently. We have not yet saved the model and performed actual predictions, but this we hope to get done by monday evening at the latest. The plan is to come back and reiterate the NN further to try and improve this, and perhaps compare the prediction results to the original assignment the data was used for. 

The first NN we simply created a 2-layer NN, with a ReLU function in the hidden layer, and a sigmoid activation function for the output layer. For this we utilized the MSE loss function, as well as the SGD algorithm for optimization. We set the learning rate as 0.001, and started out with a total of 10 epochs.

The second NN we went a bit deeper, and created a 3-layer NN, with the addition of a sigmoid activation function for the second layer. In addition we tried switching the optimizer algorithm for RMS. We also tried turning up the learning rate to 0.005.

The third NN we switched the internal Sigmoid function for a SiLU activation function, and also tried a learning_rate of 0.003. With this one, we saw the bend at which MSE decreases happening at a higher number of epochs, which made us increase number of these. Based on the plot, we could see that it had close to no improvemet after 7 epochs, but the changes from 5-7 were also not much to brag about.

We switched the internal Sigmoid function for a ReLU activation function for the fourth NN and tried a learning rate of 0.005, increasing the epochs to 20. We also changed the number of neurons to 5 and 10 in every hidden layer, respectively. We saw that after 14 iterations, MSE dropped to its lower level.

In the fifth one, we added one more hidden layer reaching the four. Also, we used Sigmoid as our activation function in every hidden layer, increased the epochs to 200 and decreased the learning rate to 0.001. 
After about 150 iterations, we achieved the lowest MSE compared to the other variations we used.

In the sixth NN, we had three hidden layers, switched to the ReLU activation function, used Tanh as the primary output function and switched to the Adam optimizer. Also, we decreased the epochs to 10 and increased the learning rate to 0.003. All of these changes didn't reduce the MSE compared to the other variations we tried.
