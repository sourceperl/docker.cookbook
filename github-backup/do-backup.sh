#!/bin/sh

echo "$(date '+%Y-%m-%dT%H:%M:%S.000'): Start backup scheduler"

while :; do
    DATE_DIR=$(date +%Y%m%d-%H%M%S)

    for user in $(echo $GITHUB_USER | tr "," "\n"); do
        echo "$(date '+%Y-%m-%dT%H:%M:%S.000'): Execute backup for ${user}, ${DATE_DIR}"
        github-backup ${user} --token=$TOKEN --all --output-directory=/data/${DATE_DIR}/${user} --private --gists
    done

    echo "$(date '+%Y-%m-%dT%H:%M:%S.000'): Do cleanup (keep last ${MAX_BACKUPS} backups)"
    ls -d1 /data/* | head -n -${MAX_BACKUPS} | xargs rm -rf

    echo "$(date '+%Y-%m-%dT%H:%M:%S.000'): Go to sleep"
    sleep 1d
done
