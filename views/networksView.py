from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import Pmw as pmw
from PIL import Image, ImageTk
from views.securityconfigView import SecurityConfig

class Networks():

    def __init__(self, root,organization="",meraki = ""):
        self.organization = organization
        self.merakiInfo = meraki
        self.root = root
        
        self.syslogValue = StringVar()

        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                           Página de templates disponibles                                ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        self.groupNetwork = pmw.Group(root,tag_text="Redes Disponibles en la Organización")
        self.groupNetwork.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        
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


        self.NetworkTable.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        self.NetworkTable.bind("<ButtonRelease>",self.select)
        self.containerTable.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)
        

        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #----                                Acciones                                    ----
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def show(self):
        n = 1
        for organization in self.merakiInfo:
            if organization['organizationName'] == self.organization:
                for network in organization['networks']:
                    self.NetworkTable.insert(parent='',index='end',iid=n,text='',values=(network['ID'],network['Name']))
                    n+=1
                    
    def update(self, organization):
        self.comment.config(text=organization)
        self.organization = organization
        for i in self.NetworkTable.get_children():
            self.NetworkTable.delete(i)
        self.show()  

    def select(self,event=None):
        curItem = self.NetworkTable.focus()
        org = self.NetworkTable.item(curItem)['values'][1]
        netId = self.NetworkTable.item(curItem)['values'][0]
        print(org)
        
        root = Tk()
        root.geometry("800x500")
        root.resizable(width=False, height=False)
        root.wm_title("VOSEDA NETWORKS -- Configuración de la red")
        root.iconbitmap("isotipo_voseda_color.ico")
        ventanaNetwork= SecurityConfig(root,self.merakiInfo,netId) 
        root.mainloop()           

#root = Tk()
#root.geometry("800x500")
#root.resizable(width=False, height=False)

#ventana = Networks(root)

#root.mainloop()