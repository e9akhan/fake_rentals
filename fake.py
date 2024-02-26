"""
    Module name :- fake
"""

from datetime import datetime, timedelta, date
import random


def create_assets(p):
    """
    Create assets.
    """
    assets = []
    purchase_date = [date.today() - timedelta(days=random.randint(366, 400))]
    for i in range(1, p + 1):
        assets.append(
            {
                "id": i,
                "purchase_date": datetime.strftime(
                    random.choice(purchase_date), "%Y-%m-%d"
                ),
            }
        )
    return assets


def search_asset(rentals, asset_id):
    """
    Search asset.
    """
    rentals = sorted(rentals, key=lambda x: x.get("id"), reverse=True)
    asset = None

    for rental in rentals:
        if rental["asset_id"] == asset_id:
            asset = rental
            break
    return asset


def create_rentals(assets, q):
    """
    Create rentals.
    """
    rentals, i = [], 1

    while len(rentals) < q:
        if not assets:
            break

        asset = random.choice(assets)
        searched_asset = search_asset(rentals, asset["id"])
        if searched_asset:
            today = datetime.strftime(date.today(), "%Y-%m-%d")
            if searched_asset["end_date"] < today:
                start_date = datetime.strptime(
                    searched_asset["end_date"], "%Y-%m-%d"
                ) + timedelta(days=1)
                end_date = start_date + timedelta(days=random.randint(1, 11))
                rentals.append(
                    {
                        "id": i,
                        "asset_id": asset["id"],
                        "start_date": datetime.strftime(start_date, "%Y-%m-%d"),
                        "end_date": datetime.strftime(end_date, "%Y-%m-%d"),
                    }
                )
                i += 1
            else:
                assets.remove(asset)
        else:
            start_date = date.today() - timedelta(days=365)
            end_date = start_date + timedelta(days=random.randint(1, 11))
            rentals.append(
                {
                    "id": i,
                    "asset_id": asset["id"],
                    "start_date": datetime.strftime(start_date, "%Y-%m-%d"),
                    "end_date": datetime.strftime(end_date, "%Y-%m-%d"),
                }
            )
            i += 1

    return rentals


if __name__ == "__main__":
    ASSETS = create_assets(10)
    print(create_rentals(ASSETS, 40))
