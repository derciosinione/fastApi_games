import os
from uuid import uuid4
from PIL import Image


def save_picture(file, folderName: str = ''):
    randon_uid = str(uuid4())
    _, f_ext = os.path.splitext(file.filename)
    picture_fn = randon_uid + f_ext
    
    path = os.path.join('static',folderName)
    if not os.path.exists(path):
        os.makedirs(path)
        
    picture_path = os.path.join(path,picture_fn)

    output_size = (125,125)
    img = Image.open(file.file)
    img.thumbnail(output_size)
    img.save(picture_path)

    return picture_fn