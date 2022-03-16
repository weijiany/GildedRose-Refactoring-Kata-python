import pytest as pytest

from gilded_rose import GildedRose
from Item import Item


class TestGildedRose:

    test_data = [
        (Item("foo", 1, 5), "foo", 0, 4),
        (Item("+5 Dexterity Vest", 10, 20), "+5 Dexterity Vest", 9, 19),
        (Item("+5 Dexterity Vest", -1, 20), "+5 Dexterity Vest", -2, 18),
        (Item("Aged Brie", 2, 0), "Aged Brie", 1, 1),
        (Item("Aged Brie", -1, 0), "Aged Brie", -2, 2),
        (Item("Elixir of the Mongoose", 5, 7), "Elixir of the Mongoose", 4, 6),
        (Item("Sulfuras, Hand of Ragnaros", 0, 80), "Sulfuras, Hand of Ragnaros", 0, 80),
        (Item("Sulfuras, Hand of Ragnaros", -1, 80), "Sulfuras, Hand of Ragnaros", -1, 80),
        (Item("Backstage passes to a TAFKAL80ETC concert", 15, 20), "Backstage passes to a TAFKAL80ETC concert", 14, 21),
        (Item("Backstage passes to a TAFKAL80ETC concert", 10, 49), "Backstage passes to a TAFKAL80ETC concert", 9, 50),
        (Item("Backstage passes to a TAFKAL80ETC concert", 5, 49), "Backstage passes to a TAFKAL80ETC concert", 4, 50),
        (Item("Backstage passes to a TAFKAL80ETC concert", 1, 20), "Backstage passes to a TAFKAL80ETC concert", 0, 23),
        (Item("Backstage passes to a TAFKAL80ETC concert", -1, 20), "Backstage passes to a TAFKAL80ETC concert", -2, 0)
    ]

    @pytest.mark.parametrize("item,name,sell_in,quality", test_data)
    def test(self, item: Item, name: str, sell_in: int, quality: int):
        app: GildedRose = GildedRose([item])
        app.update_quality()

        assert app.items[0].name == name
        assert app.items[0].sell_in == sell_in
        assert app.items[0].quality == quality
