# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /

# copy the content of the local directory to the working directory
COPY pizzabot/* /usr/pizzabot/pizzabot/
COPY scripts/* /usr/pizzabot/scripts/
COPY tests/* /usr/pizzabot/tests/
COPY __init__.py /usr/pizzabot/

# copy the dependencies file to the working directory
COPY setup.py /usr/pizzabot

# install dependencies
RUN pip install -e ./usr/pizzabot

# run tests as part of build
WORKDIR /usr/pizzabot/
RUN ./scripts/run_tests

# command to run on container start
WORKDIR /usr/pizzabot/pizzabot/
CMD [ "python", "./__main__.py" ]
