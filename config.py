IP = "192.168.178.136"
NETMASK = "255.255.255.0"
GATEWAY = "192.168.178.1"
PORT = 80
MACADDRESS = "00:22:19:f8:7e:af"

USER = "newdeveloper"

HueBasic = {
  "config": {
    "name": "Philips hue",
    "bridgeid": "001788FFFE198BF5",
    "mac": MACADDRESS,
    "modelid": "BSB001",
    "datastoreversion": "59",
    "swversion": "01041302",
    "apiversion": "1.16.0",
    "factorynew": True,
    "replacesbridgeid": None
  }
}

HueConfig = {
  "lights": {
    "1": {
      "state": {
        "on": False,
        "bri": 1,
        "hue": 0,
        "sat": 0,
        "xy": [0.5, 0.5],
        "ct": 500,
        "effect": "none",
        "alert": "none",
        "reachable": True
      },
      "type": "Custom",
      "name": "Hue",
      "modelid": "LC0015",
      "swversion": "1.0.3"
    }
  },
  "groups": {},
  "config": {
    "name": "Philips hue",
    "zigbeechannel": 11,
    "bridgeid": "001788FFFE198BF5",
    "mac": MACADDRESS,
    "dhcp": True,
    "ipaddress": IP,
    "netmask": NETMASK,
    "gateway": GATEWAY,
    "proxyaddress": "none",
    "proxyport": 0,
    "UTC": "1980-01-01T00:00:34",
    "localtime": "1980-01-01T01:00:34",
    "timezone": "Europe/Berlin",
    "modelid": "BSB001",
    "datastoreversion": "59",
    "swversion": "01041302",
    "apiversion": "1.16.0",
    "swupdate": {
      "updatestate": 0,
      "checkforupdate": False,
      "devicetypes": {
        "bridge": False,
        "lights": [],
        "sensors": []
      },
      "url": "",
      "text": "",
      "notify": False
    },
    "linkbutton": False,
    "portalservices": True,
    "portalconnection": "connecting",
    "portalstate": {
      "signedon": False,
      "incoming": False,
      "outgoing": False,
      "communication": "disconnected"
    },
    "factorynew": True,
    "replacesbridgeid": None,
    "backup": {
      "status": "idle",
      "errorcode": 0
    },
    "whitelist": {
      USER: {
        "last use date": "1980-01-01T00:01:42",
        "create date": "1980-01-01T00:01:42",
        "name": "Hue Bridge v1#iPhone"
      }
    }
  },
  "schedules": {},
  "scenes": {},
  "rules": {},
  "sensors": {
    "1": {
      "state": {
        "daylight": None,
        "lastupdated": "none"
      },
      "config": {
        "on": True,
        "configured": False,
        "sunriseoffset": 30,
        "sunsetoffset": -30
      },
      "name": "Daylight",
      "type": "Daylight",
      "modelid": "PHDL00",
      "manufacturername": "Philips",
      "swversion": "1.0"
    }
  },
  "resourcelinks": {}
}

DESCRIPTION_XML = f"""<?xml version="1.0" encoding="UTF-8" ?>
<root xmlns="urn:schemas-upnp-org:device-1-0">
<specVersion>
<major>1</major>
<minor>0</minor>
</specVersion>
<URLBase>http://{IP}:{PORT}/</URLBase>
<device>
<deviceType>urn:schemas-upnp-org:device:Basic:1</deviceType>
<friendlyName>Philips hue ({IP})</friendlyName>
<manufacturer>Royal Philips Electronics</manufacturer>
<manufacturerURL>http://www.philips.com</manufacturerURL>
<modelDescription>Philips hue Personal Wireless Lighting</modelDescription>
<modelName>Philips hue bridge 2012</modelName>
<modelNumber>929000226503</modelNumber>
<modelURL>http://www.meethue.com</modelURL>
<serialNumber>{MACADDRESS.replace(':','')}</serialNumber>
<UDN>uuid:2f402f80-da50-11e1-9b23-{MACADDRESS.replace(':','')}</UDN>
<presentationURL>index.html</presentationURL>
<iconList>
<icon>
<mimetype>image/png</mimetype>
<height>48</height>
<width>48</width>
<depth>24</depth>
<url>hue_logo_0.png</url>
</icon>
</iconList>
</device>
</root>
"""
