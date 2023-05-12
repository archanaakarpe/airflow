#!/bin/bash

# Copy data from F:mongoDB to Docker
ssh brodata2@192.168.7.209 '/home/siladmin/mongo-db'
docker ps -a
docker ps
cd ..
cd siladmin/
ls
cd mongo-db
docker-compose down
docker volume ls
docker volume rm <volume name> #replace the volume name
cd ..
cd ..
scp F:mongo/Filename brodata2@192.168.7.209:/home/siladmin/mongo-db #replace the filename