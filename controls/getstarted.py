import meraki

class getStarted():
    def __init__(self,apikey):
        self.__dashboard = meraki.DashboardAPI(apikey)
        self.__organizationsID = self.__dashboard.organizations.getOrganizations()
        self.__networksID = []

    def setInfo(self):
        for organization in self.__organizationsID:
            nets = []
            networks = self.__dashboard.organizations.getOrganizationNetworks(organization['id'])
            for network in networks:
                nets.append({'ID':network['id'],'Name':network['name']})
            data = {
                'organizationName': organization['name'],
                'organizationID' : organization['id'],
                'networks' : nets
            }
            self.__networksID.append(data)
            
    def getInfo(self):
        self.setInfo()
        print(self.__networksID)
        return self.__networksID



