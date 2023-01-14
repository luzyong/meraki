import meraki,json

class getStarted():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])
        self.__organizationsID = self.__dashboard.organizations.getOrganizations()
        self.__networksID = []
        self.status = False

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
        try:
            self.setInfo()
            self.status = True
            return self.__networksID,self.status
        except:
            return None,self.status

        



