import urllib.request, json
import mysqldb

def callMBTAApi():
    mbtaDictList = []
    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    with urllib.request.urlopen(mbtaUrl) as url:
        rowData = json.loads(url.read().decode())
        if rowData['data']:
            mbtaDictList= [
                    {
                        'vehicle_id': included['id'],
                        'direction_id': included['attributes']['bikes_allowed'],
                        'latitude': data['attributes']['latitude'],
                        'longitude': data['attributes']['longitude'],
                        'bikes_allowed': included['attributes']['bikes_allowed'],
                        'wheelchair_accessible': included['attributes']['wheelchair_accessible'],
                        'current_stop_sequence': data['attributes']['current_stop_sequence'],
                        'label': data['attributes']['label'],
                        'occupancy_status': data['attributes']['occupancy_status'],
                        'speed': data['attributes']['speed'],
                        'updated_at': data['attributes']['updated_at'],
                        'id': data['id'],
                        'current_status': data['attributes']['current_status'],
                        'route_id': data['relationships']['route']['data']['id'],
                        'stop_id': data['relationships']['stop']['data']['id'],
                        'stop_type': data['relationships']['stop']['data']['type'],
                        'trip_id': data['relationships']['trip']['data']['id'],
                        'block_id': data['relationships']['trip']['data']['type'],
                        'headsign': included['attributes']['headsign'],
                        'route_data_id': included['relationships']['route']['data']['id'],
                        'route_data_type': included['relationships']['route']['data']['type'],
                        'route_pattern_id': included['relationships']['route_pattern']['data']['id'],
                        'route_pattern_type': included['relationships']['route_pattern']['data']['type'],
                        'shape_id': included['relationships']['shape']['data']['id']
                    }
                    for included, data in zip(rowData['included'], rowData['data'])
                   ]
            mysqldb.insertMBTARecord(mbtaDictList) 

            return mbtaDictList
        
print(callMBTAApi())