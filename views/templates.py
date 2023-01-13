from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import Pmw as pmw
from PIL import Image, ImageTk
import os,re

class Templates():

    def __init__(self, root):
        self.syslogValue = StringVar()
        self.webSearch = StringVar()
        self.youtube = StringVar()
        self.templatesFiles = os.listdir("../data/templates")
        self.templateNotebook = ttk.Notebook(root)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                           Página de templates disponibles                                ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.availableTemplates = Frame(self.templateNotebook)
        self.groupTemplates = pmw.Group(self.availableTemplates,tag_text="Templates Disponibles")
        self.groupTemplates.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        self.templatesTable = ttk.Treeview(self.groupTemplates.interior())
        self.templatesTable['columns'] = ('template_id', 'template_name', 'template_compatibility')

        self.templatesTable.column("#0", width=0,  stretch=NO)
        self.templatesTable.column("template_id",anchor=CENTER, width=80)
        self.templatesTable.column("template_name",anchor=CENTER,width=80)
        self.templatesTable.column("template_compatibility",anchor=CENTER,width=80)

        self.templatesTable.heading("#0",text="",anchor=CENTER)
        self.templatesTable.heading("template_id",text="Id",anchor=CENTER)
        self.templatesTable.heading("template_name",text="Name",anchor=CENTER)
        self.templatesTable.heading("template_compatibility",text="Compatibility",anchor=CENTER)
        self.showTemplates()

        self.templatesTable.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        
        self.availableTemplates.pack()
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                          Página de creacion de nuevo template L3                         ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.Label3 = Frame(self.templateNotebook)
        self.groupLabel3 = pmw.Group(self.Label3,tag_text="Template")
        self.groupLabel3.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        self.newTemplatel3 = Frame(self.groupLabel3.interior())
        self.nombre = Label(self.newTemplatel3,text="Nombre").pack(side=LEFT)
        self.nombreIn = Entry(self.newTemplatel3).pack(side=LEFT)

        self.groupconfigL3 = pmw.Group(self.groupLabel3.interior(),tag_text="L3")
        self.groupconfigL3.pack(side=BOTTOM,expand=YES,fill=BOTH,padx=3,pady=2)

        self.configL31 = Frame(self.groupconfigL3.interior())
        self.commentcontainer = Frame(self.configL31)
        self.comment = Label(self.commentcontainer,text="Comentario").pack(side=LEFT,anchor=CENTER,padx=8,pady=1)
        self.commentIn = Entry(self.commentcontainer).pack(side=LEFT,anchor=CENTER,padx=8,pady=1)
        self.commentcontainer.pack(side=LEFT,expand=YES)
        self.protocolcontainer = Frame(self.configL31)        
        self.protocol = Label(self.protocolcontainer,text="Protocolo").pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.protcolIn = Entry(self.protocolcontainer).pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.protocolcontainer.pack(side=LEFT,expand=YES)
        self.configL31.pack(side=TOP,expand=YES, fill=BOTH)

        self.configL32 = Frame(self.groupconfigL3.interior())
        self.cidrcontainer = Frame(self.configL32)
        self.destCidr = Label(self.cidrcontainer,text="destCidr").pack(side=LEFT,anchor=CENTER,padx=16,pady=1)
        self.destCidrIn = Entry(self.cidrcontainer).pack(side=LEFT,anchor=CENTER,padx=16,pady=1)
        self.cidrcontainer.pack(side=LEFT,expand=YES)
        self.sourcecontainer = Frame(self.configL32)
        self.source = Label(self.sourcecontainer,text="Source Cid").pack(side=LEFT,anchor=CENTER,padx=5.5,pady=1)
        self.sourceIn = Entry(self.sourcecontainer).pack(side=LEFT,anchor=CENTER,padx=5.5,pady=1)
        self.sourcecontainer.pack(side=LEFT,expand=YES)
        self.configL32.pack(side=TOP,expand=YES, fill=BOTH)

        self.configL33 = Frame(self.groupconfigL3.interior())
        self.destcontainer = Frame(self.configL33)
        self.destPort = Label(self.destcontainer,text="Puerto Destino").pack(side=LEFT,anchor=CENTER,padx=5,pady=1)
        self.destPortIn = Entry(self.destcontainer).pack(side=LEFT,anchor=CENTER,padx=5,pady=1)
        self.destcontainer.pack(side=LEFT,expand=YES)
        self.origincontainer = Frame(self.configL33)
        self.originPort = Label(self.origincontainer,text="Puerto Origen").pack(side=LEFT,anchor=CENTER,padx=5,pady=1)
        self.originPortIn = Entry(self.origincontainer).pack(side=LEFT,anchor=CENTER,padx=5,pady=1)
        self.origincontainer.pack(side=LEFT,expand=YES)
        self.configL33.pack(side=TOP,expand=YES, fill=BOTH)

        self.configL34 = Frame(self.groupconfigL3.interior())
        self.policycontainer = Frame(self.configL34)
        self.policy = Label(self.policycontainer,text="Política").pack(side=LEFT,anchor=CENTER,padx=22,pady=1)
        self.policyIn = Entry(self.policycontainer).pack(side=LEFT,anchor=CENTER,padx=22,pady=1)
        self.policycontainer.pack(side=LEFT,expand=YES)
        self.syslogcontainer = Frame(self.configL34)
        self.syslog = Label(self.syslogcontainer,text="syslog Enabled").pack(side=LEFT,anchor=CENTER,padx=12.5,pady=1)
        self.syslogIn = ttk.Combobox(self.syslogcontainer, textvariable=self.syslogValue)
        self.syslogIn['values'] = ("true","false")
        self.syslogIn.pack(side=LEFT,anchor=CENTER,padx=12.5,pady=1)
        self.syslogcontainer.pack(side=LEFT,expand=YES)
        self.configL34.pack(side=TOP,expand=YES, fill=BOTH)

        self.configL35 = Frame(self.groupconfigL3.interior())
        self.addRule = Button(self.configL35,text="Agregar Regla")
        self.addRule.pack(side=RIGHT,padx=120)
        self.configL35.pack(side=TOP,expand=YES, fill=BOTH)

        self.newTemplatel3.pack(side=LEFT,expand=YES, fill=BOTH)
        self.Label3.pack(side=LEFT,expand=YES, fill=BOTH)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Página de templates de L7                                 ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.Label7 = Frame(self.templateNotebook)
        self.groupLabel7 = pmw.Group(self.Label7,tag_text="Template")
        self.groupLabel7.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        self.newTemplatel7 = Frame(self.groupLabel7.interior())
        self.nombrel7 = Label(self.newTemplatel7,text="Nombre").pack(side=LEFT)
        self.nombrel7In = Entry(self.newTemplatel7).pack(side=LEFT)

        self.groupconfigL7= pmw.Group(self.groupLabel7.interior(),tag_text="L7")
        self.groupconfigL7.pack(side=BOTTOM,expand=YES,fill=BOTH,padx=3,pady=2)

        self.configL71 = Frame(self.groupconfigL7.interior())
        self.policyl7container = Frame(self.configL71)
        self.policyl7 = Label(self.policyl7container,text="Política").pack(side=LEFT,anchor=CENTER,padx=8,pady=1)
        self.policyl7In = Entry(self.policyl7container).pack(side=LEFT,anchor=CENTER,padx=8,pady=1)
        self.policyl7container.pack(side=TOP,expand=YES)
        self.typecontainer = Frame(self.configL71)        
        self.type = Label(self.typecontainer,text="Tipo").pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.typeIn = Entry(self.typecontainer).pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.typecontainer.pack(side=TOP,expand=YES)
        self.valuecontainer = Frame(self.configL71)        
        self.value = Label(self.valuecontainer,text="Valor").pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.valueIn = Entry(self.valuecontainer).pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.valuecontainer.pack(side=TOP,expand=YES)
        self.configL71.pack(side=TOP,expand=YES, fill=BOTH)

        self.configL72 = Frame(self.groupconfigL7.interior())
        self.addRulel7 = Button(self.configL72,text="Agregar Regla")
        self.addRulel7.pack(side=RIGHT,padx=120)
        self.configL72.pack(side=TOP,expand=YES, fill=BOTH)

        self.newTemplatel7.pack(side=LEFT,expand=YES, fill=BOTH)
        self.Label7.pack(side=LEFT,expand=YES, fill=BOTH)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Página de content filtering                                 ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.wholecontainer = Frame(self.templateNotebook)
        self.categoryBlocking = Frame(self.wholecontainer)
        self.groupContent = pmw.Group(self.categoryBlocking,tag_text="Categorías de bloqueo")
        self.groupContent.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        self.ContentContainer = Frame(self.groupContent.interior())
        self.ContentLabel = Label(self.ContentContainer,text="Categorías de contenido").pack(side=TOP)
        self.Content = Entry(self.ContentContainer).pack(side=TOP,anchor=CENTER,ipadx=10,ipady=45)
        self.ContentContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.ThreatContainer = Frame(self.groupContent.interior())
        self.ThreatLabel = Label(self.ThreatContainer,text="Categorías de amenaza").pack(side=TOP)
        self.Threat = Entry(self.ThreatContainer).pack(side=TOP,anchor=CENTER,ipadx=10,ipady=45)
        self.ThreatContainer.pack(side=LEFT,expand=YES,fill=BOTH)
        self.categoryBlocking.pack(expand=YES,fill=BOTH)


        self.urlFiltering = Frame(self.wholecontainer)
        self.groupURLContent = pmw.Group(self.urlFiltering,tag_text="Filtrado URL")
        self.groupURLContent.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        
        self.blockedContainer = Frame(self.groupURLContent.interior())
        self.blockedLabel = Label(self.blockedContainer,text="Lista de URL bloqueadas").pack(side=TOP)
        self.blocked = Entry(self.blockedContainer).pack(side=TOP,anchor=CENTER,ipadx=10,ipady=45)
        self.blockedContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.allowedContainer = Frame(self.groupURLContent.interior())
        self.allowedLabel = Label(self.allowedContainer,text="Lista de URL permitidas").pack(side=TOP)
        self.allowed = Entry(self.allowedContainer).pack(side=TOP,anchor=CENTER,ipadx=10,ipady=45)
        self.allowedContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.urlFiltering.pack(expand=YES,fill=BOTH)


        self.searchFiltering = Frame(self.wholecontainer)
        self.groupsearchFiltering = pmw.Group(self.searchFiltering,tag_text="Filtrado de búsquedas")
        self.groupsearchFiltering.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        
        self.searchFilteringContainer = Frame(self.groupsearchFiltering.interior())
        self.webContainer = Frame(self.searchFilteringContainer)
        self.webLabel = Label(self.webContainer,text="Web search").pack(side=LEFT)
        self.webEntry = Entry(self.webContainer,textvariable=self.webSearch,state='disabled').pack(side=LEFT)
        self.webContainer.pack(side=LEFT,expand=YES)
        self.youtubeContainer = Frame(self.searchFilteringContainer)
        self.youtubeLabel = Label(self.youtubeContainer,text="Restricted YouTube content").pack(side=LEFT)
        self.youtubeEntry = Entry(self.youtubeContainer,textvariable=self.youtube,state='disabled').pack(side=LEFT)
        self.youtubeContainer.pack(side=LEFT,expand=YES)
        self.searchFilteringContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.searchFiltering.pack(expand=YES,fill=BOTH)
        self.wholecontainer.pack(side=BOTTOM,expand=YES)
         #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                           Página de threat protection                              ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.wholethreatcontainer = Frame(self.templateNotebook)
        self.amp = Frame(self.wholethreatcontainer)
        self.groupamp = pmw.Group(self.amp,tag_text="Advanced Malware Protection (AMP)")
        self.groupamp.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        
        self.ampContainer = Frame(self.groupamp.interior())
        self.modeContainer = Frame(self.ampContainer)
        self.modeLabel = Label(self.modeContainer,text="Modo").pack(side=LEFT)
        self.modeEntry = Entry(self.modeContainer,textvariable=self.webSearch,state='disabled').pack(side=LEFT)
        self.modeContainer.pack(side=TOP,expand=YES)
        self.urllistContainer = Frame(self.ampContainer)
        self.allowurlLabel = Label(self.urllistContainer,text="Lista de URL permitidas").pack(side=LEFT)
        self.allowurlEntry = Entry(self.urllistContainer,textvariable=self.youtube,state='disabled').pack(side=LEFT)
        self.urllistContainer.pack(side=TOP,expand=YES)
        self.filelistContainer = Frame(self.ampContainer)
        self.allowfileLabel = Label(self.filelistContainer,text="Lista de archivos permitidos").pack(side=LEFT)
        self.allowfileEntry = Entry(self.filelistContainer,textvariable=self.youtube,state='disabled').pack(side=LEFT)
        self.filelistContainer.pack(side=TOP,expand=YES)
        self.ampContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.groupintrusion = pmw.Group(self.amp,tag_text="Advanced Malware Protection (AMP)")
        self.groupintrusion.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        self.intrusionContainer = Frame(self.groupintrusion.interior())
        self.modeintrusionContainer = Frame(self.intrusionContainer)
        self.modeintrusionLabel = Label(self.modeintrusionContainer,text="Modo").pack(side=LEFT)
        self.modeintrusionEntry = Entry(self.modeintrusionContainer,textvariable=self.webSearch,state='disabled').pack(side=LEFT)
        self.modeintrusionContainer.pack(side=TOP,expand=YES)
        self.intrusionContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.amp.pack(expand=YES,fill=BOTH)
        self.wholethreatcontainer.pack(side=BOTTOM,expand=YES)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Configuración Notebook                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.templateNotebook.pack(expand=YES, fill=BOTH)
        self.templateNotebook.add(self.availableTemplates,text="Templates Disponibles")
        self.templateNotebook.add(self.Label3,text="Nuevo Template L3")
        self.templateNotebook.add(self.Label7,text="Nuevo Template L7")
        self.templateNotebook.add(self.wholecontainer,text="Content Filtering")
        self.templateNotebook.add(self.wholethreatcontainer,text="Threat Protection")


    def showTemplates(self):
        n=1
        for file in self.templatesFiles:
            extension = re.findall(r".txt|.json|.csv|.docx",file)
            templateName = file.replace(extension[0],"")
            self.templatesTable.insert(parent='',index='end',iid=n,text='',values=(n,templateName,'101'))
            n+=1

root = Tk()
root.geometry("800x500")
root.resizable(width=False, height=False)

ventana = Templates(root)

root.mainloop()