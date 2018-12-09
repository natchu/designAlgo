import datetime
import json

import pytz
from django.http import HttpResponse

from electrify.models import RawData


def fetch_raw_data(request,from_year,from_month,from_day,to_year,to_month,to_day):
    #Need to check on the timezone config
    nz = pytz.timezone('UTC')
    raw_data = RawData.objects.filter(read_timestamp__gte=datetime.datetime(int(from_year),int(from_month),int(from_day),tzinfo=nz)).\
        filter(read_timestamp__lte=datetime.datetime(int(to_year),int(to_month),int(to_day),tzinfo=nz))
    final_output = []

    for data in raw_data:
        data_dict = {
            'read_timestamp' : unicode(data.read_timestamp.replace(microsecond=0)),
            'interval_read' : unicode(data.interval_read),
            'energy_flow_direction': 'X' if data.energy_flow_direction == 0  else 'Y',
            'icp_id' : data.icp_id
        }
        final_output.append(data_dict)

    return HttpResponse(json.dumps(final_output), content_type='application/json')

