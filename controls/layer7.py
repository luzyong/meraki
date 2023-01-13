import meraki

class getLayer7():
    def __init__(self,apikey):
        self.__dashboard = meraki.DashboardAPI(apikey)

    
    def setInfo(self,network_id):
        infoLayer7 = self.__dashboard.appliance.getNetworkApplianceFirewallL7FirewallRules(network_id)
        print(infoLayer7)

    def getInfo(self,network_id):
        self.setInfo(network_id)

class setLayer7():
    def __init__(self,apikey):
        self.__dashboard = meraki.DashboardAPI(apikey)

    
    def setInfo(self,network_id):
        infoLayer7 = self.__dashboard.appliance.updateNetworkApplianceFirewallL7FirewallRules(network_id, rules=[{'policy': 'deny', 'type': 'host', 'value': 'google.com'}, {'policy': 'deny', 'type': 'port', 'value': '23'}, {'policy': 'deny', 'type': 'ipRange', 'value': '10.11.12.00/24'}, {'policy': 'deny', 'type': 'ipRange', 'value': '10.11.12.00/24:5555'}])        
        print(infoLayer7)

    def getInfo(self,network_id):
        self.setInfo(network_id)