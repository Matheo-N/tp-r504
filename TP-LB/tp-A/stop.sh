#!/bin/bash
containers=("nginx1" "nginx2" "nginx-lb")

for container in "${containers[@]}"; do
    if [ "$(docker ps -q -f name=$container)" ]; then
        echo "Arrêt du conteneur $container..."
        docker stop $container
        echo "Suppression du conteneur $container..."
        docker rm $container
    else
        echo "Le conteneur $container n'existe pas ou est déjà arrêté."
    fi
done
