So for this assignment, we attempted to create an interface for the MLFlow and for the model EDA. We ran into complications with "Unexpected error with JSON input" for the gradio interface. This could be due to a few different things:
1. The data pipeline might be having some errors, since we label encode the object columns in the dataframe for the training, but don't implement that for the gradio interface.
2. The prediction function output doesn't match what gradio needs as an input.
3. No other friggen clue

Instead we opted for the easier solution of just presenting our notebooks with the MLFlow implementation. The folders are sorted as such:

Database - This folder contains our .db file as well as the setup for this.

Model_EDA - This folder contains the notebooks we used to create the model and log the different metrics/artifacts. After this was run, we updated the database file to also contain these elements.
