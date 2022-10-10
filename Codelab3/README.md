To build the database admin image from Docker local. docker build -t mydba .
To build the database image from Docker local docker build -t mydb .
To build the django app image from docker local docker build -t mydjango .

To run the database admin container docker run --name mydba --network mynetwork -p 8080:81 -d mydba
To run the database container from the local docker run --name mydb --network mynetwork -itd -p5432:5432 mydb
To run the django app conaitner docker run -it -p8000:8000 -v "$(pwd)/app:/app" mydjango /bin/bash
