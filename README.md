## Donwload the project

Clone my repository in you local maching as :https://github.com/Huynhngocthaiduy/Recommender-system-for-movies
Due to the size of the dataset and rec_imdb_960_full.ann(annoy features list)  over 100MB. Please dowloand them by the following link https://drive.google.com/file/d/1d4QRI6DN5IkqcqYMP-dYpdAPVovwlbqF/view?usp=sharing

1. Unzip the data set in the same repository.
    Please note that the structure of the data set should be:<br>
                repository<br>
                    &ensp;MLP-20M <br>
                        &ensp;&ensp;MLP-20M<br>
                            &ensp;&ensp;&ensp;1.jpg<br>
                            &ensp;&ensp;&ensp;2.jpg<br>
                            &ensp;&ensp;&ensp;.<br>
                            &ensp;&ensp;&ensp;.<br>
                            &ensp;&ensp;&ensp;.<br>
    
## How to run
1. Install Docker and Docker compose
2. Clone this repository
3. Run `docker-compose up` in the root directory of this repository
4. Open `localhost:7860` in your browser
5. Upload an image and see the results
6. To stop the server, run 
```docker-compose down``` in the root directory of this repository
7. To remove the containers, run `docker-compose rm` in the root directory of this repository
8. To remove the images, run `docker image prune -a` in the root directory of this repository
