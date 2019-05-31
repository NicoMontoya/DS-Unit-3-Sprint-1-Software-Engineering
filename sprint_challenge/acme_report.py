#!/usr/bin/env python

"""
generate random products and print a summary of them
"""
from possible_values import *
from acme import Product
from random import randint, uniform, sample, choice

def generate_products(n=30):
    """
    generate a given number of products (default 30), randomly, 
    and return them as a list
    """
    # begin with an empty list
    list_products = []

    #for specified number of products, generate and instance of Product
    for _ in list(range(n)):

        product = Product(name='{a} {p}'.format(p=choice(products),a=choice(adjectives)), 
        price=randint(5, 100), weight=randint(5,100),flammability=uniform(0.0,2.5))

        list_products.append(product)

    return list_products
    

def inventory_report(list_products):
    """
    takes a list of products, and prints a "nice" summary
    """
    total_price = 0
    total_weight= 0 
    total_flammability = 0
    for product in list_products:
        total_price +=  product.price
        total_weight += product.weight
        total_flammability += product.flammability 

    unique_products = len(set(list_products))
    average_price = total_price / len(list_products)
    average_weight = total_weight / len(list_products)
    average_flammability = total_flammability / len(list_products)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('------------------------------------------')
    print("Unique Products: ", unique_products)
    print("Average Price of items: ", average_price)
    print("Average Weight of items: ", average_weight)
    print("Average Flammability of items: ", average_flammability)


if __name__ == '__main__':
    inventory_report(generate_products())
