# searchGarment
- This is full stack project, developed to display garments of a store. It stores data the given data set into database and creates a search platform where user can search for desired product.

### Built With
* [MongoDB](https://www.mongodb.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [React JS](https://reactjs.org/)

## Getting started

This project is build with dockers and can be installed using minimal commands.

### Prerequisites
* [docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/saratherv/searchGarment.git
   ```
2. Change directory
    ```sh
    cd searchGarment
    ```
3. Run command 
   ```sh
   sudo docker-compose up --build
   ```
4. Test Command
    ```sh
    sudo docker-compose exec backend pytest .  (Note: Run this command in separate terminal)
    ```
    
## Usage

- To access backend click, [click here](https://dry-escarpment-67178.herokuapp.com/docs)
- To access frontend click, [click here](https://blooming-castle-26206.herokuapp.com/)


## Overview of the project
Projects has multiple services running and each app has its own Dockerfile, Details about the apps is as follows-
- database, This app sets up mongodb locally.
- mongo-seed, this loads data from .jl file into mongodb collection.
- backend, this is FastAPI server, where we fetch data for the searched query.
- client, this React JS frontend which is user interface.
    


