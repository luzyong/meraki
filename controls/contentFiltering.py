import meraki,json,re
from datetime import datetime

class getContentFiltering():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])
        self.__infoContentFiltering = ''
        self.errorcode = '0'

    def setInfo(self,network_id):
        try:
            self.__infoContentFiltering = self.__dashboard.appliance.getNetworkApplianceContentFiltering(network_id)
        except:
                self.errorcode = '1'

    def getInfo(self,network_id):
        self.setInfo(network_id)
        nombre = str(datetime.today()).replace(" ","_").replace(".","-").replace(":","-")
        with open(f"../data/currentconfigs/{network_id}_ContentFiltering_{nombre}.json",'w') as fp:
            json.dump(self.__infoContentFiltering,fp,indent=4)
        if self.errorcode == "0": return self.__infoContentFiltering,self.errorcode
        if self.errorcode == "1": return None,self.errorcode

class setContentFiltering():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])
        self.__infoContentFiltering = ''

    
    def setInfo(self,networks_id,data):
        for network_id in networks_id:
            print(network_id)
            self.__infoContentFiltering = self.__dashboard.appliance.updateNetworkApplianceContentFiltering(network_id, allowedUrlPatterns=data['allowedUrlPatterns'], blockedUrlPatterns=data['blockedUrlPatterns'], blockedUrlCategories=data['blockedUrlCategories'], urlCategoryListSize=data['urlCategoryListSize'])
            print(self.__infoContentFiltering,data)

    def getInfo(self,network_id,data):
        self.setInfo(network_id,data)
        return self.__infoContentFiltering