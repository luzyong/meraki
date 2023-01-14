import meraki,json
from datetime import datetime

class getLayer7():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])
        self.__infoLayer7 = ''

    
    def setInfo(self,network_id):
        self.__infoLayer7 = self.__dashboard.appliance.getNetworkApplianceFirewallL7FirewallRules(network_id)
        #print(infoLayer7)

    def getInfo(self,network_id):
        self.setInfo(network_id)
        nombre = str(datetime.today()).replace(" ","_").replace(".","-").replace(":","-")
        with open(f"../data/currentconfigs/{network_id}_L7_{nombre}.json",'w') as fp:
            json.dump(self.__infoLayer7,fp,indent=4)
        return self.__infoLayer7

class setLayer7():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey)

    
    def setInfo(self,networks_id,data):
        for network_id in networks_id:
            infoLayer7 = self.__dashboard.appliance.updateNetworkApplianceFirewallL7FirewallRules(network_id, rules=data['rules'])        
            print(infoLayer7)

    def getInfo(self,network_id,data):
        self.setInfo(network_id,data)