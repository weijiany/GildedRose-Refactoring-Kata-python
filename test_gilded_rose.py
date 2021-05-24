# -*- coding: utf-8 -*-
import unittest
from typing import List

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_we_can_run_tests(self):
        """Ensure that we can run unit tests."""
        self.assertTrue(True)

    def test_system_lowers_both_values_for_every_item(self):
        """Test the basics.

        - All items have a SellIn value which denotes the number of days we have to sell the item
        - All items have a Quality value which denotes how valuable the item is
        - At the end of each day our system lowers both values for every item
        """
        items: List[Item] = [Item("foo", 7, 11), Item("bar", 23, 42)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(6, items[0].sell_in)
        self.assertEqual(10, items[0].quality)
        self.assertEqual("bar", items[1].name)
        self.assertEqual(22, items[1].sell_in)
        self.assertEqual(41, items[1].quality)

    def test_quality_degrades_twice_as_fast(self):
        """Once the sell by date has passed, Quality degrades twice as fast"""
        items: List[Item] = [Item("foo", 0, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)

    def test_quality_is_never_negative(self):
        """The Quality of an item is never negative"""
        items: List[Item] = [Item("foo", 7, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_increases_in_quality(self):
        """"Aged Brie" actually increases in Quality the older it gets"""
        items: List[Item] = [Item("Aged Brie", 7, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)

    def test_aged_brie_quality_increases_by_2_when_past_sellin_date(self):
        """"Aged Brie"'s Quality increases by 2 when it is past its sell-in date"""
        items: List[Item] = [Item("Aged Brie", 0, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)

    def test_quality_is_never_more_than_50(self):
        """The Quality of an item is never more than 50"""
        items: List[Item] = [Item("Aged Brie", 7, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_never_has_to_be_sold_or_decreases_in_quality(self):
        """"Sulfuras", being a legendary item, never has to be sold or decreases in Quality"""
        items: List[Item] = [Item("Sulfuras, Hand of Ragnaros", 7, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_backstage_passes(self):
        """"Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
        Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
        Quality drops to 0 after the concert"""
        items: List[Item] = [Item("Backstage passes to a TAFKAL80ETC concert", 42, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)

        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)

        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].quality)

        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
