from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import Pmw as pmw
from PIL import Image, ImageTk
from views.networksView import Networks
from views.networksTemplateView import NetworksTemplate
from views.templatesView import Templates,init

import json,re,os,sys
sys.path.append("..\\")
from controls import contentFiltering as cf, threat , layer3 as L3, layer7 as L7

class Organizations():

    def __init__(self, root,meraki=''):
        self.root = root
        self.root.wm_title("VOSEDA NETWORKS -- Meraki Client")
        self.root.iconbitmap("isotipo_voseda_color.ico")
        self.merakiInfo = meraki
        self.networksID = ''
        self.templateName = ''
        self.organization = ''
        self.templates = StringVar()

        self.contentFiltering = cf.setContentFiltering()
        self.AMP = threat.setAMP()
        self.intrusion = threat.setIntrusion()
        self.L3 = L3.setLayer3()
        self.L3inbound = L3.setInbound()
        self.L7 = L7.setLayer7()
        self.ventanaNetwork = None
        self.ventanaTemplateNetwork = None
        self.templatesFiles = os.listdir("../data/templates")



        menu = Menu(self.root)
        self.root.config(menu=menu)
        optionMenu = Menu(menu)
        optionMenu.add_command(label="Configuracion",command=self.option)
        menu.add_cascade(label="Opciones", menu=optionMenu)
        viewMenu = Menu(menu)
        viewMenu.add_command(label="Templates",command=self.views)
        menu.add_cascade(label="Ver", menu=viewMenu)
        self.OrganizationNotebook = ttk.Notebook(root)
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
        self.OrganizationTable.heading("organization_name",text="Nombre de la organización",anchor=CENTER)

        

        self.OrganizationTable.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        self.OrganizationTable.bind("<ButtonRelease>",self.select)
        self.redFrame = Frame(self.availableOrganization)
        self.redFrame.pack(side=BOTTOM,expand=YES,fill=BOTH)
        self.availableOrganization.pack()
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                           Página de asignación de templates disponibles                                ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.availableTemplateOrganization = Frame(self.OrganizationNotebook)
        self.groupTemplateOrganization = pmw.Group(self.availableTemplateOrganization,tag_text="Organizaciones Disponibles para el usuario")
        self.groupTemplateOrganization.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        
        
        self.TemplatesDisponiblesContainer = Frame(self.groupTemplateOrganization.interior())
        self.TemplatesDisponiblesLabel = Label(self.TemplatesDisponiblesContainer,text="Templates").pack(side=TOP)
        self.TemplatesDisponibles = Listbox(self.TemplatesDisponiblesContainer)
        self.showTemplates()    
        self.TemplatesDisponibles.pack(side=BOTTOM,anchor=CENTER,padx=12.5,pady=1)
        self.TemplatesDisponiblesContainer.pack(side=LEFT)


        self.OrganizationTableTemplate = ttk.Treeview(self.groupTemplateOrganization.interior())
        self.OrganizationTableTemplate['columns'] = ('organization_id', 'organization_name')

        self.OrganizationTableTemplate.column("#0", width=0,  stretch=NO)
        self.OrganizationTableTemplate.column("organization_id",anchor=CENTER,width=5)
        self.OrganizationTableTemplate.column("organization_name",anchor=CENTER,width=495)

        self.OrganizationTableTemplate.heading("#0",text="",anchor=CENTER)
        self.OrganizationTableTemplate.heading("organization_id",text="Id",anchor=CENTER)
        self.OrganizationTableTemplate.heading("organization_name",text="Nombre de la organización",anchor=CENTER)
        self.OrganizationTableTemplate.pack(side=BOTTOM,expand=YES,fill=BOTH,padx=3,pady=2)
        self.OrganizationTableTemplate.bind("<ButtonRelease>",self.selectTemplateOrg,add='+')

        self.redTemplateFrame = Frame(self.availableTemplateOrganization)
        self.redTemplateFrame.pack(side=BOTTOM,expand=YES,fill=BOTH)

        self.sendContainer = Frame(self.redTemplateFrame)
        self.enviar = Button(self.sendContainer,text="Configurar Template",command=self.configurar)
        self.enviar.pack(side=RIGHT,padx=120)
        self.sendContainer.pack(side=BOTTOM,expand=YES,fill=BOTH)
        self.availableTemplateOrganization.pack(side=BOTTOM)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Configuración Notebook                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.OrganizationNotebook.pack(expand=YES, fill=BOTH)
        self.OrganizationNotebook.add(self.availableOrganization,text="Organizaciones Disponibles")
        self.OrganizationNotebook.add(self.availableTemplateOrganization,text="Asignar Templates")
        self.show()  
        
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Acciones                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  
    def selectTemplateOrg(self, event=None):
        
        curOrgItem = self.OrganizationTableTemplate.focus()
        curTempItem = self.TemplatesDisponibles.curselection()

        if curTempItem != '' and curOrgItem != '':

            self.organization = self.OrganizationTableTemplate.item(curOrgItem)['values'][1]
            self.templateName = self.TemplatesDisponibles.get(curTempItem)
            if self.ventanaTemplateNetwork == None: 
                
                self.ventanaTemplateNetwork = NetworksTemplate(root=self.redTemplateFrame,meraki=self.merakiInfo,organization=self.organization)
                self.root.resizable(width=True, height=True)
                self.root.geometry("800x700")
                self.root.resizable(width=False, height=False)
                self.root.wm_title("VOSEDA NETWORKS -- Meraki Client")
                self.root.iconbitmap("isotipo_voseda_color.ico")
            else:
                self.ventanaTemplateNetwork.update(self.organization)


    def select(self,event=None):
        curItem = self.OrganizationTable.focus()
        org = self.OrganizationTable.item(curItem)['values'][1]
        
        if self.ventanaNetwork == None: 
            self.ventanaNetwork= Networks(self.redFrame,org,self.merakiInfo)            
        else:
            self.ventanaNetwork.update(org)


    def show(self):
        n = 1
        for organization in self.merakiInfo:
            self.OrganizationTable.insert(parent='',index='end',iid=n,text='',values=(n,organization['organizationName']))
            self.OrganizationTableTemplate.insert(parent='',index='end',iid=n,text='',values=(n,organization['organizationName']))
            n+=1
    def showTemplates(self):
        n=1
        for file in self.templatesFiles:
            extension = re.findall(r".txt|.json|.csv|.docx",file)
            templateName = file.replace(extension[0],"")
            self.TemplatesDisponibles.insert(n,templateName)
            n+=1
    
    def configurar(self):
        self.networksID = self.ventanaTemplateNetwork.getNets()
        templateInfo = json.load(open(f"../data/templates/{self.templateName}.json"))
        keys = templateInfo.keys()
        for key in keys:
            if templateInfo[key] == "" : 
                continue
            if key == 'content_filtering':
                self.contentFiltering.getInfo(self.networksID,templateInfo['content_filtering'])
            if key == 'intrusion':
                self.intrusion.getInfo(self.networksID,templateInfo['intrusion'])
            if key == 'malware':
                self.AMP.getInfo(self.networksID,templateInfo['malware'])
            if key == 'L3_inbound':
                self.L3inbound.getInfo(self.networksID,templateInfo['L3_inbound'])
            if key == 'L3_outbound':
                self.L3.getInfo(self.networksID,templateInfo['L3_outbound'])
            if key == 'L7':
                self.L7.getInfo(self.networksID,templateInfo['L7'])
            
    
    def views(self):
        ventana = init()
        

    def option(self):
        from views.configuracionView import Configuracion,init as cinit
        self.root.destroy()
        ventana = cinit()
