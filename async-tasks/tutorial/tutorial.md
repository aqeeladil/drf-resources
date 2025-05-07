## 1. Postgresql Setup (using docker cli)

```bash
docker pull postgres
docker images

docker run --name my-postgres-db -e POSTGRES_USER=aqeel -e POSTGRES_DB=my_database -e POSTGRES_PASSWORD=12345 -p 5432:5432 -d postgres

# If you want to persist your database data even after container restarts, you can mount a volume:
docker run --name my-postgres-db -e POSTGRES_USER=aqeel -e POSTGRES_DB=my_database -e POSTGRES_PASSWORD=12345 -p 5432:5432 -v my_pg_data:/var/lib/postgresql/data -d postgres

docker ps
docker volume ls
docker volume inspect my_pg_data
docker network ls

# Connect to PostgreSQL CLI in the container:
docker exec -it my-postgres-db psql -U aqeel -d my_database

# If you'd rather use a folder on your Windows machine instead of a Docker-managed volume
# Make sure the my_local_data folder exists in the root of the current working directory, or Docker will create it.
docker update -v ./my_local_pg_data:/var/lib/postgresql/data

# To ensure your PostgreSQL container starts automatically when Docker Desktop boots up on your Windows machine.
docker update --restart unless-stopped my-postgres-db

# to stop the container
docker stop my-postgres-db

# to delete the container
docker rm my-postgres-db
```

---

## 2. Redis Setup (using docker cli)

```bash
docker pull redis

# docker run --name my-redis-server -p 6379:6379 -v my_redis_data:/data -d redis
docker run --name my-redis-server -p 6379:6379 -v ./my_local_redis_data:/data --restart unless-stopped -d redis     

docker images
docker ps
docker volume ls
docker network ls

# To access the Redis command-line interface from inside the container:
docker exec -it my-redis-server redis-cli

# you can try these commands inside the redis container
PING
SET mykey "hello"
GET mykey
```

## 3. Postgresql & Redis (docker compose)

```bash
# In the same directory as your docker-compose.yml
docker-compose up -d

# to stop the container
docker-compose down

docker images
docker ps
docker volume ls
docker network ls

# get inside the containers
docker exec -it my-redis-server redis-cli
docker exec -it my-postgres-db psql -U aqeel -d my_database
```
