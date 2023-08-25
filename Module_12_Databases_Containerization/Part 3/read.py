# pip install redis
import redis

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# read all values in dictionary
r_values = {}
for key in ['Milk', 'Bread']:
    r_values[key] = r.get(key)

print(r_values)