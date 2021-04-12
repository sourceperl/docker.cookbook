# github-backup

Backup github repository and gist to docker volume "github-backup-data-vol".

First, copy template file and edit it with good credential:

```bash
cp env.private.template env.private
nano env.private
```

Now we can run image build and start container:

```bash
docker-compose up -d
```
