from tkinter import *
from tkinter import ttk
import Pmw as pmw
import sys
sys.path.append("..\\")
from controls.getstarted import getStarted 


import json

class Configuracion():
    

    def __init__(self, root):
        self.root = root
        self.apikeyValue = StringVar()
        self.merakiInfo = ""
        self.newConfig = []
        self.configNotebook = ttk.Notebook(root)

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
        self.containerLabel = Frame(self.apikey)
        self.apikeyLabel = Label(self.containerLabel,text="Para poder visualizar las redes disponibles en sus organizaciones, es necesario generar una API Key. \n\nIntroduzca su API Key")
        self.apikeyLabel.pack(side=TOP, expand=YES, fill=BOTH)
        self.containerLabel.pack(side=TOP, anchor=CENTER)
        self.containerEntry = Frame(self.apikey)
        self.apikeyEntry = Entry(self.containerEntry,textvariable=self.apikeyValue).pack(side=LEFT,expand=NO)
        self.buscar = Button(self.containerEntry,text="Buscar",command=self.Show)
        self.buscar.pack(side=LEFT, expand=NO, padx=2)
        self.containerEntry.pack(side=TOP, anchor=CENTER)
        self.containerResult = Frame(self.apikey)
        self.resultLabel = Label(self.containerResult,text="")
        self.resultLabel.pack(side=TOP, expand=YES, fill=BOTH)
        self.containerResult.pack(side=TOP, anchor=CENTER)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Subgrupo Resultados                                       ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.apikey.pack(side=TOP,expand=YES, fill=BOTH)

        self.configure = Frame(self.grupoAPI.interior())
        self.addRule = Button(self.configure,text="Comenzar",command=self.configurar)
        self.addRule.pack(side=RIGHT,padx=120)
        self.addRule.config(state='disabled')
        self.configure.pack(side=TOP,expand=YES, fill=BOTH)
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


    def Show(self):
        data = {
                "apiKey":self.apikeyValue.get()
                }
        with open('../data/currentUser.json','w') as fp:
            json.dump(data,fp,indent = 4)
        newConfigObj = getStarted()
        self.merakiInfo,status = newConfigObj.getInfo()
        if status:
            self.addRule.config(state='normal')
            self.resultLabel.config(text="Su API Key es válida y puede comenzar a usar la aplicación")
        else:
            self.resultLabel.config(text="Su API Key es inválida, por favor verifíquela")


    def configurar(self):
        from organizationsView import Organizations
        self.root.destroy()
        root = Tk()
        root.geometry("800x500")
        root.resizable(width=False, height=False)

        ventanaOrganization = Organizations(root,self.merakiInfo)

        root.mainloop()
        
                        

root = Tk()

root.geometry("800x500")
root.resizable(width=False, height=False)
root.wm_title("VOSEDA NETWORKS -- Meraki Client")
root.iconbitmap("isotipo_voseda_color.ico")
configuracion = Configuracion(root)

root.mainloop()