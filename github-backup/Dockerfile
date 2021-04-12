FROM alpine:3.12

# Alpine setup
RUN apk add --update --no-cache tzdata git python3 py3-pip
# default timezone
ENV TZ=Europe/Paris

# add backup tool
RUN pip3 install github-backup==0.39.0 && github-backup -v

# add data directory
RUN mkdir /data

# command setup
COPY do-backup.sh /opt/do-backup.sh
RUN chmod +x /opt/do-backup.sh
CMD ["/opt/do-backup.sh"]
