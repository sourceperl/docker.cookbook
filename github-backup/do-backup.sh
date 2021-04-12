#!/bin/sh

log_msg () {
    echo "$(date '+%Y-%m-%dT%H:%M:%S')    : $1"
}

log_msg "Start backup tool"

while :; do
    sleep 1m
    log_msg "Wait next run schedule at 05:10"
    while [ $(date '+%H:%M') != '05:10' ]; do sleep 15s; done

    DATE_DIR=$(date +%Y%m%d-%H%M%S)

    for user in $(echo $GITHUB_USER | tr "," "\n"); do
        log_msg "Execute backup for ${user}, ${DATE_DIR}"
        github-backup ${user} --token=$TOKEN --all --output-directory=/data/${DATE_DIR}/${user} --private --gists
    done

    log_msg "Do cleanup (keep last ${MAX_BACKUPS} backups)"
    ls -d1 /data/* | head -n -${MAX_BACKUPS} | xargs rm -rf
done
