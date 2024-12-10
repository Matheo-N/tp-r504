#!/bin/bash

# Nom du conteneur
CONTAINER_NAME=tp4-app

# Nom de l'image
IMAGE_NAME=im-tp4

# Réseau
NETWORK_NAME=net-tp4

# Port à publier
PORT=5000

# Fonction pour arrêter le conteneur si il existe déjà
function stop_container() {
  docker stop $CONTAINER_NAME &> /dev/null
  docker rm $CONTAINER_NAME &> /dev/null
}

# Arrête le conteneur si il existe déjà
stop_container

# Lance le conteneur
docker run -d \
  --name $CONTAINER_NAME \
  --network $NETWORK_NAME \
  -p $PORT:$PORT \
  $IMAGE_NAME
