import soundfile as sf
import librosa
import os
from tqdm import tqdm 


# script to downsample audio files to a lower sampling rate
# TODO cleanup and generalize this

if __name__ == '__main__':
    INPUT_DIR = './'
    OUTPUT_DIR = './16k'

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    files = [file for file in os.listdir(INPUT_DIR) if 'wav' in file]
    for filename in tqdm(files):
        y, sr = librosa.load(f'{INPUT_DIR}/{filename}', sr=16000)
        sf.write(f'{OUTPUT_DIR}/{filename}', y, sr)

