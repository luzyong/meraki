from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import Pmw as pmw
from PIL import Image, ImageTk
import json
from networks import Networks
from networks2 import NetworksTemplate

class Organizations():

    def __init__(self, root, api='',meraki=''):
        self.root = root
        self.apikeyValue = api
        self.merakiInfo = meraki
        self.templates = StringVar()
        self.OrganizationNotebook = ttk.Notebook(root)
        self.ventanaNetwork = None
        #self.file = open('../data/currentConfig.json')
        #self.currentConfig = json.load(self.file)


        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                           Página de organizaciones disponibles                                ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.availableOrganization = Frame(self.OrganizationNotebook)
        self.groupOrganization = pmw.Group(self.availableOrganization,tag_text="Organizaciones Disponibles para el usuario")
        self.groupOrganization.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        
        self.apikey = Frame(self.groupOrganization.interior())


        self.OrganizationTable = ttk.Treeview(self.groupOrganization.interior())
        self.OrganizationTable['columns'] = ('organization_id', 'organization_name')

        self.OrganizationTable.column("#0", width=0,  stretch=NO)
        self.OrganizationTable.column("organization_id",anchor=CENTER,width=5)
        self.OrganizationTable.column("organization_name",anchor=CENTER,width=495)

        self.OrganizationTable.heading("#0",text="",anchor=CENTER)
        self.OrganizationTable.heading("organization_id",text="Id",anchor=CENTER)
        self.OrganizationTable.heading("organization_name",text="Name",anchor=CENTER)

        

        self.OrganizationTable.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        self.OrganizationTable.bind("<ButtonRelease-1>",self.select)
        self.availableOrganization.pack()
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                           Página de asignación de templates disponibles                                ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.availableTemplateOrganization = Frame(self.OrganizationNotebook)
        self.groupTemplateOrganization = pmw.Group(self.availableTemplateOrganization,tag_text="Organizaciones Disponibles para el usuario")
        self.groupTemplateOrganization.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        
        
        self.TemplatesDisponiblesContainer = Frame(self.groupTemplateOrganization.interior())
        self.TemplatesDisponibles = Listbox(self.TemplatesDisponiblesContainer)
        #self.TemplatesDisponibles = ttk.Combobox(self.TemplatesDisponiblesContainer, textvariable=self.templates)
        self.TemplatesDisponibles.insert(1, "Nachos")
        self.TemplatesDisponibles.insert(2, "Sandwich")
        self.TemplatesDisponibles.insert(3, "Burger")
        self.TemplatesDisponibles.insert(4, "Pizza")
        self.TemplatesDisponibles.insert(5, "Burrito")
        #self.TemplatesDisponibles['values'] = ("true","false")
        self.okay = Button(self.TemplatesDisponiblesContainer,text="Mostrar redes compatibles",command=self.selectTemplateOrg)
        self.okay.pack(side=BOTTOM)
        
        self.TemplatesDisponibles.pack(side=BOTTOM,anchor=CENTER,padx=12.5,pady=1)
        self.TemplatesDisponiblesContainer.pack(side=LEFT)


        self.OrganizationTableTemplate = ttk.Treeview(self.groupTemplateOrganization.interior())
        self.OrganizationTableTemplate['columns'] = ('organization_id', 'organization_name')

        self.OrganizationTableTemplate.column("#0", width=0,  stretch=NO)
        self.OrganizationTableTemplate.column("organization_id",anchor=CENTER,width=5)
        self.OrganizationTableTemplate.column("organization_name",anchor=CENTER,width=495)

        self.OrganizationTableTemplate.heading("#0",text="",anchor=CENTER)
        self.OrganizationTableTemplate.heading("organization_id",text="Id",anchor=CENTER)
        self.OrganizationTableTemplate.heading("organization_name",text="Name",anchor=CENTER)


        self.OrganizationTableTemplate
        self.OrganizationTableTemplate.pack(side=BOTTOM,expand=YES,fill=BOTH,padx=3,pady=2)
        self.OrganizationTableTemplate.bind("<ButtonRelease-2>",self.selectTemplateOrg)
        self.availableTemplateOrganization.pack(side=LEFT)
        
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Configuración Notebook                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.OrganizationNotebook.pack(expand=YES, fill=BOTH)
        self.OrganizationNotebook.add(self.availableOrganization,text="Organizaciones Disponibles")
        self.OrganizationNotebook.add(self.availableTemplateOrganization,text="Asignar Templates")
        self.show()
        #if self.OrganizationTableTemplate.focus() == '' or self.TemplatesDisponibles.curselection() == '':
        #    self.okay.config(state='disabled')
        
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Acciones                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  
    def selectTemplateOrg(self, event=None):
        
        curOrgItem = self.OrganizationTableTemplate.focus()
        curTempItem = self.TemplatesDisponibles.curselection()

        if curTempItem != '' and curOrgItem != '':

            org = self.OrganizationTableTemplate.item(curOrgItem)['values'][1]
            tmplt = self.TemplatesDisponibles.get(curTempItem)
            ventanaTemplates = NetworksTemplate(root=self.root,meraki=self.merakiInfo,organization=org,template=tmplt)
        print(org,tmplt)
        print("Hola")
        
        #self.ventanaNetwork.update('')

    def select(self,event=None):
        curItem = self.OrganizationTable.focus()
        org = self.OrganizationTable.item(curItem)['values'][1]
        
        if self.ventanaNetwork == None:
            self.ventanaNetwork= Networks(self.root,org,self.merakiInfo)
            
        else:
            self.ventanaNetwork.update(org)


    def show(self):
        n = 1
        for organization in self.merakiInfo:
            self.OrganizationTable.insert(parent='',index='end',iid=n,text='',values=(n,organization['organizationName']))
            self.OrganizationTableTemplate.insert(parent='',index='end',iid=n,text='',values=(n,organization['organizationName']))
            n+=1
        """aux = ''
        for item in self.currentConfig[0]['configuration']:
            if item['org_name'] != aux:
                aux = item['org_name']
                self.OrganizationTable.insert(parent='',index='end',iid=n,text='',values=(n,aux))
                n+=1"""

#root = Tk()
#root.geometry("800x500")
#root.resizable(width=False, height=False)

#ventana = Organizations(root)

#root.mainloop()