# owncloud

Simple http owncloud server. Use official owncloud image with mariadb and redis container.


Build and start the stack (with owncloud as stack name):

```bash
docker-compose up -p owncloud -d
```

Owncloud is available at localhost:8080 as http.


Provide an https public endpoint with stunnel:

```bash
# add stunnel package
sudo apt install stunnel4
# build SSL key/cert
sudo openssl req -x509 -newkey rsa:4096 -days 3650 -nodes \
                 -subj "/C=FR/ST=Haut-de-France/L=Loos/CN=owncloud-srv" \
                 -keyout /etc/stunnel/https.key \
                 -out /etc/stunnel/https.crt
# add conf file
sudo cp stunnel/https.conf /etc/stunnel/
# load stunnel at system startup
sudo systemctl enable stunnel4.service
# restart service
sudo systemctl restart stunnel4.service
```
