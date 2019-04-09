import requests
from bs4 import BeautifulSoup
import folium
import json
from folium.plugins import FastMarkerCluster
from folium.plugins import MarkerCluster

# TODO:
# include violations in the tooltip
# add search bar
# remove and correct points outside of Delaware
# deploy to a github pages - outside facing
# make sure map is always up to date - be able to tell when new inspections
# are added, and redo map accordingly
# link to violations
# create a funciton to convert violation codes into readable violations
# rank violations/filter on violations?

# url = 'https://dhss.delaware.gov/dhss/dph/hsp/Default.aspx?listAll=1&sort=Establishment'

# response = requests.get(url)
# if response.status_code == 200:
#     page_content = response.text
# # print(page_content)

# soup = BeautifulSoup(page_content, 'html.parser')

# table = soup.find('table')

# list_of_rows = []
# for row in table.findAll('tr'):
#     list_of_cells = []
#     for cell in row.findAll(['td']):
#         text = cell.text
#         text = text.strip()
#         list_of_cells.append(str(text))

#     list_of_rows.append(list_of_cells)

# for item in list_of_rows:
#     with open('inspections.txt', 'a') as f:
#         f.write(str(item) + '\n')

# addresses = set()
# with open('inspections.txt', 'r') as f:
#     for line in f:
#         elements = line.split(',')
#         addresses.add(
#             ''.join(elements[0] + elements[1] + elements[2] + elements[3]))

# def build_request(location):
#     geocode_response = requests.get(
#         'http://www.mapquestapi.com/geocoding/v1/address?key=wdJE3DIcdZOazZA0G8xnV6wsk1zHYEtV&location={}'.
#         format(location))
#     if geocode_response.status_code == 200:
#         response_data = geocode_response.text
#     else:
#         print("There was an error")
#     return response_data

# def parse(data):
#     parsed_data = json.loads(data)
#     return parsed_data

# def lat_long(parsed_data):
#     lat = parsed_data['results'][0]['locations'][0]['latLng']['lat']
#     lng = parsed_data['results'][0]['locations'][0]['latLng']['lng']
#     return lat, lng

# latlongs = set()
# with open('coords.txt', 'a') as coords_file:
#     for address in addresses:
#         new_address = address.replace("'", "").replace('[', '')
#         data_latlong = lat_long(parse(build_request(new_address)))
#         # latlongs.add(data_latlong)
#         coords_file.write("{} {} + '\n'".format(data_latlong, new_address))

# plotting the points on the map

m = folium.Map(location=(39.7447, -75.5484), prefer_canvas=True)
tooltip = 'Click me!'
mc = MarkerCluster()

with open('coords.txt', 'r') as plot_file:
    for coords in plot_file:
        coords = coords.split(' ')
        lat, lng = coords[0], coords[1]
        place = ' '.join(coords[2:])
        lat = float(lat[:-1])
        lng = float(lng)

        popup = folium.Popup(place + '\n', parse_html=True)

        mc.add_child(
            folium.Marker(location=[lat, lng], tooltip=tooltip, popup=popup))

m.add_child(mc)

m.save('points.html')
