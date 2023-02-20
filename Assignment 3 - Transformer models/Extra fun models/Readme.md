We've decided to separate the models we created for fun and the one we created for the assignment. This folder contain our "fun models".

The first model is a simple Text2Image pipeline model, where no significant changes were made to the default setup. The model has just been loaded in and set up with functions and a gradio interface in order for the user to try it out. In future iterations, we might experiment with different kinds of diffusion models, as well as changing up the scheduler within these in order to gain a better understanding of how these parameters/model features work and change the output.

The second model uses an audio dataset and tries to find similarities amongst the different audios. It seems to generate pretty good results and gives the user the opportunity to try it out based on the index. We'll experiment more on this to implement a gradio interface in order to make it more user friendly.
