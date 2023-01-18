
curVal = ''
addinvent = ''

qrSelect_workshift = 'SELECT shiftnum ,cashcode  FROM workshift WHERE time_end >%s '
qrSelect_last_workshift_date = 'SELECT MAX(time_end) AS "MaxDate" FROM workshift'

qrSelect_workshift_open = 'SELECT shiftnum ,cashcode  FROM workshift WHERE time_end IS NULL AND time_beg >%s  '
qrSelect_last_workshift_date_open = 'SELECT MAX(time_beg) AS "MaxDate" FROM workshift Where time_end IS NULL'
