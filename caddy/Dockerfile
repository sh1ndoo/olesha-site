# Этап 1: Сборка фронтенда (остается без изменений)
FROM node:20-alpine as build-stage
WORKDIR /app/
COPY frontend/package.json /app/
RUN npm install
COPY frontend /app/
RUN npm run build

# Этап 2: Production-образ с Caddy (вместо Nginx)
FROM caddy:latest as production-stage
COPY --from=build-stage /app/dist /dist/