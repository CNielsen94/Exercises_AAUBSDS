So for this assignment, we attempted to create an interface for the MLFlow and for the model EDA. We ran into complications with "Unexpected error with JSON input" for the gradio interface. This could be due to a few different things:
1. The data pipeline might be having some errors, since we label encode the object columns in the dataframe for the training, but don't implement that for the gradio interface.
2. The prediction function output doesn't match what gradio needs as an input.
3. No other friggen clue
