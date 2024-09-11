import json


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def get_list_of_shops() -> list:
        with open("app/config.json", "r") as file:
            data = json.load(file)

        shops_list = data["shops"]
        shops = [
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            for shop in shops_list
        ]
        return shops
