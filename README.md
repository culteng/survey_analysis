# Strickland Institute Diversity Survey

## code
### `cleaning.py`
- pulls in a csv from `data/raw`
- cleans column names, data, converts to categoricals...
- then saves cleaned as new csv in `data/cleaned`

### `analysis.py`
- pulls in all CSVs stored in `data/cleaned`
- loads them into a single pd.DataFrame
- generates charts & saves them to `imgs/`

### `report.py` 
- will select text based on results
- pulls charts from `imgs/`
- generates a pdf
