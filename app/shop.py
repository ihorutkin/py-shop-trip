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

    @classmethod
    def get_list_of_shops(cls) -> list:
        with open("app/config.json", "r") as file:
            data = json.load(file)

        shops_list = data.get("shops")
        shops = [
            Shop(
                name=shop.get("name"),
                location=shop.get("location"),
                products=shop.get("products")
            )
            for shop in shops_list
        ]
        return shops
