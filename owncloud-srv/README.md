# owncloud

Simple http owncloud server. Use official owncloud image with mariadb and redis container.


Build and start the stack (with owncloud as stack name):

```bash
docker-compose up -p owncloud -d
```

Owncloud is now available at localhost:8080 as http.


See nginx-rproxy/ to setup a reverse-proxy to serve owncloud files.
