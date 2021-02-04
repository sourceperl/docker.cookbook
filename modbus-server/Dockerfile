FROM python:3.9-slim

# main app in /usr/src/app
WORKDIR /usr/src/app
COPY app.py ./

# add python app requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

# avoid to run python app as root
ARG username=mbus-srv 
RUN groupadd -r $username && \
    useradd --no-log-init -r -g $username $username
USER $username

# setup environnement 
ENV PYTHONUNBUFFERED=1

# use tcp/5020 instead of tcp/502 to avoid root need
EXPOSE 5020

# run app
CMD [ "python", "./app.py" ]
