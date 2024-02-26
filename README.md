# Randomizing Data

## Asset

```python
assets = [
    {"id": <int>, "purchase_date": "YYYY-MM-DD"},
    {"id": <int>, "purchase_date": "YYYY-MM-DD"},
    ...
]
```

**Write a function that creates `assets` with p random items of varying purchase dates that are between x days ago and today**

```
def create_assets(p):
    return None
```

## Rental

```
rentals = [
    {"id": 1, "asset_id": 1, "start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"},
    {"id": 2, "asset_id": 2, "start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"},
    {"id": 3, "asset_id": 3, "start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"},
    {"id": 4, "asset_id": 2, "start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"},
    {"id": 5, "asset_id": 3, "start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"},
    ...
]
```

**Write a function that uses `assets` created previously and creates `rentals` with q random items of varying start and end dates**

```
def create_rentals(assets, q):
    return None
```

Constraints:
1. For a given asset, start and end dates may be adjacent but may not overlap at all.
2. Start dates cannot be greater than `datetime.date.today()`

Example:

✅ Items with the same asset_id and a start/end of 2023-12-05/2023-12-09 and 2023-12-10/2023-12-23<br>
❎ Items with the same asset_id and a start/end of 2023-12-05/2023-12-09 and 2023-12-08/2023-12-23