import requests
import sqlite3
import json
from ApiCall import ApiCall

requests_list = [
    'GetInverterRealtimeData.cgi',
]

parameters = {'Scope': 'System', 'DataCollection': 'MinMaxSensorData'}

api_call = ApiCall('GetInverterRealtimeData.cgi', parameters)
response = api_call.call_api()

print(response.text)
#
# response = response.text
#
# response_json = json.loads(response)

# db_connection = sqlite3.connect(
#     '/home/dude/Documents/sqlitedatabases/open-api')
#
# values_to_insert = [tuple(i.values()) for i in response_json]
# print(values_to_insert)
#
# query = '''
#     insert into meteo(
#         id_stacji,
#         stacja,
#         data_pomiaru,
#         godzina_pomiaru,
#         temperatura,
#         predkosc_wiatru,
#         kierunek_wiatru,
#         wilgotnosc_wzgledna,
#         suma_opadu,
#         cisnienie
#     ) values (?,?,?,?,?,?,?,?,?,?)
# '''
#
# cur = db_connection.cursor()
# cur.executemany(query, values_to_insert)
# db_connection.commit()
# db_connection.close()
