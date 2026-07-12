import os
from PIL import Image

def convert_to_webp(input_folder, output_folder):
    # Controllo se la cartella di output esiste, altrimenti la creo
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Scandisco tutti i file nella cartella di input
    for filename in os.listdir(input_folder):
        filepath = os.path.join(input_folder, filename)
        
        # Verifico se il file è un'immagine PNG o JPG
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            # Apro l'immagine
            with Image.open(filepath) as img:
                # Prendo il nome del file senza estensione
                file_name = os.path.splitext(filename)[0]
                
                # Compongo il percorso del file di output in formato WebP
                output_filepath = os.path.join(output_folder, f"{file_name}.webp")
                
                # Converto l'immagine in formato WebP e la salvo
                img.save(output_filepath, "WEBP")

    print("Conversione completata!")

if __name__ == "__main__":
    # Chiedo all'utente di specificare la cartella di input e di output
    input_folder = input("Inserisci il percorso della cartella di input: ")
    output_folder = input("Inserisci il percorso della cartella di output: ")
    
    # Eseguo la conversione
    convert_to_webp(input_folder, output_folder)