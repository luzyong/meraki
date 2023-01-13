import meraki

class getContentFiltering():
    def __init__(self,apikey):
        self.__dashboard = meraki.DashboardAPI(apikey)

    
    def setInfo(self,network_id):
        infoContentFiltering = self.__dashboard.appliance.getNetworkApplianceContentFiltering(network_id)
        print(infoContentFiltering)

    def getInfo(self,network_id):
        self.setInfo(network_id)

class setContentFiltering():
    def __init__(self,apikey):
        self.__dashboard = meraki.DashboardAPI(apikey)

    
    def setInfo(self,network_id):
        infoContentFiltering = self.__dashboard.appliance.updateNetworkApplianceContentFiltering(network_id, allowedUrlPatterns=['http://www.example.org', 'http://help.com.au'], blockedUrlPatterns=['http://www.example.com', 'http://www.betting.com'], blockedUrlCategories=['meraki:contentFiltering/category/1', 'meraki:contentFiltering/category/7'], urlCategoryListSize='topSites')
        print(infoContentFiltering)

    def getInfo(self,network_id):
        self.setInfo(network_id)