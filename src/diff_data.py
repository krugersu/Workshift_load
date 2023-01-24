
# curVal = ''
# addinvent = ''

# qrSelect_workshift = 'SELECT shiftnum ,cashcode  FROM workshift WHERE time_end >%s '
# qrSelect_last_workshift_date = 'SELECT MAX(time_end) AS "MaxDate" FROM workshift'

# qrSelect_workshift_open = 'SELECT shiftnum ,cashcode  FROM workshift WHERE time_end IS NULL AND time_beg >%s  '
# qrSelect_last_workshift_date_open = 'SELECT MAX(time_beg) AS "MaxDate" FROM workshift Where time_end IS NULL'


curVal = ''
addinvent = ''

# qrSelect_workshift = 'SELECT shiftnum ,cashcode,CAST(time_end AS char)  FROM workshift WHERE time_end >%s '
qrSelect_workshift = '''SELECT shiftnum , shopcode, CAST(time_end AS char) , cashcode, CAST(time_beg AS char), workshiftid, storeId,cashId, scode,
                        checknum1, checknum2,  CAST(sumSale AS char), CAST(sumGain AS char), CAST(sumDrawer AS char),
                        CAST(firstchecktime AS char), CAST(sumsalecash AS char), CAST(sumsalenoncash AS char), CAST(sumsaleother AS char), CAST(sumgaincash AS char),
                        CAST(sumgainnoncash AS char), CAST(sumrefund AS char), CAST(sumrefundcash AS char), CAST(sumrefundnoncash AS char), countsale, countrefund
                        FROM workshift WHERE time_end >%s '''
qrSelect_last_workshift_date = 'SELECT MAX(time_end) AS "MaxDate" FROM workshift'

qrSelect_workshift_open = 'SELECT shiftnum ,cashcode,CAST(time_beg AS char),shopcode  FROM workshift WHERE time_end IS NULL AND time_beg >%s  '
qrSelect_last_workshift_date_open = 'SELECT MAX(time_beg) AS "MaxDate" FROM workshift Where time_end IS NULL'
