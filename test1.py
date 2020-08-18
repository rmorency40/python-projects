#! /usr/bin/env python3

import itertools
import sys
from random import shuffle
import datetime
from  scenario4_input import *

for x ,k in  itertools.zip_longest(range(nbtargets), range (nblines)):
    data = []
    data.append('<Order transactionId="Trans{imsi}"> <CreateSubscription iccid ="{iccid}" imsi ="{imsi}" initialState ="{iniState}" cardProfile ="{cardProf}"> <Ota-security> <MBCard serialNumber="{iccid}"> <SecurityDomain securityDomainID="{secDom}" defaultSyncID="default" implicitRcAlgoNumber="6" proprietaryRcAlgoNumber="6"> <Sync value="0000000001"/> <Keyset versionNumber="1"> <Kic value="85C3A3C7035625761A4576B1C26E{iccid}" algoNumber="12"/> <Kid value="817356ABBC6FA36B74E194FA16BA{iccid}" algoNumber="3"/> </Keyset> <Keyset versionNumber="2"> <Kic value="68330CA022F78D736A0E14826F28{iccid}" algoNumber="12"/> <Kid value="19ECDC4A0061FFBFE96C3E3BA283{iccid}" algoNumber="3"/> </Keyset> </SecurityDomain> </MBCard> </Ota-security> </CreateSubscription> </Order>\n'.format( iccid = '{}{:07d}{}'.format(prefixIccid,x*nblines+k,suffix), imsi= '{}{:07d}{}'.format(prefixImsi,x*nblines+k,suffix),iniState = initialState,cardProf = cardProfile,secDom = secDom))
    topheader = []
    
    topheader.append('<ProvisioningOrders generateReport="true">\n')
    if initialState == 'INACTIVE' :
       topheader.append('<Order transactionId="Trans{imsi}"> <CreateSubscription iccid ="{iccid}" imsi ="{imsi}" initialState ="{iniState}" cardProfile ="{cardProf}"><Sekms-data> \n')#.format( iccid = '{}{:07d}{}'.format(prefixIccid,x*nblines+k,suffix), imsi= '{}{:07d}{}'.format(prefixImsi,x*nblines+k,suffix),iniState = initialState,cardProf = cardProfile)
                        
    else:
       topheader.append('<Order transactionId="Trans{imsi}"> <CreateSubscription iccid ="{iccid}" imsi ="{imsi}" msisdn ="{msisdn}" initialState ="{iniState}") cardProfile ="{cardProf}"><Sekms-data> \n')
    #print(data)
    print(topheader)
