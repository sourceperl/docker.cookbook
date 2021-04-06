FROM python:3.9

# main app in /usr/src/app
WORKDIR /usr/src/app

# add python app requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

# setup timezone to Europe/Paris (for debian buster img)
RUN ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata

# avoid to run python app as root
ARG username=py-app
RUN groupadd -r $username && \
    useradd --no-log-init -r -g $username $username
USER $username

# setup environnement 
ENV PYTHONUNBUFFERED=1

# run app
COPY app.py ./
CMD [ "python", "./app.py" ]
