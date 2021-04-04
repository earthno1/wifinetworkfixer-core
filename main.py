import pywifi

wifi = pywifi.PyWiFi()
eth0 = wifi.interfaces()[0]
if eth0.status() == pywifi.const.IFACE_DISCONNECTED:
    print(eth0.scan())
