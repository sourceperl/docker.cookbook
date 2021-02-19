FROM debian:buster

# setup timezone to Europe/Paris
RUN ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata

# packages install
# add non-free archive area (need for mbrola packages)
# install alsa-utils (aplay tool), python3/pip3, espeak and mbrola packages
RUN sed -i -e's/ main/ main contrib non-free/g' /etc/apt/sources.list \
    && apt-get update \
    --quiet \
    && apt-get install \
    --yes \
    --no-install-recommends \
    --no-install-suggests \
    pulseaudio \
    alsa-utils \
    python3 \
    python3-pip \
    espeak \
    mbrola \
    mbrola-fr1 \
    && apt-get clean

# main app in /usr/src/app
WORKDIR /usr/src/app

# add python app requirements
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# avoid to run python app as root
ARG USERNAME=py-app
RUN groupadd -r $USERNAME && \
    useradd -g $USERNAME $USERNAME && \
    gpasswd -a $USERNAME audio

# setup environnement 
ENV PYTHONUNBUFFERED=1

# run app
COPY app.py ./
CMD [ "python3", "./app.py" ]
