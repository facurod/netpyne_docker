# Build a Docker container for your NetPyNE model
Use this script to export a NetPyNE model into a Docker container.

## Requirements:
- A netpyne model uploaded to github.
- a mod folder in the root directory within the github repo (in order to have the mod files already compiled ones you run the container).
- Docker installed in your personal computer.

## Instructions:
### create the image:
- Create a folder in your machine and copy **dockerfile** into it. 
- Launch the Docker app in your machine.
- Type in the terminal: `docker build -t container_tag --build-arg GITHUB=your_model_github_repository -f ./dockerfile .`  (container_tag is the name you will give to the container. You can choose any name. Don't forget the whitespace followed by a dot at the very end)
### run the container:
- `docker run -it container_tag bash`

### run your python model:
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