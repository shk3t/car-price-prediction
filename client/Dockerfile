FROM node:23-alpine
WORKDIR /client
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build
CMD npm run preview