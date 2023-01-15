import meraki,json
from datetime import datetime

class getAMP():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])
        self.__infoContentFiltering = ''
        self.errorcode = '0'
    
    def setInfo(self,network_id):
        try:
            self.__infoContentFiltering = self.__dashboard.appliance.getNetworkApplianceSecurityMalware(network_id)
        except:
            self.errorcode = '1'

    def getInfo(self,network_id):
        self.setInfo(network_id)
        nombre = str(datetime.today()).replace(" ","_").replace(".","-").replace(":","-")
        with open(f"../data/currentconfigs/{network_id}_AMP_{nombre}.json",'w') as fp:
            json.dump(self.__infoContentFiltering,fp,indent=4)
        if self.errorcode == "0": return self.__infoContentFiltering, self.errorcode
        if self.errorcode == "1": return None, self.errorcode

class setAMP():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])
        self.__infoContentFiltering = ''

    
    def setInfo(self,networks_id,data):
        for network_id in networks_id:
            self.__infoContentFiltering = self.__dashboard.appliance.updateNetworkApplianceSecurityMalware(network_id, mode=data['mode'], allowedUrls=data['allowedUrls'],allowedFiles=data['allowedFiles'])
            print(self.__infoContentFiltering)

    def getInfo(self,network_id,data):
        self.setInfo(network_id,data)

class getIntrusion():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])
        self.__infoContentFiltering=''
        self.errorcode = '0'
    
    def setInfo(self,network_id):
        try:
            self.__infoContentFiltering = self.__dashboard.appliance.getNetworkApplianceSecurityIntrusion(network_id)
        except:
            self.errorcode = '1'

    def getInfo(self,network_id):
        self.setInfo(network_id)
        nombre = str(datetime.today()).replace(" ","_").replace(".","-").replace(":","-")
        with open(f"../data/currentconfigs/{network_id}_Intrusion_{nombre}.json",'w') as fp:
            json.dump(self.__infoContentFiltering,fp,indent=4)
        if self.errorcode == "0": return self.__infoContentFiltering, self.errorcode
        if self.errorcode == "1": return None, self.errorcode

class setIntrusion():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])
        self.__infoContentFiltering = ''

    
    def setInfo(self,networks_id,data):
        for network_id in networks_id:
            self.__infoContentFiltering = self.__dashboard.appliance.updateNetworkApplianceSecurityIntrusion(network_id,mode=data['mode'],idsRulesets=data['idsRulesets'],protectedNetworks=data['protectedNetworks'])
            print(self.__infoContentFiltering)

    def getInfo(self,network_id,data):
        self.setInfo(network_id,data)