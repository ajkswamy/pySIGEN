from PIL import Image
from PIL.TiffImagePlugin import TiffImageFile
import os
import logging
import numpy as np
import typing


def tifStack2ImageSeq(tifFile: str, tiffOutDir: str):

    logging.info("[tifStack2ImageSeq] Got Input File: {}\nOutput directory: {}".format(tifFile, tiffOutDir))
    fileName = os.path.split(tifFile)[1]
    inStub, inExt = fileName.split('.')

    assert inExt in ["tif", "tiff"], \
        "tifFile must have '.tif' or '.tiff' extension"

    if not os.path.isdir(tiffOutDir):
        os.makedirs(tiffOutDir)

    try:
        logging.info("[tifStack2ImageSeq] Opening {}".format(tifFile))
        tif = Image.open(tifFile)
    except Exception as e:
        raise(IOError('Error opening {} as an image.'.format(tifFile)))

    assert isinstance(tif, TiffImageFile), "{} could not be read a TIFF Image Stack".format(tifFile)

    logging.info("[tifStack2ImageSeq] Writing individual slices as "
                 "{}xxxx.bmp to {}".format(inStub, tiffOutDir))
    for ind in range(tif.n_frames):
        tif.seek(ind)
        opFile = os.path.join(tiffOutDir, "{}{:04d}.bmp".format(inStub, ind))
        tif.save(opFile)

# from http://stackoverflow.com/questions/21953835/run-subprocess-and-print-output-to-logging/21978778#21978778
def log_subprocess_output(pipe: typing.Union[bytes, None], subproc_name: str= '??'):

    if pipe:
        for line in pipe.split(b"\n"):
            logging.info('[subprocess {}] {}'.format(subproc_name, line.decode("utf-8")))

#***********************************************************************************************************************

