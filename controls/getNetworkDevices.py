import meraki,json


class getNetworkDevices():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])
        self.__networkDevices = ''
        self.__models = []

    def setModels(self, network_id):
        self.__networkDevices = self.__dashboard.networks.getNetworkDevices(network_id)
        for device in self.__networkDevices:
            if device['model'] not in self.__models:
                self.__models.append(device['model'])

    def getModels(self, network_id):
        self.setModels(network_id)
        return self.__models
