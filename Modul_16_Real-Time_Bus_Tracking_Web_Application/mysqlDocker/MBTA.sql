CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id varchar(255) not null,
    latitude decimal(11,8) not null,
    longitude decimal(11,8) not null,
    current_status varchar(255),
    current_stop_sequence INT(11),
    direction_id BOOLEAN,
    label INT(4),
    occupancy_status VARCHAR(255),
    speed FLOAT,
    vehicle_id INT(8),
    updated_at TIMESTAMP,
    route_id INT(4),
    stop_id INT(4),
    stop_type varchar(255),
    trip_id INT(10),
    bikes_allowed BOOLEAN,
    block_id varchar(255),
    headsign varchar(255),
    wheelchair_accessible BOOLEAN,
    route_data_id varchar(255),
    route_data_type varchar(255),
    route_pattern_id varchar(255),
    route_pattern_type varchar(255),
    shape_id varchar(255)
);
