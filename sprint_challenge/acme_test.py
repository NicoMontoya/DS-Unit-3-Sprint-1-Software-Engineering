#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, inventory_report
from possible_values import *


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
    
    def test_explode(self):
        """Test if explode function works properly"""
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), '...boom!')

    def test_stealability(self):
        """TEst if stealability function works properly"""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), 'Kinda stealable.')

    def test_default_num_products(self):
        """Test default number of products"""
        items = generate_products()
        self.assertEqual(len(items), 30)

    # def test_legal_names(self):
    #     """Test that names are legit"""
    #       # I want to generate a list of all possible values.
    #       # then I want to go through all items in generated list
    #       # and check if the item is in the list of all possible items
    #       pass



if __name__ == '__main__':
    unittest.main()