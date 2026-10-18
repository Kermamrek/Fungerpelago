from __future__ import annotations

from dataclasses import dataclass

from BaseClasses import Item, ItemClassification


@dataclass
class ItemData:
    classification: ItemClassification
    id: int


# fmt: off
ITEMS = {
    # RANDOM ITEMS
    "Random Minor Item": ItemData(ItemClassification.filler, 5001),  # Common Event 23
    "Random Minor Book": ItemData(ItemClassification.useful, 5002),  # Common Event 25, despite being a minor book it contains recipes and pinecone pig
    "Random Rare Book": ItemData(ItemClassification.useful, 5003),  # Common Event 26
    "Random Food Item": ItemData(ItemClassification.filler, 5004),  # Common Event 52
    "Random Rare Item": ItemData(ItemClassification.useful, 5005),  # Common Event 58
    "Random Alchemy": ItemData(ItemClassification.useful, 5006),  # Common Event 68
    "Random Good Armor": ItemData(ItemClassification.useful, 5007),  # Common Event 141
    "Random Scroll Item": ItemData(ItemClassification.useful, 5008),  # Common Event 149
    "Random Rare Book (Ancient)": ItemData(ItemClassification.useful, 5009),  # Common Event 178
    "Random Minor Book (Ancient)": ItemData(ItemClassification.filler, 5010),  # Common Event 179, despite being ancient I think every book here is useless
    "Soul stone": ItemData(ItemClassification.useful, 2115),  # Common Event 200 ... It's called "Random Great Item" but its just a soul stone
    "Random Weapon": ItemData(ItemClassification.useful, 5011),  # Common Event 238
    "Random Minor Weapon": ItemData(ItemClassification.useful, 5012),  # Common Event 239
    "Nights Random Item": ItemData(ItemClassification.filler, 5013),  # Common Event 250 TODO: look at where this is used? Probably Dungeon Nights and can be ignored
    "Guard Loot": ItemData(ItemClassification.filler, 5014),  # Common Event 253
    "Lizardman Loot": ItemData(ItemClassification.useful, 5015),  # Common Event 254
    "Lord of Flies Loot": ItemData(ItemClassification.useful, 5016),  # Common Event 255
    "Yellow Mage Loot": ItemData(ItemClassification.useful, 5017),  # Common Event 256

    # ITEMS FOUND IN "RANDOM ___ ITEM"
    # HAVE NOT CHECKED USEFUL STATUS FOR MOST OF THESE
    "Glass vial": ItemData(ItemClassification.filler, 2009),
    "Pipe": ItemData(ItemClassification.filler, 2073),
    "Nitroglycerin powder": ItemData(ItemClassification.filler, 2071),
    "Red vial": ItemData(ItemClassification.useful, 2054),
    "Ale": ItemData(ItemClassification.filler, 2038),
    "Small key": ItemData(ItemClassification.useful, 2020),
    "Cloth hood": ItemData(ItemClassification.filler, 7),
    "Leather helmet": ItemData(ItemClassification.filler, 8),
    "Oil": ItemData(ItemClassification.filler, 2012),
    "White vial": ItemData(ItemClassification.filler, 2052),
    "Water vial": ItemData(ItemClassification.filler, 2085),
    "Wooden buckler": ItemData(ItemClassification.filler, 16),
    "Bear trap": ItemData(ItemClassification.filler, 2076),
    "Raw meat": ItemData(ItemClassification.filler, 2152),
    "Throwing knife": ItemData(ItemClassification.filler, 2169),
    "Worm juice": ItemData(ItemClassification.filler, 2171),
    "Throwing dart": ItemData(ItemClassification.filler, 2182),
    "Pinecone": ItemData(ItemClassification.filler, 2026),

    "Poems of love and torment": ItemData(ItemClassification.filler, 2004),
    "Ma'havre": ItemData(ItemClassification.filler, 2023),
    "Studies of Gro-goroth I": ItemData(ItemClassification.filler, 2024),
    "The Fellowship ch.1": ItemData(ItemClassification.filler, 2025),
    "Studies of Alll-mer I": ItemData(ItemClassification.filler, 2036),
    "Studies of Sylvian I": ItemData(ItemClassification.filler, 2039),
    "Assassin's handbook I": ItemData(ItemClassification.filler, 2047),
    "Creation of life": ItemData(ItemClassification.filler, 2056),
    "The Tale of the Pocketcat I": ItemData(ItemClassification.filler, 2080),
    "The Tale of the Pocketcat II": ItemData(ItemClassification.filler, 2178),
    "Blood & Flower magic I": ItemData(ItemClassification.filler, 2083),
    "Torn page": ItemData(ItemClassification.filler, 2086),
    "Anathomia": ItemData(ItemClassification.filler, 2136),
    "The Fellowship ch.2": ItemData(ItemClassification.filler, 2137),
    "Pinecone pig instructions": ItemData(ItemClassification.filler, 2170),
    "The Penance Knights": ItemData(ItemClassification.filler, 2203),

    "Wheat flour": ItemData(ItemClassification.filler, 2017),
    "Moldy bread": ItemData(ItemClassification.filler, 2031),
    "Cheese": ItemData(ItemClassification.filler, 2037),
    "Cabbage": ItemData(ItemClassification.filler, 2043),
    "Salami": ItemData(ItemClassification.filler, 2068),
    "Blueberries": ItemData(ItemClassification.filler, 2069),
    "Turnip": ItemData(ItemClassification.filler, 2204),

    # Pretty much only comes from the terror and starvation food roll
    "Rotten Egg": ItemData(ItemClassification.filler, 2208),
    "Rotten Turnip": ItemData(ItemClassification.filler, 2206),
    "Rotten Meatpie": ItemData(ItemClassification.filler, 2207),
    "Rotten Vegetable pie": ItemData(ItemClassification.filler, 2209),
    "Rotten Cabbage": ItemData(ItemClassification.filler, 2210),
    "Rotten Tomato": ItemData(ItemClassification.filler, 2211),
    "Rotten Carrot": ItemData(ItemClassification.filler, 2212),
    "Rotten Blueberries": ItemData(ItemClassification.filler, 2213),

    "The Fellowship ch.2 (Original)": ItemData(ItemClassification.filler, 2138),
    "The Fellowship ch.1 (Original)": ItemData(ItemClassification.filler, 2139),
    "Natural doctrine I": ItemData(ItemClassification.filler, 2155),
    "Natural doctrine II": ItemData(ItemClassification.filler, 2156),

    "Black vial": ItemData(ItemClassification.filler, 2011),
    "Purple vial": ItemData(ItemClassification.filler, 2053),
    "Green vial": ItemData(ItemClassification.filler, 2061),
    "Orange vial": ItemData(ItemClassification.filler, 2078),

    "Iron mace": ItemData(ItemClassification.filler, 1003),
    "Iron spear": ItemData(ItemClassification.filler, 1010),
    "Short bow": ItemData(ItemClassification.filler, 1011),
    "Empty scroll": ItemData(ItemClassification.filler, 2088),
    "Spider shield": ItemData(ItemClassification.filler, 17),
    "Eagle crest shield": ItemData(ItemClassification.filler, 18),
    "Plate mail": ItemData(ItemClassification.filler, 14),
    "Fur armor": ItemData(ItemClassification.filler, 12),
    "Ring of the still-blood": ItemData(ItemClassification.filler, 28),
    "Sorcerer's stone": ItemData(ItemClassification.filler, 27),
    "Thorned ring": ItemData(ItemClassification.filler, 30),
    "Trench coat": ItemData(ItemClassification.filler, 46),
    "Cursed iron mace": ItemData(ItemClassification.filler, 1015),
    "Cursed short sword": ItemData(ItemClassification.filler, 1013),
    "Eyeglasses": ItemData(ItemClassification.filler, 51),
    "Eastern perfume": ItemData(ItemClassification.filler, 52),
    "Morning star": ItemData(ItemClassification.filler, 1038),
    "Bone shears": ItemData(ItemClassification.filler, 1034),

    "Scroll of thievery": ItemData(ItemClassification.useful, 2102),
    "Scroll of the highwaymen": ItemData(ItemClassification.useful, 2103),
    "Scroll of lockpicking": ItemData(ItemClassification.useful, 2104),
    "Scroll of fencing": ItemData(ItemClassification.useful, 2105),
    "Scroll of the swordsman": ItemData(ItemClassification.useful, 2106),
    "Scroll of the general": ItemData(ItemClassification.useful, 2107),
    "Scroll of the wizards": ItemData(ItemClassification.useful, 2108),
    "Scroll of the dark mage": ItemData(ItemClassification.useful, 2109),
    "Scroll of the wildman": ItemData(ItemClassification.useful, 2110),
    "Scroll of marksmanship": ItemData(ItemClassification.useful, 2111),
    "Scroll of berserk": ItemData(ItemClassification.useful, 2112),
    "Scroll of the long sword": ItemData(ItemClassification.useful, 2113),
    "Scroll of the black arts": ItemData(ItemClassification.useful, 2174),
    "Scroll of the church of healing": ItemData(ItemClassification.useful, 2175),
    "Scroll of the church of Sylvian": ItemData(ItemClassification.useful, 2176),
    "Scroll of the leeches": ItemData(ItemClassification.useful, 2177),

    # MULTIPLES
    "Tinderbox x5": ItemData(ItemClassification.filler, 6007),
    "Tobacco x2": ItemData(ItemClassification.filler, 6074),
    # Fundementally does not matter these have the same value, as the function looks at the name
    "Silver coin x5": ItemData(ItemClassification.filler, 6059),
    "Silver coin x12": ItemData(ItemClassification.filler, 6059),
    "Silver coin x6": ItemData(ItemClassification.filler, 6059),
    "Silver coin x3": ItemData(ItemClassification.filler, 6059),
    "Dirt x5": ItemData(ItemClassification.filler, 6058),
    # Special case since its two different items
    "Cloth fragment and Stick": ItemData(ItemClassification.filler, 6000),

    "Eggs x2": ItemData(ItemClassification.filler, 6015),
    "Carrots x2": ItemData(ItemClassification.filler, 6042),
    "Tomato x2": ItemData(ItemClassification.filler, 6064),
    "Dried mushroom x2": ItemData(ItemClassification.filler, 6065),

    "Glass vials x3": ItemData(ItemClassification.filler, 6009),
    "White vial x2": ItemData(ItemClassification.filler, 6052),

    "Light blue vial x2": ItemData(ItemClassification.filler, 6067),
    "Iron arrow x3": ItemData(ItemClassification.filler, 6075),
    "Silver coin x35": ItemData(ItemClassification.filler, 6059),

    # NOTHING
    "Nothing": ItemData(ItemClassification.filler, 9999),

    # NOTE: there may be more loot tables, since there's way more enemy types- double check?
    # FIXED ITEMS
    "Torch": ItemData(ItemClassification.useful, 2005),  # Ones on the cave walls
    "Cube of depths": ItemData(ItemClassification.progression, 2119),
    "Blue demon powder": ItemData(ItemClassification.useful, 2183),
    "Book pages I": ItemData(ItemClassification.useful, 2184),
    "Book pages II": ItemData(ItemClassification.useful, 2185),
    "Book pages III": ItemData(ItemClassification.useful, 2186),
    "Map #1": ItemData(ItemClassification.progression, 2162),
    "Map #2": ItemData(ItemClassification.progression, 2163),
    "Map #3": ItemData(ItemClassification.progression, 2188),
    "Mockup book": ItemData(ItemClassification.progression, 2049),
    "Bonesaw": ItemData(ItemClassification.useful, 2140),
    "Lucky coin": ItemData(ItemClassification.useful, 2201),
    "Scroll of transmutation": ItemData(ItemClassification.useful, 2164),
    "Scroll of walking on water": ItemData(ItemClassification.progression, 2161),
    "Stick": ItemData(ItemClassification.filler, 2027),
    "Explosive vial": ItemData(ItemClassification.progression | ItemClassification.useful, 2079),
    "Vault key": ItemData(ItemClassification.progression, 2202),
    "Rope": ItemData(ItemClassification.progression, 2199),
    "Skinning knife": ItemData(ItemClassification.useful, 2044),
    "Cell keys F3": ItemData(ItemClassification.progression, 2048),
    "2F key": ItemData(ItemClassification.progression, 2051),
    "King's passage key": ItemData(ItemClassification.progression, 2180),
    "Old passage key": ItemData(ItemClassification.progression, 2179),

    # SOULS/ENEMY REWARDS
    # Set these as multi-items since they're required for one person's S ending... will this break something?
    "Crow Mauler soul": ItemData(ItemClassification.progression | ItemClassification.useful, 36),
    "Salmonsnake soul": ItemData(ItemClassification.progression | ItemClassification.useful, 38),
    "Cavemother soul": ItemData(ItemClassification.progression | ItemClassification.useful, 41),
    "Old Knight soul": ItemData(ItemClassification.progression | ItemClassification.useful, 2123),
    "Iron Shakespeare soul": ItemData(ItemClassification.progression | ItemClassification.useful, 37),
    "White angel soul": ItemData(ItemClassification.progression | ItemClassification.useful, 39),
    "Black witch soul": ItemData(ItemClassification.progression | ItemClassification.useful, 40),
    "Butterfly soul": ItemData(ItemClassification.progression | ItemClassification.useful, 42),
    "Old guardian soul": ItemData(ItemClassification.progression | ItemClassification.useful, 43),
    "Endless soul": ItemData(ItemClassification.progression | ItemClassification.useful, 2126),  # Required for an ending/gets you hexen skills
    "Domination soul": ItemData(ItemClassification.progression | ItemClassification.useful, 2127),  # Required for an ending/gets you hexen skills
    "Enlightened soul": ItemData(ItemClassification.progression | ItemClassification.useful, 2128),  # Required for an ending/gets you hexen skills
    "Tormented soul": ItemData(ItemClassification.progression | ItemClassification.useful, 2129),  # Required for an ending/gets you hexen skills
    "Crow emblem key": ItemData(ItemClassification.progression, 2148),

    # BOOKS/PAPERS
    # NOTE: (a large majority of these have been listed as filler due to not being important in any way. Would this mess something up?
    "Captain's orders": ItemData(ItemClassification.filler, 2018),
    "List of inmates": ItemData(ItemClassification.filler, 2019),
    "Captain's diary 1": ItemData(ItemClassification.filler, 2022),
    "Torturer's notes 1": ItemData(ItemClassification.filler, 2035),
    "Captain's diary 2": ItemData(ItemClassification.filler, 2081),
    "Captain's diary 3": ItemData(ItemClassification.filler, 2082),
    "Book of Fears": ItemData(ItemClassification.useful, 2098),
    "Buckman's letter": ItemData(ItemClassification.filler, 2181),
    "Diary of an unknown guard": ItemData(ItemClassification.filler, 2157),

    # WEAPONS
    "Short sword": ItemData(ItemClassification.useful, 1001),  # Gaunt knight drop
    "Claymore": ItemData(ItemClassification.useful, 1005),  # Trading kid to pocketcat
    "Dagger": ItemData(ItemClassification.useful, 1006),
    "Long sword": ItemData(ItemClassification.useful, 1007),  # D'arce drop
    "Eastern sword": ItemData(ItemClassification.useful | ItemClassification.trap, 1008),
    "Sergal spear": ItemData(ItemClassification.useful, 1016),
    "Miasma": ItemData(ItemClassification.useful, 1020),
    "Shark teeth": ItemData(ItemClassification.useful, 1032),
    "War scythe": ItemData(ItemClassification.useful, 1036),  # Dragon thing in ancient city
    "Blue sin": ItemData(ItemClassification.useful, 1049),

    # ARMOUR
    "Stone crown": ItemData(ItemClassification.progression | ItemClassification.useful, 11),  # Can take cube without pissing anyone off
    "Iron mask": ItemData(ItemClassification.useful, 31),
    "Gaunt plate armor": ItemData(ItemClassification.useful, 33),
    "Gaunt bascinet": ItemData(ItemClassification.useful, 34),
    "Red scarf": ItemData(ItemClassification.useful, 44),
    "Penance armor (body)": ItemData(ItemClassification.useful, 54),
    "Penance armor (head)": ItemData(ItemClassification.useful, 55),
    "Eastern silk robes": ItemData(ItemClassification.useful, 56),
    "Jingasa kabuto": ItemData(ItemClassification.useful, 57),

    # ACCESSORIES
    "Peculiar doll": ItemData(ItemClassification.useful, 19),
    "Everwatching talisman": ItemData(ItemClassification.useful, 20),  # Enki drop
    "Cavewolf paw": ItemData(ItemClassification.useful, 26),
    "Ring of wraiths": ItemData(ItemClassification.useful, 29),
    "Monocle": ItemData(ItemClassification.useful, 50),
    "Charm of the yggaegetsu": ItemData(ItemClassification.useful, 58),

    # STORE ITEMS
    "Sorceror's stone": ItemData(ItemClassification.useful, 27),
    "Soul devour necklace": ItemData(ItemClassification.useful, 47),
    "Elixir of mind": ItemData(ItemClassification.useful, 2166),
    "Elixir of body": ItemData(ItemClassification.useful, 2167),
    "Purifying talisman": ItemData(ItemClassification.progression, 2149),
    "Quill": ItemData(ItemClassification.filler, 2087),
    "Blue vial": ItemData(ItemClassification.useful, 2028),
    "Bottle of whiskey": ItemData(ItemClassification.useful, 2030),
    "Dried meat": ItemData(ItemClassification.useful, 2016),
    "Opium powder": ItemData(ItemClassification.useful, 2072),
    "Iron arrow": ItemData(ItemClassification.filler, 2075),
    "Alchemillia Vol. 1": ItemData(ItemClassification.useful, 2133),
    "Alchemillia Vol. 2": ItemData(ItemClassification.useful, 2013),
    "Recipes of the 15th century": ItemData(ItemClassification.useful, 2003),
    "Ancient book": ItemData(ItemClassification.useful, 2001),
    "Book of enlightenment": ItemData(ItemClassification.useful, 2040),
    "Book of forgotten memories": ItemData(ItemClassification.useful, 2002),
    "Potion of full healing": ItemData(ItemClassification.trap, 2099),
    "Potion of full sanity": ItemData(ItemClassification.trap, 2100),
    "Potion of life": ItemData(ItemClassification.trap, 2101),

    # OTHER
    "Green herb": ItemData(ItemClassification.useful | ItemClassification.filler, 2094),
    "Blue herb": ItemData(ItemClassification.useful | ItemClassification.filler, 2095),
    "Red herb": ItemData(ItemClassification.useful | ItemClassification.filler, 2132),
    "Dried mushroom": ItemData(ItemClassification.progression, 2065),  # Change this back to useful/filler once testing is done
    "Light blue vial": ItemData(ItemClassification.useful, 2067),  # Trotur gift AND potential shop item
    "Catnip": ItemData(ItemClassification.filler, 2194),
    "Glow mushroom": ItemData(ItemClassification.filler, 2066),  # Can only be obtained via empty scroll
    "Yellow vial": ItemData(ItemClassification.useful, 2033),
    "Salmonsnake Meat": ItemData(ItemClassification.useful, 2091),
    "Lesser soul": ItemData(ItemClassification.progression | ItemClassification.useful, 2116),
    "Gnome milk": ItemData(ItemClassification.useful, 2057),
    "Gnome egg": ItemData(ItemClassification.useful, 2060),
    "Scroll of pyromancy trick": ItemData(ItemClassification.useful, 2159),  # Secret hideout loot
    "Scroll of combustion": ItemData(ItemClassification.useful, 2160),  # Secret hideout loot
    "Rotten meat": ItemData(ItemClassification.filler | ItemClassification.trap, 2021),
    "Cloth fragment": ItemData(ItemClassification.useful | ItemClassification.filler, 2008),
    "Stone": ItemData(ItemClassification.filler, 2084),

    # "Random Blood Magic": Common Event 29 - probably not an item
    # "Greater Blood Magic": Common Event 97 - probably not an item
    # "Captain's diary 1 (3)": odd one, look at item 0032- same name but different diary entry
    # "Eclipse talisman": # Talk to a yellow mage, but can be done multiple times... should this be in?
    # S ending items... Spirit Anchor, King's crown, etc
    # Cave moss - you need to farm a drop to plant a seed for this, should it be added?
    # Items deliberately NOT added:
    # Black vials - they are more like things that are "crafted", you fill them up with the fluid
    # "Ancient One soul": Don't include this one. You get it from killing the girl and she is required for the main ending
}
# fmt: on


class FungerItem(Item):
    game = "Fear & Hunger"
