# Stage 1: Builder

FROM node:20 AS builder

WORKDIR /app

COPY app/package*.json ./

RUN npm install

COPY app/. .


# Stage 2: Runtime

FROM node:20-slim

WORKDIR /app

COPY --from=builder /app/package*.json ./
COPY --from=builder /app/server.js ./
COPY --from=builder /app/node_modules ./node_modules

EXPOSE 3000

CMD ["node", "server.js"]
