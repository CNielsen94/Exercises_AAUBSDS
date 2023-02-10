Assignment 2 - CNN 
(This will be updated in better detail upon further code review)

For the second assignment, we had to create a CNN with a dataset of our own choosing. We choose to go with the classical MNIST data over handwritten digits, and try to predict which digit that had been written by hand. We created two variations with a similar architecture, but different parameter setups. We chose to keep a similar architecture, due to the nature of the predictions being multi-label classification.
The main differences between the two CNNs was the number of neurons within the dense layers (self.fc1 and self.fc1 within the defined ConvNet class).

For the first CNN we went with 1000 neurons, as this was used in an example we had found online for the same type of data. We kept the n_epochs at 10 for both networks for the sake of comparison between the other parameters. We also changed the learning_rate of the network from 0.01 to 0.05, to see what kind of difference this might make. In both cases we used the Stochastic Gradient Descend algorithm for optimization, and CrossEntropyLoss for the loss function.

We found that using a significantly lower number of neurons (1000 in the first network, and 100 in the second) within the dense layers, along with a learning_rate that was five times higher in the second network, no real difference was found in terms of prediction accuracy on the test data. It would be interesting to how much the number of neurons could be reduced within the same network, before a real loss on accuracy occurs. We also would like to try is to adapt the number of channels within the Conv2d-layers, as these stayed static between the two networks, going from one output to 32, and 32 to 64. 

Assignment 2 - RNN
(This will be updated in better detail upon further code review)

For the second part of the second assignment we had to create a RNN or LSTM. We decided to try to implement a LSTM based of stock data from apple from 2006 - 2018. We created two variations of the network with different hidden state and different epochs. Due to the time constraint and the groups schedule unfortunately we haven't gone as deep in the understanding and the adaption of the LSTM with our data, compared to our CNN network.

We have troubles with the data adaption and can see major flaws in the early stages of our illustrations. We will keep working on this part of the assignment during the weekend and coming week and hopefully implement it correctly and with a deeper understanding. Consider this a first draft.
