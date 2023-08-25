import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    port=5306,
    user="root",
    password="password",
    database="MBTAdb"
    )
    print(mbtaList)

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = """
    insert into mbta_buses 
    ( id,latitude, longitude, current_stop_sequence, direction_id, label, occupancy_status, speed,vehicle_id, updated_at, bikes_allowed, block_id, wheelchair_accessible, route_id, stop_id, stop_type, trip_id, headsign, route_data_id, route_data_type, route_pattern_id, route_pattern_type, shape_id)
    values (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
    
        val = (mbtaDict['id'], mbtaDict['latitude'], mbtaDict['longitude'], mbtaDict['current_stop_sequence'], mbtaDict['direction_id'], mbtaDict['label'], mbtaDict['occupancy_status'], mbtaDict['speed'],mbtaDict['vehicle_id'], mbtaDict['updated_at'], mbtaDict['bikes_allowed'], mbtaDict['block_id'], mbtaDict['wheelchair_accessible'], mbtaDict['route_id'], mbtaDict['stop_id'], mbtaDict['stop_type'], mbtaDict['trip_id'], mbtaDict['headsign'], mbtaDict['route_data_id'], mbtaDict['route_data_type'], mbtaDict['route_pattern_id'], mbtaDict['route_pattern_type'], mbtaDict['shape_id'])
        print("_*********************FUCKKKKKKKKKKKKKK*****************************************")
        print(val)
        mycursor.execute(sql, val)

    mydb.commit()







# column_names = ['id', 'latitude', 'longitude', 'current_stop_sequence', 'direction_id', 'label', 'occupancy_status', 'speed', 'updated_at', 'bikes_allowed', 'block_id', 'wheelchair_accessible']