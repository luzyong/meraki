from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import Pmw as pmw
from PIL import Image, ImageTk
import json
from networks import Networks

class Organizations():

    def __init__(self, root):
        self.root = root
        self.syslogValue = StringVar()
        self.OrganizationNotebook = ttk.Notebook(root)
        self.file = open('../data/currentConfig.json')
        self.currentConfig = json.load(self.file)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                           Página de templates disponibles                                ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.availableOrganization = Frame(self.OrganizationNotebook)
        self.groupOrganization = pmw.Group(self.availableOrganization,tag_text="Organizaciones Disponibles para el usuario")
        self.groupOrganization.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        self.OrganizationTable = ttk.Treeview(self.groupOrganization.interior())
        self.OrganizationTable['columns'] = ('organization_id', 'organization_name')

        self.OrganizationTable.column("#0", width=0,  stretch=NO)
        self.OrganizationTable.column("organization_id",anchor=CENTER,width=5)
        self.OrganizationTable.column("organization_name",anchor=CENTER,width=495)

        self.OrganizationTable.heading("#0",text="",anchor=CENTER)
        self.OrganizationTable.heading("organization_id",text="Id",anchor=CENTER)
        self.OrganizationTable.heading("organization_name",text="Name",anchor=CENTER)

        self.show()

        self.OrganizationTable.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        self.OrganizationTable.bind("<ButtonRelease-1>",self.select)
        self.availableOrganization.pack()
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Configuración Notebook                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.OrganizationNotebook.pack(expand=YES, fill=BOTH)
        self.OrganizationNotebook.add(self.availableOrganization,text="Organizaciones Disponibles")
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Acciones                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  
    def select(self,event=None):
        curItem = self.OrganizationTable.focus()
        org = self.OrganizationTable.item(curItem)['values'][1]
        ventanaNetwork= Networks(self.root,org,self.currentConfig)
        print (self.OrganizationTable.item(curItem))

    def show(self):
        n = 1
        aux = ''
        for item in self.currentConfig[0]['configuration']:
            if item['org_name'] != aux:
                aux = item['org_name']
                self.OrganizationTable.insert(parent='',index='end',iid=n,text='',values=(n,aux))
                n+=1

root = Tk()
root.geometry("800x500")
root.resizable(width=False, height=False)

ventana = Organizations(root)

root.mainloop()