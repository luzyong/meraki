from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import Pmw as pmw
from PIL import Image, ImageTk

class Templates():

    def __init__(self, root):
        self.syslogValue = StringVar()
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

        self.templatesTable.insert(parent='',index='end',iid=0,text='',
        values=('1','Ninja','101','Oklahoma', 'Moore'))
        self.templatesTable.insert(parent='',index='end',iid=1,text='',
        values=('2','Ranger','102','Wisconsin', 'Green Bay'))
        self.templatesTable.insert(parent='',index='end',iid=2,text='',
        values=('3','Deamon','103', 'California', 'Placentia'))
        self.templatesTable.insert(parent='',index='end',iid=3,text='',
        values=('4','Dragon','104','New York' , 'White Plains'))
        self.templatesTable.insert(parent='',index='end',iid=4,text='',
        values=('5','CrissCross','105','California', 'San Diego'))
        self.templatesTable.insert(parent='',index='end',iid=5,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))

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
        #----                                Configuración Notebook                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.templateNotebook.pack(expand=YES, fill=BOTH)
        self.templateNotebook.add(self.availableTemplates,text="Templates Disponibles")
        self.templateNotebook.add(self.Label3,text="Nuevo Template L3")
        self.templateNotebook.add(self.Label7,text="Nuevo Template L7")


root = Tk()
root.geometry("800x500")
root.resizable(width=False, height=False)

ventana = Templates(root)

root.mainloop()