import json,os
from datetime import datetime

def createTemplateFile(name='',data=''):
    print(name,data)
    templatesFiles = os.listdir("../data/templates")
    archivo = name+'.json'
    datakeys = data.keys()
    
    if archivo in templatesFiles:
        jsonFile = json.load(open(f"../data/templates/{name}.json"))
        jsonFile['metadata']['last_modified']=str(datetime.today())
        for keys in datakeys:
            if jsonFile[keys] == "" : 
                jsonFile[keys] = data[keys]
                continue
            if keys == 'content_filtering':
                for allowedPattern in data[keys]['allowedUrlPatterns']:
                    jsonFile['content_filtering']['allowedUrlPatterns'].append(allowedPattern)
                for blockedPattern in data[keys]['blockedUrlPatterns']:
                    jsonFile['content_filtering']['blockedUrlPatterns'].append(blockedPattern)
                for blockedCategory in data[keys]['blockedUrlCategories']:
                    jsonFile['content_filtering']['blockedUrlCategories'].append(blockedCategory)
                jsonFile['content_filtering']['urlCategoryListSize'] = data[keys]['urlCategoryListSize']
            if keys == 'intrusion':
                jsonFile['intrusion']['mode'] = data[keys]['mode']
                jsonFile['intrusion']['idsRulesets'] = data[keys]['idsRulesets']
                jsonFile['intrusion']['protectedNetworks']['useDefault'] = data[keys]['protectedNetworks']['useDefault']
                for include in data[keys]['protectedNetworks']['includedCidr']:
                    jsonFile['intrusion']['protectedNetworks']['includedCidr'].append(include)
                for exclude in data[keys]['protectedNetworks']['excludedCidr']:
                    jsonFile['intrusion']['protectedNetworks']['excludedCidr'].append(exclude)
            if keys == 'malware':
                jsonFile['malware']['mode'] = data[keys]['mode']
                for allowedUrl in data[keys]['allowedUrls']:
                    jsonFile['malware']['allowedUrls'].append(allowedUrl)
                for allowedFile in data[keys]['allowedFiles']:
                    jsonFile['malware']['allowedFiles'].append(allowedFile)
            if keys == 'L3_inbound':
                for rule in data[keys]['rules']:
                    jsonFile['L3_inbound']['rules'].append(rule)
            if keys == 'L3_outbound':
                
                for rule in data[keys]['rules']:
                    jsonFile['L3_outbound']['rules'].append(rule) 
            if keys == 'L7':
                for rule in data[keys]['rules']:
                    jsonFile['L7']['rules'].append(rule)           

        with open(f"../data/templates/{name}.json",'w') as fp:
            json.dump(jsonFile,fp,indent=4)
    else:
        jsonData={
            "metadata":{
                "devices":["MX"],
                "date_creation":str(datetime.today()),
                "last_modified":str(datetime.today())
            },
            "content_filtering":data['content_filtering'] if 'content_filtering' in datakeys else "",
            "intrusion":data['intrusion'] if 'intrusion' in datakeys else "",
            "malware":data['malware'] if 'malware' in datakeys else "",
            "L3_inbound":data['L3_inbound'] if 'L3_inbound' in datakeys else "",
            "L3_outbound":data['L3_outbound'] if 'L3_outbound' in datakeys else "",
            "L7":data['L7'] if 'L7' in datakeys else ""
            }

        with open(f"../data/templates/{name}.json",'w') as fp:
            json.dump(jsonData,fp,indent=4)
