# docker.cookbook

Some useful docker images and howto

## Docker setup for Raspberry Pi

Ensure Raspbian is up to date:

```bash
sudo apt-get update && sudo apt-get upgrade -y
```
Use official get-docker script from docker:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
rm get-docker.sh
```
For use docker cli with pi user, we need to add it to docker group. Then reboot to take into account:

```bash
sudo usermod -aG docker pi
sudo reboot
```

We can install portainer (a web container management tool) on docker:

```bash
docker run -d -p 0.0.0.0:8000:8000 -p 0.0.0.0:9000:9000 --name=portainer \
           --restart=always \
           -v /var/run/docker.sock:/var/run/docker.sock \
           -v portainer_data:/data portainer/portainer-ce
```

Now you can connect to portainer tool at http://localhost:9000/
