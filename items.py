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
    "Random Minor Item": ItemClassification.filler, # Common Event 23
    "Random Minor Book": ItemClassification.useful, # Common Event 25, despite being a minor book it contains recipes and pinecone pig
    "Random Rare Book": ItemClassification.useful, # Common Event 26
    "Random Food Item": ItemClassification.filler, # Common Event 52
    "Random Rare Item": ItemClassification.useful, # Common Event 58
    "Random Alchemy": ItemClassification.useful, # Common Event 68
    "Random Good Armor": ItemClassification.useful, # Common Event 141
    "Random Scroll Item": ItemClassification.useful, # Common Event 149
    "Random Rare Book (Ancient)": ItemClassification.useful, # Common Event 178
    "Random Minor Book (Ancient)": ItemClassification.filler, # Common Event 179, despite being ancient I think every book here is useless
    "Soul Stone": ItemClassification.useful, # Common Event 200 ... It's called "Random Great Item" but its just a soul stone
    "Random Weapon": ItemClassification.useful, # Common Event 238
    "Random Minor Weapon": ItemClassification.useful, # Common Event 239
    "Nights Random Item": ItemClassification.filler, # Common Event 250 TODO: look at where this is used? Probably Dungeon Nights and can be ignored
    "Guard Loot": ItemClassification.filler, # Common Event 253
    "Lizardman Loot": ItemClassification.useful, # Common Event 254
    "Lord of Flies Loot": ItemClassification.useful, # Common Event 255
    "Yellow Mage Loot": ItemClassification.useful, # Common Event 256
    # NOTE: there may be more loot tables, since there's way more enemy types- double check?
    # FIXED ITEMS
    "Torch": ItemClassification.useful, # Ones on the cave walls
    "Cube of depths": ItemClassification.progression,
    "Blue demon powder": ItemClassification.useful,
    "Book pages I": ItemClassification.useful,
    "Book pages II": ItemClassification.useful,
    "Book pages III": ItemClassification.useful,
    "Map #1": ItemClassification.progression,
    "Map #2": ItemClassification.progression,
    "Map #3": ItemClassification.progression,
    "Mockup book": ItemClassification.progression,
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
    # NOTE: (a large majority of these have been listed as filler due to not being important in any way. Would this mess something up?
    "Captain's orders": ItemClassification.filler,
    "List of inmates": ItemClassification.filler,
    "Captain's diary 1": ItemClassification.filler,
    "Torturer's notes 1": ItemClassification.filler,
    "Captain's diary 2": ItemClassification.filler,
    "Captain's diary 3": ItemClassification.filler,
    "Book of Fears": ItemClassification.useful,
    "Buckman's letter": ItemClassification.filler,
    # WEAPONS
    "Short sword": ItemClassification.useful, # Gaunt knight drop
    "Long sword": ItemClassification.useful, # D'arce drop
    "Dagger": ItemClassification.useful,
    "Shark teeth": ItemClassification.useful,
    "War scythe": ItemClassification.useful, # Dragon thing in ancient city
    "Claymore": ItemClassification.useful, # Trading kid to pocketcat
    "Eastern sword": ItemClassification.useful | ItemClassification.trap,
    "Blue sin": ItemClassification.useful,
    "Sergal spear": ItemClassification.useful,
    "Miasma": ItemClassification.useful,
    # ARMOUR
    "Stone crown": ItemClassification.progression | ItemClassification.useful, # Can take cube without pissing anyone off
    "Iron mask": ItemClassification.useful,
    "Gaunt bascinet": ItemClassification.useful,
    "Red scarf": ItemClassification.useful,
    "Penance armor (head)": ItemClassification.useful,
    "Jingasa kabuto": ItemClassification.useful,
    "Penance armor (body)": ItemClassification.useful,
    "Eastern silk robes": ItemClassification.useful,
    # ACCESSORIES
    "Everwatching talisman": ItemClassification.useful, # Enki drop
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

class FungerItem(Item):
    game = "Fear & Hunger"

def create_item_with_correct_classification(world: FungerWorld, name: str) -> FungerItem:
     classification = ITEMS[name]
     if name == "Torch" and (world.options.DifficultyChoice.terror_and_starvation || world.options.DifficultyChoice.hard_mode):
        classification = ItemClassification.progression
     return FungerItem(name, classification, ITEM_NAME_TO_ID[name], world.player)
