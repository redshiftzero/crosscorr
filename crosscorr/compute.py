import fitsio
import pdb

import estimators


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



def read_all_data(config_file):
    default_columns = ['RA', 'DEC', 'Z']
    photometric_cat = fitsio.read(config['data_p'], 
                                  cols=default_columns)
    spectroscopic_cat = fitsio.read(config['data_s'],
                                    cols=default_columns)

    return photometric_cat, spectroscopic_cat



