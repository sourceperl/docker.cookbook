#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# simple http api server to add tag to influxdb time series

import re
from flask import Flask, jsonify, request
from influxdb import InfluxDBClient

# some consts
TAG_REGEX = '^[a-zA-Z0-9_]*$'

# Flask app
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World !'


@app.route('/api/set_tag/<tag>', methods=['GET', 'POST'])
def set_tag(tag):
    # validate tag
    if not re.match(TAG_REGEX, tag):
        return jsonify({'status': 'error', 'msg': 'bad tag name "%s"' % tag}), 400
    # validate value
    try:
        value = float(request.args.get('value'))
    except:
        return jsonify({'status': 'error',
                        'msg': 'bad value "%s" for tag "%s"' % (request.args.get('value'), tag)}), 400
    # add tag to time series
    l_metrics = [
        {'measurement': 'tag_historian',
         'tags': {'tag': tag},
         'fields': {'value': value}}
    ]
    idb.write_points(points=l_metrics)
    # return good status
    return jsonify({'status': 'ok'}), 200


@app.route('/api/set_tag_list', methods=['POST'])
def set_tag_list():
    # process input data
    tag_l = list(request.json)
    # influxdb feed loop
    l_metrics = []
    for tag, value in tag_l:
        # validate tag
        if not re.match(TAG_REGEX, tag):
            return jsonify({'status': 'error',
                            'msg': 'bad tag name "%s"' % tag}), 400
        # validate value
        try:
            value = float(value)
        except:
            return jsonify({'status': 'error',
                            'msg': 'bad value "%s" for tag "%s"' % (value, tag)}), 400
        # add tags to time series
        l_metrics.append(
            {
                'measurement': 'tag_historian',
                'tags': {
                    'tag': tag,
                },
                'fields': {
                    'value': value,
                },
            },
        )
    idb.write_points(points=l_metrics)
    # return good status
    return jsonify({'status': 'ok'}), 200


if __name__ == '__main__':
    # connect to influxdb DB
    idb = InfluxDBClient(host='influxdb-srv', port=8086)
    idb.switch_database('mydb')
    # start flask app
    app.run(host='0.0.0.0')
