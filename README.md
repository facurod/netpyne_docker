# Build a Docker container for your NetPyNE model
Use this script to export a NetPyNE model into a Docker container.

## Requirements:
- A netpyne model uploaded to github.
- a mod folder in the root directory within the github repo (in order to have the mod files already compiled ones you run the container).
- Docker installed in your personal computer.

## Instructions:
### create the image:
- Clone this repo. 
- Launch the Docker app in your machine.
- Open a terminar and go inside netpyne_docker folder.
- Type: `python netpyne_docker container_tag model_github_repository`  

NOTES: **container_tag** is the name you will give to your Docker container. **model_github_repository** is the github URL where you are sharing your model.
### run the container:
- `docker run -it container_tag bash`
### exit from container:
- `exit`

### run your python model (when your are inside the container):
- python init.py

### Container packages
- Linux (Devian)
- NEURON (7.6.2)
- Miniconda3 (Python 3.7)
- NetPyNE (develpment_py3)
- pyNeuroML

### NOTES:
- Type in a termina `source activate snakes` to log into the virtual environment that contains NEURON and NetPyNE.
- The mod files will be already compiled ones you open the container.
- The building will run in the background, so check the out.log and err.log files.

### Docker 101:
- get docker containers: `docker ps`
- delete all images: `docker system prune -a` (removes absolutely everything)
- get list of images: `docker images -a`
- kill all active containers: `docker kill $(docker ps -q)`
- remove all containers: `docker rm $(docker ps -a -q)`
- remove all images: `docker rmi $(docker images -q)`