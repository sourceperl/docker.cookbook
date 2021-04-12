#!/usr/bin/env python3

import logging
import time
import traceback
import influxdb
import psutil


# logging setup
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.ERROR)
# db setup
db = influxdb.InfluxDBClient(host='influxdb', port=8086, database='mydb')


while True:
    # list of points to write in db
    points_l = list()
    
    # CPU temperature
    try:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
            cpu_temp = float(f.read()) / 1000
            points_l.append(dict(measurement='rpi', tags=dict(tag='cpu_temp'), fields=dict(value=float(cpu_temp))))
    except Exception:
        logging.error(traceback.format_exc())

    # memory usage
    try:
        mem = psutil.virtual_memory()
        points_l.append(dict(measurement='rpi', tags=dict(tag='mem_total'), fields=dict(value=float(mem.total/1024**2))))
        points_l.append(dict(measurement='rpi', tags=dict(tag='mem_used'), fields=dict(value=float(mem.used/1024**2))))
        points_l.append(dict(measurement='rpi', tags=dict(tag='mem_free'), fields=dict(value=float(mem.free/1024**2))))
    except Exception:
        logging.error(traceback.format_exc())

    # disk usage
    try:
        disk = psutil.disk_usage('/')
        disk_usage = round(disk.used/1024**2)
        points_l.append(dict(measurement='rpi', tags=dict(tag='disk_usage'), fields=dict(value=float(disk_usage))))
    except Exception:
        logging.error(traceback.format_exc())

    # db write
    try:
        if points_l: 
            db.write_points(points_l)
    except Exception:
        logging.error(traceback.format_exc())
    
    time.sleep(60.0)
