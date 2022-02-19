import requests
import sqlite3
import json

requests = [
    'GetInverterRealtimeData.cgi',

]

parameters = {'Scope': 'System'}
response = requests.get(
    'http://192.168.1.61/solar_api/v1/GetInverterRealtimeData.cgi', params=parameters)

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
