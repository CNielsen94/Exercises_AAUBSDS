This is our repository for the docker file assignment on DS AAUBS.

What we've basically done is to take the necessary ipynb files (maybe an extra or two) from the third assignment, and made this repository ready for dockerization. 
We updated the streamlit with the necessary data pipeline components to allow for prediction on user input, and added in default values to each text box to allow the user to play around with the app more easily. 
Small bug in the code atm causes an error field to appear in the bottom, but it doesn't affect the functionality of the app.

HOW TO RUN THE APP: You will need to clone the app folder for assignment 4 and dockerize it before uploading and running the image to your desired cloud service. 
Alternatively you can simply utilize our existing docker hub image from the links below.

We've chosen to run the image on Google Run, since we can set the service so that the application will only spin up/run whenever a request happens. 
To do this you must create a new service on Google run. When you first start up a new service, you can select a container image url. 
Enter your own image name on docker hub, (or copy/paste milibub/my-streamlit-app:latest) into this field, give the service a name and choose an appropriate location for computing. 
Set the appropriate settings to allow for access through the public internet, and the preferred settings for execution environment. 
Finally you may have to change the container port to 8501 as it defaults to 8080. Streamlit typically runs on port 8501, so this can cause issues if this isn't changed accordingly. 
This can be done in the Container tab under "Container, Networking, Security" (you will scroll by if you're setting up execution environment.)

Bobs your uncle, you got an inaccurate HR prediction application to determine peoples future, up and running on the internet.

LINKS: Link for the docker hub repository
- https://hub.docker.com/layers/milibub/my-streamlit-app/latest/images/sha256:67df9c475a42f681a6480b184093e7b95bd7e99128ad1b53392a815fb687b542

Link for the running streamlit app on Google cloud (It might need a minute to start up)
- https://my-streamlit-app-a3dimrupja-lz.a.run.app/
