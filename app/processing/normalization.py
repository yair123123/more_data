import random
from typing import List, Dict

import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
from toolz import pipe
from toolz.curried import partial





import pandas as pd
import random
from geopy import Nominatim

def convert_unknown_to_none(val):
    if isinstance(val, str) and val in ["unknown", "Unknown", "none", "None"]:
        return None
    elif isinstance(val, float) and pd.isna(val):
        return None
    return val

def convert_address_to_points(address):
    try:
        geolocator = Nominatim(user_agent="geo_locator")
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        return None
    except Exception as e:
        print(e)
        return (None,None)

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
    pd_data["latitude"], pd_data["longitude"] = zip(*pd_data.apply(lambda row: convert_address_to_points(f"{row['City']}, {row['Country']}"), axis=1))
    new_pd['region'] = None
    new_pd['target_type'] = None
    new_pd['target1'] = None
    new_pd['target_nationality'] = None
    new_pd['group_name'] = pd_data.get('Perpetrator', None)
    new_pd['group_name2'] = None
    new_pd['attacktype1_txt'] = pd_data.get('Weapon', None)
    new_pd['num_terrorists'] = None
    new_pd['summary'] = pd_data.get('Description', None)
    new_pd['num_spread'] = pd_data.get('Injuries', None)
    new_pd['num_killed'] = pd_data.get('Fatalities', None)


    return  new_pd.applymap(convert_unknown_to_none)
