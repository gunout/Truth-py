def encoder_mot(mot):
    """
    Encode un mot en séquence numérique A=1, B=2, ..., Z=26
    """
    mot = mot.upper().strip()
    resultat = []
    
    for lettre in mot:
        if lettre.isalpha():
            numero = ord(lettre) - ord('A') + 1
            resultat.append(str(numero))
    
    return '.'.join(resultat)

def decoder_sequence(sequence):
    """
    Décode une séquence numérique en mot
    """
    nombres = sequence.split('.')
    mot_decode = []
    
    for nombre in nombres:
        if nombre.isdigit():
            numero = int(nombre)
            if 1 <= numero <= 26:
                lettre = chr(numero + ord('A') - 1)
                mot_decode.append(lettre)
    
    return ''.join(mot_decode)

def interface_terminal():
    """
    Interface interactive pour le terminal
    """
    print("=== Encodeur/Décodeur A=1, B=2, ..., Z=26 ===")
    print("Commandes:")
    print("  - Entrez un mot pour l'encoder en chiffres")
    print("  - Entrez une séquence (ex: 16.1.25.19) pour la décoder")
    print("  - 'quit' pour quitter")
    print("-" * 50)
    
    while True:
        try:
            entree = input("\nEntrez un mot ou une séquence : ").strip()
            
            if entree.lower() == 'quit':
                print("Au revoir !")
                break
            
            if not entree:
                continue
            
            # Vérifier si l'entrée est une séquence numérique
            if '.' in entree and all(part.isdigit() for part in entree.split('.')):
                # C'est une séquence à décoder
                resultat = decoder_sequence(entree)
                print(f"🔓 Décodé : {resultat}")
            else:
                # C'est un texte à encoder
                resultat = encoder_mot(entree)
                print(f"🔒 Encodé : {resultat}")
                
        except KeyboardInterrupt:
            print("\n\nAu revoir !")
            break
        except Exception as e:
            print(f"❌ Erreur : {e}")

# Version simple sans menu
def encodeur_simple():
    """
    Version ultra-simple : on entre un mot, il donne les chiffres
    """
    print("=== Encodeur Simple A=1, B=2, ..., Z=26 ===")
    print("Entrez un mot (ou 'quit' pour quitter)\n")
    
    while True:
        mot = input("Mot à encoder : ").strip()
        
        if mot.lower() == 'quit':
            break
            
        if mot:
            try:
                chiffres = encoder_mot(mot)
                print(f"→ {chiffres}\n")
            except Exception as e:
                print(f"Erreur : {e}\n")

# Lancement du programme
if __name__ == "__main__":
    # Choisir l'interface souhaitée :
    
    # Interface complète (encode et decode)
    interface_terminal()
    
    # Ou interface simple (encode seulement)
    # encodeur_simple()
