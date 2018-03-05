"""Usage:
  storeFinder.py find_store --address="<address>"
  storeFinder.py find_store --address="<address>" [--units=(mi|km)] [--output=text|json]
  storeFinder.py find_store --zip=<zip>
  storeFinder.py find_store --zip=<zip> [--units=(mi|km)] [--output=text|json]
  """
from docopt import docopt
import json
import data
import sys



if __name__ == '__main__':

    try:
        dict_list = data.get_data_from_csv('store-locations.csv')
        arguments = docopt(__doc__)
        if not dict_list:
            raise TypeError
    except:
        print('No data found in the csv file / docopt unable to parse the arguments in the cli command')

    try:
        if arguments['--address'] != None:
            address = arguments['--address']
            units = 'mi' if arguments['--units'] is None else arguments['--units']# check this
            output = 'text' if arguments['--output'] is None else arguments['--output']
            print(data.find_closest_store(dict_list,address,units,output,'address'))
        elif arguments['--zip'] !=None:

            zip_code= arguments['--zip']
            units = 'mi' if arguments['--units'] is None else arguments['--units']# check this
            output = 'text' if arguments['--output'] is None else arguments['--output']
            res=data.find_closest_store(dict_list,zip_code,units,output,'zipcode')
            print(res)

        else:
            print('Invalid Input. Please try again')
    except:
        print('Invalid data . Please try again')
