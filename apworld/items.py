from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import FungerWorld

# TODO: Do item IDs need to be static and pre-defined?

# ITEM CLASSIFICATIONS
# Type declarations from archipelago.js:
# none: 0 - Considered "Filler" or "Junk" item. despite being called "none" in js it is called "filler" here?
# progression: 1 - Item unlocks advancement of some sort, sometimes not necessary to clear the game but still required to progress something
# useful: 2 - Item is considered "useful to have", worth discussing the difference between this and filler
# trap: 4 - Item can inconvenience a player, could we add more of these as a bit? should we?
# More info (perhaps not definitive): https://archipelago.miraheze.org/wiki/Item
ITEMS = {
    # RANDOM ITEMS
    "Random Minor Item": (Itemclassification.filler, 5001),  # Common Event 23
    "Random Minor Book": (Itemclassification.useful, 5002), # Common Event 25, despite being a minor book it contains recipes and pinecone pig
    "Random Rare Book": (Itemclassification.useful, 5003), # Common Event 26
    "Random Food Item": (Itemclassification.filler, 5004), # Common Event 52
    "Random Rare Item": (Itemclassification.useful, 5005), # Common Event 58
    "Random Alchemy": (Itemclassification.useful, 5006),  # Common Event 68
    "Random Good Armor": (Itemclassification.useful, 5007),  # Common Event 141
    "Random Scroll Item": (Itemclassification.useful, 5008),  # Common Event 149
    "Random Rare Book (Ancient)": (Itemclassification.useful, 5009),  # Common Event 178
    "Random Minor Book (Ancient)": (Itemclassification.filler, 5010), # Common Event 179, despite being ancient I think every book here is useless
    "Soul Stone": (Itemclassification.useful, 2115), # Common Event 200 ... It's called "Random Great Item" but its just a soul stone
    "Random Weapon": (Itemclassification.useful, 5011),  # Common Event 238
    "Random Minor Weapon": (Itemclassification.useful, 5012), # Common Event 239
    "Nights Random Item": (Itemclassification.filler, 5013), # Common Event 250 TODO: look at where this is used? Probably Dungeon Nights and can be ignored
    "Guard Loot": (Itemclassification.filler, 5014),  # Common Event 253
    "Lizardman Loot": (Itemclassification.useful, 5015),  # Common Event 254
    "Lord of Flies Loot": (Itemclassification.useful, 5016), # Common Event 255
    "Yellow Mage Loot": (Itemclassification.useful, 5017),  # Common Event 256
    # NOTE: there may be more loot tables, since there's way more enemy types- double check?
    # FIXED ITEMS
    "Torch": (Itemclassification.useful, 2005),  # Ones on the cave walls
    "Cube of depths": (Itemclassification.progression, 2119),
    "Blue demon powder": (Itemclassification.useful, 2183),
    "Book pages I": (Itemclassification.useful, 2184),
    "Book pages II": (Itemclassification.useful, 2185),
    "Book pages III": (Itemclassification.useful, 2186),
    "Map #1": (Itemclassification.progression, 2162),
    "Map #2": (Itemclassification.progression, 2163),
    "Map #3": (Itemclassification.progression, 2188),
    "Mockup book": (Itemclassification.progression, 2049),
    "Bonesaw": (Itemclassification.useful, 2140),
    "Lucky coin": (Itemclassification.useful, 2201),
    "Scroll of transmutation": (Itemclassification.useful, 2164),
    "Scroll of walking on water": (Itemclassification.progression, 2161),
    "Stick": (Itemclassification.filler, 2027),
    "Explosive vial": (Itemclassification.progression | ItemClassification.useful, 2079),
    "Vault key": (Itemclassification.progression,
    "Rope": (Itemclassification.progression, 2199),
    "Skinning knife": (Itemclassification.useful, 2044),
    "Cell keys F3": (Itemclassification.progression, 2048),
    "2F key": (Itemclassification.progression, 2051),
    "King's passage key": (Itemclassification.progression, 2180),
    "Old passage key": (Itemclassification.progression, 2179),
    # SOULS/ENEMY REWARDS
    # Set these as multi-items since they're required for one person's S ending... will this break something?
    "Crow Mauler soul": (Itemclassification.progression | ItemClassification.useful, 36),
    "Salmonsnake soul": (Itemclassification.progression | ItemClassification.useful, 38),
    "Cavemother soul": (Itemclassification.progression | ItemClassification.useful, 41),
    "Old Knight soul": (Itemclassification.progression | ItemClassification.useful,
    "Iron Shakespeare soul": (Itemclassification.progression | ItemClassification.useful, 37),
    "White angel soul": (Itemclassification.progression | ItemClassification.useful, 39),
    "Black witch soul": (Itemclassification.progression | ItemClassification.useful, 40),
    "Butterfly soul": (Itemclassification.progression | ItemClassification.useful, 42),
    "Old guardian soul": (Itemclassification.progression | ItemClassification.useful, 43),
    "Endless soul": (Itemclassification.progression
    | ItemClassification.useful, 2126), # Required for an ending/gets you hexen skills
    "Domination soul": (Itemclassification.progression
    | ItemClassification.useful, 2127), # Required for an ending/gets you hexen skills
    "Enlightened soul": (Itemclassification.progression
    | ItemClassification.useful, 2128), # Required for an ending/gets you hexen skills
    "Tormented soul": (Itemclassification.progression
    | ItemClassification.useful, 2129),  # Required for an ending/gets you hexen skills
    "Crow emblem key": (Itemclassification.progression, 2148),
    # BOOKS/PAPERS
    # NOTE: (a large majority of these have been listed as filler due to not being important in any way. Would this mess something up?
    "Captain's orders": (Itemclassification.filler, 2018),
    "List of inmates": (Itemclassification.filler, 2019),
    "Captain's diary 1": (Itemclassification.filler, 2022),
    "Torturer's notes 1": (Itemclassification.filler, 2035),
    "Captain's diary 2": (Itemclassification.filler, 2081),
    "Captain's diary 3": (Itemclassification.filler, 2082),
    "Book of Fears": (Itemclassification.useful, 2098),
    "Buckman's letter": (Itemclassification.filler, 2181),
    # WEAPONS
    "Short sword": (ItemClassification.useful, 1001),  # Gaunt knight drop
    "Claymore": (ItemClassification.useful, 1005),  # Trading kid to pocketcat
    "Dagger": (ItemClassification.useful, 1006),
    "Long sword": (ItemClassification.useful, 1007),  # D'arce drop
    "Eastern sword": (ItemClassification.useful | ItemClassification.trap, 1008),
    "Sergal spear": (ItemClassification.useful, 1016),
    "Miasma": (ItemClassification.useful, 1020),
    "Shark teeth": (ItemClassification.useful, 1032),
    "War scythe": (Itemclassification.useful, 1036),  # Dragon thing in ancient city
    "Blue sin": (ItemClassification.useful, 1049),
    # ARMOUR
    "Stone crown": (Itemclassification.progression
    | ItemClassification.useful, 11), # Can take cube without pissing anyone off
    "Iron mask": (Itemclassification.useful, 31),
    "Gaunt plate armor": (Itemclassification.useful, 33),
    "Gaunt bascinet": (Itemclassification.useful, 34),
    "Red scarf": (Itemclassification.useful, 44),
    "Penance armor (body)": (Itemclassification.useful, 54),
    "Penance armor (head)": (Itemclassification.useful, 55),
    "Eastern silk robes": (Itemclassification.useful, 56),
    "Jingasa kabuto": (Itemclassification.useful, 57),
    # ACCESSORIES
    "Peculiar doll": (Itemclassification.useful, 19),
    "Everwatching talisman": (Itemclassification.useful, 20),  # Enki drop
    "Cavewolf paw": (Itemclassification.useful, 26),
    "Ring of wraiths": (Itemclassification.useful, 29),
    "Monocle": (Itemclassification.useful, 50),
    "Charm of the Yggaegetsu": (Itemclassification.useful, 58),
    # STORE ITEMS
    "Sorceror's stone": (Itemclassification.useful, 27),
    "Soul devour necklace": (Itemclassification.useful, 47),
    "Elixir of mind": (Itemclassification.useful, 2166),
    "Elixir of body": (Itemclassification.useful, 2167),
    "Purifying talisman": (Itemclassification.progression, 2149),
    "Quill": (Itemclassification.filler, 2087),
    "Blue vial": (Itemclassification.useful, 2028),
    "Bottle of whiskey": (Itemclassification.useful, 2030),
    "Dried meat": (Itemclassification.useful, 2016),
    "Opium powder": (Itemclassification.useful, 2072),
    "Iron arrow": (Itemclassification.filler, 2075),
    "Alchemillia Vol. 1": (Itemclassification.useful, 2133),
    "Alchemillia Vol. 2": (Itemclassification.useful, 2013),
    "Recipes of the 15th century": (Itemclassification.useful, 2003),
    "Ancient book": (Itemclassification.useful, 2001),
    "Book of enlightenment": (Itemclassification.useful, 2040),
    "Book of forgotten memories": (Itemclassification.useful, 2002),
    "Potion of full healing": (Itemclassification.trap, 2099),
    "Potion of full sanity": (Itemclassification.trap, 2100),
    "Potion of life": (Itemclassification.trap, 2101),
    # OTHER
    "Green herb": (Itemclassification.useful | ItemClassification.filler, 2094),
    "Blue herb": (Itemclassification.useful | ItemClassification.filler, 2095),
    "Red herb": (Itemclassification.useful | ItemClassification.filler, 2132),

    "Dried mushroom": (Itemclassification.progression, 2065), # Change this back to useful/filler once testing is done

    "Light blue vial": (Itemclassification.useful, 2067), # Trotur gift AND potential shop item
    "Catnip": (Itemclassification.filler, 2194),
    "Glow mushroom": (Itemclassification.filler, 2066), # Can only be obtained via empty scroll
    "Yellow vial": (Itemclassification.useful,
    "Salmonsnake Meat": (Itemclassification.useful, 2091),
    "Lesser soul": (Itemclassification.progression | ItemClassification.useful, 2116),
    "Gnome milk": (Itemclassification.useful, 2057),
    "Gnome egg": (Itemclassification.useful, 2060),
    "Scroll of pyromancy trick": (Itemclassification.useful, 2159),  # Secret hideout loot
    "Scroll of combustion": (Itemclassification.useful, 2160), # Secret hideout loot
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


ITEM_NAME_TO_ID = {item_name: index + 1 for index, item_name in enumerate(ITEMS)}


class FungerItem(Item):
    game = "Fear & Hunger"


def create_item_with_correct_classification(world: FungerWorld, name: str) -> FungerItem:
    classification = ITEMS[name]
    if name == "Torch" and (
        world.options.DifficultyChoice.terror_and_starvation or world.options.DifficultyChoice.hard_mode
    ):
        classification = ItemClassification.progression
    return FungerItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


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
