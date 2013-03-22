#!/usr/bin/env python

import os
from time import time
from common.entities import Interface, pcapFile
#from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser

__author__ = 'catalyst256'
__copyright__ = 'Copyright 2013, Sniffmypackets Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'catalyst256'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'

__all__ = [
    'dotransform'
]

#@superuser
@configure(
    label='Sniff Packets [pcap]',
    description='Sniffs packets on interface and saves to file',
    uuids=[ 'sniffMyPackets.v2.interface2pcap' ],
    inputs=[ ( 'sniffMyPackets', Interface ) ],
    debug=True
)
def dotransform(request, response):
  
    interface = request.value
    tstamp = int(time())
    fileName = '/tmp/'+str(tstamp)+'.pcap'
    
    if 'sniffMyPackets.count' in request.fields:
      pktcount = request.fields['sniffMyPackets.count']
    else:
      pktcount = 300
    
    cmd = 'tshark -i ' + interface + ' -F libpcap' + ' -s 0 -c ' + pktcount + ' -w ' + fileName
    os.system(cmd)
    cmd2 = 'editcap ' + fileName + ' -F libpcap ' + fileName
    os.system(cmd2)
    e = pcapFile(fileName)
    response += e
    return response
