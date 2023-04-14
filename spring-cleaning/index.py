# data is in a submodule, run `git submodule update --init --recursive --remote` from root to fetch
import os
import numpy as np
import soundfile as sf
import librosa
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances

SCRIPT_FILEPATH = os.path.realpath(os.path.dirname(__file__))
DATASET_PATH = os.path.join(SCRIPT_FILEPATH, '..', 'data', 'audio', 'to_clean')

class AudioFile:
    def __init__(self, filename):
        filepath = os.path.join(DATASET_PATH, filename)
        data, samplerate = sf.read(filepath)

        self.name = filename
        self.data = data
        self.samplerate = samplerate
        self.filepath = filepath

def main():
    all_files = [AudioFile(filepath) for filepath in os.listdir(DATASET_PATH)]

    all_audios = np.vstack([file.data for file in all_files])
    distance_matrix = pairwise_distances(all_audios, metric='l2', n_jobs=-1)

    # Add a large number to the diagonal to avoid self-matches
    distance_matrix = distance_matrix + 1000000 * np.eye(distance_matrix.shape[0])

    # find the minimum distance for each audio file
    distances = np.min(distance_matrix, axis=0)

    # find the index for each minimum distance
    min_distance_indices = np.argmin(distance_matrix, axis=0)

    # for each distance in distances, if it's less than 5, replace with the index of 
    # the minimum distance in the distance matrix. Otherwise, replace with a -1
    ids = np.where(distances < 5, min_distance_indices, -1)

    # filter out the -1s 
    ids = ids[ids != -1]

    for id in ids:
        print(all_files[id].filepath)

if __name__ == "__main__":
    main()


