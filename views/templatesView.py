from tkinter import *
from tkinter import ttk,scrolledtext
import tkinter.font as tkFont
import Pmw as pmw
from PIL import Image, ImageTk
import os,re,json
import sys
sys.path.append("..\\")
from controls.createTemplate import createTemplateFile 

class Templates():

    def __init__(self, root):
        self.syslogValue = StringVar()
        self.syslogValueInb = StringVar()
        self.webSearch = StringVar()
        self.youtube = StringVar()
        self.contentFilteringName = StringVar()
        self.threatName = StringVar()
        self.variablesL3 = [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
        self.variablesoutL3 = [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
        self.variablesL7 = [StringVar(),StringVar(),StringVar()]
        self.variablesIntrusion = [StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
        self.variablesMalware = [StringVar(),StringVar(),StringVar()]
        self.variablesCF =[StringVar(),StringVar(),StringVar(),StringVar()]
        self.L3Name = StringVar()
        self.L7Name = StringVar()
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
        self.newTemplatel3 = Frame(self.Label3)
        self.nombre = Label(self.newTemplatel3,text="Nombre").pack(side=LEFT)
        self.nombreIn = Entry(self.newTemplatel3,textvariable=self.L3Name)
        self.nombreIn.pack(side=LEFT)
        self.newTemplatel3.pack(fill=BOTH,padx=2,pady=10)

        self.containerInL3 = Frame(self.Label3)
        self.groupInconfigL3 = pmw.Group(self.containerInL3,tag_text="Inbound L3")
        self.groupInconfigL3.pack(side=BOTTOM,expand=YES,fill=BOTH,padx=3,pady=2)

        self.configInL31 = Frame(self.groupInconfigL3.interior())
        self.Incommentcontainer = Frame(self.configInL31)
        self.Incomment = Label(self.Incommentcontainer,text="Comentario").pack(side=LEFT,anchor=CENTER,padx=8,pady=1)
        self.IncommentIn = Entry(self.Incommentcontainer,textvariable=self.variablesL3[0]).pack(side=LEFT,anchor=CENTER,padx=8,pady=1)
        self.Incommentcontainer.pack(side=LEFT,expand=YES)
        self.Inprotocolcontainer = Frame(self.configInL31)        
        self.Inprotocol = Label(self.Inprotocolcontainer,text="Protocolo").pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.InprotcolIn = Entry(self.Inprotocolcontainer,textvariable=self.variablesL3[1]).pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.Inprotocolcontainer.pack(side=LEFT,expand=YES)
        self.configInL31.pack(side=TOP,expand=YES, fill=BOTH)

        self.InconfigL32 = Frame(self.groupInconfigL3.interior())
        self.Incidrcontainer = Frame(self.InconfigL32)
        self.IndestCidr = Label(self.Incidrcontainer,text="destCidr").pack(side=LEFT,anchor=CENTER,padx=16,pady=1)
        self.IndestCidrIn = Entry(self.Incidrcontainer,textvariable=self.variablesL3[2]).pack(side=LEFT,anchor=CENTER,padx=16,pady=1)
        self.Incidrcontainer.pack(side=LEFT,expand=YES)
        self.Insourcecontainer = Frame(self.InconfigL32)
        self.Insource = Label(self.Insourcecontainer,text="Source Cid").pack(side=LEFT,anchor=CENTER,padx=5.5,pady=1)
        self.InsourceIn = Entry(self.Insourcecontainer,textvariable=self.variablesL3[3]).pack(side=LEFT,anchor=CENTER,padx=5.5,pady=1)
        self.Insourcecontainer.pack(side=LEFT,expand=YES)
        self.InconfigL32.pack(side=TOP,expand=YES, fill=BOTH)

        self.configInL33 = Frame(self.groupInconfigL3.interior())
        self.Indestcontainer = Frame(self.configInL33)
        self.IndestPort = Label(self.Indestcontainer,text="Puerto Destino").pack(side=LEFT,anchor=CENTER,padx=5,pady=1)
        self.IndestPortIn = Entry(self.Indestcontainer,textvariable=self.variablesL3[4]).pack(side=LEFT,anchor=CENTER,padx=5,pady=1)
        self.Indestcontainer.pack(side=LEFT,expand=YES)
        self.Inorigincontainer = Frame(self.configInL33)
        self.InoriginPort = Label(self.Inorigincontainer,text="Puerto Origen").pack(side=LEFT,anchor=CENTER,padx=5,pady=1)
        self.InoriginPortIn = Entry(self.Inorigincontainer,textvariable=self.variablesL3[5]).pack(side=LEFT,anchor=CENTER,padx=5,pady=1)
        self.Inorigincontainer.pack(side=LEFT,expand=YES)
        self.configInL33.pack(side=TOP,expand=YES, fill=BOTH)

        self.configInL34 = Frame(self.groupInconfigL3.interior())
        self.Inpolicycontainer = Frame(self.configInL34)
        self.Inpolicy = Label(self.Inpolicycontainer,text="Política").pack(side=LEFT,anchor=CENTER,padx=22,pady=1)
        self.InpolicyIn = Entry(self.Inpolicycontainer,textvariable=self.variablesL3[6]).pack(side=LEFT,anchor=CENTER,padx=22,pady=1)
        self.Inpolicycontainer.pack(side=LEFT,expand=YES)
        self.Insyslogcontainer = Frame(self.configInL34)
        self.Insyslog = Label(self.Insyslogcontainer,text="syslog Enabled").pack(side=LEFT,anchor=CENTER,padx=12.5,pady=1)
        self.InsyslogIn = ttk.Combobox(self.Insyslogcontainer, textvariable=self.syslogValueInb)
        self.InsyslogIn['values'] = ("true","false")
        self.InsyslogIn.pack(side=LEFT,anchor=CENTER,padx=12.5,pady=1)
        self.Insyslogcontainer.pack(side=LEFT,expand=YES)
        self.configInL34.pack(side=TOP,expand=YES, fill=BOTH)
        self.containerInL3.pack(expand=YES,fill=BOTH)

        self.containerL3 = Frame(self.Label3)
        self.groupconfigL3 = pmw.Group(self.containerL3,tag_text="Outbound L3")
        self.groupconfigL3.pack(side=BOTTOM,expand=YES,fill=BOTH,padx=3,pady=2)

        self.configL31 = Frame(self.groupconfigL3.interior())
        self.commentcontainer = Frame(self.configL31)
        self.comment = Label(self.commentcontainer,text="Comentario").pack(side=LEFT,anchor=CENTER,padx=8,pady=1)
        self.commentIn = Entry(self.commentcontainer,textvariable=self.variablesoutL3[0]).pack(side=LEFT,anchor=CENTER,padx=8,pady=1)
        self.commentcontainer.pack(side=LEFT,expand=YES)
        self.protocolcontainer = Frame(self.configL31)        
        self.protocol = Label(self.protocolcontainer,text="Protocolo").pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.protcolIn = Entry(self.protocolcontainer,textvariable=self.variablesoutL3[1]).pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.protocolcontainer.pack(side=LEFT,expand=YES)
        self.configL31.pack(side=TOP,expand=YES, fill=BOTH)

        self.configL32 = Frame(self.groupconfigL3.interior())
        self.cidrcontainer = Frame(self.configL32)
        self.destCidr = Label(self.cidrcontainer,text="destCidr").pack(side=LEFT,anchor=CENTER,padx=16,pady=1)
        self.destCidrIn = Entry(self.cidrcontainer,textvariable=self.variablesoutL3[2]).pack(side=LEFT,anchor=CENTER,padx=16,pady=1)
        self.cidrcontainer.pack(side=LEFT,expand=YES)
        self.sourcecontainer = Frame(self.configL32)
        self.source = Label(self.sourcecontainer,text="Source Cid").pack(side=LEFT,anchor=CENTER,padx=5.5,pady=1)
        self.sourceIn = Entry(self.sourcecontainer,textvariable=self.variablesoutL3[3]).pack(side=LEFT,anchor=CENTER,padx=5.5,pady=1)
        self.sourcecontainer.pack(side=LEFT,expand=YES)
        self.configL32.pack(side=TOP,expand=YES, fill=BOTH)

        self.configL33 = Frame(self.groupconfigL3.interior())
        self.destcontainer = Frame(self.configL33)
        self.destPort = Label(self.destcontainer,text="Puerto Destino").pack(side=LEFT,anchor=CENTER,padx=5,pady=1)
        self.destPortIn = Entry(self.destcontainer,textvariable=self.variablesoutL3[4]).pack(side=LEFT,anchor=CENTER,padx=5,pady=1)
        self.destcontainer.pack(side=LEFT,expand=YES)
        self.origincontainer = Frame(self.configL33)
        self.originPort = Label(self.origincontainer,text="Puerto Origen").pack(side=LEFT,anchor=CENTER,padx=5,pady=1)
        self.originPortIn = Entry(self.origincontainer,textvariable=self.variablesoutL3[5]).pack(side=LEFT,anchor=CENTER,padx=5,pady=1)
        self.origincontainer.pack(side=LEFT,expand=YES)
        self.configL33.pack(side=TOP,expand=YES, fill=BOTH)

        self.configL34 = Frame(self.groupconfigL3.interior())
        self.policycontainer = Frame(self.configL34)
        self.policy = Label(self.policycontainer,text="Política").pack(side=LEFT,anchor=CENTER,padx=22,pady=1)
        self.policyIn = Entry(self.policycontainer,textvariable=self.variablesoutL3[6]).pack(side=LEFT,anchor=CENTER,padx=22,pady=1)
        self.policycontainer.pack(side=LEFT,expand=YES)
        self.syslogcontainer = Frame(self.configL34)
        self.syslog = Label(self.syslogcontainer,text="syslog Enabled").pack(side=LEFT,anchor=CENTER,padx=12.5,pady=1)
        self.syslogIn = ttk.Combobox(self.syslogcontainer, textvariable=self.syslogValue)
        self.syslogIn['values'] = ("true","false")
        self.syslogIn.pack(side=LEFT,anchor=CENTER,padx=12.5,pady=1)
        self.syslogcontainer.pack(side=LEFT,expand=YES)
        self.configL34.pack(side=TOP,expand=YES, fill=BOTH)
        self.containerL3.pack(expand=YES,fill=BOTH)

        self.configL35 = Frame(self.Label3)
        self.addRule = Button(self.configL35,text="Agregar Regla",command=self.templateL3)
        self.addRule.pack(side=RIGHT,padx=120)
        self.configL35.pack(expand=YES,fill=BOTH)

        self.Label3.pack(side=LEFT,expand=YES, fill=BOTH)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Página de templates de L7                                 ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.Label7 = Frame(self.templateNotebook)


        self.newTemplatel7 = Frame(self.Label7)
        self.nombrel7 = Label(self.newTemplatel7,text="Nombre").pack(side=LEFT)
        self.nombrel7In = Entry(self.newTemplatel7,textvariable=self.L7Name)
        self.nombrel7In.pack(side=LEFT)
        self.newTemplatel7.pack(fill=BOTH,padx=2,pady=10)

        self.containerL7 = Frame(self.Label7)
        self.groupconfigL7= pmw.Group(self.containerL7,tag_text="L7")
        self.groupconfigL7.pack(side=BOTTOM,expand=YES,fill=BOTH,padx=3,pady=2)

        self.configL71 = Frame(self.groupconfigL7.interior())
        self.policyl7container = Frame(self.configL71)
        self.policyl7 = Label(self.policyl7container,text="Política").pack(side=LEFT,anchor=CENTER,padx=8,pady=1)
        self.policyl7In = Entry(self.policyl7container,textvariable=self.variablesL7[0]).pack(side=LEFT,anchor=CENTER,padx=8,pady=1)
        self.policyl7container.pack(side=TOP,expand=YES)
        self.typecontainer = Frame(self.configL71)        
        self.type = Label(self.typecontainer,text="Tipo").pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.typeIn = Entry(self.typecontainer,textvariable=self.variablesL7[1]).pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.typecontainer.pack(side=TOP,expand=YES)
        self.valuecontainer = Frame(self.configL71)        
        self.value = Label(self.valuecontainer,text="Valor").pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.valueIn = Entry(self.valuecontainer,textvariable=self.variablesL7[2]).pack(side=LEFT,anchor=CENTER,padx=10,pady=1)
        self.valuecontainer.pack(side=TOP,expand=YES)
        self.configL71.pack(side=TOP,expand=YES, fill=BOTH)

        self.containerL7.pack(expand=YES,fill=BOTH)

        self.configL72 = Frame(self.Label7)
        self.addRulel7 = Button(self.configL72,text="Agregar Regla",command=self.templateL7)
        self.addRulel7.pack(side=RIGHT,padx=120)
        self.configL72.pack(expand=YES,fill=BOTH)

        
        self.Label7.pack(side=LEFT,expand=YES, fill=BOTH)
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Página de content filtering                                 ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.wholecontainer = Frame(self.templateNotebook)
        
        self.newTemplateContentFiltering = Frame(self.wholecontainer)
        self.nombreCF = Label(self.newTemplateContentFiltering,text="Nombre").pack(side=LEFT)
        self.nombreCFIn = Entry(self.newTemplateContentFiltering,textvariable=self.contentFilteringName)
        self.nombreCFIn.pack(side=LEFT)
        self.newTemplateContentFiltering.pack(expand=YES,fill=BOTH,padx=2)

        self.categoryBlocking = Frame(self.wholecontainer)
        self.groupContent = pmw.Group(self.categoryBlocking,tag_text="Categorías de bloqueo")
        self.groupContent.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)


        self.ContentContainer = Frame(self.groupContent.interior())
        self.ContentLabel = Label(self.ContentContainer,text="Categorías de contenido").pack(side=TOP)
        self.Content = Entry(self.ContentContainer,textvariable=self.variablesCF[0]).pack(side=TOP,anchor=CENTER,ipadx=10,ipady=45)
        self.ContentContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.ThreatContainer = Frame(self.groupContent.interior())
        self.ThreatLabel = Label(self.ThreatContainer,text="Categorías de amenaza").pack(side=TOP)
        self.Threat = Entry(self.ThreatContainer,textvariable=self.variablesCF[1]).pack(side=TOP,anchor=CENTER,ipadx=10,ipady=45)
        self.ThreatContainer.pack(side=LEFT,expand=YES,fill=BOTH)
        self.categoryBlocking.pack(expand=YES,fill=BOTH)


        self.urlFiltering = Frame(self.wholecontainer)
        self.groupURLContent = pmw.Group(self.urlFiltering,tag_text="Filtrado URL")
        self.groupURLContent.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        
        self.blockedContainer = Frame(self.groupURLContent.interior())
        self.blockedLabel = Label(self.blockedContainer,text="Lista de URL bloqueadas").pack(side=TOP)
        self.blocked = Entry(self.blockedContainer,textvariable=self.variablesCF[2]).pack(side=TOP,anchor=CENTER,ipadx=10,ipady=35)
        self.blockedContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.allowedContainer = Frame(self.groupURLContent.interior())
        self.allowedLabel = Label(self.allowedContainer,text="Lista de URL permitidas").pack(side=TOP)
        self.allowed = Entry(self.allowedContainer,textvariable=self.variablesCF[3]).pack(side=TOP,anchor=CENTER,ipadx=10,ipady=35)
        self.allowedContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.urlFiltering.pack(expand=YES,fill=BOTH)
        


        self.configCF = Frame(self.wholecontainer)
        self.addRuleCF = Button(self.configCF,text="Agregar Regla",command=self.templateCF)
        self.addRuleCF.pack(side=RIGHT,padx=120)
        self.configCF.pack(expand=YES,fill=BOTH)

        self.wholecontainer.pack(side=BOTTOM,expand=YES)
         #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                           Página de threat protection                              ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.wholethreatcontainer = Frame(self.templateNotebook)
        self.newTemplateThreatProtection = Frame(self.wholethreatcontainer)
        self.nombreTP = Label(self.newTemplateThreatProtection,text="Nombre").pack(side=LEFT)
        self.nombreTPIn = Entry(self.newTemplateThreatProtection,textvariable=self.threatName)
        self.nombreTPIn.pack(side=LEFT)
        self.newTemplateThreatProtection.pack(fill=BOTH,padx=2,pady=10)

        self.amp = Frame(self.wholethreatcontainer)
        self.groupamp = pmw.Group(self.amp,tag_text="Advanced Malware Protection (AMP)")
        self.groupamp.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        
        self.ampContainer = Frame(self.groupamp.interior())
        self.modeContainer = Frame(self.ampContainer)
        self.modeLabel = Label(self.modeContainer,text="Modo").pack(side=LEFT)
        self.modeEntry = ttk.Combobox(self.modeContainer,textvariable=self.variablesMalware[0])
        self.modeEntry['values'] = ("enabled","disabled")
        self.modeEntry.pack(side=LEFT)
        self.modeContainer.pack(side=TOP,expand=YES)
        self.ampCon = Frame(self.ampContainer)
        self.urllistContainer = Frame(self.ampCon)
        self.allowurlLabel = Label(self.urllistContainer,text="Lista de URL permitidas").pack(side=LEFT)
        self.allowurlEntry = Entry(self.urllistContainer,textvariable=self.variablesMalware[1]).pack(side=LEFT,ipadx=10,ipady=35)
        self.urllistContainer.pack(side=LEFT,expand=YES,padx=45)
        self.filelistContainer = Frame(self.ampCon)
        self.allowfileLabel = Label(self.filelistContainer,text="Lista de archivos permitidos").pack(side=LEFT)
        self.allowfileEntry = Entry(self.filelistContainer,textvariable=self.variablesMalware[2]).pack(side=LEFT,ipadx=10,ipady=35)
        self.filelistContainer.pack(side=LEFT,expand=YES,padx=45)
        self.ampCon.pack(side=TOP,expand=YES)
        self.ampContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.groupintrusion = pmw.Group(self.amp,tag_text="Intrution Detection and Prevention")
        self.groupintrusion.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        self.intrusionContainer = Frame(self.groupintrusion.interior())
        self.modeintrusionContainer = Frame(self.intrusionContainer)
        self.modeintrusionLabel = Label(self.modeintrusionContainer,text="Modo").pack(side=LEFT)
        self.modeintrusionEntry = ttk.Combobox(self.modeintrusionContainer,textvariable=self.variablesIntrusion[0])
        self.modeintrusionEntry['values'] = ("disabled","detection","prevention")
        self.modeintrusionEntry.pack(side=LEFT)
        self.modeintrusionContainer.pack(side=TOP,expand=YES)
        self.rulesetintrusionContainer = Frame(self.intrusionContainer)
        self.rulesetintrusionLabel = Label(self.rulesetintrusionContainer,text="Ruleset").pack(side=LEFT)
        self.rulesetintrusionEntry = ttk.Combobox(self.rulesetintrusionContainer,textvariable=self.variablesIntrusion[1])
        self.rulesetintrusionEntry['values'] = ("connectivity","balanced","security")
        self.rulesetintrusionEntry.pack(side=LEFT)
        self.rulesetintrusionContainer.pack(side=TOP,expand=YES)
        self.container = Frame(self.intrusionContainer)
        self.includedContainer = Frame(self.container)
        self.includedLabel = Label(self.includedContainer,text="Cidr Incluidas").pack(side=LEFT)
        self.includedEntry = Entry(self.includedContainer,textvariable=self.variablesIntrusion[2]).pack(side=LEFT,ipadx=10,ipady=35)
        self.includedContainer.pack(side=LEFT,expand=YES,padx=45)
        self.excludedContainer = Frame(self.container)
        self.excludedLabel = Label(self.excludedContainer,text="Cidr Excluidas").pack(side=LEFT)
        self.excludedEntry = Entry(self.excludedContainer,textvariable=self.variablesIntrusion[3]).pack(side=LEFT,ipadx=10,ipady=35)
        self.excludedContainer.pack(side=LEFT,expand=YES,padx=45)
        self.container.pack(side=TOP,expand=YES)
        self.intrusionContainer.pack(side=LEFT,expand=YES,fill=BOTH)

        self.amp.pack(expand=YES,fill=BOTH)

        self.configTP = Frame(self.wholethreatcontainer)
        self.addRuleTP = Button(self.configTP,text="Agregar Regla",command=self.templateTP)
        self.addRuleTP.pack(side=RIGHT,padx=120)
        self.configTP.pack(expand=YES,fill=BOTH)
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
            self.templatesTable.insert(parent='',index='end',iid=n,text='',values=(n,templateName,'MX'))
            n+=1
    

    def templateCF(self):
        nombre = self.contentFilteringName.get()
        allowedUrl = self.variablesCF[3].get().split(",")
        blockedUrl = self.variablesCF[2].get().split(",")
        categories = self.variablesCF[0].get().split(",")+self.variablesCF[1].get().split(",")
        urlCategories = []
        categorias = json.load(open("../data/categorias.json"))
        for category in categories:
            for categoria in categorias['blockedUrlCategories']:
                if category.upper() == categoria['name'].upper():
                    urlCategories.append(categoria['id'])

        data={
            "content_filtering":{
                "allowedUrlPatterns": allowedUrl,
                "blockedUrlPatterns": blockedUrl,
                "blockedUrlCategories": urlCategories,
                "urlCategoryListSize": "topSites"
            }
        }
        createTemplateFile(nombre,data)

    def templateTP(self):
        nombre = self.threatName.get()
        includeCidr = self.variablesIntrusion[2].get().split(",")
        excludeCidr = self.variablesIntrusion[3].get().split(",")
        data={
            "intrusion":{
                "mode": self.variablesIntrusion[0].get(),
                "idsRulesets": self.variablesIntrusion[1].get(),
                "protectedNetworks": {
                    "useDefault": "false",
                    "includedCidr": includeCidr,
                    "excludedCidr": excludeCidr
                }
            },
            "malware":{
                "mode": self.variablesMalware[0],
                "allowedUrls": [
                    {
                        "url": self.variablesMalware[1],
                        "comment": "App Meraki"
                    }
                ],
                "allowedFiles": [
                    {
                        "sha256": self.variablesMalware[2],
                        "comment": "App Meraki"
                    }
                ]
            }
        }
        createTemplateFile(nombre,data)

    def templateL3(self):
        nombre = self.L3Name.get()
        data={
            "L3_inbound":{
                "rules": [
                    {
                        "comment": self.variablesL3[0].get(),
                        "policy": self.variablesL3[6].get(),
                        "protocol": self.variablesL3[1].get(),
                        "destPort": self.variablesL3[4].get(),
                        "destCidr": self.variablesL3[2].get(),
                        "srcPort": self.variablesL3[5].get(),
                        "srcCidr": self.variablesL3[3].get(),
                        "syslogEnabled": self.syslogValueInb.get()
                    }
                ]
            },
        "L3_outbound":{
                "rules": [
                    {
                        "comment": self.variablesoutL3[0].get(),
                        "policy": self.variablesoutL3[6].get(),
                        "protocol": self.variablesoutL3[1].get(),
                        "destPort": self.variablesoutL3[4].get(),
                        "destCidr": self.variablesoutL3[2].get(),
                        "srcPort": self.variablesoutL3[5].get(),
                        "srcCidr": self.variablesoutL3[3].get(),
                        "syslogEnabled": self.syslogValue.get()
                    }
                ]
            }
        }
        createTemplateFile(nombre,data) 

    def templateL7(self):
            nombre = self.L7Name.get()
            data={
                "L7":{
                    "rules": [
                        {
                            "policy": self.variablesL7[0].get(),
                            "type": self.variablesL7[1].get(),
                            "value": self.variablesL7[2].get()
                        },
                    ]
                }
            }
            createTemplateFile(nombre,data)    

class init():
    def __init__(self):   
        root = Toplevel()
        root.geometry("800x500")
        root.resizable(width=False, height=False)
        root.wm_title("VOSEDA NETWORKS -- Templates")
        root.iconbitmap("isotipo_voseda_color.ico")
        ventana = Templates(root)

        root.mainloop()

#root = Tk()
#root.geometry("800x500")
#root.resizable(width=False, height=False)

#ventana = Templates(root)

#root.mainloop()