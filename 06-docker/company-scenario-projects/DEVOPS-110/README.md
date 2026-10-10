# DEVOPS-110 — Multi-Stage Node.js Web App

## Project Overview

This project is a small Node.js application built to practice multi-stage Docker builds.

The app is intentionally simple so the main focus stays on the Docker workflow:

- build a single-stage image
- build a multi-stage image
- compare image sizes
- inspect image history
- understand what belongs in build time and what belongs in runtime

## Learning Objectives

- Practice a single-stage Node.js Dockerfile first
- Split build and runtime work across two stages
- Use a named builder stage
- Copy only the files needed to run the app
- Use `.dockerignore` to keep the build context clean

## Application Overview

The application is a minimal HTTP server that responds with:

- `DEVOPS-110`
- `Multi-Stage Docker Build`
- `Node.js application is running successfully.`

It listens on port `3000`.

## Project Structure

```text
DEVOPS-110/
├── app/
│   ├── package.json
│   └── server.js
├── Dockerfile
├── Dockerfile.single
├── .dockerignore
└── README.md
```

## Build vs Run

Before writing the Dockerfiles, it helps to separate what Node needs to build and what it needs to run.

Build-time needs:

- `Node.js`
- `npm`
- `package.json`
- dependencies

Runtime needs:

- `Node.js`
- application files
- installed dependencies

The final image should keep only the runtime pieces.

## Single-Stage Dockerfile

`Dockerfile.single` shows the straightforward approach.

It:

- uses a Node.js image
- sets a working directory
- copies the application files
- installs dependencies
- starts the server

Build it with:

```bash
docker build -f Dockerfile.single -t devops-110-single:v1 .
```

## Multi-Stage Dockerfile

`Dockerfile` is the production-style version.

It has two stages:

- `builder` installs dependencies and prepares the app
- the final stage uses a smaller Node.js runtime image

The key idea is that the final image does not need the full development environment.

Build it with:

```bash
docker build -t devops-110-multi:v1 .
```

## Run Image

Run the single-stage image:

```bash
docker run -d --name devops110-single -p 3001:3000 devops-110-single:v1
```

Test it:

```bash
curl http://localhost:3001
```

Run the multi-stage image:

```bash
docker run -d --name devops110-multi -p 3001:3000 devops-110-multi:v1
```

Test it:

```bash
curl http://localhost:3001
```

## Compare Images

Check the image list:

```bash
docker images
```

Inspect layer history:

```bash
docker history devops-110-single:v1
docker history devops-110-multi:v1
```

Inspect the final image metadata:

```bash
docker image inspect devops-110-multi:v1
```

## Inspect the Container

Enter the running multi-stage container:

```bash
docker exec -it devops110-multi sh
```

Then check:

```bash
node --version
ls -la
```

This helps you see what actually made it into the runtime image.

## Docker Ignore

The `.dockerignore` file keeps unnecessary files out of the build context.

This helps avoid:

- slow builds
- accidental copies of local files
- larger image contexts than needed

## Useful Docker Commands

```bash
docker rm -f devops110-single
docker rm -f devops110-multi
docker rmi devops-110-single:v1
docker rmi devops-110-multi:v1
```

## What I Learned

- Build-time dependencies are not always runtime dependencies
- Multi-stage builds help separate those concerns cleanly
- The builder stage can include tools that should not ship in production
- The final image should contain only what is needed to run the app
- Measuring image size and layer history is part of understanding the result

## Workflow

```text
Source Code
   ↓
Builder Stage
   ↓
npm install
   ↓
Runtime Stage
   ↓
Container on port 3000
```
