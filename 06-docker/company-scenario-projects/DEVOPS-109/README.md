# DEVOPS-109 — Multi-Stage Docker Practice

## Project Overview

This project is a small Flask application built for one goal: practicing a multi-stage Docker build.

The application is intentionally simple. It only needs to confirm that the container starts correctly and serves a page inside Docker.

## Learning Objectives

- Build a working single-stage image first
- Build a multi-stage image with a named builder stage
- Copy installed dependencies from the builder stage into the final stage
- Use a slim runtime image
- Compare image sizes and layer history
- Understand why the builder image is not used at runtime

## Application Overview

The Flask app shows:

- `DEVOPS-109`
- `Multi-Stage Docker Application`
- `Running successfully inside Docker.`

## Project Structure

```text
DEVOPS-109/
├── app/
│   └── run.py
├── requirements.txt
├── Dockerfile.single
├── Dockerfile
└── README.md
```

## Dockerfile Explanation

### Single-stage image

`Dockerfile.single` is the first version.

It:

- starts from one Python image
- installs the dependencies directly in that image
- copies the application
- runs Flask

### Multi-stage image

`Dockerfile` is the improved version.

It:

- uses a `builder` stage to install dependencies
- copies those dependencies into a smaller runtime image
- keeps the final image focused on running the app

The key idea is that the build tools and temporary install step stay behind in the builder stage.

## Build Image

Build the single-stage image first:

```bash
docker build -f Dockerfile.single -t devops-109-single:v1 .
```

Build the multi-stage image:

```bash
docker build -t devops-109-multi:v1 .
```

## Run Image

Run the single-stage version:

```bash
docker run -d --name devops109-single -p 5001:5000 devops-109-single:v1
```

Test it:

```bash
curl http://localhost:5001
```

Run the multi-stage version:

```bash
docker run -d --name devops109-multi -p 5001:5000 devops-109-multi:v1
```

Test it:

```bash
curl http://localhost:5001
```

## Tag Image

If you want to tag an existing image with another name:

```bash
docker tag devops-109-multi:v1 fazalhamzakhan/devops-109-multi:v1
```

## Docker Login

Log in before pushing to Docker Hub:

```bash
docker login
```

## Push Image to Docker Hub

```bash
docker push fazalhamzakhan/devops-109-multi:v1
```

## Remove Local Image

```bash
docker rmi devops-109-multi:v1
```

## Pull Image from Docker Hub

```bash
docker pull fazalhamzakhan/devops-109-multi:v1
```

## Run Pulled Image

```bash
docker run -d --name devops109-pulled -p 5001:5000 fazalhamzakhan/devops-109-multi:v1
```

## Docker Image Versioning

This project uses `v1` as the first tag.

That keeps the image history easy to understand and lets you publish future changes as `v2`, `v3`, and so on.

## Useful Docker Commands

```bash
docker images
docker history devops-109-single:v1
docker history devops-109-multi:v1
docker image inspect devops-109-multi:v1
docker rm -f devops109-single
docker rm -f devops109-multi
docker rm -f devops109-pulled
```

## What I Learned

- A multi-stage Dockerfile separates build work from runtime work
- The final image can stay smaller and cleaner
- `COPY --from=builder` is the bridge between stages
- The builder image is only used during the build, not when the container runs
- The app behavior stays the same even when the image build process changes

## Workflow

```text
Source Code
   ↓
Dockerfile.single or Dockerfile
   ↓
docker build
   ↓
Local Docker Image
   ↓
docker run
   ↓
Container running on port 5000
```
