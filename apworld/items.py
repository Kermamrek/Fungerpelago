from __future__ import annotations

from collections import namedtuple
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import FungerWorld

ItemData = namedtuple("ItemData", ["classification", "id"])

# fmt: off
ITEM_DATA = {
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
    "Soul Stone": ItemData(ItemClassification.useful, 2115),  # Common Event 200 ... It's called "Random Great Item" but its just a soul stone
    "Random Weapon": ItemData(ItemClassification.useful, 5011),  # Common Event 238
    "Random Minor Weapon": ItemData(ItemClassification.useful, 5012),  # Common Event 239
    "Nights Random Item": ItemData(ItemClassification.filler, 5013),  # Common Event 250 TODO: look at where this is used? Probably Dungeon Nights and can be ignored
    "Guard Loot": ItemData(ItemClassification.filler, 5014),  # Common Event 253
    "Lizardman Loot": ItemData(ItemClassification.useful, 5015),  # Common Event 254
    "Lord of Flies Loot": ItemData(ItemClassification.useful, 5016),  # Common Event 255
    "Yellow Mage Loot": ItemData(ItemClassification.useful, 5017),  # Common Event 256

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
    "Charm of the Yggaegetsu": ItemData(ItemClassification.useful, 58),

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

    # "Random Blood Magic": Common Event 29 - probably not an item
    # "Greater Blood Magic": Common Event 97 - probably not an item
    # "Cloth Fragment": You can get these from every bed, should these be APItems? maybe a setting to enable/disable them or make them non-important? (see ttyd pit 100 trials)
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


def create_item_with_correct_classification(world: FungerWorld, name: str) -> FungerItem:
    classification, id = ITEM_DATA[name]
    if name == "Torch" and (
        world.options.DifficultyChoice.terror_and_starvation or world.options.DifficultyChoice.hard_mode
    ):
        classification = ItemClassification.progression
    return FungerItem(name, classification, id, world.player)


def create_all_items(world: FungerWorld) -> None:

    # Look at APQuest items.py for more info on filler items
    # Right now this is just a hardcoded list of the first two screens for testing

    itempool: list[Item] = [
        # Fortress
        world.create_item("Random Food Item"),
        world.create_item("Random Food Item"),
        world.create_item("Random Food Item"),
        world.create_item("Random Minor Item"),
        world.create_item("Random Minor Item"),
        world.create_item("Random Minor Item"),
        world.create_item("Random Minor Item"),
        # Level 1 Left Entrance
        world.create_item("Random Food Item"),
        world.create_item("Random Food Item"),
        world.create_item("Dried mushroom"),
    ]

    world.multiworld.itempool += itempool
