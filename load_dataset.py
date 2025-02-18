from datasets import load_dataset
from scipy.io.wavfile import write
import pronouncing
import time
import os

target_phone = "ER"
num_samples = 25

ds = load_dataset("naharte/portuguese_english")

idx = []
audios = []
sentences = []
phs = []
for i in range(len(ds['train']['audio'])):
    if len(idx) >= num_samples:
        break
    found = False
    t = ds['train']['transcription'][i]
    words = t.split(' ')
    word_idx = 0
    while word_idx < len(words) and not found:
        phones = pronouncing.phones_for_word(words[word_idx])
        word_idx += 1 

        if len(phones) == 0:
            continue
        phones = phones[0] # Only take primary pronuciation
        if any(target_phone in phone for phone in phones.split(" ")):
            idx.append(i)
            audios.append(ds['train']['audio'][i])
            sentences.append(t)
            phs.append(phones)
            found = True

print(f"IDXs for sentences containing {target_phone}:")
for s_id, sentence, ph in zip(idx, sentences, phs):
    print(f"{s_id}: {sentence} / {ph}")

ans = input("Do you want to download these samples?")
if ans == 'y':
    if not os.path.isdir(target_phone):
        os.mkdir(target_phone)
    for s_id, sentence, audio in zip(idx, sentences, audios):
        write(target_phone + "/" + audio['path'], audio['sampling_rate'], audio['array'])
