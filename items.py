from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import APQuestWorld

# ITEM IDS
ITEM_NAME_TO_ID = {
    # RANDOM ITEMS
    "Random Minor Item": 1, # Common Event 23
    "Random Minor Book": 2, # Common Event 25
    "Random Rare Book": 3, # Common Event 26
    "Random Food Item": 4, # Common Event 52
    "Random Rare Item": 5, # Common Event 58
    "Random Alchemy": 6, # Common Event 68
    "Random Good Armor": 7, # Common Event 141
    "Random Scroll Item": 8, # Common Event 149
    "Random Rare Book (Ancient)": 9, # Common Event 178
    "Random Minor Book (Ancient)": 10, # Common Event 179
    "Soul Stone": 11, # Common Event 200 ... It's called "Random Great Item" but its just a soul stone
    "Random Weapon": 12, # Common Event 238
    "Random Minor Weapon": 13, # Common Event 239
    "Nights Random Item": 14, # Common Event 250 TODO: look at where this is used?
    "Guard Loot": 15, # Common Event 253
    "Lizardman Loot": 16, # Common Event 254
    "Lord of Flies Loot": 17, # Common Event 255
    "Yellow Mage Loot": 18, # Common Event 256
    # NOTE: there may be more loot tables, since there's way more enemy types- double check?
    # FIXED ITEMS
    "Torch": 19, # Ones on the cave walls
    "Cube of depths": 20,
    "Blue demon powder": 21,
    "Book pages I": 22,
    "Book pages II": 23,
    "Book pages III": 24,
    "Map #1": 25,
    "Map #2": 26,
    "Map #3": 27,
    "Mockup book": 28,
    "Bonesaw": 30,
    "Lucky coin": 31,
    "Scroll of transmutation": 32,
    "Scroll of walking on water": 33,
    "Stick": 34,
    "Explosive vial": 35,
    "Vault key": 75,
    "Rope": 82,
    "Skinning knife": 83,
    "Cell keys F3": 85,
    "2F key": 86,
    "King's passage key": 87,
    "Old passage key": 88,
    # SOULS/ENEMY REWARDS
    "Crow Mauler soul": 36,
    "Cavemother soul": 37,
    "Salmonsnake soul": 38,
    "Old Knight soul": 39,
    "Iron Shakespeare soul": 40,
    "White angel soul": 53,
    "Black witch soul": 54,
    "Old guardian soul": 55,
    "Butterfly soul": 56,
    "Endless soul": 41, # Required for an ending/gets you hexen skills
    "Domination soul": 42, # Required for an ending/gets you hexen skills
    "Enlightened soul": 43, # Required for an ending/gets you hexen skills
    "Tormented soul": 44, # Required for an ending/gets you hexen skills
    "Crow emblem key": 45,
    # BOOKS/PAPERS
    "Captain's orders": 46,
    "List of inmates": 47,
    "Captain's diary 1": 48,
    "Torturer's notes 1": 49,
    "Captain's diary 2": 50,
    "Captain's diary 3": 51,
    "Book of Fears": 52,
    "Buckman's letter": 84,
    # WEAPONS
    "Short sword": 57, # Gaunt knight drop
    "Long sword": 58, # D'arce drop
    "Dagger": 59,
    "Shark teeth": 60,
    "War scythe": 61, # Dragon thing in ancient city
    "Claymore": 62, # Trading kid to pocketcat
    "Eastern sword": 63, # Trap item
    "Blue sin": 64,
    "Sergal spear": 65,
    "Miasma": 66,
    # ARMOUR
    "Stone crown": 67, # Can take cube without pissing anyone off
    "Iron mask": 68,
    "Gaunt bascinet": 69,
    "Red scarf": 70,
    "Penance armor (head)": 71,
    "Jingasa kabuto": 72,
    "Penance armor (body)": 73,
    "Eastern silk robes": 74,
    # ACCESSORIES
    "Everwatching talisman": 76, # Enki drop
    "Charm of the Yggaegetsu": 77,
    "Peculiar doll": 78,
    "Cavewolf paw": 79,
    "Ring of wraiths": 80,
    "Monocle": 81,
    # STORE ITEMS
    "Sorceror's stone": 89,
    "Soul devour necklace": 90,
    "Elixir of mind": 29,
    "Elixir of body": 91,
    "Purifying talisman": 92,
    "Quill": 93,
    "Blue vial": 94,
    "Bottle of whiskey": 95,
    "Dried meat": 96,
    "Opium powder": 97,
    "Iron arrow": 98,
    "Alchemillia Vol. 1": 99,
    "Alchemillia Vol. 2": 100,
    "Recipes of the 15th century": 101,
    "Ancient book": 102,
    "Book of enlightenment": 103,
    "Book of forgotten memories": 104,
    # OTHER
    "Green herb": 105,
    "Blue herb": 106,
    "Red herb": 107,
    "Dried mushroom": 108,
    "Light blue vial": 109, # Trotur gift AND potential shop item
    "Catnip": 110,
    "Glow mushroom": 111, # Can only be obtained via empty scroll
    "Yellow vial": 112,
    "Salmonsnake Meat": 113,
    "Potion of full healing": 114, # Trap item
    "Potion of full sanity": 115, # Trap item
    "Potion of life": 116, # Trap item
    "Lesser soul": 117,
    "Gnome milk": 118,
    "Gnome egg": 119,
    "Scroll of pyromancy trick": 120, # Secret hideout loot
    "Scroll of combustion": 121, # Secret hideout loot

    # "Random Blood Magic": 4, Common Event 29 - probably not an item
    # "Greater Blood Magic": 4, Common Event 97 - probably not an item
    # "Cloth Fragment": You can get these from every bed, should these be APItems? maybe a setting to enable/disable them or make them non-important? (see ttyd pit 100 trials)
    # "Captain's diary 1 (3)": odd one, look at item 0032- same name but different diary entry
    # "Eclipse talisman": 75, # Talk to a yellow mage, but can be done multiple times... should this be in?
    # S ending items... Spirit Anchor, King's crown, etc
    # Cave moss - you need to farm a drop to plant a seed for this, should it be added?

    # Items deliberately NOT added:
    # Black vials - they are more like things that are "crafted", you fill them up with the fluid
    # "Ancient One soul": Don't include this one. You get it from killing the girl and she is required for the main ending

}

