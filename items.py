from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import APQuestWorld

# ITEM IDS
ITEM_NAME_TO_ID = {
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
    
    # "Random Blood Magic": 4, Common Event 29 - probably not an item
    # "Greater Blood Magic": 4, Common Event 97 - probably not an item
}

# ITEM CLASSIFICATIONS
DEFAULT_ITEM_CLASSIFICATIONS = {
    #"Key": ItemClassification.progression,
    #"Sword": ItemClassification.progression | ItemClassification.useful,  # Items can have multiple classifications.
    #"Shield": ItemClassification.progression,
    #"Hammer": ItemClassification.progression,
    #"Health Upgrade": ItemClassification.useful,
    #"Confetti Cannon": ItemClassification.filler,
    #"Math Trap": ItemClassification.trap,
}

class APQuestItem(Item):
    game = "Fear & Hunger"
