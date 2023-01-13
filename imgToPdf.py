import os
from PIL import Image
import math
import sys

def main():
  # Définissez le chemin du dossier contenant les images
  image_folder = 'programmes/imgToPdf/img'

  image_folderAbs = os.path.abspath(image_folder)
  #fichier d'erreur:
  err = []

  allFile = os.listdir(image_folderAbs)
  # Parcourez tous les fichiers du dossier
  allImg = [f for f in allFile if isImg(f)]

  for file in allImg:
    # Chargez l'image
    try:
      image = Image.open(os.path.join(image_folder, file))
      image = image.convert('RGB')

      # Créez le nom du fichier PDF en remplaçant l'extension de l'image par .pdf
      pdf_filename = os.path.splitext(file)[0] + '.pdf'

      # Enregistrez l'image dans un fichier PDF
      image.save(os.path.join(image_folder, pdf_filename), 'PDF')
      
      os.remove(os.path.join(image_folder, file))
    except:
      err.append(file)
      continue
    
    progressBar(len(allImg), allImg.index(file)+1, err)

def isImg(file):
  if file.endswith(('.heic','.jpg','.png','.jpeg','.tif','.bmp','.JPG','.PNG','.JPEG','.TIF','.BMP')):
    return file 

def progressBar(nbVal, actVal, err):
  percent = actVal/nbVal
  nEquals = math.floor(percent*20)
  bar = '=' * nEquals + ' ' * ( 20 - nEquals )

  print("\r", end='')
  print(f"[{bar}] {percent*100:.2f}%", end='')

  if percent == 1:
    print("\nFin d'execution")
    if err != []:
      print("Erreurs:")
      for el in err:
        print(el)

if __name__ == '__main__':
  main()