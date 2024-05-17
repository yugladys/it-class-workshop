# use official python base image - https://github.com/docker-library/python/blob/89b2500cd1255b1be5f57c1bce598f031172bb0a/3.11/slim-bullseye/Dockerfile
FROM python:3.11-slim-bullseye

# -- Exercise: create non-root group and non-root user
# -- create a system group names "user" with -r flag
RUN groupadd -r user
# -- reate user and add it to the group
RUN useradd -r -g user user

# set working directory in the container 
WORKDIR /app

# copy the requirements file into the container
COPY streamlit_app/requirements.txt .

# install the required dependencies
RUN pip install -r requirements.txt

# -- Exercise: Install additional package on the OS and create extra layer
# RUN apt-get update && apt-get install -y \
#     curl

# copy the rest of the application code into the container
COPY streamlit_app/app.py .
COPY streamlit_app/data.csv .

# --Exercise: change the ownership of working directory to non-root
RUN chown -R user:user /app

# --Exercise: switch to the non-root user and run application with it
USER user

# command to run the application; in CMD you add an executable command
CMD [ "streamlit", "run", "app.py" ]


# -- Exercise: add second CMD instruction
# CMD ["echo", "This is my second CMD"]