# ITEM CLASSIFICATIONS
# Type declarations from archipelago.js:
# none: 0 - Considered "Filler" or "Junk" item. despite being called "none" in js it is called "filler" here?
# progression: 1 - Item unlocks advancement of some sort, sometimes not necessary to clear the game but still required to progress something
# useful: 2 - Item is considered "useful to have", worth discussing the difference between this and filler
# trap: 4 - Item can inconvenience a player, could we add more of these as a bit? should we?
# More info (perhaps not definitive): https://archipelago.miraheze.org/wiki/Item
DEFAULT_ITEM_CLASSIFICATIONS = {
    "Random Minor Item": ItemClassification.filler,
    "Random Minor Book": ItemClassification.useful, # Despite being a minor book it contains recipes and pinecone pig
    "Random Rare Book": ItemClassification.useful,
    "Random Food Item": ItemClassification.filler,
    "Random Rare Item": ItemClassification.useful,
    "Random Alchemy": ItemClassification.useful,
    "Random Good Armor": ItemClassification.useful,
    "Random Scroll Item": ItemClassification.useful,
    "Random Rare Book (Ancient)": ItemClassification.useful,
    "Random Minor Book (Ancient)": ItemClassification.filler, # Despite being ancient I think every book here is useless
    "Soul Stone": ItemClassification.useful,
    "Random Weapon": ItemClassification.useful,
    "Random Minor Weapon": ItemClassification.useful,
    "Nights Random Item": ItemClassification.filler, # TODO: look at where this is used?
    "Guard Loot": ItemClassification.filler,
    "Lizardman Loot": ItemClassification.useful,
    "Lord of Flies Loot": ItemClassification.useful,
    "Yellow Mage Loot": ItemClassification.useful,
    # FIXED ITEMS
    "Torch": ItemClassification.useful,
    "Cube of depths": ItemClassification.progression,
    "Blue demon powder": ItemClassification.useful,
    "Book pages I": ItemClassification.useful,
    "Book pages II": ItemClassification.useful,
    "Book pages III": ItemClassification.useful,
    "Map #1": ItemClassification.progression,
    "Map #2": ItemClassification.progression,
    "Map #3": ItemClassification.progression,
    "Mockup book": ItemClassification.progression,
    "Gnome milk": ItemClassification.useful,
    "Bonesaw": ItemClassification.useful,
    "Lucky coin": ItemClassification.useful,
    "Scroll of transmutation": ItemClassification.useful,
    "Scroll of walking on water": ItemClassification.progression,
    "Stick": ItemClassification.filler,
    "Explosive vial": ItemClassification.progression | ItemClassification.useful,
    "Vault key": ItemClassification.progression,
    "Rope": ItemClassification.progression,
    "Skinning knife": ItemClassification.useful,
    "Cell keys F3": ItemClassification.progression,
    "2F key": ItemClassification.progression,
    "King's passage key": ItemClassification.progression,
    "Old passage key": ItemClassification.progression,
    # SOULS/ENEMY REWARDS
    # Set these as multi-items since they're required for one person's S ending... will this break something?
    "Crow Mauler soul": ItemClassification.progression | ItemClassification.useful,
    "Cavemother soul": ItemClassification.progression | ItemClassification.useful,
    "Salmonsnake soul": ItemClassification.progression | ItemClassification.useful,
    "Old Knight soul": ItemClassification.progression | ItemClassification.useful,
    "White angel soul": ItemClassification.progression | ItemClassification.useful,
    "Black witch soul": ItemClassification.progression | ItemClassification.useful,
    "Old guardian soul": ItemClassification.progression | ItemClassification.useful,
    "Butterfly soul": ItemClassification.progression | ItemClassification.useful,
    "Iron Shakespeare soul": ItemClassification.progression | ItemClassification.useful,
    "Endless soul": ItemClassification.progression | ItemClassification.useful, # Required for an ending/gets you hexen skills
    "Domination soul": ItemClassification.progression | ItemClassification.useful, # Required for an ending/gets you hexen skills
    "Enlightened soul": ItemClassification.progression | ItemClassification.useful, # Required for an ending/gets you hexen skills
    "Tormented soul": ItemClassification.progression | ItemClassification.useful, # Required for an ending/gets you hexen skills
    "Crow emblem key": ItemClassification.progression,
    # BOOKS/PAPERS
    # NOTE: a large majority of these have been listed as filler due to not being important in any way. Would this mess something up?
    "Captain's orders": ItemClassification.filler,
    "List of inmates": ItemClassification.filler,
    "Captain's diary 1": ItemClassification.filler,
    "Torturer's notes 1": ItemClassification.filler,
    "Captain's diary 2": ItemClassification.filler,
    "Captain's diary 3": ItemClassification.filler,
    "Book of Fears": ItemClassification.useful,
    "Buckman's letter": ItemClassification.filler,
    # WEAPONS
    "Short sword": ItemClassification.useful,
    "Long sword": ItemClassification.useful,
    "Dagger": ItemClassification.useful,
    "Shark teeth": ItemClassification.useful,
    "War scythe": ItemClassification.useful,
    "Claymore": ItemClassification.useful,
    "Eastern sword": ItemClassification.trap,
    "Blue sin": ItemClassification.useful,
    "Sergal spear": ItemClassification.useful,
    "Miasma": ItemClassification.useful,
    # ARMOUR
    "Stone crown": ItemClassification.progression | ItemClassification.useful,
    "Iron mask": ItemClassification.useful,
    "Gaunt bascinet": ItemClassification.useful,
    "Red scarf": ItemClassification.useful,
    "Penance armor (head)": ItemClassification.useful,
    "Jingasa kabuto": ItemClassification.useful,
    "Penance armor (body)": ItemClassification.useful,
    "Eastern silk robes": ItemClassification.useful,
    # ACCESSORIES
    "Everwatching talisman": ItemClassification.useful,
    "Charm of the Yggaegetsu": ItemClassification.useful,
    "Peculiar doll": ItemClassification.useful,
    "Cavewolf paw": ItemClassification.useful,
    "Ring of wraiths": ItemClassification.useful,
    "Monocle": ItemClassification.useful,
    # STORE ITEMS
    "Sorceror's stone": ItemClassification.useful,
    "Soul devour necklace": ItemClassification.useful,
    "Elixir of mind": ItemClassification.useful,
    "Elixir of body": ItemClassification.useful,
    "Purifying talisman": ItemClassification.progression,
    "Quill": ItemClassification.filler,
    "Blue vial": ItemClassification.useful,
    "Bottle of whiskey": ItemClassification.useful,
    "Dried meat": ItemClassification.useful,
    "Opium powder": ItemClassification.useful,
    "Iron arrow": ItemClassification.filler,
    "Alchemillia Vol. 1": ItemClassification.useful,
    "Alchemillia Vol. 2": ItemClassification.useful,
    "Recipes of the 15th century": ItemClassification.useful,
    "Ancient book": ItemClassification.useful,
    "Book of enlightenment": ItemClassification.useful,
    "Book of forgotten memories": ItemClassification.useful,
    # OTHER
    "Green herb": ItemClassification.useful | ItemClassification.filler,
    "Blue herb": ItemClassification.useful | ItemClassification.filler,
    "Red herb": ItemClassification.useful | ItemClassification.filler,
    "Dried mushroom": ItemClassification.useful | ItemClassification.filler,
    "Light blue vial": ItemClassification.useful, # Trotur gift AND potential shop item
    "Catnip": ItemClassification.filler,
    "Glow mushroom": ItemClassification.filler, # Can only be obtained via empty scroll
    "Yellow vial": ItemClassification.useful,
    "Salmonsnake Meat": ItemClassification.useful,
    "Potion of full healing": ItemClassification.trap,
    "Potion of full sanity": ItemClassification.trap,
    "Potion of life": ItemClassification.trap,
    "Lesser soul": ItemClassification.progression | ItemClassification.useful,
    "Gnome milk": ItemClassification.useful,
    "Gnome egg": ItemClassification.useful,
    "Scroll of pyromancy trick": ItemClassification.useful, # Secret hideout loot
    "Scroll of combustion": ItemClassification.useful, # Secret hideout loot
}

class APQuestItem(Item):
    game = "Fear & Hunger"
