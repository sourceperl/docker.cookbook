FROM redis:6.2.5

# add configuration
COPY redis.conf /etc/redis/redis.conf
COPY users.acl /etc/redis/users.acl

# redis listen port
EXPOSE 6379

# start redis with configuration file
CMD ["redis-server", "/etc/redis/redis.conf"]
