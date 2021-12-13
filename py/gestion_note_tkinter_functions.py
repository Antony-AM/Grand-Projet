from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv


def ajoutNote(*donneesNote) :
    """
    Cette fonction a pour objectif d'ajouter une note dans la base de données
    IN :
    OUT :
    """    
    data = ouverture_fichier_csv('notes.csv')

    nouvelle_note = [] 

    id_note = int(data[-1][0])+1
    id = donneesNote[0]
    annee = donneesNote[1]
    matiere = donneesNote[2]
    note = donneesNote[3]

    nouvelle_note.append(id_note)
    nouvelle_note.append(annee)
    nouvelle_note.append(id)
    nouvelle_note.append(matiere)
    nouvelle_note.append(note)

    data.append(nouvelle_note)
    ecriture_fichier_csv(data, 'notes.csv')
        
    return    
    

def modificationNote(*donneesNote) :
    """
    Cette fonction a pour objectif de modifier une note dans la base de données du programme
    IN :
    OUT :
    """
    data = ouverture_fichier_csv('notes.csv')
    id = donneesNote[0]
    annee = donneesNote[1]
    matiere = donneesNote[2]
    note = donneesNote[3]
    id_note = donneesNote[4]
    replace = []
    for i in range(len(data)):
        if data[i][0] == id_note:
            id_note = data[i][0]
            replace.append(id_note)
            replace.append(annee)
            replace.append(id)
            replace.append(matiere)
            replace.append(note)
                
            data[i] = replace
            ecriture_fichier_csv(data, 'notes.csv')
            print("\nModification effectuée \n")
            break
    return    
    
def suppressionNote(*donneesNote) :
    """
    Cette fonction a pour objectif de supprimer une note dans la base de données
    IN :
    OUT :
    """
    data = ouverture_fichier_csv('notes.csv')
    id_note = donneesNote[0]

    for i in range(len(data)):
        if data[i][0] == id_note:
            del data[i]
            break
    ecriture_fichier_csv(data, 'notes.csv')
    print("\nSuppression effectuée \n")



    return