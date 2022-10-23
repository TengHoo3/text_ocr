# OCR in Docker Environment
This Repo uses OCR to return text and coordinates from an image inputted by the user

# How to use Docker
To build docker image
'''
docker-compose build
'''

To run docker container (-d argument to run in detached mode / in the background)
'''
docker-compose up -d
'''

To stop docker container
'''
docker-compose down
'''

# Input
- Image (ideally JPG/PNG format)

# Output
- Text and their respective coordinates (in list format)

# Postprocessing
- Once you have the text and the their respective coordinates, a lot can be done through post processing which can be found in online resources