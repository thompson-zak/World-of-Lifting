# Base python package
FROM python:3.10.6-slim-buster

# Working directory
WORKDIR /

# Copy the dependencies
COPY requirements.txt ./

# Install the dependencies
RUN pip3 install -r requirements.txt

# Copy the files
COPY . .

# Expose a port
EXPOSE 5000

# Executable commands
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]