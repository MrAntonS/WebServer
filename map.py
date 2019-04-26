import requests
import test
import os

#создаем карту
geocoder_api_server = "http://static-maps.yandex.ru/1.x/"
def get_map(x, y, zoom, filename, slovar, size=450, map_type="map"):
    params = {"l": map_type,
              "z": str(zoom),
              "ll": ",".join([str(x),str(y)]),
              "size": ",".join([str(500), str(400)]),
              "pt": slovar}
    response = requests.get(geocoder_api_server, params=params)
    if not response:
        err = "Http статус:"+str(response.status_code)+"("+str(response.reason)+")"
        return False, err
    
    try:
        # Передаем
        with open(filename, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        return False, ex
    return True, None

def bbox(bbox, zoom, filename, size=450, map_type="sat"):
    a, b = bbox[0], bbox[1]
    a = ",".join([str(a[0]), str(a[1])])
    b=",".join([str(b[0]), str(b[1])])
    params = {"l": map_type,
              "z": str(zoom),
              "bbox": "~".join([a,b]),
              "size": ",".join([str(size), str(size)])}
    response = requests.get(geocoder_api_server, params=params)
    if not response:
        err = "Http статус:"+str(response.status_code)+"("+str(response.reason)+")"
        return False, err
    
    try:
        with open(filename, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        return False, ex
    return True, None


if __name__ == "__main__":
    x, y = '37', '55'
    zoom = 10
    filename = "map.png"
    print(get_map(x, y, zoom, filename) )