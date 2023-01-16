from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import Pmw as pmw
from PIL import Image, ImageTk
import json,re,sys
sys.path.append("..\\")
from controls import contentFiltering as cf, threat , layer3 as L3, layer7 as L7

class SecurityConfig():

    def __init__(self, root,meraki='',networkId=''):
        self.root = root
        self.networkId = networkId
        self.merakiInfo = meraki
        self.contentFiltering = cf.getContentFiltering()
        self.AMP = threat.getAMP()
        self.intrusion = threat.getIntrusion()
        self.L3 = L3.getLayer3()
        self.L3inbound = L3.getInbound()
        self.L7 = L7.getLayer7()


        self.ContentNotebook = ttk.Notebook(root)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                           Página de content filtering                               ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.wholecontainer = Frame(self.ContentNotebook)
        self.categoryBlocking = Frame(self.wholecontainer)
        self.groupContent = pmw.Group(self.categoryBlocking,tag_text="Categorías de bloqueo")
        self.groupContent.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        self.ContentContainer = Frame(self.groupContent.interior())
        self.ContentLabel = Label(self.ContentContainer,text="Categorías de contenido").pack(side=TOP)
        self.Content = Listbox(self.ContentContainer)
        self.Content.pack(side=TOP,anchor=CENTER,ipadx=45)
        self.ContentContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.ThreatContainer = Frame(self.groupContent.interior())
        self.ThreatLabel = Label(self.ThreatContainer,text="Categorías de amenaza").pack(side=TOP)
        self.Threat = Listbox(self.ThreatContainer)      
        self.Threat.pack(side=TOP,anchor=CENTER,ipadx=45)
        self.ThreatContainer.pack(side=LEFT,expand=YES,fill=BOTH)
        self.categoryBlocking.pack(expand=YES,fill=BOTH)


        self.urlFiltering = Frame(self.wholecontainer)
        self.groupURLContent = pmw.Group(self.urlFiltering,tag_text="Filtrado URL")
        self.groupURLContent.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        
        self.blockedContainer = Frame(self.groupURLContent.interior())
        self.blockedLabel = Label(self.blockedContainer,text="Lista de URL bloqueadas").pack(side=TOP)
        self.blocked = Listbox(self.blockedContainer)
        self.blocked.pack(side=TOP,anchor=CENTER,ipadx=45)
        self.blockedContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.allowedContainer = Frame(self.groupURLContent.interior())
        self.allowedLabel = Label(self.allowedContainer,text="Lista de URL permitidas").pack(side=TOP)
        self.allowed = Listbox(self.allowedContainer)
        self.allowed.pack(side=TOP,anchor=CENTER,ipadx=55)
        self.allowedContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.urlFiltering.pack(expand=YES,fill=BOTH)

        self.wholecontainer.pack(side=BOTTOM,expand=YES)
        
         #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                           Página de threat protection                              ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.wholethreatcontainer = Frame(self.ContentNotebook)
        self.amp = Frame(self.wholethreatcontainer)
        self.groupamp = pmw.Group(self.amp,tag_text="Advanced Malware Protection (AMP)")
        self.groupamp.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        
        self.ampContainer = Frame(self.groupamp.interior())
        self.modeContainer = Frame(self.ampContainer)
        self.modeLabel = Label(self.modeContainer,text="Modo").pack(side=LEFT)
        self.modeEntry = Entry(self.modeContainer)
        self.modeEntry.pack(side=LEFT)
        self.modeContainer.pack(side=TOP,expand=YES)
        self.urllistContainer = Frame(self.ampContainer)
        self.allowurlLabel = Label(self.urllistContainer,text="Lista de URL permitidas").pack(side=LEFT)
        self.allowurlEntry = Entry(self.urllistContainer)
        self.allowurlEntry.pack(side=LEFT)
        self.urllistContainer.pack(side=TOP,expand=YES)
        self.filelistContainer = Frame(self.ampContainer)
        self.allowfileLabel = Label(self.filelistContainer,text="Lista de archivos permitidos").pack(side=LEFT)
        self.allowfileEntry = Entry(self.filelistContainer)
        self.allowfileEntry.pack(side=LEFT)
        self.filelistContainer.pack(side=TOP,expand=YES)
        self.ampContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.groupintrusion = pmw.Group(self.amp,tag_text="Advanced Malware Protection (AMP)")
        self.groupintrusion.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        self.intrusionContainer = Frame(self.groupintrusion.interior())
        self.modeintrusionContainer = Frame(self.intrusionContainer)
        self.modeintrusionLabel = Label(self.modeintrusionContainer,text="Modo").pack(side=LEFT)
        self.modeintrusionEntry = Entry(self.modeintrusionContainer)
        self.modeintrusionEntry.pack(side=LEFT)
        self.modeintrusionContainer.pack(side=TOP,expand=YES)
        self.intrusionContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.amp.pack(expand=YES,fill=BOTH)
        self.wholethreatcontainer.pack(side=BOTTOM,expand=YES)
                #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                          Página de creacion de nuevo template L3                         ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.Label3 = Frame(self.ContentNotebook)
        self.inbound = Frame(self.Label3)
        self.groupLabel3 = pmw.Group(self.inbound,tag_text="Inbound")
        self.groupLabel3.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        self.newTemplatel3 = Frame(self.groupLabel3.interior())

        self.L3Table = ttk.Treeview(self.newTemplatel3)
        self.L3Table['columns'] = ('L3_id', 'L3_policy','L3_description','L3_protocol','L3_source','L3_src','L3_destination','L3_dst','L3_syslog')

        self.L3Table.column("#0", width=0,  stretch=NO)
        self.L3Table.column("L3_id",anchor=CENTER,width=5)
        self.L3Table.column("L3_policy",anchor=CENTER,width=62)
        self.L3Table.column("L3_description",anchor=CENTER,width=62)
        self.L3Table.column("L3_protocol",anchor=CENTER,width=62)
        self.L3Table.column("L3_source",anchor=CENTER,width=62)
        self.L3Table.column("L3_src",anchor=CENTER,width=62)
        self.L3Table.column("L3_destination",anchor=CENTER,width=62)
        self.L3Table.column("L3_dst",anchor=CENTER,width=62)
        self.L3Table.column("L3_syslog",anchor=CENTER,width=62)

        self.L3Table.heading("#0",text="",anchor=CENTER)
        self.L3Table.heading("L3_id",text="Id",anchor=CENTER)
        self.L3Table.heading("L3_policy",text="Política",anchor=CENTER)
        self.L3Table.heading("L3_description",text="Descripción de la regla",anchor=CENTER)
        self.L3Table.heading("L3_protocol",text="Protocolo",anchor=CENTER)
        self.L3Table.heading("L3_source",text="Source",anchor=CENTER)
        self.L3Table.heading("L3_src",text="Puerto Src",anchor=CENTER)
        self.L3Table.heading("L3_destination",text="Destino",anchor=CENTER)
        self.L3Table.heading("L3_dst",text="Puerto Dst",anchor=CENTER)
        self.L3Table.heading("L3_syslog",text="Syslog",anchor=CENTER)
        
        self.L3Table.pack(side=BOTTOM,expand=YES,fill=BOTH,padx=3,pady=2)

        self.newTemplatel3.pack(side=LEFT,expand=YES, fill=BOTH)
        self.inbound.pack(expand=YES,fill=BOTH)

        self.outbound = Frame(self.Label3)
        self.groupOLabel3 = pmw.Group(self.outbound,tag_text="Outbound")
        self.groupOLabel3.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        self.newTemplateOl3 = Frame(self.groupOLabel3.interior())

        self.L3TableO = ttk.Treeview(self.newTemplateOl3)
        self.L3TableO['columns'] = ('L3_id', 'L3_policy','L3_description','L3_protocol','L3_source','L3_src','L3_destination','L3_dst','L3_syslog')

        self.L3TableO.column("#0", width=0,  stretch=NO)
        self.L3TableO.column("L3_id",anchor=CENTER,width=5)
        self.L3TableO.column("L3_policy",anchor=CENTER,width=62)
        self.L3TableO.column("L3_description",anchor=CENTER,width=62)
        self.L3TableO.column("L3_protocol",anchor=CENTER,width=62)
        self.L3TableO.column("L3_source",anchor=CENTER,width=62)
        self.L3TableO.column("L3_src",anchor=CENTER,width=62)
        self.L3TableO.column("L3_destination",anchor=CENTER,width=62)
        self.L3TableO.column("L3_dst",anchor=CENTER,width=62)
        self.L3TableO.column("L3_syslog",anchor=CENTER,width=62)

        self.L3TableO.heading("#0",text="",anchor=CENTER)
        self.L3TableO.heading("L3_id",text="Id",anchor=CENTER)
        self.L3TableO.heading("L3_policy",text="Política",anchor=CENTER)
        self.L3TableO.heading("L3_description",text="Descripción de la regla",anchor=CENTER)
        self.L3TableO.heading("L3_protocol",text="Protocolo",anchor=CENTER)
        self.L3TableO.heading("L3_source",text="Source",anchor=CENTER)
        self.L3TableO.heading("L3_src",text="Puerto Src",anchor=CENTER)
        self.L3TableO.heading("L3_destination",text="Destino",anchor=CENTER)
        self.L3TableO.heading("L3_dst",text="Puerto Dst",anchor=CENTER)
        self.L3TableO.heading("L3_syslog",text="Syslog",anchor=CENTER)
        
        self.L3TableO.pack(side=BOTTOM,expand=YES,fill=BOTH,padx=3,pady=2)

        self.newTemplateOl3.pack(side=LEFT,expand=YES, fill=BOTH)
        self.outbound.pack(expand=YES,fill=BOTH)
        self.Label3.pack(side=LEFT,expand=YES, fill=BOTH)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Página de templates de L7                                 ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.Label7 = Frame(self.ContentNotebook)
        self.groupLabel7 = pmw.Group(self.Label7,tag_text="Reglas de Firewall")
        self.groupLabel7.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        self.newTemplatel7 = Frame(self.groupLabel7.interior())

        self.L7Table = ttk.Treeview(self.newTemplatel7)
        self.L7Table['columns'] = ('L7_id', 'L7_policy','L7_type','L7_value')

        self.L7Table.column("#0", width=0,  stretch=NO)
        self.L7Table.column("L7_id",anchor=CENTER,width=5)
        self.L7Table.column("L7_policy",anchor=CENTER,width=165)
        self.L7Table.column("L7_type",anchor=CENTER,width=165)
        self.L7Table.column("L7_value",anchor=CENTER,width=165)

        self.L7Table.heading("#0",text="",anchor=CENTER)
        self.L7Table.heading("L7_id",text="Id",anchor=CENTER)
        self.L7Table.heading("L7_policy",text="Política",anchor=CENTER)
        self.L7Table.heading("L7_type",text="Tipo",anchor=CENTER)
        self.L7Table.heading("L7_value",text="Valor",anchor=CENTER)
        
        
        self.L7Table.pack(side=BOTTOM,expand=YES,fill=BOTH,padx=3,pady=2)
        self.newTemplatel7.pack(side=LEFT,expand=YES, fill=BOTH)
        self.Label7.pack(side=LEFT,expand=YES, fill=BOTH)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Configuración Notebook                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.ContentNotebook.pack(expand=YES, fill=BOTH)
        self.ContentNotebook.add(self.wholecontainer,text="Content Filtering")
        self.ContentNotebook.add(self.wholethreatcontainer,text="Threat Protection")
        self.ContentNotebook.add(self.Label3,text="L3")
        self.ContentNotebook.add(self.Label7,text="L7")

        self.showCF()
        self.showTP()
        self.showL3()
        self.showL7()
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Acciones                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  

    def showCF(self):
        cfConfig,errorcode = self.contentFiltering.getInfo(self.networkId)
        if errorcode == "0":
            t=1
            c=1
            b=1
            a =1
            for category in cfConfig['blockedUrlCategories']:
                matchThreat = re.search(r'[meraki:contentFiltering/category/T]{1}[\d]+', category['id'])
                matchContent = re.search(r'[meraki:contentFiltering/category/C]{1}[\d]+', category['id'])
                if matchThreat != None:
                                self.Threat.insert(t, category['name'])
                                t+=1
                if matchContent != None:
                                self.Content.insert(c, category['name'])
                                c+=1
            for blocked in cfConfig['blockedUrlPatterns']:
                self.blocked.insert(b,blocked)
                b+=1
            for allowed in cfConfig['allowedUrlPatterns']:
                self.allowed.insert(a,allowed)
                a+=1
        if errorcode == "1":
            self.root.destroy()
            messagebox.showwarning(title = "Ooops",message = "Configuración disponible solo para redes MX")

    def showTP(self):
        aux = ''
        ampConfig, errorcode = self.AMP.getInfo(self.networkId)
        if errorcode == "0":
            self.allowfileEntry.delete(0,END)
            self.modeEntry.delete(0,END)
            self.allowfileEntry.delete(0,END)

            self.modeEntry.insert(0,ampConfig['mode'])

            if len(ampConfig['allowedUrls'])>0:
                for element in ampConfig['allowedUrls']:
                    aux += element+" "
                self.allowurlEntry.insert(0,aux)
            else: self.allowurlEntry.insert(0,'-')

            if len(ampConfig['allowedUrls'])>0:
                for element in ampConfig['allowedFiles']:
                    aux += element+" "
                self.allowfileEntry.insert(0,aux)
            else: self.allowfileEntry.insert(0,'-')
        intrusionConfig, errorcode = self.intrusion.getInfo(self.networkId)
        if errorcode == "0":
            self.modeintrusionEntry.insert(0,intrusionConfig['mode'])
            self.modeEntry.configure(state='disabled')
            self.allowfileEntry.configure(state='disabled')
            self.allowurlEntry.configure(state='disabled')
            self.modeintrusionEntry.configure(state='disabled')

    def showL3(self):
        outbound, errorcodeO = self.L3.getInfo(self.networkId)
        inbound, errorcodeI = self.L3inbound.getInfo(self.networkId)
        if errorcodeI == "0" and errorcodeO == "0":
            o=1
            i=1
            for rule in outbound['rules']:
                self.L3TableO.insert(parent='',index='end',iid=o,text='',values=(o,rule['policy'],rule['comment'],rule['protocol'],rule['srcCidr'],rule['srcPort'],rule['destCidr'],rule['destPort'],rule['syslogEnabled']))
                o+=1
            for rule in inbound['rules']:
                self.L3Table.insert(parent='',index='end',iid=i,text='',values=(i,rule['policy'],rule['comment'],rule['protocol'],rule['srcCidr'],rule['srcPort'],rule['destCidr'],rule['destPort'],rule['syslogEnabled']))
                i+=1
            
    def showL7(self):
        configL7, errorcode = self.L7.getInfo(self.networkId)
        if errorcode == "0":
            n=1
            for rule in configL7['rules']:
                self.L7Table.insert(parent='',index='end',iid=n,text='',values=(n,rule['policy'],rule['type'],rule['value']['name']))
                n+=1
#root = Tk()
#root.geometry("800x550")
#root.resizable(width=False, height=False)

#ventana = SecurityConfig(root)

#root.mainloop()