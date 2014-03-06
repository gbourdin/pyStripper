# coding=utf-8
from NFOStripper import NFOStripper
import os
import config

NFOS_DIR = "./nfos/"

def test_NFOStripper():
    # We'll skip testing for access since we can assume we have enough
    # permissions over the files we're running this test on.
    for nfo in os.listdir(NFOS_DIR):
        if nfo.endswith(".nfo"):
            config.INPUT_FILE = os.path.abspath(os.path.join(NFOS_DIR, nfo))
            config.OUTPUT_FILE = os.path.abspath(os.path.join(NFOS_DIR, nfo.replace(".nfo", ".txt")))

            # Create new stripper.
            stripper = NFOStripper()
            # Strip all the ascii
            stripper.strip()
            # Write the output
            stripper.write_output()


if __name__ == '__main__':
    test_NFOStripper()