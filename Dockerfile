# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /

# copy the content of the local src, scripts and tests directory to the working directory
COPY src/* /usr/pizzabot/src/
COPY scripts/* /usr/pizzabot/scripts/
COPY tests/* /usr/pizzabot/tests/
COPY __init__.py /usr/pizzabot/

# copy the dependencies file to the working directory
COPY requirements.txt /usr/pizzabot

# install dependencies
RUN pip install -r /usr/pizzabot/requirements.txt

# run tests as part of build
WORKDIR /usr/pizzabot/
RUN ./scripts/run_tests

# command to run on container start
WORKDIR /usr/pizzabot/src/
CMD [ "python", "./__main__.py" ]
