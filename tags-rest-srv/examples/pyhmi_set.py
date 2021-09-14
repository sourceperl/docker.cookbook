#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import requests
from pyHMI.DS_ModbusTCP import ModbusTCPDevice
from pyHMI.Tag import Tag


# some class
class Devices(object):
    # init datasource
    # PLC TBox
    tbx = ModbusTCPDevice('163.111.181.85', port=502, timeout=2.0, refresh=1.0)
    # init modbus tables
    tbx.add_floats_table(5030, 16)


class Tags(object):
    # Tbox PLC
    P_GNY_DN900 = Tag(0.0, src=Devices.tbx, ref={'type': 'float', 'addr': 5030})
    P_ARL = Tag(90.0, src=Devices.tbx, ref={'type': 'float', 'addr': 5034})
    Q_ANTENNES = Tag(0.0, src=Devices.tbx, ref={'type': 'float', 'addr': 5038})
    POS_VL = Tag(0.0, src=Devices.tbx, ref={'type': 'float', 'addr': 5040})
    POS_MV7 = Tag(0.0, src=Devices.tbx, ref={'type': 'float', 'addr': 5042})
    P_CPTGE = Tag(0.0, src=Devices.tbx, ref={'type': 'float', 'addr': 5044})
    P_AM_VL = Tag(0.0, src=Devices.tbx, ref={'type': 'float', 'addr': 5046})
    P_AV_VL = Tag(0.0, src=Devices.tbx, ref={'type': 'float', 'addr': 5048})
    REG_C_ACTIVE = Tag(0.0, src=Devices.tbx, ref={'type': 'float', 'addr': 5050})
    REG_C_CSR = Tag(0.0, src=Devices.tbx, ref={'type': 'float', 'addr': 5052})
    REG_M_P_AVAL = Tag(0.0, src=Devices.tbx, ref={'type': 'float', 'addr': 5054})
    REG_PID_P_OUT = Tag(0.0, src=Devices.tbx, ref={'type': 'float', 'addr': 5058})
    REG_SORTIE = Tag(0.0, src=Devices.tbx, ref={'type': 'float', 'addr': 5060})
    # virtual (a tag from tag(s))
    DELTA_P_VL = Tag(0, get_cmd=lambda: Tags.P_AM_VL.e_val - Tags.P_AV_VL.e_val)
    ECART_C_M = Tag(0, get_cmd=lambda: Tags.REG_C_ACTIVE.e_val - Tags.REG_M_P_AVAL.e_val)


if __name__ == '__main__':
    # wait modbus thread startup
    time.sleep(1.0)
    # main loop
    while True:
        # for every items in Tags class
        tag_l = list()
        for var_name, var in Tags.__dict__.items():
            if not var_name.startswith('__') and type(var) is Tag:
                if not var.err:
                    tag_l.append((var_name, var.val))
        # if list is not empty, send to http srv
        if tag_l:
            try:
                r = requests.post('http://localhost:5000/api/set_tag_list', json=tag_l)
                # print(r.status_code, r.text.strip())
            except Exception as e:
                print(e)
        # wait for next update
        time.sleep(15.0)
