# FastAPI Issue 548
*This repository created for reproduce [FastAPI](https://github.com/tiangolo/fastapi) Swagger [bug](https://github.com/tiangolo/fastapi/issues/548)*

## Local run (required Docker)

Clone project

`git clone git@github.com:i8enn/fastapi-issue-548.git`

Checkout branch

`git checkout import-uvicorn`

Build docker images and up app containers

`docker-compose up`

See browser:

http://localhost:8000/docs - Application **without** uvicorn reload (Swagger not working)

## Bug details

@xgenvn [comment](https://github.com/tiangolo/fastapi/issues/548#issuecomment-589942896).

## Remove docker images

`docker-compose down --rmi all`
