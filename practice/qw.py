from datetime import timedelta
from django.utils import timezone
from datetime import datetime

threshold_time = datetime.now() - timedelta(days=1)
print(datetime.now(), timedelta(days=1))
print(threshold_time)