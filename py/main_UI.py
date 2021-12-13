#-------------------------------------------------------------------------------
#
# Name: Projet GP211 Gestion Scolaire
#
# Noms : Abdel Malak, Boresy
# Prenoms :Antony, Eloïse
#
# Classe :2PE
# Groupe :2
#
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from lib_commun import *
from gestion_etudiant_tkinter_functions import *
from gestion_note_tkinter_functions import *

#***************************************************************************
#---------------------------------------------------------------------------
#                  Préparation de la fenêtre de l'accueil
#---------------------------------------------------------------------------
#***************************************************************************


window = Tk()
widthset = window.winfo_screenwidth()
heightset = window.winfo_screenheight()

window.title("Pegasus 2.0")
geometryset = str(widthset)+"x"+str(heightset)
window.geometry(geometryset)
window.configure(bg="#ffffff")

window.attributes('-fullscreen', True)
window.bind('<Escape>', lambda e: window.attributes('-fullscreen', False))
window.bind('<F11>', lambda e: window.attributes('-fullscreen', True))


#***************************************************************************
#---------------------------------------------------------------------------
#                  Partie Gestion Etudiant
#---------------------------------------------------------------------------
#***************************************************************************


def window_gestion_etudiant():
    """ fonction qui créée une nouvelle fenêtre pour accéder à la gestion etudiant  """
    newWindow = Toplevel(window)
    newWindow.geometry(geometryset)
    
    newWindow.attributes('-fullscreen', True)
    newWindow.bind(' <Escape> ', lambda e: newWindow.attributes(
        '-fullscreen', False))

    #########  canvas preparation  #########
    
    canvas2 = Canvas(
        newWindow,
        bg="#ffffff",
        height=heightset,
        width=widthset,
        borderwidth=widthset,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    
    canvas2.place(x=0, y=0)
    
    #########  Background  #########
    
    Etudiantbackground = Image.open("canvas\Etudiant_background.png")
    Etudiantbackground = Etudiantbackground.resize((widthset, heightset), Image.ANTIALIAS)
    Etudiantbackground = ImageTk.PhotoImage(Etudiantbackground)
    canvas2.create_image(
        widthset/2, heightset/2,
        image=Etudiantbackground)
    
    #########  TABLEAU  #########
    
    data = ouverture_fichier_csv('etudiants.csv')
    
    columns = ('#1', '#2', '#3', '#4', '#5')
    tableau = ttk.Treeview(newWindow, columns=columns, show='headings', height=16)
    
    tableau.heading('#1', text='ID')
    tableau.heading('#2', text='Genre')
    tableau.heading('#3', text='Nom')
    tableau.heading('#4', text='Prénom')
    tableau.heading('#5', text='Email')
    tableau.column('#1', width=int(50*widthset/1920))
    tableau.column('#2', width=int(50*widthset/1920))
    tableau.column('#3', width=int(250*widthset/1920))
    tableau.column('#4', width=int(250*widthset/1920))
    tableau.column('#5', width=int(300*widthset/1920))
    
    global count    
    count = 0
    for i in range(1, len(data)):
        tableau.insert('', i, values=data[i])
        count += 1
    tableau.pack()
    tableau.place(x=783*widthset/1920, y=360*heightset/1080, width=int(960*widthset/1920), height=(340*heightset/1080))
    
    
    #########  Valeurs demandées  #########
    
    
    r = StringVar()
    radiobutton_M = Radiobutton(newWindow, variable=r, value="M", bg = '#F1F1F1')
    radiobutton_F = Radiobutton(newWindow, variable=r, value="F", bg = '#F1F1F1')
    radiobutton_M.place(x=354*widthset/1920, y=573*heightset/1080)
    radiobutton_F.place(x=448*widthset/1920, y=573*heightset/1080)

    
    saisi_prenom_img = Image.open("canvas\img_textBox0.png")
    saisi_prenom_img = saisi_prenom_img.resize((int(300*widthset/1920), int(48*heightset/1080)), Image.ANTIALIAS)
    saisi_prenom_img = ImageTk.PhotoImage(saisi_prenom_img)
    
    canvas2.create_image(
        440*widthset/1920, 307*heightset/1080,
        image = saisi_prenom_img)

    saisi_prenom = Entry(newWindow,
        bd = 0,
        bg = "#f1f1f1",
        highlightthickness = 0,
        font= 15)

    saisi_prenom.place(
        x = 320*widthset/1920, y = 283*heightset/1080,
        width = 252*widthset/1920,
        height = 48*heightset/1080)


    saisi_nom_img = Image.open("canvas\img_textBox1.png")
    saisi_nom_img = saisi_nom_img.resize((int(300*widthset/1920), int(48*heightset/1080)), Image.ANTIALIAS)
    saisi_nom_img = ImageTk.PhotoImage(saisi_nom_img)
    
    canvas2.create_image(
        440*widthset/1920, 400*heightset/1080,
        image = saisi_nom_img)
    
    saisi_nom = Entry(newWindow,
        bd = 0,
        bg = "#f1f1f1",
        highlightthickness = 0,
        font= 15)
    
    saisi_nom.place(
        x = 320*widthset/1920, y = 376*heightset/1080,
        width = 252*widthset/1920,
        height = 48*heightset/1080)
    

    saisi_email_img = Image.open("canvas\img_textBox1.png")
    saisi_email_img = saisi_email_img.resize((int(300*widthset/1920), int(48*heightset/1080)), Image.ANTIALIAS)
    saisi_email_img = ImageTk.PhotoImage(saisi_email_img)
    
    canvas2.create_image(
        440*widthset/1920, 493*heightset/1080,
        image = saisi_email_img)
    
    saisi_email = Entry(newWindow,
        bd = 0,
        bg = "#f1f1f1",
        highlightthickness = 0,
        font= 15)
    
    saisi_email.place(
        x = 320*widthset/1920, y = 469*heightset/1080,
        width = 252*widthset/1920,
        height = 48*heightset/1080)

    
    #########  Sélection et changement de valeurs dans le tableau  #########

    def select_record():
        """ fonction qui permet de sélectionner une donnée"""
        saisi_prenom.delete(0, END)
        saisi_nom.delete(0, END)
        saisi_email.delete(0, END)
        radiobutton_F.deselect()
        radiobutton_M.deselect()

        selected = tableau.focus()
        values = tableau.item(selected, 'values')
        
        if values[1]=="M":
            radiobutton_M.invoke()
        
        if values[1]=="F":
            radiobutton_F.invoke()
        
        saisi_prenom.insert(0, values[3])
        saisi_nom.insert(0, values[2])
        saisi_email.insert(0, values[4])
        
        
    def add_record():
        """ fonction qui permet d'ajouter un etudiant """
        data = ouverture_fichier_csv('etudiants.csv')
        id = int(data[-1][0])+1 
        nom = saisi_nom.get()
        nom = nom.upper()
        genre = r.get()
        global count
        tableau.insert(parent='', index='end', iid=count, text='', values=(id, genre, nom, saisi_prenom.get(), saisi_email.get()))
        count+=1
        
        ajoutEtudiant(saisi_nom.get(), saisi_prenom.get(),
                      genre, saisi_email.get())
        
        saisi_prenom.delete(0, END)
        saisi_nom.delete(0, END)
        saisi_email.delete(0, END)
        
    def update_record():
        """fonction qui permet de modifier un étudiant """
        selected = tableau.focus()
        values = tableau.item(selected, 'values')
        id = values[0]
        genre = r.get()
        modificationEtudiant(id, saisi_prenom.get(),
                             saisi_nom.get(), genre, saisi_email.get())
        tableau.item(selected, text="", values=(
            id, genre, saisi_nom.get(), saisi_prenom.get(), saisi_email.get()))

        saisi_prenom.delete(0, END)
        saisi_nom.delete(0, END)
        saisi_email.delete(0, END)

    def remove_record():
        """fonction qui permet de retirer un étudiant"""
        selected = tableau.focus()
        values = tableau.item(selected, 'values')
        id = values[0]
        suppressionEtudiant(id)
        x = tableau.selection()[0]
        tableau.delete(x)
        saisi_prenom.delete(0, END)
        saisi_nom.delete(0, END)
        saisi_email.delete(0, END)

    def clicker(e):
        """ fonction qui permet de faire l'action de cliquer """
        select_record()

    tableau.bind("<ButtonRelease-1>", clicker)


    #########  Boutons Ajouter, Modifier, Supprimer et Retour  #########


    Bouton_Etudiant_Ajouter = Image.open("canvas\Etudiant_Ajouter.png")
    Bouton_Etudiant_Ajouter = Bouton_Etudiant_Ajouter.resize(
        (int(420*widthset/1920), int(70*heightset/1080)), Image.ANTIALIAS)
    Bouton_Etudiant_Ajouter = ImageTk.PhotoImage(Bouton_Etudiant_Ajouter)
    bea = Button(newWindow,
    image=Bouton_Etudiant_Ajouter,
    borderwidth=0,
    highlightthickness=0,
    command=add_record,
    relief="flat")

    bea.place(
        x=154*widthset/1920, y=757*heightset/1080,
        width=420*widthset/1920,
        height=70*heightset/1080)
    
    
    Bouton_Etudiant_Supprimer = Image.open("canvas\Etudiant_Supprimer.png")
    Bouton_Etudiant_Supprimer = Bouton_Etudiant_Supprimer.resize(
        (int(200*widthset/1920), int(70*heightset/1080)), Image.ANTIALIAS)
    Bouton_Etudiant_Supprimer = ImageTk.PhotoImage(Bouton_Etudiant_Supprimer)
    bes = Button(newWindow,
    image=Bouton_Etudiant_Supprimer,
    borderwidth=0,
    highlightthickness=0,
    command=remove_record,
    relief="flat")

    bes.place(
        x=374*widthset/1920, y=660*heightset/1080,
        width=200*widthset/1920,
        height=70*heightset/1080)
    
    
    Bouton_Etudiant_Modifier = Image.open("canvas\Etudiant_Modifier.png")
    Bouton_Etudiant_Modifier = Bouton_Etudiant_Modifier.resize(
        (int(200*widthset/1920), int(70*heightset/1080)), Image.ANTIALIAS)
    Bouton_Etudiant_Modifier = ImageTk.PhotoImage(Bouton_Etudiant_Modifier)
    bem = Button(newWindow,
    image=Bouton_Etudiant_Modifier,
    borderwidth=0,
    highlightthickness=0,
    command=update_record,
    relief="flat")

    bem.place(
        x=154*widthset/1920, y=660*heightset/1080,
        width=200*widthset/1920,
        height=70*heightset/1080)
    
    
    Bouton_Etudiant_Retour = Image.open("canvas\Etudiant_Retour.png")
    Bouton_Etudiant_Retour = Bouton_Etudiant_Retour.resize(
        (int(150*widthset/1920), int(60*heightset/1080)), Image.ANTIALIAS)
    Bouton_Etudiant_Retour = ImageTk.PhotoImage(Bouton_Etudiant_Retour)
    ber = Button(newWindow,
    image=Bouton_Etudiant_Retour,
    borderwidth=0,
    highlightthickness=0,
    command=newWindow.destroy,
    relief="flat")

    ber.place(
        x=94*widthset/1920, y=61*heightset/1080,
        width=150*widthset/1920,
        height=60*heightset/1080)

    
    
    
    newWindow.mainloop()
    
    
    
#***************************************************************************
#---------------------------------------------------------------------------
#                  Partie Gestion Note
#---------------------------------------------------------------------------
#***************************************************************************    
    


def window_gestion_note():
    """ fonction qui créée une nouvelle fenêtre pour accéder à la gestion note """
    newWindow = Toplevel(window)
    newWindow.geometry(geometryset)
    newWindow.attributes('-fullscreen', True)
    newWindow.bind(' <Escape> ', lambda e: newWindow.attributes(
        '-fullscreen', False))
    
    #########  canvas preparation  #########
    
    canvas3 = Canvas(
        newWindow,
        bg="#ffffff",
        height=heightset,
        width=widthset,
        borderwidth=widthset,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    
    canvas3.place(x=0, y=0)
    
    #########  Background  #########
    
    Notesbackground = Image.open("canvas\Background_Notes.png")
    Notesbackground = Notesbackground.resize((widthset, heightset), Image.ANTIALIAS)
    Notesbackground = ImageTk.PhotoImage(Notesbackground)
    canvas3.create_image(
        widthset/2, heightset/2,
        image=Notesbackground)
    
    #########  TABLEAU  #########
    
    data = ouverture_fichier_csv('notes.csv')
    
    columns = ('#1', '#2', '#3', '#4', '#5')
    tableau = ttk.Treeview(newWindow, columns=columns, show='headings')
    
    tableau.heading('#1', text='ID Note')
    tableau.heading('#2', text='Année')
    tableau.heading('#3', text='ID étudiant')
    tableau.heading('#4', text='Matière')
    tableau.heading('#5', text='Note')

    tableau.column('#1', width=int(50*widthset/1920))
    tableau.column('#2', width=int(100*widthset/1920))
    tableau.column('#3', width=int(50*widthset/1920))
    tableau.column('#2', width=int(100*widthset/1920))
    tableau.column('#5', width=int(50*widthset/1920))

    
    global count    
    count = 0
    for i in range(1, len(data)):
        tableau.insert('', i, values=data[i])
        count += 1
    tableau.pack()
    
    tableau.place(x=783*widthset/1920, y=290*heightset/1080, width=int(960*widthset/1920), height=(490*heightset/1080))
    
    #########  Valeurs demandées  #########
    
    saisi_annee_img = Image.open("canvas\img_textBox0_Notes.png")
    saisi_annee_img = saisi_annee_img.resize((int(300*widthset/1920), int(48*heightset/1080)), Image.ANTIALIAS)
    saisi_annee_img = ImageTk.PhotoImage(saisi_annee_img)
    
    canvas3.create_image(
        440*widthset/1920, 307*heightset/1080,
        image = saisi_annee_img)

    saisi_annee = Entry(newWindow,
        bd = 0,
        bg = "#f1f1f1",
        highlightthickness = 0,
        font= 15)

    saisi_annee.place(
        x = 320*widthset/1920, y = 283*heightset/1080,
        width = 252*widthset/1920,
        height = 48*heightset/1080)
    
    
    
    saisi_id_img = Image.open("canvas\img_textBox1_Notes.png")
    saisi_id_img = saisi_id_img.resize((int(300*widthset/1920), int(48*heightset/1080)), Image.ANTIALIAS)
    saisi_id_img = ImageTk.PhotoImage(saisi_id_img)
    
    canvas3.create_image(
        440*widthset/1920, 393*heightset/1080,
        image = saisi_id_img)

    saisi_id = Entry(newWindow,
        bd = 0,
        bg = "#f1f1f1",
        highlightthickness = 0,
        font= 15)

    saisi_id.place(
        x = 320*widthset/1920, y = 369*heightset/1080,
        width = 252*widthset/1920,
        height = 48*heightset/1080)
    
    
    saisi_matiere_img = Image.open("canvas\img_textBox2_Notes.png")
    saisi_matiere_img = saisi_matiere_img.resize((int(300*widthset/1920), int(48*heightset/1080)), Image.ANTIALIAS)
    saisi_matiere_img = ImageTk.PhotoImage(saisi_matiere_img)
    
    canvas3.create_image(
        440*widthset/1920, 486*heightset/1080,
        image = saisi_matiere_img)

    saisi_matiere = Entry(newWindow,
        bd = 0,
        bg = "#f1f1f1",
        highlightthickness = 0,
        font= 15)

    saisi_matiere.place(
        x = 320*widthset/1920, y = 462*heightset/1080,
        width = 252*widthset/1920,
        height = 48*heightset/1080)
    
    
    saisi_note_img = Image.open("canvas\img_textBox3_Notes.png")
    saisi_note_img = saisi_note_img.resize((int(300*widthset/1920), int(48*heightset/1080)), Image.ANTIALIAS)
    saisi_note_img = ImageTk.PhotoImage(saisi_note_img)
    
    canvas3.create_image(
        440*widthset/1920, 580*heightset/1080,
        image = saisi_note_img)

    saisi_note = Entry(newWindow,
        bd = 0,
        bg = "#f1f1f1",
        highlightthickness = 0,
        font= 15)

    saisi_note.place(
        x = 320*widthset/1920, y = 556*heightset/1080,
        width = 252*widthset/1920,
        height = 48*heightset/1080)
    
    #########  Sélection et changement de valeurs dans le tableau  #########
    
    def select_record():
        """ fonction qui sert à sélectionner les élements du tableau"""
        saisi_annee.delete(0, END)
        saisi_id.delete(0, END)
        saisi_matiere.delete(0, END)
        saisi_note.delete(0, END)

        selected = tableau.focus()
        values = tableau.item(selected, 'values')

        saisi_annee.insert(0, values[1])
        saisi_id.insert(0, values[2])
        saisi_matiere.insert(0, values[3])
        saisi_note.insert(0, values[4])
    
    def add_record():
        """ fonction qui permet d'ajouter des données dans le tableau"""
        data = ouverture_fichier_csv('notes.csv')
        id_note = int(data[-1][0])+1
        annee = saisi_annee.get()
        id = saisi_id.get()
        matiere = saisi_matiere.get()
        note = saisi_note.get()
        global count
        tableau.insert(parent='', index='end', iid=count, text='', values=(id_note, annee,id , matiere, note))
        count+=1

        ajoutNote(id, annee, matiere, note)
        
        saisi_annee.delete(0, END)
        saisi_id.delete(0, END)
        saisi_matiere.delete(0, END)
        saisi_note.delete(0, END)
    
    def update_record():
        """fonction qui permet de modifier les données du tableau"""
        selected = tableau.focus()
        values = tableau.item(selected, 'values')
        id_note = values[0]
        annee = saisi_annee.get()
        id = saisi_id.get()
        matiere = saisi_matiere.get()
        note = saisi_note.get()
        
        modificationNote(id, annee, matiere, note, id_note) 
           
        tableau.item(selected, text="", values=(
            id_note, annee, id, matiere, note))
        
        saisi_annee.delete(0, END)
        saisi_id.delete(0, END)
        saisi_matiere.delete(0, END)
        saisi_note.delete(0, END)
        
    def remove_record():
        """fonction qui permet de modifier des données dans le tableau"""
        selected = tableau.focus()
        values = tableau.item(selected, 'values')    
        id_note = values[0]
        suppressionNote(id_note)
        x = tableau.selection()[0]
        tableau.delete(x)
        saisi_annee.delete(0, END)
        saisi_id.delete(0, END)
        saisi_matiere.delete(0, END)
        saisi_note.delete(0, END)
        

    def clicker(e):
        """ fonction qui prend en compte l'action de cliquer """
        select_record()

    tableau.bind("<ButtonRelease-1>", clicker)
    
    
    #########  Boutons Ajouter, Modifier, Supprimer et Retour #########
    
    
    Bouton_Note_Ajouter = Image.open("canvas\Ajouter_Notes.png")
    Bouton_Note_Ajouter = Bouton_Note_Ajouter.resize(
        (int(420*widthset/1920), int(70*heightset/1080)), Image.ANTIALIAS)
    Bouton_Note_Ajouter = ImageTk.PhotoImage(Bouton_Note_Ajouter)
    bna = Button(newWindow,
    image=Bouton_Note_Ajouter,
    borderwidth=0,
    highlightthickness=0,
    command=add_record,
    relief="flat")

    bna.place(
        x=154*widthset/1920, y=757*heightset/1080,
        width=420*widthset/1920,
        height=70*heightset/1080)
    
    
    Bouton_Note_Supprimer = Image.open("canvas\Supprimer_Notes.png")
    Bouton_Note_Supprimer = Bouton_Note_Supprimer.resize(
        (int(200*widthset/1920), int(70*heightset/1080)), Image.ANTIALIAS)
    Bouton_Note_Supprimer = ImageTk.PhotoImage(Bouton_Note_Supprimer)
    bns = Button(newWindow,
    image=Bouton_Note_Supprimer,
    borderwidth=0,
    highlightthickness=0,
    command=remove_record,
    relief="flat")

    bns.place(
        x=374*widthset/1920, y=660*heightset/1080,
        width=200*widthset/1920,
        height=70*heightset/1080)
    
    
    Bouton_Note_Modifier = Image.open("canvas\Modifier_Notes.png")
    Bouton_Note_Modifier = Bouton_Note_Modifier.resize(
        (int(200*widthset/1920), int(70*heightset/1080)), Image.ANTIALIAS)
    Bouton_Note_Modifier = ImageTk.PhotoImage(Bouton_Note_Modifier)
    bnm = Button(newWindow,
    image=Bouton_Note_Modifier,
    borderwidth=0,
    highlightthickness=0,
    command=update_record,
    relief="flat")

    bnm.place(
        x=154*widthset/1920, y=660*heightset/1080,
        width=200*widthset/1920,
        height=70*heightset/1080)
    
    
    Bouton_Note_Retour = Image.open("canvas\Retour_Notes.png")
    Bouton_Note_Retour = Bouton_Note_Retour.resize(
        (int(150*widthset/1920), int(60*heightset/1080)), Image.ANTIALIAS)
    Bouton_Note_Retour = ImageTk.PhotoImage(Bouton_Note_Retour)
    bnr = Button(newWindow,
    image=Bouton_Note_Retour,
    borderwidth=0,
    highlightthickness=0,
    command=newWindow.destroy,
    relief="flat")

    bnr.place(
        x=94*widthset/1920, y=61*heightset/1080,
        width=150*widthset/1920,
        height=60*heightset/1080)
    
    newWindow.mainloop()

#----------------------------
#########  Accueil  #########
#----------------------------

#########  canvas preparation  #########

canvas = Canvas(
    window,
    bg="#ffffff",
    height=heightset,
    width=widthset,
    borderwidth=widthset,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

#########  Background  #########

background_img = Image.open("canvas\l_arriere_plan.png")
background_img = background_img.resize((widthset, heightset), Image.ANTIALIAS)
background_img = ImageTk.PhotoImage(background_img)
background = canvas.create_image(
    widthset/2, heightset/2,
    image=background_img)

#########  Boutons Gestion Etudiant, Gestion Notes et Quitter  #########

Bouton_Gestion_Etudiant = Image.open("canvas\Bouton_Gestion_Etudiant.png")
Bouton_Gestion_Etudiant = Bouton_Gestion_Etudiant.resize(
    (int(996*widthset/1920), int(149*heightset/1080)), Image.ANTIALIAS)
Bouton_Gestion_Etudiant = ImageTk.PhotoImage(Bouton_Gestion_Etudiant)

b0 = Button(
    image=Bouton_Gestion_Etudiant,
    borderwidth=0,
    highlightthickness=0,
    command=window_gestion_etudiant,
    relief="flat")

b0.place(
    x=462*widthset/1920, y=320*heightset/1080,
    width=996*widthset/1920,
    height=148*heightset/1080)


Bouton_Gestion_Note = Image.open("canvas\Bouton_Gestion_Notes.png")
Bouton_Gestion_Note = Bouton_Gestion_Note.resize(
    (int(996*widthset/1920), int(150*heightset/1080)), Image.ANTIALIAS)
Bouton_Gestion_Note = ImageTk.PhotoImage(Bouton_Gestion_Note)
b1 = Button(
    image=Bouton_Gestion_Note,
    borderwidth=0,
    highlightthickness=0,
    command=window_gestion_note,
    relief="flat")

b1.place(
    x=462*widthset/1920, y=585*heightset/1080,
    width=996*widthset/1920,
    height=149*heightset/1080)


Bouton_Exit = Image.open("canvas\Bouton_Sortie.png")
Bouton_Exit = Bouton_Exit.resize(
    (int(338*widthset/1920), int(94*heightset/1080)), Image.ANTIALIAS)
Bouton_Exit = ImageTk.PhotoImage(Bouton_Exit)

b2 = Button(
    image=Bouton_Exit,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat")

b2.place(
    x=1458*widthset/1920, y=855*heightset/1080,
    width=338*widthset/1920,
    height=94*heightset/1080)




window.resizable(True, True)
window.mainloop()
