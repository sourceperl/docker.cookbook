# docker.cookbook

Some useful docker images and howto

## Docker setup for Raspberry Pi

Ensure we are up to date:

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

Some fix for Raspberry as docker host:

```bash
# enable cgroup: add "cgroup_enable=memory cgroup_memory=1" to kernel args
sudo sed -i '/cgroup_enable=memory/!s/$/ cgroup_enable=memory/' /boot/cmdline.txt
sudo sed -i '/cgroup_memory=1/!s/$/ cgroup_memory=1/' /boot/cmdline.txt
# exclude docker virtual interfaces from dhcpcd
# this avoid dhcpcd service crashes (see https://github.com/raspberrypi/linux/issues/4092/)
sudo sh -c 'echo "" >> /etc/dhcpcd.conf'
sudo sh -c 'echo "# exclude docker virtual interfaces" >> /etc/dhcpcd.conf'
sudo sh -c 'echo "denyinterfaces veth*" >> /etc/dhcpcd.conf'

sudo reboot
```

We can install portainer (a web container management tool) on docker:

```bash
docker run -d -p 0.0.0.0:9000:9000 --name=portainer --restart=always \
           -v /var/run/docker.sock:/var/run/docker.sock \
           -v portainer-data-vol:/data portainer/portainer-ce
```

Add docker-compose (here for v2.4.0):

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.4.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Now you can connect to portainer tool at http://localhost:9000/
