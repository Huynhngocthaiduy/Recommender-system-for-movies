
## How to run
Clone my repository in you local maching as :https://github.com/Huynhngocthaiduy/Recommender-system-for-movies-firs.git
### Download data set
Due to the size of the data set over 100MB. Please dowloand the dataset by the following likd
1. Unzip the data set in the same repository.
    Please note that the structure of the data set should be:
                repository /n
                    MLP-20M /n
                        MLP-20M /n
                            1.jpg /n
                            2.jpg /n
                            . /n
                            .
                            .
1. Install Docker and Docker compose
2. Clone this repository
3. Run `docker-compose up` in the root directory of this repository
4. Open `localhost:7860` in your browser
5. Upload an image and see the results
6. To stop the server, run 
```docker-compose down``` in the root directory of this repository
7. To remove the containers, run `docker-compose rm` in the root directory of this repository
8. To remove the images, run `docker image prune -a` in the root directory of this repository
