So for this first assignment we repurposed our Attrition ANN for predicting output, so that it now queries data from a database using SQLite3. 

We cleaned the 3 dataframes up quickly in the HR_Attrition_NN_withDB.ipynb notebook, as well as creating a fourth one, before loading it into the HR_DB.db database. We then loaded the data into our neural network and trained our model. 

In the Gradio_interface_attrition.ipynb we then load in the model and .db files from the github repository, whereafter we created 2 interfaces. 
The first of these was to let the user predict their own attrition using sliders to affect the input tensor, in order to produce an output prediction.

The second interface is for searching up an EmployeeID and using a query built into the prediction function, the interface will fetch the variables for that EmployeeID and produce an output for that employee.

This functionality could be useful had the model not been terrible at predictions, and if some of the other variables had been properly tested. It could:
1. Possibly help with the initial screening process of new employees by having them fill a survey or somehow getting other information.
2. Help identify valuable employees that are worth giving extra attention before attrition occurs. Whilst searching up individual employees up by their ID, it might be useful to use the function for predicting a list of EmployeeID's that are likely to suffer from Attrition. This would enable you to compare these ID's to a score of an employees value in terms of productivity or similar.
