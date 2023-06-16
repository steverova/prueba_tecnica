import googlemaps
import json
import http.client


def get_coordinates(address):

    gmaps = googlemaps.Client(key='')

    geocode_result = gmaps.geocode(address)

    return geocode_result[0]['geometry']['location']


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


def increase_address(address, prev_neighborhood):
    """
    Obtiene la direccion y con el .split la convierte a un array de string 
    para asi trabajar con la pposicion 0 
    """

    a_address = address.split(" ")

    """
    al ser string, se pasa a entero para que sume en la funcion y 
    se vuelve a pasar a string para que conncierde con el tipo de dato en el array
    """
   
    a_address[0] = str(sum(int(a_address[0])))

    # Con el join se vuelve a formar el string de la ruta y se le asigna a una nueva variable

    new_address = ' '.join(a_address)

    # Se llama a la funcion get_coordinates() y se le pasa por parametro la ruta, esta obtiene las coordenadas.

    coord = get_coordinates(new_address)
    
    """
    Con las coordenadas, se llama a ala funcion get_neighborhood() y se le pasan las corrdendas como paramatro 
    y se obtiene el vecinadario donde esta ubicado
    """
    
    neighborhood = get_neighborhood(coord)

    print('Address: ' + new_address)

    print('Neighborhood: ' + neighborhood)

    print("============================")
    
    """
    Al ser una funcion recursiva, a la misma se la pasa el vecindario, para asi hacer una validacion, 
    cuando no se cumpla esta se detiene.
    cuando el vecindario sea igual an anterior procede a seguir llamando 
    La funcion de lo contrario se detiene.
    """
    
    if neighborhood == prev_neighborhood:
        increase_address(new_address, neighborhood)
