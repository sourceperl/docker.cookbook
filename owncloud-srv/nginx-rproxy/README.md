# nginx reverse proxy

Nginx reverse proxy setup:

```bash
# install nginx
sudo apt-get install nginx
sudo mkdir /etc/nginx/ssl/
# add a self-signed SSL key/cert
sudo openssl req -x509 -newkey rsa:4096 -days 3650 -nodes \
                 -subj "/C=FR/ST=Haut-de-France/L=Loos/CN=oc-srv" \
                 -keyout /etc/nginx/ssl/https.key \
                 -out /etc/nginx/ssl/https.crt
# copy and activate conf
sudo cp proxy.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/proxy.conf /etc/nginx/sites-enabled/proxy.conf
# check consistency
sudo nginx -t
# reload nginx
sudo systemctl reload nginx.service 
```
