# Installation (Docker)

To start `ankerctl` using docker compose on your local machine, run:

```sh
curl -O https://raw.githubusercontent.com/anselor/ankermake-m5-protocol/exiles/docker-compose.yaml
curl -O https://raw.githubusercontent.com/anselor/ankermake-m5-protocol/exiles/compose.sh
curl -O https://raw.githubusercontent.com/anselor/ankermake-m5-protocol/exiles/.env
docker-compose build
./compose.sh up
```

To start `ankerctl` using docker compose as a daemon service running on another system:

```sh
curl -O https://raw.githubusercontent.com/anselor/ankermake-m5-protocol/exiles/docker-compose.yaml
curl -O https://raw.githubusercontent.com/anselor/ankermake-m5-protocol/exiles/compose.sh
curl -O https://raw.githubusercontent.com/anselor/ankermake-m5-protocol/exiles/.env
docker-compose build
./compose.sh -o up -d
```

## Logging into AnkerMake

Once the container is running, you must log in to your AnkerMake account so that your configuration can be pulled from AnkerMake's API. 
Read the [Login Instructions page](login-instructions.md) for how to authenticate.

For docker, you can run the CLI login command interactively inside the running container like so:

```sh
docker exec -it ankerctl /app/ankerctl.py config login
```
