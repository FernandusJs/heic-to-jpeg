# import necessary libraries.
import os
import pyheif
from PIL import Image


# function to import the heic files from a path.

def convert_heic_to_jpg(path):
    for filename in os.listdir(path):
        if filename.endswith(".heic"):
            heif_file = pyheif.read(os.path.join(path, filename))
            # read bytes from the heic file, convert to PIL image.
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )
            # save the file
            image_path = os.path.splitext(os.path.join(path, filename))[0] + ".jpg"
            image.save(image_path, "JPEG")
# call function, give path the path of the folder which has to be converted.
convert_heic_to_jpg("/")