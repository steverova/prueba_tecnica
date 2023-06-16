import googlemaps
import json
import http.client

def get_coordinates(address):
    
    gmaps = googlemaps.Client(key='AIzaSyCaUv_2wD8ZDmOQOzRhgkQJ1hH1qbRtldk')
    
    geocode_result = gmaps.geocode(address)
    
    return  geocode_result[0]['geometry']['location']

def get_neighborhood(coord):    
    
    latitude = str(coord["lng"])
    
    longitude = str(coord["lat"])

    url = "/arcgis/rest/services/Public/COP_OpenData/MapServer/125/query?geometryType=esriGeometryPoint&returnGeometry=false&f=pjson&geometry=" + \
        latitude+"%2C"+longitude+"%0D%0A&inSR=4623"

    conn = http.client.HTTPSConnection("www.portlandmaps.com")
    conn.request("GET", url)

    data = conn.getresponse().read()
    
    return json.loads(data)["features"][0]["attributes"]["NAME"]

def sum(number):
      return number+100

def increase_address(address, prev_neighborhood=None):
   
    a_address = address.split(" ")
    
    a_address[0] = str(sum(int(a_address[0])))
    
    new_address = ' '.join(a_address)
    
    coord = get_coordinates(new_address)
    
    neighborhood = get_neighborhood(coord)
    
    print('Address: '+ address)
    
    print('Neighborhood: '+ neighborhood)
    
    print("============================")
    
    if neighborhood == prev_neighborhood:
        increase_address(new_address, neighborhood)
