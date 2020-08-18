#=================

#nb target => number of file
nbtargets=1
#number of line per file
#nblines=35*12*3600
nblines=1
#500
scenario=4

#=================

#Iccid Prefix need to be on 10 digit => Iccid : prefixIccid(10d)nb(7d)suffix(3d)
prefixIccid='8901410321'
#Imsi Prefix need to be on 5 digit   => Imsi : prefixImsi(5d)nb(7d)suffix(3d)
prefixImsi='89401'
#suffix need to be on 3 digit        => used  to avoid to be overlapping existing range
suffix='444'
#first number
begin=0


#suffix need to be on 3 digit        => used  to avoid to be overlapping existing range
suffix2='565'


#=================
customerID    = 'ATT'
cardProfile   = 'UICCB_GEM_64_RETAIL_100'
secDom        = 'A0000000030000'
initialState  = 'INACTIVE'

filename='LPM_{}_{}'.format(prefixIccid,nblines)
