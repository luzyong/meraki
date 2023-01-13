import meraki

class getLayer3():
    def __init__(self,apikey):
        self.__dashboard = meraki.DashboardAPI(apikey)

    
    def setInfo(self,network_id):
        infoLayer3 = self.__dashboard.appliance.getNetworkApplianceFirewallL3FirewallRules(network_id)
        print(infoLayer3)

    def getInfo(self,network_id):
        self.setInfo(network_id)

class setLayer3():
    def __init__(self,apikey):
        self.__dashboard = meraki.DashboardAPI(apikey)

    
    def setInfo(self,network_id):
        infoLayer3 = self.__dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(network_id, rules=[{'comment': 'Allow TCP traffic to subnet with HTTP servers.', 'policy': 'allow', 'protocol': 'tcp', 'destPort': '443', 'destCidr': '192.168.1.0/24', 'srcPort': 'Any', 'srcCidr': 'Any', 'syslogEnabled': False}])        
        print(infoLayer3)

    def getInfo(self,network_id):
        self.setInfo(network_id)