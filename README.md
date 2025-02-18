# Install
python -m pip install datasets
python -m pip install pronouncing
pyhton -m pip install librosa

# Use
There are three variables you should be concerned with; `target_phone`, `num_samples`, and `data_pth`.  

`target_phone` is the phoneme you would like to extract in the sentences, ex. `AA`, `ER`, `AE`.

`num_samples` controls how many occurences you would like to save of the selected phoneme, ex. `10`, `25`, `50`.

`data_pth` should be set as the path to the hugging face dataset, ex. `naharte/portuguese_english`, `naharte/chinese_english`. 

Edit these variables in the `load\_datasets.py` file before calling

```python
python3 load_datasets.py
```

The file will take a moment to run. It will then display the sentences it has found with the selected phoneme. To save the `.wav` files for the sentences, just type `y` and hit enter.
