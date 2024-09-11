import json

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    customers_list = data["customers"]
    fuel_price = data["FUEL_PRICE"]
    customers = [
        Customer(
            name=person["name"],
            product_cart=person["product_cart"],
            location=person["location"],
            money=person["money"],
            car=Car(
                person["car"]["brand"],
                person["car"]["fuel_consumption"],
                fuel_price
            )
        )
        for person in customers_list
    ]

    shops_list = data["shops"]
    shops = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        for shop in shops_list
    ]

    for customer in customers:
        min_cost = 1000000
        cheapest_shop = None
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            customer.get_shop(shop, customer.car)

            if customer.cost_of_trip(shop, customer.car) < min_cost:
                min_cost = customer.cost_of_trip(shop, customer.car)
                cheapest_shop = shop
        if min_cost < customer.money:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            print("")
            customer.print_receipt(cheapest_shop)
            print(f"{customer.name} rides home")
            cost = customer.cost_of_trip(cheapest_shop, customer.car)
            print(f"{customer.name} now has {customer.money - cost} dollars")
            print("")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")


# shop_trip()
