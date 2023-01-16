from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import Pmw as pmw
import sys,re, json
sys.path.append("..\\")
from controls.getNetworkDevices import getNetworkDevices
from PIL import Image, ImageTk


class NetworksTemplate():

    def __init__(self, root,meraki = "",organization=''):
        self.organization = organization
        self.merakiInfo = meraki
        self.networks = []
        self.syslogValue = StringVar()
        self.Devices = getNetworkDevices()
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


        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Acciones                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def select(self,event=None):
        self.NetworkTable.selection_toggle(self.NetworkTable.focus())
        curItem = self.NetworkTable.selection()
        if len(curItem)>0:
            self.networks.clear()
            for element in curItem:
                ID = self.NetworkTable.item(element)['values'][0]
                self.networks.append(ID)



    def show(self):
        
        n = 1
        for organization in self.merakiInfo:
            if organization['organizationName'] == self.organization:
                for network in organization['networks']:
                    devices = self.Devices.getModels(network['ID'])
                    for device in devices:
                        match = re.search(r'MX{1}\w+', device)
                        if match != None:
                            self.NetworkTable.insert(parent='',index='end',iid=n,text='',values=(network['ID'],network['Name']))
                            n+=1
                            break

    def getNets(self):
        return self.networks
        
    def update(self, organization):
        self.comment.config(text=organization)
        self.organization = organization
        for i in self.NetworkTable.get_children():
            self.NetworkTable.delete(i)
        self.show() 
#root = Tk()
#root.geometry("800x500")
#root.resizable(width=False, height=False)

#ventana = Networks(root)

#root.mainloop()