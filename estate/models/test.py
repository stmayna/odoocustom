from datetime import datetime, timedelta
from dateutil.relativedelta import *

date = datetime.today()
print(date)

date = date + relativedelta(months=+3)
print(date)