""" This is a basic python script demonstrating the use of mne to load an
EEG file.

By David Western, Sep 2020.
"""

import argparse
import mne

def main(args):
    filepath = 'Path/to/an/edfFile.edf'

    # Load edf file into an mne object:
    eeg = mne.io.read_raw_edf(args.filepath)

    # Extract the signals to a numpy array:
    eegData = eeg.get_data()

    print(f"Extracted EEG data array with the following shape: {eegData.shape}")


if __name__ == '__main__':
    # Handle arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("edfPath", help="Path to copy of TUH EEG dataset containing EDF files.")
    args = parser.parse_args()

    main(args)