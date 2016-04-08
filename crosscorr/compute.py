import numpy as np
import fitsio
import pdb



def load_fits(fits, cols):
    """
    Load fits file using fitsio

    Args: 
         fits (str): input filename
         cols: list of strings to read in
    Returns:
         numpy ndarray 
    """

    return fitsio.read(fits, columns=cols) 


def read_all_data(config):
    default_columns = ['RA', 'DEC', 'Z', 'MAG_I']
    photometric_cat = fitsio.read(config['data_p'], 
                                  cols=default_columns)
    spectroscopic_cat = fitsio.read(config['data_s'],
                                    cols=default_columns)

    return photometric_cat, spectroscopic_cat
