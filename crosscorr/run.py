import sys
import os
import yaml
import argparse
import subprocess
import pdb

import compute


"""
crosscorr:
This module is used to compute cross-correlation
redshifts for sets of galaxies. 
"""


def process_configuration(filename):
    with open(filename, 'r') as f:
        config = yaml.load(f)
    return config


def main(config):
    data_p, data_s = compute.read_all_data(cfg)
    
    # Apply any cuts (on mass, mag, etc.) TODO

    # Cut into regions of roughly equal galaxy density

    # Compute redshift distributions in each jackknife region

    # Use regions to estimate uncertainty 



if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, help="pass your configuration file",
                        default="default.yaml")
    args = parser.parse_args()

    print("[*] Starting CROSSCORR...")
    cfg = process_configuration(args.config)
    main(cfg)
