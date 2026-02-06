import os
from PIL import Image
import pillow_avif  # Assicurati di aver fatto: pip install pillow-avif-plugin

def converti_avif_nella_cartella():
    # Prende la cartella dove si trova lo script
    cartella_attuale = os.getcwd()
    # Crea una sottocartella per non fare confusione con i file originali
    cartella_output = os.path.join(cartella_attuale, "convertite_jpg")

    if not os.path.exists(cartella_output):
        os.makedirs(cartella_output)

    print(f"Sto cercando file .avif in: {cartella_attuale}")

    for nome_file in os.listdir(cartella_attuale):
        if nome_file.lower().endswith(".avif"):
            percorso_input = os.path.join(cartella_attuale, nome_file)
            nome_senza_estensione = os.path.splitext(nome_file)[0]
            percorso_output = os.path.join(cartella_output, f"{nome_senza_estensione}.jpg")

            try:
                with Image.open(percorso_input) as img:
                    # Obbligatorio convertire in RGB per il formato JPG
                    img_rgb = img.convert("RGB")
                    img_rgb.save(percorso_output, "JPEG", quality=95)
                
                print(f"✅ Successo: {nome_file} -> {nome_senza_estensione}.jpg")
            except Exception as e:
                print(f"❌ Errore su {nome_file}: {e}")

if __name__ == "__main__":
    converti_avif_nella_cartella()
    print("\nProcedura terminata. Trovi i file nella cartella 'convertite_jpg'.")