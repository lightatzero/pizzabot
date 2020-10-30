# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /

# copy the content of the local directory to the working directory
COPY pizzabot/* /usr/pizzabot/pizzabot/
COPY scripts/* /usr/pizzabot/scripts/
COPY tests/* /usr/pizzabot/tests/
COPY bin/* /usr/pizzabot/bin/

# copy the dependencies file to the working directory
COPY setup.py /usr/pizzabot

# install dependencies
RUN pip install -e ./usr/pizzabot

# run tests as part of build
WORKDIR /usr/pizzabot/
RUN ./scripts/run_tests

# command to run on container start
CMD ["pizzabot", "5x5 (0, 0) (1, 3) (4,4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)"]
