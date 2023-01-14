import meraki,json
from datetime import datetime

class getInbound():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])
        self.__infoLayer3 = ''

    def setInfo(self,network_id):
        self.__infoLayer3 = self.__dashboard.appliance.getNetworkApplianceFirewallInboundFirewallRules(network_id)  

    def getInfo(self,network_id):
        self.setInfo(network_id)
        nombre = str(datetime.today()).replace(" ","_").replace(".","-").replace(":","-")
        with open(f"../data/currentconfigs/{network_id}_InboundL3_{nombre}.json",'w') as fp:
            json.dump(self.__infoLayer3,fp,indent=4)
        return self.__infoLayer3

class setInbound():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])

    
    def setInfo(self,networks_id,data):
        for network_id in networks_id:
            infoLayer3 = self.__dashboard.applianceupdateNetworkApplianceFirewallInboundFirewallRules(network_id, rules=data['rules'])        
            print(infoLayer3)

    def getInfo(self,network_id,data):
        self.setInfo(network_id,data)
class getLayer3():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])
        self.__infoLayer3 = ''

    
    def setInfo(self,network_id):
        self.__infoLayer3 = self.__dashboard.appliance.getNetworkApplianceFirewallL3FirewallRules(network_id)

    def getInfo(self,network_id):
        self.setInfo(network_id)
        nombre = str(datetime.today()).replace(" ","_").replace(".","-").replace(":","-")
        with open(f"../data/currentconfigs/{network_id}_OutboundL3_{nombre}.json",'w') as fp:
            json.dump(self.__infoLayer3,fp,indent=4)
        return self.__infoLayer3

class setLayer3():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])

    def setInfo(self,networks_id,data):
        for network_id in networks_id:
            infoLayer3 = self.__dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(network_id, rules=data['rules'])        
            print(infoLayer3)

    def getInfo(self,network_id,data):
        self.setInfo(network_id,data)