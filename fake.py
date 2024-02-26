"""
    Module name :- fake
"""

import datetime
import random
import os
import csv


def create_assets(p):
    """
    Create assets.
    """
    assets = []
    purchase_date = [
        datetime.date.today() - datetime.timedelta(days=random.randint(366, 400))
    ]
    for i in range(1, p + 1):
        assets.append(
            {
                "id": i,
                "purchase_date": datetime.datetime.strftime(
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
    rentals = []
    i = 1

    while len(rentals) < q:
        asset = random.choice(assets)
        searched_asset = search_asset(rentals, asset["id"])

        if searched_asset:
            today = datetime.datetime.strftime(datetime.date.today(), "%Y-%m-%d")

            if searched_asset["end_date"] < today:
                start_date = datetime.datetime.strptime(
                    searched_asset["end_date"], "%Y-%m-%d"
                ) + datetime.timedelta(days=random.randint(1, 2))
                end_date = start_date + datetime.timedelta(days=random.randint(1, 11))
                rentals.append(
                    {
                        "id": i,
                        "asset_id": asset["id"],
                        "start_date": datetime.datetime.strftime(
                            start_date, "%Y-%m-%d"
                        ),
                        "end_date": datetime.datetime.strftime(end_date, "%Y-%m-%d"),
                    }
                )
                i += 1
        else:
            start_date = datetime.date.today() - datetime.timedelta(days=365)
            end_date = start_date + datetime.timedelta(days=random.randint(1, 11))
            rentals.append(
                {
                    "id": i,
                    "asset_id": asset["id"],
                    "start_date": datetime.datetime.strftime(start_date, "%Y-%m-%d"),
                    "end_date": datetime.datetime.strftime(end_date, "%Y-%m-%d"),
                }
            )
            i += 1

    return rentals


def main():
    """
    Main method.
    """
    assets = create_assets(10)
    rentals = create_rentals(assets, 40)

    filepath = os.path.join(os.getcwd(), "rentals.csv")

    with open(filepath, "w", encoding="utf-8") as f:
        headers = rentals[0].keys()
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rentals)


if __name__ == "__main__":
    main()
