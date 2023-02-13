Assignment 2 - CNN 
(This will be updated in better detail upon further code review)

For the second assignment, we had to create a CNN with a dataset of our own choosing. We choose to go with the classical MNIST data over handwritten digits, and try to predict which digit that had been written by hand. We created two variations with a similar architecture, but different parameter setups. We chose to keep a similar architecture, due to the nature of the predictions being multi-label classification.
The main differences between the two CNNs was the number of neurons within the dense layers (self.fc1 and self.fc1 within the defined ConvNet class).

For the first CNN we went with 1000 neurons, as this was used in an example we had found online for the same type of data. We kept the n_epochs at 10 for both networks for the sake of comparison between the other parameters. We also changed the learning_rate of the network from 0.01 to 0.05, to see what kind of difference this might make. In both cases we used the Stochastic Gradient Descend algorithm for optimization, and CrossEntropyLoss for the loss function.

We found that using a significantly lower number of neurons (1000 in the first network, and 100 in the second) within the dense layers, along with a learning_rate that was five times higher in the second network, no real difference was found in terms of prediction accuracy on the test data. It would be interesting to how much the number of neurons could be reduced within the same network, before a real loss on accuracy occurs. We also would like to try is to adapt the number of channels within the Conv2d-layers, as these stayed static between the two networks, going from one output to 32, and 32 to 64. 

Assignment 2 - RNN / LSTM


For the second part of the second assignment we had to create a RNN or LSTM. We decided to try to implement a LSTM based of stock data from apple during the years 2006 - 2018. We first created two variations of the network with different hidden state and different epochs, based on hamids code example with starbucks stock data. 

After reviewing and discussions we realized that hamid's example is based on predicting the volume of a stock, not price, and in his example his timeperiod is very limited so the variance is small. In our data however, we have a very big variance in the volume over the years. Thats one of the reasons the predictions in these trials are very weird. We also realized we're trying to predict the volume based on price variables, which also doenst make sense. 

In the other trials, the two first ones in the notebook, we used code found online from an article. This code utilizes more hidden states aswell as two layers instead of one. The code also only use one of the variables for the prediction, the close price of the apple stock. Compared to the starbucks trials which try to predict the volume based on several pricing variables.

We have a sequence length of 20, and sequence length determines the number of previous time steps that the model takes into consideration when making a prediction for the next time step. So with a sequence length of 20 the model takes the observations at time steps t-19 to t-1 as input when predicting the value at time step t.
And as we see in the first trial, with a hidden state of 32, two layers, 100 epochs and a sequence length of 20, it predicts very well on the stock price.
In the second trial however we can see it performs substantially worse when reducing the hidden state to 16 and the number of epochs to 30.

In the folder "experimental stuff" in our repository we have an updated version of the notebook where we together with hamid tried to change his starbucks code for our data to only use the price in trying to predict the price aswell as changing the layers to two. 
