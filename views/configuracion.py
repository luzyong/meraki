from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import Pmw as pmw
from PIL import Image, ImageTk
import sys
sys.path.append("..\\")
from controls.getstarted import getStarted 
import json

class Configuracion():
    

    def __init__(self, root):
        self.apikeyValue = StringVar()
        self.merakiInfo = ""
        self.newConfig = []
        self.configNotebook = ttk.Notebook(root)
        #----Seccion de imagen----
        #self.VosedaFrame = Frame(self.master)
        #self.imageVoseda = Canvas(self.VosedaFrame)
        #self.imageVoseda.pack(padx=1,pady=1)
        #self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\LuzYong\\Documents\\Trabajo\\ScriptsPython\\Meraki\\isotipo_voseda_color.png"))
        #self.imageVoseda.create_image(50,50,anchor=NW,image=self.img)
        #self.VosedaFrame.pack()
        #self.master.pack()
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                   Página de configuración                                ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.masterConfig = Frame(self.configNotebook)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                   Grupo API Key                                          ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.grupoAPI = pmw.Group(self.masterConfig,tag_text="API Key")
        self.grupoAPI.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        self.apikey = Frame(self.grupoAPI.interior())

        self.apikeyEntry = Entry(self.apikey,textvariable=self.apikeyValue).pack(side=LEFT,expand=NO)
        self.buscar = Button(self.apikey,text="Buscar",command=self.Show)
        self.buscar.pack(side=LEFT, expand=NO)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Subgrupo Resultados                                       ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.grupoResult = pmw.Group(self.grupoAPI.interior(),tag_text="Resultados")
        self.grupoResult.pack(side=BOTTOM,expand=YES,fill=BOTH,padx=3,pady=2)
        self.OrganizationTable = ttk.Treeview(self.grupoResult.interior(),selectmode='none')
        self.OrganizationTable['columns'] = ('organization_id', 'organization_name','network_name')

        self.OrganizationTable.column("#0", width=0,  stretch=NO)
        self.OrganizationTable.column("organization_id",anchor=CENTER,width=125)
        self.OrganizationTable.column("organization_name",anchor=CENTER,width=125)
        self.OrganizationTable.column("network_name",anchor=CENTER,width=125)
        #self.OrganizationTable.column("selected",anchor=CENTER,width=125)

        self.OrganizationTable.heading("#0",text="",anchor=CENTER)
        self.OrganizationTable.heading("organization_id",text="Id",anchor=CENTER)
        self.OrganizationTable.heading("organization_name",text="Organization",anchor=CENTER)
        self.OrganizationTable.heading("network_name",text="Network",anchor=CENTER)
        #self.OrganizationTable.heading("selected",text="",anchor=CENTER)

        self.OrganizationTable.pack(side=BOTTOM,expand=YES,fill=BOTH,padx=3,pady=2)
        self.OrganizationTable.bind("<ButtonRelease-1>",self.select)
        self.apikey.pack(side=LEFT,expand=YES, fill=BOTH)

        self.configure = Frame(self.grupoAPI.interior())
        self.addRule = Button(self.configure,text="Configurar",command=self.configurar)
        self.addRule.pack(side=RIGHT,padx=120)
        self.configure.pack(side=BOTTOM,expand=YES, fill=BOTH)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Configuración Notebook                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::        
        self.configNotebook.pack(expand=YES, fill=BOTH)
        self.configNotebook.add(self.masterConfig,text="Configuración")
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Acciones                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  
    def select(self,event=None):
        self.OrganizationTable.selection_toggle(self.OrganizationTable.focus())
        #print (self.OrganizationTable.selection())

    def Show(self):
        newConfigObj = getStarted(self.apikeyValue.get())
        self.merakiInfo = newConfigObj.getInfo()
        n = 1
        for organization in self.merakiInfo:
            for network in organization['networks']:
                self.OrganizationTable.insert(parent='',index='end',iid=n,text='',values=(n,organization['organizationName'],network['Name']))
                n+=1

    def configurar(self):
        curItem = self.OrganizationTable.selection()
        aux = []
        for item in curItem:
            #print(self.OrganizationTable.item(item)['values'])
            for organization in self.merakiInfo:
                seleccion = self.OrganizationTable.item(item)['values']
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
                        

root = Tk()
root.geometry("800x500")
root.resizable(width=False, height=False)

configuracion = Configuracion(root)

root.mainloop()