
import csv
import pprint
import geocoder
from math import cos, asin, sqrt
import zipcode
import  json
import sys
import os


def get_data_from_csv(file_name):
    dict_list=[]
    try:
        with open(file_name, 'r',encoding='utf-8') as f:
            reader=csv.DictReader(f)
            for line in reader:
                dict_list.append(line)
    except:
        print('Invalid file name / file format not recognized')

    return dict_list

def compare_lat_lng(lat1, lon1, lat2, lon2):
    try:
        p = 0.017453292519943295
        a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    except:
        return 0.0
    else:
        return 12742 * asin(sqrt(a))


def zip_to_geocode(zip):
    try:
        geo_code= zipcode.isequal(str(zip))
        if geo_code is None:
            raise Exception
    except:
        geo_code='Invalid zip code or zip code format not recogized'
        return None
    else:
        return [geo_code.lat,geo_code.lon]
def get_lat_lng(address):
    try:
        geo_code=geocoder.google(address)
    except:
        return None
    return geo_code.latlng
def find_closest_store(dict_list,val,units,output,addr_zip):
    try:
        if addr_zip=='zipcode':
            geo_code= zip_to_geocode(val)
        else:
            geo_code = get_lat_lng(val)
        closest_store={}
        distance = None
        if geo_code is None:
            raise TypeError
        else:
            for row in dict_list:
                distance_delta= compare_lat_lng(geo_code[0],geo_code[1],float(row['Latitude']),float(row['Longitude']))
                if distance is None or distance > distance_delta:
                    distance = distance_delta
                    closest_store['Store_Name']=row['Store Name']
                    closest_store['Address'] = '{}, {}, {} {}'.format(row['Address'],row['City'],row['State'],row['Zip Code'])
                    closest_store['Distance'] = round(distance,3)
                else:
                    continue
            if units == 'km':
                closest_store['Distance']=round(closest_store['Distance']*1.609,3)
            if output =='json':
                closest_store = json.dumps(closest_store)
            else:
                closest_store="The closest store is {} at {} and is {} {} from the given {}".format(closest_store['Store_Name'],closest_store['Address'],closest_store['Distance'],units,addr_zip)
    except:
        closest_store='Invalid address/zipcode/unable to contact the server.Please try again'
        return closest_store
    return closest_store
