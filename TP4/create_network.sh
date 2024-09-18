#!/bin/bash

# Script pour créer un réseau Docker de type bridge nommé net-tp4

# Vérifier si le réseau existe déjà
if [[ $(docker network ls --filter name=^net-tp4$ -q) ]]; then
    echo "Le réseau 'net-tp4' existe déjà."
else
    # Créer le réseau
    docker network create --driver bridge net-tp4
    echo "Réseau 'net-tp4' créé avec succès."
fi

