from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import Pmw as pmw
import sys,re, json
sys.path.append("..\\")
from controls.getNetworkDevices import getNetworkDevices
from PIL import Image, ImageTk


class NetworksTemplate():

    def __init__(self, root,organization="",meraki = "",template='',api=''):
        self.organization = organization
        self.merakiInfo = meraki
        self.templateName = template
        self.syslogValue = StringVar()
        self.Devices = getNetworkDevices(api)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                           Página de templates disponibles                                ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.groupNetwork = pmw.Group(root,tag_text=f"Redes en la Organización compatibles con el Template seleccionado")
        self.groupNetwork.pack(side=TOP,expand=YES,fill=BOTH,pady=2)

        
        self.orgnamecontainer = Frame(self.groupNetwork.interior())
        self.comment = Label(self.orgnamecontainer,text=self.organization)
        self.comment.pack(side=LEFT,anchor=CENTER,padx=8,pady=1)
        self.orgnamecontainer.pack(side=TOP)
 

        self.containerTable = Frame(self.groupNetwork.interior())
        self.NetworkTable = ttk.Treeview(self.containerTable,selectmode='none')
        self.NetworkTable['columns'] = ('Network_id', 'Network_name')

        self.NetworkTable.column("#0", width=0,  stretch=NO)
        self.NetworkTable.column("Network_id",anchor=CENTER,width=5)
        self.NetworkTable.column("Network_name",anchor=CENTER,width=495)

        self.NetworkTable.heading("#0",text="",anchor=CENTER)
        self.NetworkTable.heading("Network_id",text="Id",anchor=CENTER)
        self.NetworkTable.heading("Network_name",text="Nombre de la red",anchor=CENTER)
        self.show()

        self.NetworkTable.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        self.NetworkTable.bind("<ButtonRelease-1>",self.select)
        self.containerTable.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        self.configure = Frame(self.groupNetwork.interior())
        self.addRule = Button(self.configure,text="Configurar",command=self.configurar)
        self.addRule.pack(side=RIGHT,padx=120)
        self.addRule.config(state='disabled')
        self.configure.pack(side=TOP,expand=YES, fill=BOTH)

        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Acciones                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def select(self,event=None):
        self.NetworkTable.selection_toggle(self.NetworkTable.focus())

    def configurar(self):
        
        curItem = self.NetworkTable.selection()
        aux = []
        for item in curItem:
            for organization in self.merakiInfo:
                seleccion = self.NetworkTable.item(item)['values']
                for network in organization['networks']:
                    if organization['organizationName'] == seleccion[1] and network['Name'] == seleccion[2]:
                        data = {
                            "org_id":organization['organizationID'],
                            "org_name":organization['organizationName'],
                            "net_id":network['ID'],
                            "net_name":network['Name']
                        }
                        aux.append(data)
        self.newConfig.append({"key":self.apikeyValue.get(),"configuration":aux})
        with open('../data/currentConfig.json','w') as fp:
            json.dump(self.newConfig,fp,indent = 4)

    def show(self):
        
        n = 1
        for organization in self.merakiInfo:
            if organization['organizationName'] == self.organization:
                for network in organization['networks']:
                    devices = self.Devices.getModels(network['ID'])
                    for device in devices:
                        print(device)
                        match = re.search(r'MX{1}\w+', device)
                        if match != None:
                            print(match,"match")
                            self.NetworkTable.insert(parent='',index='end',iid=n,text='',values=(n,network['Name']))
                            n+=1
                            break
    
    def update(self, organization, template):
        self.comment.config(text=organization)
        self.organization = organization
        self.templateName = template
        for i in self.NetworkTable.get_children():
            self.NetworkTable.delete(i)
        self.show() 
#root = Tk()
#root.geometry("800x500")
#root.resizable(width=False, height=False)

#ventana = Networks(root)

#root.mainloop()