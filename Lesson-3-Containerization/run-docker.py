
#!/usr/bin/env bash

# Build image
docker build --tag=api .

# list docker images
docker image ls

# run app
docker run -p 8080:5001 api
