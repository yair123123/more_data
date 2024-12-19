import random
from typing import List, Dict

import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
from toolz import pipe
from toolz.curried import partial



a = {0: 'eventid', 1: 'year', 2: 'month', 3: 'day', 4: 'country', 5: 'city', 6: 'latitude', 7: 'longitude', 8: 'region',
 9: 'target_type', 10: 'target1', 11: 'target_nationality', 12: 'group_name', 13: 'group_name2', 14: 'attacktype1_txt',
 15: 'num_terrorists', 16: 'num_spread', 17: 'num_killed'}

import pandas as pd
import random


def normalization(pd_data: pd.DataFrame) -> pd.DataFrame:
    pd_data['date'] = pd.to_datetime(pd_data['Date'], errors='coerce')

    pd_data['year'] = pd_data['date'].dt.year
    pd_data['month'] = pd_data['date'].dt.month
    pd_data['day'] = pd_data['date'].dt.day

    new_pd = pd.DataFrame()
    new_pd['eventid'] = [random.randint(1, 10000000) for _ in range(len(pd_data))]
    new_pd['year'] = pd_data['year']
    new_pd['month'] = pd_data['month']
    new_pd['day'] = pd_data['day']
    new_pd['country'] = pd_data.get('Country', None)
    new_pd['city'] = pd_data.get('City', None)
    new_pd['latitude'] = None
    new_pd['longitude'] = None
    new_pd['region'] = None
    new_pd['target_type'] = None
    new_pd['target1'] = None
    new_pd['target_nationality'] = None
    new_pd['Perpetrator'] = pd_data.get('Perpetrator', None)
    new_pd['group_name2'] = None
    new_pd['attacktype1_txt'] = pd_data.get('Weapon', None)
    new_pd['num_terrorists'] = None
    new_pd['Description'] = pd_data.get('Description', None)
    new_pd['num_spread'] = pd_data.get('Injuries', None)
    new_pd['num_killed'] = pd_data.get('Fatalities', None)

    return new_pd
