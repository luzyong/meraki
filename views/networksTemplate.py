from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import Pmw as pmw
import sys
sys.path.append("..\\")
from controls.getNetworkDevices import getNetworkDevices
from PIL import Image, ImageTk
import re

class NetworksTemplate():

    def __init__(self, root,organization="",meraki = "",template='',api=''):
        self.organization = organization
        self.merakiInfo = meraki
        self.templateName = template
        self.syslogValue = StringVar()
        self.Devices = getNetworkDevices(api)
        #self.NetworkNotebook = ttk.Notebook(root)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                           Página de templates disponibles                                ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #self.availableNetwork = Frame(self.NetworkNotebook)
        self.groupNetwork = pmw.Group(root,tag_text=f"Redes en la Organización compatibles con el Template seleccionado")
        self.groupNetwork.pack(side=TOP,expand=YES,fill=BOTH,pady=2)

        
        self.orgnamecontainer = Frame(self.groupNetwork.interior())
        self.comment = Label(self.orgnamecontainer,text=self.organization)
        self.comment.pack(side=LEFT,anchor=CENTER,padx=8,pady=1)
        self.orgnamecontainer.pack(side=TOP)
 

        self.containerTable = Frame(self.groupNetwork.interior())
        self.NetworkTable = ttk.Treeview(self.containerTable)
        self.NetworkTable['columns'] = ('Network_id', 'Network_name')

        self.NetworkTable.column("#0", width=0,  stretch=NO)
        self.NetworkTable.column("Network_id",anchor=CENTER,width=5)
        self.NetworkTable.column("Network_name",anchor=CENTER,width=495)

        self.NetworkTable.heading("#0",text="",anchor=CENTER)
        self.NetworkTable.heading("Network_id",text="Id",anchor=CENTER)
        self.NetworkTable.heading("Network_name",text="Nombre de la red",anchor=CENTER)
        self.show()

        """self.NetworkTable.insert(parent='',index='end',iid=0,text='',
        values=('1','Ninja','101','Oklahoma', 'Moore'))
        self.NetworkTable.insert(parent='',index='end',iid=1,text='',
        values=('2','Ranger','102','Wisconsin', 'Green Bay'))
        self.NetworkTable.insert(parent='',index='end',iid=2,text='',
        values=('3','Deamon','103', 'California', 'Placentia'))
        self.NetworkTable.insert(parent='',index='end',iid=3,text='',
        values=('4','Dragon','104','New York' , 'White Plains'))
        self.NetworkTable.insert(parent='',index='end',iid=4,text='',
        values=('5','CrissCross','105','California', 'San Diego'))
        self.NetworkTable.insert(parent='',index='end',iid=5,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))"""

        self.NetworkTable.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        self.containerTable.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        
        #self.availableNetwork.pack()
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Configuración Notebook                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #self.NetworkNotebook.pack(expand=YES, fill=BOTH)
        #self.NetworkNotebook.add(self.availableNetwork,text="Redes Disponibles")

        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Acciones                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
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