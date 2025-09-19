
To run enterprise docker:

1. Create a working dir
1. Setup python virtual env
1. Install SAM cli
1. Load SAM enterprise image to docker
```
docker load -i solace-agent-mesh-enterprise-<tag>.tar

```
1. Create a docker compose file with the following content
```
services:
  sam-ent:
    image: 868978040651.dkr.ecr.us-east-1.amazonaws.com/solace-agent-mesh-enterprise:1.0.31-0a9b58220a
    container_name: sam-ent
    platform: linux/amd64
    # entrypoint: /bin/bash
    stdin_open: true       # same as -it
    tty: true              # same as -it
    volumes:
      - ./configs:/app/configs
      - ./.env:/app/.env
    networks:
      - sam-network
    ports:
      - "0.0.0.0:8000:8000"        # expose container port 8000 as port 8000 on host IP 0.0.0.0

networks:
  sam-network:
    external: true          # reuse your existing network

```

Note
- Update the image name:tag to what you your image is called. Execute `docker images` to get a list
- `platform: linux/amd64` if you are running on mac
- `networks: sam-network` if you are attempting to connect to a local solace broker running on docker. More below

There are two modes of operation for SAM
1. Connect with broker (Cloud or Software)
2. Run without broker (Dev Mode)

You can run a local solace broker on docker using the following command
```
docker run -d -p 8080:8080 -p 55554:55555 -p 8008:8008 -p 1883:1883 -p 5672:5672 -p 9000:9000 -p 2222:2222 --shm-size=2g --env username_admin_globalaccesslevel=admin --env username_admin_password=admin --name=solace solace/solace-pubsub-standard
```

Note: If you are running solace broker on local host via a docker image, you will have to add the solace and sam containers to the same network

```
docker network connect sam-network solace
docker network connect sam-network sam-ent
```
and use `ws://solace:8008` as your `SOLACE_BROKER_URL` value in the `.env` file


1. `docker compose up` --> runs sam enterprise 
1. Navigate to `http://localhost:8001/` from your browser and see the WebUI Gateway 