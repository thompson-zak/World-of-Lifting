#Base image
FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json ./

# install project dependencies
RUN npm install

# Copy the project files
COPY . .

# Expose a port
EXPOSE 8080

# Development Build
CMD ["npm", "run", "serve"]

# Production Build
# Build the project
#RUN npm run build

# Executables
# CMD [ "http-server", "dist" ]