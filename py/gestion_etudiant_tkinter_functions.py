from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv




def ajoutEtudiant(*donneesEtudiant) :
        """
        Cette fonction a pour objectif d'ajouter un étudiant dans la base de données
        IN :
        OUT :
        """
        data = ouverture_fichier_csv('etudiants.csv')
        check = False
        nom = donneesEtudiant[1]
        prénom = donneesEtudiant[0]

        for i in range(len(data)):
            if data[i][2] != nom.upper() and data[i][3] != prénom:
                check = False
            elif data[i][2] == nom.upper() and data[i][3] == prénom:
                check = True
                break
            
        if check == False:
            nouvel_eleve = []
            id = int(data[-1][0])+1        
            nouvel_eleve.append(id)
            genre = donneesEtudiant[2]
            genre = genre.upper()
            nouvel_eleve.append(genre)
            nom = donneesEtudiant[1]
            nom = nom.upper()
            nouvel_eleve.append(nom)
            nouvel_eleve.append(donneesEtudiant[0])
            nouvel_eleve.append(donneesEtudiant[3])

            data.append(nouvel_eleve)

            ecriture_fichier_csv(data, 'etudiants.csv')
            print("\nNouvel élève ajouté \n")    
        else:
            print("\nL'étudiant existe déjà \nSi vous souhaitez modifier les informations, utilisez Modification Etudiant")
        return 
    
    
def modificationEtudiant(*donneesEtudiant) :
        """
        Cette fonction a pour objectif de modifier les données pour un étudiant dans la base de données
        IN :
        OUT :
        """
        data = ouverture_fichier_csv('etudiants.csv')
        id = donneesEtudiant[0]
        prenom = donneesEtudiant[1]
        nom = donneesEtudiant[2]
        genre = donneesEtudiant[3]
        genre = genre.upper()
        email = donneesEtudiant[4]
        
        check = True
        
        for i in range(len(data)):

            if data[i][0] != id:
                check = True
            elif data[i][0] == id:
                check = False
                break
        if check == False:
            new_data = []
        
            new_data.append(id)
            new_data.append(genre)
            nom = donneesEtudiant[2]
            nom = nom.upper()
            new_data.append(nom)
            new_data.append(prenom)
            new_data.append(email)
            data[i] = new_data
            ecriture_fichier_csv(data, 'etudiants.csv')
            print("\nModification effectuée \n")
            
        else:
            print("\nL'étudiant n'existe pas, veuillez réessayer ! \n")    
                
        
    
def suppressionEtudiant(id) :
        """
        Cette fonction a pour objectif de supprimer un étudiant de la base de données
        IN :
        OUT :
        """
        check = True
        data = ouverture_fichier_csv('etudiants.csv')

        for i in range(len(data)):

            if data[i][0] != id:
                check = True
            elif data[i][0] == id:
                check = False
                break

        if check == False:
            for i in range(len(data)):
                if data[i][0] == id:
                    del data[i]
                    break
            ecriture_fichier_csv(data, 'etudiants.csv')
            print("\nSuppression effectuée \n")
        else:
            print("\nL'étudiant n'existe pas, veuillez réessayer ! \n")

        return