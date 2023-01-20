import meraki,json
from datetime import datetime

class getInbound():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])
        self.__infoLayer3 = ''
        self.errorcode = "0"

    def setInfo(self,network_id):
        try:
            self.__infoLayer3 = self.__dashboard.appliance.getNetworkApplianceFirewallInboundFirewallRules(network_id)  
        except:
                self.errorcode = '1'

    def getInfo(self,network_id):
        self.setInfo(network_id)
        nombre = str(datetime.today()).replace(" ","_").replace(".","-").replace(":","-")
        with open(f"../data/currentconfigs/{network_id}_InboundL3_{nombre}.json",'w') as fp:
            json.dump(self.__infoLayer3,fp,indent=4)
        if self.errorcode == "0": return self.__infoLayer3, self.errorcode
        if self.errorcode == "1": return None, self.errorcode

class setInbound():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])

    
    def setInfo(self,networks_id,data):
        for network_id in networks_id:
            infoLayer3 = self.__dashboard.appliance.updateNetworkApplianceFirewallInboundFirewallRules(network_id, rules=data['rules'])        

    def getInfo(self,network_id,data):
        self.setInfo(network_id,data)

class getLayer3():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])
        self.__infoLayer3 = ''
        self.errorcode = '0'
    
    def setInfo(self,network_id):
        try:
            self.__infoLayer3 = self.__dashboard.appliance.getNetworkApplianceFirewallL3FirewallRules(network_id)
        except:
            self.errorcode = '1'

    def getInfo(self,network_id):
        self.setInfo(network_id)
        nombre = str(datetime.today()).replace(" ","_").replace(".","-").replace(":","-")
        with open(f"../data/currentconfigs/{network_id}_OutboundL3_{nombre}.json",'w') as fp:
            json.dump(self.__infoLayer3,fp,indent=4)
        if self.errorcode == "0": return self.__infoLayer3, self.errorcode
        if self.errorcode == "1": return None, self.errorcode

class setLayer3():
    def __init__(self):
        apikey = json.load(open('../data/currentUser.json'))
        self.__dashboard = meraki.DashboardAPI(apikey['apiKey'])

    def setInfo(self,networks_id,data):
        for network_id in networks_id:
            infoLayer3 = self.__dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(network_id, rules=data['rules'])        


    def getInfo(self,network_id,data):
        self.setInfo(network_id,data)