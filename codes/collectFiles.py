import os
import shutil

# Percorso della directory principale in cui ci sono le subdirectory
root_dir = r'C:\Users\Garda6\testi_bs'

# Directory di destinazione in cui incollare tutti i file
destination_dir = r'C:\Users\Garda6\raw-data'

# Crea la directory di destinazione se non esiste
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Variabile per mantenere il contatore dei nomi sequenziali
counter = 1

# Scansiona tutte le subdirectory e i file
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        # Costruisci il percorso completo del file
        file_path = os.path.join(subdir, file)
        
        # Crea un nome sequenziale per il file
        new_name = f'{counter:04d}{os.path.splitext(file)[1]}'
        new_path = os.path.join(destination_dir, new_name)
        
        # Copia il file nella destinazione con il nuovo nome
        shutil.copy(file_path, new_path)
        
        # Incrementa il contatore
        counter += 1

print("Copia e rinomina completati!")
