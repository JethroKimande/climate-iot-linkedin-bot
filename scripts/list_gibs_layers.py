import requests
import xml.etree.ElementTree as ET
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


GIBS_WMS_URL = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"


def fetch_layers():
    params = {
        "SERVICE": "WMS",
        "REQUEST": "GetCapabilities"
    }
    response = requests.get(GIBS_WMS_URL, params=params)

    if response.status_code != 200:
        print(f"❌ Failed to fetch capabilities: {response.status_code}")
        return []

    root = ET.fromstring(response.text)
    layers = []

    for layer in root.iter("{http://www.opengis.net/wms}Layer"):
        name = layer.find("{http://www.opengis.net/wms}Name")
        title = layer.find("{http://www.opengis.net/wms}Title")
        if name is not None and title is not None:
            layers.append((name.text, title.text))

    return layers


def main():
    print("🌐 Available GIBS Layers:")
    for name, title in fetch_layers():
        print(f"- {name}: {title}")


if __name__ == "__main__":
    main()
