# Music Genre Classification using Convolutional Neural Networks (CNNs)
## Introduction
This project is a Final Year Projct for the BSc(Hons) at the University of Wolverhanmpton. This is a web application that uses a Convolutional Neural Network (CNN) to classify music genres. The CNN is trained using the dataset genereated from the GTZAN dataset. The web application is bulit using Django and CNN is trained using Keras with Python. The web application is deployed on Heroku. The web application can be accessed at.

## Dataset
The dataset used for training the CNN is the GTZAN dataset which can be easily downloaded from the Kaggle (https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification). The dataset contains 1000 audio files for each genre. The audio files are in .wav format. The dataset is divided into 10 folders, one for each genre. The dataset is used to generate a new dataset containig the new MFCCs features. The new dataset is saved as a .csv file. The new dataset is used to train the CNN.

## CNN
The CNN is trained using Keras with Python. The CNN is a Sequential model with 3 convolutional layers and 2 dense layers. The CNN is trained for 60 epochs with a batch size of 3. The CNN is trained using the new dataset generated from the GTZAN dataset. The CNN is saved as a .h5 file. The CNN is loaded in the web application to classify the music genres.

## Web Application
The web application is built using Django. The web application has 4 pages. The first page is the home page where webapp name is written with some designs and has get start button to start with the app. The second page is where user can uplod a audio file. The third page is about the web app. The fourth page is the result page where the user can see the result of the classification. The web application uses the CNN to classify the music genres.
