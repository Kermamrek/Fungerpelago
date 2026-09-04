from __future__ import annotations

from dataclasses import dataclass, field

from BaseClasses import Location


def generate_id():
    global id_tracker
    if "id_tracker" not in globals():
        id_tracker = 0
    id_tracker += 1
    return id_tracker


@dataclass
class LocationData:
    item_name: str
    id: int = field(default_factory=generate_id)


@dataclass
class RegionData:
    name: str
    locations: dict[str, LocationData] | None = None
    variants: dict[str, dict[str, LocationData]] | None = None
    connections: list[str] = field(default_factory=list)


REGIONS = [
    RegionData(
        "Fortress",
        locations={
            "Bottom Right Crate": LocationData("Random Minor Item"),
            "Right Crate (Left)": LocationData("Random Minor Item"),
            "Right Crate (Top)": LocationData("Random Minor Item"),
            "Right Crate (Right)": LocationData("Random Minor Item"),
            "Right Barrel": LocationData("Random Food Item"),
            "Left Barrel (Left)": LocationData("Random Food Item"),
            "Left Barrel (Right)": LocationData("Random Food Item"),
        },
        connections=["Level 1 - Stairway", "Level 1 - Entrance"],
    ),
    RegionData(
        "Level 1 - Stairway",
        locations={
            "Entrance Barrel (Left)": LocationData("Random Food Item"),
            "Entrance Barrel (Right)": LocationData("Random Food Item"),
            "Dried Mushroom (Left Entrance)": LocationData("Dried mushroom"),
        },
        connections=["Level 2 - Basement"],
    ),
    RegionData(
        "Level 1 - Entrance",
        variants={
            "A": {
                # List of things that need proper implementation:
                # Captains Orders/List of Inmates
                # Do we make the girl a drop or just let the player get her?
                # Shelf (Glass/Tinderboxes)
                # Shelf (in kitchen, on right)
                # Chest
                # Kitchen Table
                # Crate that is in the storeroom that has a weird RNG tree
                # Decide what to do with beds
                # Bookshelves that aren't the minor bookshelf
                # Enemies
                # Meat piles on table
                "Entrance Crate (1)": LocationData("Random Minor Item"),
                "Entrance Crate (2)": LocationData("Random Minor Item"),
                "Entrance Crate (3)": LocationData("Random Minor Item"),
                "Entrance Crate (4)": LocationData("Random Minor Item"),
                "Storeroom Crate": LocationData("Random Minor Item"),
                "Storeroom Shelf": LocationData("Random Minor Item"),
                "Storeroom Barrel": LocationData("Random Food Item"),
                "Hallway Crate (1)": LocationData("Random Minor Item"),
                "Hallway Crate (2)": LocationData("Random Minor Item"),
                "Hallway Crate (3)": LocationData("Random Minor Item"),
                "Hallway Crate (4)": LocationData("Random Minor Item"),
                "Hallway Crate (5)": LocationData("Random Minor Item"),
                "Statue Crate": LocationData("Random Minor Item"),
                "Hidden Room Barrel (1)": LocationData("Random Food Item"),
                "Hidden Room Barrel (2)": LocationData("Random Food Item"),
                "Hidden Room Crate": LocationData("Random Minor Item"),
                "Library Minor Bookshelf": LocationData("Random Minor Book"),
                "Library Mockup Bookshelf": LocationData("Mockup book"),
                "Kitchen Shelf (1)": LocationData("Random Minor Item"),
                "Rondon Flag": LocationData("Cloth fragment"),
                "Book of Fears": LocationData("Book of Fears"),
            },
            "B": {
                # List of things that need proper implementation:
                # Captains Orders/List of Inmates
                # Do we make the girl a drop or just let the player get her?
                # Shelf (Glass/Tinderboxes)
                # Shelf (in kitchen, on right)
                # Chest
                # Kitchen Table
                # Crate that is in the storeroom that has a weird RNG tree
                # Decide what to do with beds
                # Bookshelves that aren't the minor bookshelf
                # Enemies
                # Meat piles on table
                "West Hallway Crate (1)": LocationData("Random Minor Item"),
                "West Hallway Crate (2)": LocationData("Random Minor Item"),
                "West Hallway Crate (3)": LocationData("Random Minor Item"),
                "West Hallway Crate (4)": LocationData("Random Minor Item"),
                "East Hallway Crate (1)": LocationData("Random Minor Item"),
                "East Hallway Crate (2)": LocationData("Random Minor Item"),
                "East Hallway Crate (3)": LocationData("Random Minor Item"),
                "North Hallway Crate (1)": LocationData("Random Minor Item"),
                "North Hallway Crate (2)": LocationData("Random Minor Item"),
                "North Hallway Crate (3)": LocationData("Random Minor Item"),
                "North Hallway Crate (4)": LocationData("Random Minor Item"),
                "North Hallway Barrel": LocationData("Random Food Item"),
                "Northeast Hallway Barrel (1)": LocationData("Random Food Item"),
                "Northeast Hallway Barrel (2)": LocationData("Random Food Item"),
                "Hidden Room Barrel (1)": LocationData("Random Food Item"),
                "Hidden Room Barrel (2)": LocationData("Random Food Item"),
                "Hidden Room Crate": LocationData("Random Minor Item"),
                "Kitchen Barrel (1)": LocationData("Random Food Item"),
                "Kitchen Barrel (2)": LocationData("Random Food Item"),
                "Torture Room Crate (1)": LocationData("Random Minor Item"),
                "Torture Room Crate (2)": LocationData("Random Minor Item"),
                "Torture Room Crate (3)": LocationData("Random Minor Item"),
                "Book of Fears": LocationData("Book of Fears"),
                "Library Minor Bookshelf": LocationData("Random Minor Book"),
                "Library Mockup Bookshelf": LocationData("Mockup book"),
                "Rondon Flag": LocationData("Cloth fragment"),
                "North Entrance Barrel": LocationData("Random Food Item"),
                "North Entrance Shelf (1)": LocationData("Random Food Item"),
            },
            "C": {
                # List of things that need proper implementation:
                # Captains Orders/List of Inmates
                # Do we make the girl a drop or just let the player get her?
                # Shelf (Glass/Tinderboxes)
                # Shelf (in kitchen, on right)
                # Chest
                # Kitchen Table
                # Crate that is in the storeroom that has a weird RNG tree
                # Decide what to do with beds
                # Bookshelves that aren't the minor bookshelf
                # Enemies
                # Meat piles on table
                "Rondon Flag": LocationData("Cloth fragment"),
                "Book of Fears": LocationData("Book of Fears"),
                "Entrance Crate (1)": LocationData("Random Minor Item"),
                "Entrance Crate (2)": LocationData("Random Minor Item"),
                "Left Hidden Room Barrel (1)": LocationData("Random Food Item"),
                "Left Hidden Room Barrel (2)": LocationData("Random Food Item"),
                "Left Hidden Room Barrel (3)": LocationData("Random Food Item"),
                "Left Hidden Room Barrel (4)": LocationData("Random Food Item"),
                "Left Hidden Room Crate": LocationData("Random Minor Item"),
                "Kitchen Shelf (1)": LocationData("Random Minor Item"),
                "Right Hidden Room Barrel (1)": LocationData("Random Food Item"),
                "Right Hidden Room Barrel (2)": LocationData("Random Food Item"),
                "Right Hidden Room Shelf": LocationData("Random Minor Item"),
                "Right Hidden Room Crate": LocationData("Random Minor Item"),
                "Right Storeroom Barrel (1)": LocationData("Random Food Item"),
                "Right Storeroom Barrel (2)": LocationData("Random Food Item"),
                "Right Storeroom Shelf": LocationData("Random Minor Item"),
                "Right Storeroom Crate (1)": LocationData("Random Minor Item"),
                "Right Storeroom Crate (2)": LocationData("Random Minor Item"),
                "Right Storeroom Crate (3)": LocationData("Random Minor Item"),
                "Right Storeroom Crate (4)": LocationData("Random Minor Item"),
                "Right Storeroom Crate (5)": LocationData("Random Minor Item"),
                "Right Storeroom Crate (6)": LocationData("Random Minor Item"),
                "Right Storeroom Crate (7)": LocationData("Random Minor Item"),
                "Right Storeroom Crate (8)": LocationData("Random Minor Item"),
                "Left Storeroom Barrel": LocationData("Random Food Item"),
                "Left Storeroom Crate (1)": LocationData("Random Minor Item"),
                "Left Storeroom Crate (2)": LocationData("Random Minor Item"),
                "Left Storeroom Crate (3)": LocationData("Random Minor Item"),
                "Left Storeroom Shelf": LocationData("Random Minor Item"),
                "Library Mockup Bookshelf": LocationData("Mockup book"),
                "Library Minor Bookshelf": LocationData("Random Minor Book"),
                "Captain's Crate": LocationData("Random Minor Item"),
            },
            "D": {
                # List of things that need proper implementation:
                # Captains Orders/List of Inmates
                # Do we make the girl a drop or just let the player get her?
                # Shelf (Glass/Tinderboxes)
                # Shelf (in kitchen, on right)
                # Chest
                # Kitchen Table
                # Crate that is in the storeroom that has a weird RNG tree
                # Decide what to do with beds
                # Bookshelves that aren't the minor bookshelf
                # Enemies
                # Meat piles on table
                "Book of Fears": LocationData("Book of Fears"),
                "Entrance Storeroom Crate (1)": LocationData("Random Minor Item"),
                "Entrance Storeroom Crate (2)": LocationData("Random Minor Item"),
                "Entrance Storeroom Barrel": LocationData("Random Food Item"),
                "Entrance Crate (1)": LocationData("Random Minor Item"),
                "Entrance Crate (2)": LocationData("Random Minor Item"),
                "Entrance Crate (3)": LocationData("Random Minor Item"),
                "Kitchen Crate (1)": LocationData("Random Minor Item"),
                "Kitchen Crate (2)": LocationData("Random Minor Item"),
                "Kitchen Crate (3)": LocationData("Random Minor Item"),
                "Kitchen Barrel (1)": LocationData("Random Food Item"),
                "Kitchen Barrel (2)": LocationData("Random Food Item"),
                "Storeroom Crate (1)": LocationData("Random Minor Item"),
                "Storeroom Barrel": LocationData("Random Food Item"),
                "Storeroom Shelf": LocationData("Random Minor Item"),
                "Hallway Crate (1)": LocationData("Random Minor Item"),
                "Hallway Crate (2)": LocationData("Random Minor Item"),
                "North Hallway Shelf": LocationData("Random Minor Item"),
                "North Hallway Barrel": LocationData("Random Food Item"),
                "Captain's Barrel": LocationData("Random Food Item"),
                "Captain's Bookshelf": LocationData("Random Minor Book"),
                "Library Mockup Bookshelf": LocationData("Mockup book"),
                "Hidden Room Barrel (1)": LocationData("Random Food Item"),
                "Hidden Room Barrel (2)": LocationData("Random Food Item"),
                "Hidden Room Crate": LocationData("Random Minor Item"),
            },
        },
        connections=["Level 1 - Courtyard"],
    ),
    RegionData(
        "Level 1 - Courtyard",
        variants={
            "A": {
                "Courtyard Green Herb": LocationData("Green herb"),
                "Courtyard Blue Herb": LocationData("Blue herb"),
                "Courtyard Stick": LocationData("Stick"),
            },
            "B": {
                "Courtyard Green Herb": LocationData("Green herb"),
                "Courtyard Blue Herb": LocationData("Blue herb"),
                "Courtyard Stick": LocationData("Stick"),
                "Courtyard Barrel (1)": LocationData("Random Food Item"),
                "Courtyard Barrel (2)": LocationData("Random Food Item"),
            },
        },
        connections=["Level 1 - Inner hall"],
    ),
    RegionData(
        "Level 1 - Inner hall",
        variants={
            "A": {
                # List of things that need proper implementation:
                # Captain's desk doesn't have conditionals but gives a key and diary at the same time, does this work?
                # Buckman stuff, not sure if it gives any items though
                # Bookcase in captain's room and library (2 left)
                # does the human hydra do anything?
                # Enemies, etc
                # Should we make the sacrifice a location? (same for the praying and orgy?)
                # berserk set
                # Double check to see if anything is missing
                # CHANGE SCROLL HINT BOOKS
                "Rondon Flag (1)": LocationData("Cloth fragment"),
                "Rondon Flag (2)": LocationData("Cloth fragment"),
                "Captain's Inner Room Shelf (1)": LocationData("Random Minor Item"),
                "Captain's Inner Room Shelf (2)": LocationData("Random Minor Item"),
                "Captain's Inner Room Bookshelf (1)": LocationData("Random Minor Book"),
                "Torture Room Skinning Knife": LocationData("Skinning knife"),
                "Torture Room Bonesaw": LocationData("Bonesaw"),
                "Trortur Room Skinning Knife": LocationData("Skinning knife"),
                "Library Hallway Crate (1)": LocationData("Random Minor Item"),
                "Library Hallway Crate (2)": LocationData("Random Minor Item"),
                "Library Hallway Crate (3)": LocationData("Random Minor Item"),
                "Library Hallway Barrel": LocationData("Random Food Item"),
                "Library Bookshelf (1)": LocationData("Random Minor Book"),
                "Library Bookshelf (2)": LocationData("Random Minor Book"),
                "Library Bookshelf (3)": LocationData("Random Minor Book"),
                "Library Bookshelf (4)": LocationData("Random Minor Book"),
                "Book Pages I": LocationData("Book pages I"),
                "Torture Hallway Barrel": LocationData("Random Food Item"),
                "Trortur Room Barrel": LocationData("Random Food Item"),
            },
            "B": {
                # List of things that need proper implementation:
                # Captain's desk doesn't have conditionals but gives a key and diary at the same time, does this work?
                # Buckman stuff, not sure if it gives any items though
                # Bookcase in captain's room and library
                # does the human hydra do anything?
                # Enemies, etc
                # Should we make the sacrifice a location? (same for the praying and orgy?)
                # berserk set
                # Double check to see if anything is missing
                # CHANGE SCROLL HINT BOOKS
                "Rondon Flag (1)": LocationData("Cloth fragment"),
                "Rondon Flag (2)": LocationData("Cloth fragment"),
                "Sacrifice Room Bookshelf (1)": LocationData("Random Minor Book"),
                "Sacrifice Room Shelf (1)": LocationData("Random Minor Item"),
                "Sacrifice Room Shelf (2)": LocationData("Random Minor Item"),
                "Hydra Hallway Crate (1)": LocationData("Random Minor Item"),
                "Hydra Hallway Crate (2)": LocationData("Random Minor Item"),
                "Library Hallway Crate (1)": LocationData("Random Minor Item"),
                "Library Hallway Crate (2)": LocationData("Random Minor Item"),
                "Torture Hallway Barrel": LocationData("Random Food Item"),
                "Trortur Room Barrel": LocationData("Random Food Item"),
                "Torture Room Skinning Knife": LocationData("Skinning knife"),
                "Torture Room Bonesaw": LocationData("Bonesaw"),
                "Trortur Room Skinning Knife": LocationData("Skinning knife"),
                "Library Bookshelf (1)": LocationData("Random Minor Book"),
                "Library Bookshelf (2)": LocationData("Random Minor Book"),
                "Library Bookshelf (3)": LocationData("Random Minor Book"),
                "Library Bookshelf (4)": LocationData("Random Minor Book"),
                "Library Bookshelf (5)": LocationData("Random Minor Book"),
                "Library Bookshelf (6)": LocationData("Random Minor Book"),
                "Book Pages I": LocationData("Book pages I"),
            },
            "C": {
                # List of things that need proper implementation:
                # Captain's desk doesn't have conditionals but gives a key and diary at the same time, does this work?
                # Buckman stuff, not sure if it gives any items though
                # Bookcase in captain's room and library
                # does the human hydra do anything?
                # Enemies, etc
                # Should we make the sacrifice a location? (same for the praying and orgy?)
                # berserk set
                # Double check to see if anything is missing
                # There's a silent hill 2 reference with the crow here, would it be cool to add a reference if the game is in the server? is SH2 in archipelago?
                # CHANGE SCROLL HINT BOOKS
                "East Hallway Crate (1)": LocationData("Random Minor Item"),
                "East Hallway Crate (2)": LocationData("Random Minor Item"),
                "East Hallway Crate (3)": LocationData("Random Minor Item"),
                "East Hallway Crate (4)": LocationData("Random Minor Item"),
                "East Hallway Crate (5)": LocationData("Random Minor Item"),
                "East Hallway Barrel": LocationData("Random Food Item"),
                # Second shelf is inaccessible but event still exists
                "Captain's Inner Room Shelf": LocationData("Random Minor Item"),
                "Captain's Inner Room Crate": LocationData("Random Minor Item"),
                "Captain's Inner Room Barrel": LocationData("Random Food Item"),
                "Library Bookshelf (1)": LocationData("Random Minor Book"),
                "Library Bookshelf (2)": LocationData("Random Minor Book"),
                "Library Bookshelf (3)": LocationData("Random Minor Book"),
                "Library Bookshelf (4)": LocationData("Random Minor Book"),
                "Library Bookshelf (5)": LocationData("Random Minor Book"),
                "Library Bookshelf (6)": LocationData("Random Minor Book"),
                "Book Pages I": LocationData("Book pages I"),
                "Iron Maiden Room Crate (1)": LocationData("Random Minor Item"),
                "Iron Maiden Room Crate (2)": LocationData("Random Minor Item"),
                "Torture Room Bonesaw": LocationData("Bonesaw"),
                "Torture Room Skinning Knife": LocationData("Skinning knife"),
                "Trortur Room Skinning Knife": LocationData("Skinning knife"),
            },
        },
        connections=["Level 1 - Backyard", "Level 2 - Blood pit"],
    ),
    RegionData(
        "Level 2 - Blood pit",
        locations={
            # Lizardman
        },
        connections=["Level 1 - Hidden backyard", "Level 3 - Prisons", "Level 4 - Caverns"],
    ),
    RegionData(
        "Level 1 - Backyard",
        locations={
            "Backyard Stick": LocationData("Stick"),
            # Weird huge conditional tree on the dagger but it might not be that relevant?
            # "Backyard Dagger": LocationData("Dagger"),
            "Orgy Stick": LocationData("Stick"),
            "Orgy Red Herb": LocationData("Stick"),
            "Backyard Blue Herb (West)": LocationData("Blue herb"),
            "Backyard Blue Herb (East)": LocationData("Blue herb"),
            "Backyard Green Herb": LocationData("Green herb"),
            "Backyard Barrel (1)": LocationData("Random Food Item"),
            "Backyard Barrel (2)": LocationData("Random Food Item"),
            "Backyard Barrel (3)": LocationData("Random Food Item"),
            "Backyard Crate": LocationData("Random Minor Item"),
            "Butterfly Soul": LocationData("Butterfly soul"),
        },
        connections=["Level 1 - Hidden backyard"],
    ),
    RegionData(
        "Level 1 - Hidden backyard",
        locations={
            # Dog has no loot
            "Hidden Backyard Stick (1)": LocationData("Stick"),
            "Hidden Backyard Stick (2)": LocationData("Stick"),
        },
        connections=["Level 3 - Thicket"],
        # CHANGE TO LEVEL 2 THICKET WHEN CHEST IMPLEMENTED
    ),
    # RegionData(
    #     "Level 2 - Thicket",
    #     locations={
    #         # Chest needs to be implemented. variants as well
    #     },
    #     connections=["Level 3 - Thicket"],
    # ),
    RegionData(
        "Level 3 - Thicket",
        variants={
            # Chests and enemies needs to be implemented
            "A": {
                "West Branch Urn (1)": LocationData("Random Minor Item"),
                "West Branch Urn (2)": LocationData("Random Minor Item"),
                "East Branch Urn (1)": LocationData("Random Minor Item"),
                "East Branch Urn (2)": LocationData("Random Minor Item"),
                "Thicket Lucky Coin": LocationData("Lucky coin"),
            },
            "B": {
                "West Branch Urn (1)": LocationData("Random Minor Item"),
                "West Branch Urn (2)": LocationData("Random Minor Item"),
                "North Branch Urn (1)": LocationData("Random Minor Item"),
                "North Branch Urn (2)": LocationData("Random Minor Item"),
                "Thicket Lucky Coin": LocationData("Lucky coin"),
            },
            # "C": {
            #     # not in use?
            #     "West Branch Urn (1)": LocationData("Random Minor Item"),
            #     "West Branch Urn (2)": LocationData("Random Minor Item"),
            #     "North Branch Urn (1)": LocationData("Random Minor Item"),
            #     "North Branch Urn (2)": LocationData("Random Minor Item"),
            # },
        },
        connections=["Level 4 - Thicket"],
    ),
    RegionData(
        "Level 4 - Thicket",
        variants={
            "A": {
                # Chests, sword and enemies needs to be implemented
                "East Branch Urn (1)": LocationData("Random Minor Item"),
                "East Branch Urn (2)": LocationData("Random Minor Item"),
                # Soul stone can be made inaccessible by failing coin flip?
                "Thicket Soul Stone": LocationData("Soul stone"),
                "Center Branch Urn": LocationData("Random Minor Item"),
                "South Branch Urn": LocationData("Random Minor Item"),
            },
            "B": {
                # Chests, sword and enemies needs to be implemented
                "East Branch Urn (1)": LocationData("Random Minor Item"),
                "East Branch Urn (2)": LocationData("Random Minor Item"),
                # Soul stone can be made inaccessible by failing coin flip?
                "Thicket Soul Stone": LocationData("Soul stone"),
                "Center Branch Urn": LocationData("Random Minor Item"),
                "South Branch Urn": LocationData("Random Minor Item"),
                "West Branch Urn": LocationData("Random Minor Item"),
            },
            # Thicket C exists but again isn't used?
        },
        # connections=["Tree of the Depths - Thicket Level 3"],
    ),
    RegionData(
        "Level 2 - Basement",
        variants={
            "A": {
                "Rune Room Dried Mushroom (West)": LocationData("Dried Mushroom"),
                "Rune Room Dried Mushroom (North)": LocationData("Dried Mushroom"),
                "Rune Room Dried Mushroom (Northeast)": LocationData("Dried Mushroom"),
                "Rune Room Dried Mushroom (East)": LocationData("Dried Mushroom"),
                "Hallway Dried Mushroom": LocationData("Dried Mushroom"),
                "Miasma": LocationData("Miasma"),
                "Rune Room Barrel (1)": LocationData("Random Food Item"),
                "Rune Room Barrel (2)": LocationData("Random Food Item"),
                "Rune Room Barrel (3)": LocationData("Random Food Item"),
                "Rune Room Crate": LocationData("Random Minor Item"),
                "Rune Room Blue Herb": LocationData("Blue Herb"),
                "Rune Room Green Herb": LocationData("Green Herb"),
                "Keg Room Barrel (Left)": LocationData("Random Food Item"),
                "Keg Room Barrel (Right)": LocationData("Random Food Item"),
                # Note: Change the description text/pickup text for this one?
                "Keg Room Rotten Meat": LocationData("Rotten meat"),
                "Vertical Hallway Crate (1)": LocationData("Random Minor Item"),
                "Vertical Hallway Crate (2)": LocationData("Random Minor Item"),
                "Vertical Hallway Crate (3)": LocationData("Random Minor Item"),
                "Vertical Hallway Crate (Right)": LocationData("Random Minor Item"),
                "Corpse Pile Hallway Crate": LocationData("Random Minor Item"),
                "Corpse Pile Hallway Crate (2)": LocationData("Random Minor Item"),
                "Corpse Pile Hallway Barrel (Left)": LocationData("Random Food Item"),
                "Corpse Pile Hallway Barrel (Right)": LocationData("Random Food Item"),
                # TODO: Armour racks/Weapon Racks/the chest are not common events. They have not been added in because of that, fix them first
            },
            "B": {
                "Entryway Dried Mushroom": LocationData("Dried Mushroom"),
                "Rune Room Dried Mushroom (Southwest)": LocationData("Dried Mushroom"),
                "Rune Room Dried Mushroom (West)": LocationData("Dried Mushroom"),
                "Rune Room Dried Mushroom (Northeast)": LocationData("Dried Mushroom"),
                "Rune Room Dried Mushroom (East)": LocationData("Dried Mushroom"),
                "Rune Room Blue Herb": LocationData("Blue herb"),
                "Hallway Blue Herb": LocationData("Blue herb"),
                "Hallway Green Herb": LocationData("Green herb"),
                "Kitchen Rotten Meat": LocationData("Rotten meat"),
                "Kitchen Barrel": LocationData("Random Food Item"),
                "Miasma": LocationData("Miasma"),
                "Armory Hallway Barrel": LocationData("Random Food Item"),
                "Armory Hallway Crate (1)": LocationData("Random Minor Item"),
                "Armory Hallway Crate (2)": LocationData("Random Minor Item"),
                "Armory Hallway Crate (3)": LocationData("Random Minor Item"),
                "Armory Hallway Crate (4)": LocationData("Random Minor Item"),
                "Armory Hallway Crate (5)": LocationData("Random Minor Item"),
                "Armory Hallway Crate (6)": LocationData("Random Minor Item"),
                "Armory Hallway Crate (7)": LocationData("Random Minor Item"),
                "Centre Hallway Crate (1)": LocationData("Random Minor Item"),
                "Centre Hallway Crate (2)": LocationData("Random Minor Item"),
                "Moss Hallway Dried Mushroom (1)": LocationData("Dried Mushroom"),
                "Moss Hallway Dried Mushroom (2)": LocationData("Dried Mushroom"),
                "Moss Hallway Dried Mushroom (3)": LocationData("Dried Mushroom"),
                "Right Hallway Crate": LocationData("Random Minor Item"),
                # TODO: Armour racks/Weapon Racks/the chest are not common events. They have not been added in because of that, fix them first
            },
        },
        connections=["Level 3 - Basement"],
        # Add flip side basement
    ),
    # RegionData(  # TODO: Can only enter once, items not added yet in RPGMaker
    #     "Flip side - Basement"  # ,
    #     # locations = {
    #     #     "Flipside Basement - Room 3 Barrel (Left)": LocationData("Random Food Item"),
    #     #     "Flipside Basement - Room 3 Barrel (Right)": LocationData("Random Food Item"),
    #     #     "Flipside Basement - Room 5 Crate (Left)": LocationData("Random Minor Item"),
    #     #     "Flipside Basement - Room 5 Crate (Left)": LocationData("Random Minor Item"),
    #     # }
    # ),
    RegionData(
        "Level 3 - Basement",
        locations={
            # List of things that need proper implementation:
            # Shakespeare drops, and the bed crow mauler drop?
            # Bed
            # Armory room is completely untouched due to everything being complicated
            # I noticed the "miasma spots" here, I don't fully know how they work, do they need to be reworked?
            # Even though there are three crates in this room, they all share the same switch?
            "Moss Room Crate": LocationData("Random Minor Item"),
            "Moss Room Barrel (1)": LocationData("Random Food Item"),
            "Moss Room Barrel (2)": LocationData("Random Food Item"),
            "Moss Room Barrel (3)": LocationData("Random Food Item"),
            "Moss Room Dried Mushroom": LocationData("Dried Mushroom"),
            "Shakespeare Room Dried Mushroom (1)": LocationData("Dried Mushroom"),
            "Shakespeare Room Dried Mushroom (2)": LocationData("Dried Mushroom"),
            "Shakespeare Room Dried Mushroom (3)": LocationData("Dried Mushroom"),
            "Shakespeare Room Dried Mushroom (4)": LocationData("Dried Mushroom"),
            "Shakespeare Room Barrel (1)": LocationData("Random Food Item"),
            "Shakespeare Room Barrel (2)": LocationData("Random Food Item"),
            "Shakespeare Room Barrel (3)": LocationData("Random Food Item"),
            "Shakespeare Room Barrel (4)": LocationData("Random Food Item"),
            "Shakespeare Room Barrel (5)": LocationData("Random Food Item"),
            "Shakespeare Room Barrel (6)": LocationData("Random Food Item"),
            "Shakespeare Room Crate (1)": LocationData("Random Minor Item"),
            "Shakespeare Room Crate (2)": LocationData("Random Minor Item"),
            "Shakespeare Room Crate (3)": LocationData("Random Minor Item"),
            "Shakespeare Room Crate (4)": LocationData("Random Minor Item"),
            "Shakespeare Room Crate (5)": LocationData("Random Minor Item"),
            "Shakespeare Room Crate (6)": LocationData("Random Minor Item"),
            "Shakespeare Room Crate (7)": LocationData("Random Minor Item"),
            "Shakespeare Room Crate (8)": LocationData("Random Minor Item"),
            "Shakespeare Room Crate (9)": LocationData("Random Minor Item"),
            "Shakespeare Room Crate (10)": LocationData("Random Minor Item"),
            "Shakespeare Room Crate (11)": LocationData("Random Minor Item"),
            "Shakespeare Room Blue Herb": LocationData("Blue herb"),
            "Shakespeare Room Red Herb": LocationData("Red herb"),
            "Maiden Statue Barrel": LocationData("Random Food Item"),
            "North Room Crate (1)": LocationData("Random Minor Item"),
            "North Room Crate (2)": LocationData("Random Minor Item"),
        },
        connections=["Level 3 - Prisons"],
    ),
    RegionData(
        "Level 3 - Prisons",
        variants={
            "A": {
                # List of things that need proper implementation:
                # beds
                # enemies
                # what is the weird passageway that is blocked off by rocks?
                # chest
                # random rare book on the table
                # check back stairwell, haven't added those in yet because its evented a bit weird
                # doll
                "Cell Secret Crate (1)": LocationData("Random Minor Item"),
                "Cell Secret Crate (2)": LocationData("Random Minor Item"),
                "Cell Secret Crate (3)": LocationData("Random Minor Item"),
                "Cell Secret Crate (4)": LocationData("Random Minor Item"),
                "Cell Secret Crate (5)": LocationData("Random Minor Item"),
                "Cell Secret Crate (6)": LocationData("Random Minor Item"),
                "Cell Secret Barrel (1)": LocationData("Random Food Item"),
                "Cell Secret Barrel (2)": LocationData("Random Food Item"),
                "Prison Crate (1)": LocationData("Random Minor Item"),
                "Prison Crate (2)": LocationData("Random Minor Item"),
                "Prison Crate (3)": LocationData("Random Minor Item"),
                "Prison Crate (4)": LocationData("Random Minor Item"),
                "Prison Barrel (1)": LocationData("Random Food Item"),
                "Prison Barrel (2)": LocationData("Random Food Item"),
                "Prison Captain's Barrel (1)": LocationData("Random Food Item"),
                "Prison Captain's Barrel (2)": LocationData("Random Food Item"),
                "Prison Captain's Barrel (3)": LocationData("Random Food Item"),
                "Prison Captain's Barrel (4)": LocationData("Random Food Item"),
                "Prison Captain's Barrel (5)": LocationData("Random Food Item"),
                "Prison Captain's Crate (1)": LocationData("Random Minor Item"),
                "Prison Captain's Crate (2)": LocationData("Random Minor Item"),
                "Prison Captain's Crate (3)": LocationData("Random Minor Item"),
                "Prison Captain's Crate (4)": LocationData("Random Minor Item"),
                "Prison Captain's Crate (5)": LocationData("Random Minor Item"),
                "Prison Captain's Shelf (1)": LocationData("Random Minor Item"),
                "Prison Captain's Shelf (2)": LocationData("Random Minor Item"),
                "Prison Captain's Diary": LocationData("Captain's diary 2"),
                "Prison Rondon Flag (1)": LocationData("Cloth fragment"),
                "Prison Rondon Flag (2)": LocationData("Cloth fragment"),
            },
            "B": {
                # List of things that need proper implementation:
                # beds
                # enemies
                # what is the weird passageway that is blocked off by rocks?
                # chest
                # random rare book on the table
                # check back stairwell, haven't added those in yet because its evented a bit weird
                # doll
                "Cell Secret Crate (1)": LocationData("Random Minor Item"),
                "Cell Secret Crate (2)": LocationData("Random Minor Item"),
                "Cell Secret Crate (3)": LocationData("Random Minor Item"),
                "Cell Secret Crate (4)": LocationData("Random Minor Item"),
                "Cell Secret Crate (5)": LocationData("Random Minor Item"),
                "Cell Secret Crate (6)": LocationData("Random Minor Item"),
                "Cell Secret Barrel (1)": LocationData("Random Food Item"),
                "Cell Secret Barrel (2)": LocationData("Random Food Item"),
                "Prison Crate (1)": LocationData("Random Minor Item"),
                "Prison Crate (2)": LocationData("Random Minor Item"),
                "Prison Crate (3)": LocationData("Random Minor Item"),
                "Prison Crate (4)": LocationData("Random Minor Item"),
                "Prison Crate (5)": LocationData("Random Minor Item"),
                "Prison Crate (6)": LocationData("Random Minor Item"),
                "Prison Crate (7)": LocationData("Random Minor Item"),
                "Prison Barrel (1)": LocationData("Random Food Item"),
                "Prison Barrel (2)": LocationData("Random Food Item"),
                "Prison Storeroom Crate (1)": LocationData("Random Minor Item"),
                "Prison Storeroom Crate (2)": LocationData("Random Minor Item"),
                "Prison Storeroom Crate (3)": LocationData("Random Minor Item"),
                "Prison Storeroom Crate (4)": LocationData("Random Minor Item"),
                "Prison Storeroom Crate (5)": LocationData("Random Minor Item"),
                "Prison Storeroom Crate (6)": LocationData("Random Minor Item"),
                "Prison Storeroom Crate (7)": LocationData("Random Minor Item"),
                "Prison Storeroom Barrel (1)": LocationData("Random Food Item"),
                "Prison Storeroom Barrel (2)": LocationData("Random Food Item"),
                "Prison Captain's Crate (1)": LocationData("Random Minor Item"),
                "Prison Captain's Crate (2)": LocationData("Random Minor Item"),
                "Prison Captain's Shelf (1)": LocationData("Random Minor Item"),
                "Prison Captain's Shelf (2)": LocationData("Random Minor Item"),
                "Prison Captain's Diary": LocationData("Captain's diary 2"),
            },
            "C": {
                # List of things that need proper implementation:
                # beds
                # enemies
                # what is the weird passageway that is blocked off by rocks?
                # chest
                # random rare book on the table
                # check back stairwell, haven't added those in yet because its evented a bit weird
                # doll
                # the hidden cell in this variant has a weird/glitchy looking inaccessible crate and barrel? haven't added it yet, check to see if you can get it
                "Cell Secret Crate (1)": LocationData("Random Minor Item"),
                "Cell Secret Crate (2)": LocationData("Random Minor Item"),
                "Cell Secret Crate (3)": LocationData("Random Minor Item"),
                "Cell Secret Crate (4)": LocationData("Random Minor Item"),
                "Cell Secret Crate (5)": LocationData("Random Minor Item"),
                "Cell Secret Barrel (1)": LocationData("Random Food Item"),
                "Cell Secret Barrel (2)": LocationData("Random Food Item"),
                "Prison Captain's Crate (1)": LocationData("Random Minor Item"),
                "Prison Captain's Crate (2)": LocationData("Random Minor Item"),
                "Prison Captain's Shelf (1)": LocationData("Random Minor Item"),
                "Prison Captain's Shelf (2)": LocationData("Random Minor Item"),
                "Prison Captain's Diary": LocationData("Captain's diary 2"),
                "Prison Crate (1)": LocationData("Random Minor Item"),
                "Prison Crate (2)": LocationData("Random Minor Item"),
                "Prison Crate (3)": LocationData("Random Minor Item"),
                "Prison Crate (4)": LocationData("Random Minor Item"),
                "Prison Crate (5)": LocationData("Random Minor Item"),
                "Prison Crate (6)": LocationData("Random Minor Item"),
                "Prison Barrel (1)": LocationData("Random Food Item"),
                "Prison Barrel (2)": LocationData("Random Food Item"),
                "Prison Barrel (3)": LocationData("Random Food Item"),
                "Prison Barrel (4)": LocationData("Random Food Item"),
                "Prison Barrel (5)": LocationData("Random Food Item"),
            },
        },
        connections=["Staircase"],
    ),
    RegionData(
        "Level 4 - Caverns",
        variants={
            "A": {
                # Cavemother soul?
                # Pocketcat?
                # Moonless?
                # Yellow fluid can be gained here but it is a craftable
                "Cavern Eggs Soul Stone": LocationData("Soul stone"),
                "Pocketcat Crate (1)": LocationData("Random Minor Item"),
                "Pocketcat Crate (2)": LocationData("Random Minor Item"),
                "Pocketcat Barrel": LocationData("Random Food Item"),
            },
            "B": {
                # Cavemother soul?
                # Pocketcat?
                # Moonless?
                # Yellow fluid can be gained here but it is a craftable
                "Cavern Eggs Soul Stone": LocationData("Soul stone"),
                "Pocketcat Crate (1)": LocationData("Random Minor Item"),
                "Pocketcat Crate (2)": LocationData("Random Minor Item"),
                "Pocketcat Barrel": LocationData("Random Food Item"),
            },
        },
        connections=["Level 5 - Mines"],
    ),
    RegionData(
        "Level 5 - Mines",
        # Lizardman lair?
        variants={
            "A": {
                # Lizardmen, Wizards, Salmonsnake soul, old guard Soul
                # Spirit anchor for S ending?
                # Nostramus' Chest, bookshelves
                # Change O LORD GIVE ENLIGHTENMENT hint
                "Mineshaft Crate": LocationData("Random Minor Item"),
                "Mineshaft Barrel": LocationData("Random Food Item"),
                "Alchemy Room Urn": LocationData("Random Minor Item"),
                "Lizardman Room Urn (1)": LocationData("Random Minor Item"),
                "Lizardman Room Urn (2)": LocationData("Random Minor Item"),
                "Lizardman Room Crate (1)": LocationData("Random Minor Item"),
                "Lizardman Room Crate (2)": LocationData("Random Minor Item"),
                "Lizardman Room Crate (3)": LocationData("Random Minor Item"),
                "Sealed Hidden Room (Scroll of Combustion)": LocationData("Scroll of combustion"),
                "Sealed Hidden Room (Scroll of Pyromancy Trick)": LocationData("Scroll of pyromancy trick"),
                "Minecart": LocationData("Stone"),
                "Minecart (2)": LocationData("Stone"),
                "Tomb Urn": LocationData("Random Minor Item"),
                "Alchemy Bookshelf": LocationData("Random Alchemy"),
                "Alchemy Bookshelf Explosive Vial": LocationData("Explosive vial"),
                "Book Pages II": LocationData("Book pages II"),
                # For these torches, add in a way to see what item is on the wall before using Tinderboxes
                "Torch (1)": LocationData("Torch"),
                "Torch (2)": LocationData("Torch"),
                "Torch (3)": LocationData("Torch"),
                "Torch (4)": LocationData("Torch"),
            },
            "B": {
                # Lizardmen, Wizards, Salmonsnake soul, old guard Soul
                # Spirit anchor for S ending?
                # Nostramus' Chest, bookshelves
                # Change O LORD GIVE ENLIGHTENMENT hint
                "Mineshaft Crate (1)": LocationData("Random Minor Item"),
                "Mineshaft Barrel (1)": LocationData("Random Food Item"),
                "Mineshaft Crate (2)": LocationData("Random Minor Item"),
                "Mineshaft Barrel (2)": LocationData("Random Food Item"),
                "Mineshaft Crate (3)": LocationData("Random Minor Item"),
                "Mineshaft Crate (4)": LocationData("Random Minor Item"),
                "Mineshaft Barrel (3)": LocationData("Random Food Item"),
                "Mineshaft Urn (1)": LocationData("Random Minor Item"),
                "Mineshaft Urn (2)": LocationData("Random Minor Item"),
                "Alchemy Room Urn": LocationData("Random Minor Item"),
                "Tomb Urn": LocationData("Random Minor Item"),
                "Minecart": LocationData("Stone"),
                "Minecart (2)": LocationData("Stone"),
                "Alchemy Bookshelf": LocationData("Random Alchemy"),
                "Alchemy Bookshelf Explosive Vial": LocationData("Explosive vial"),
                "Book Pages II": LocationData("Book pages II"),
                "Lizardman Room Urn (1)": LocationData("Random Minor Item"),
                "Lizardman Room Urn (2)": LocationData("Random Minor Item"),
                "Lizardman Room Crate (1)": LocationData("Random Minor Item"),
                "Lizardman Room Crate (2)": LocationData("Random Minor Item"),
                "Lizardman Room Crate (3)": LocationData("Random Minor Item"),
                "Sealed Hidden Room (Scroll of Combustion)": LocationData("Scroll of combustion"),
                "Sealed Hidden Room (Scroll of Pyromancy Trick)": LocationData("Scroll of pyromancy trick"),
                # For these torches, add in a way to see what item is on the wall before using Tinderboxes
                "Torch (1)": LocationData("Torch"),
                "Torch (2)": LocationData("Torch"),
                "Torch (3)": LocationData("Torch"),
                "Torch (4)": LocationData("Torch"),
            },
            "C": {
                # Lizardmen, Wizards, Salmonsnake soul, old guard Soul
                # Spirit anchor for S ending?
                # Nostramus' Chest, bookshelves
                # Change O LORD GIVE ENLIGHTENMENT hint
                "Mineshaft Crate (1)": LocationData("Random Minor Item"),
                "Mineshaft Barrel (1)": LocationData("Random Food Item"),
                "Mineshaft Crate (2)": LocationData("Random Minor Item"),
                "Mineshaft Crate (3)": LocationData("Random Minor Item"),
                "Mineshaft Barrel (2)": LocationData("Random Food Item"),
                "Mineshaft Barrel (3)": LocationData("Random Food Item"),
                "Mineshaft Barrel (4)": LocationData("Random Food Item"),
                "Mineshaft Barrel (5)": LocationData("Random Food Item"),
                "Mineshaft Barrel (6)": LocationData("Random Food Item"),
                "Mineshaft Barrel (7)": LocationData("Random Food Item"),
                "Alchemy Room Urn": LocationData("Random Minor Item"),
                "Alchemy Bookshelf": LocationData("Random Alchemy"),
                "Alchemy Bookshelf Explosive Vial": LocationData("Explosive vial"),
                "Book Pages II": LocationData("Book pages II"),
                "Minecart": LocationData("Stone"),
                "Minecart (2)": LocationData("Stone"),
                "Lizardman Room Urn (1)": LocationData("Random Minor Item"),
                "Lizardman Room Urn (2)": LocationData("Random Minor Item"),
                "Lizardman Room Crate (1)": LocationData("Random Minor Item"),
                "Lizardman Room Crate (2)": LocationData("Random Minor Item"),
                "Lizardman Room Crate (3)": LocationData("Random Minor Item"),
                "Sealed Hidden Room (Scroll of Combustion)": LocationData("Scroll of combustion"),
                "Sealed Hidden Room (Scroll of Pyromancy Trick)": LocationData("Scroll of pyromancy trick"),
                # For these torches, add in a way to see what item is on the wall before using Tinderboxes
                "Torch (1)": LocationData("Torch"),
                "Torch (2)": LocationData("Torch"),
                "Torch (3)": LocationData("Torch"),
                "Torch (4)": LocationData("Torch"),
            },
        },
        connections=["Level 6 - Mines", "Level 6 - Mines (2)"],
    ),
    RegionData(
        "Level 6 - Mines",
        locations={
            # add Enemies, shopkeeper
            "Entrance Urn (1)": LocationData("Random Minor Item"),
            "Entrance Urn (2)": LocationData("Random Minor Item"),
            "Entrance Urn (3)": LocationData("Random Minor Item"),
            "Entrance Urn (4)": LocationData("Random Minor Item"),
            "Entrance Urn (5)": LocationData("Random Minor Item"),
            "Entrance Barrel (1)": LocationData("Random Food Item"),
            "Entrance Barrel (2)": LocationData("Random Food Item"),
            "Entrance Barrel (3)": LocationData("Random Food Item"),
            # There is a fourth barrel but I think it is unobtainable
            "Entrance Crate": LocationData("Random Minor Item"),
            "Village Crate (1)": LocationData("Random Minor Item"),
            # Village Pocketcat Crate is only moved when pocketcat moves? does it share a switch with another crate?
            "Village Pocketcat Crate": LocationData("Random Minor Item"),
            "Village Barrel (1)": LocationData("Random Food Item"),
            "Village Barrel (2)": LocationData("Random Food Item"),
            "Village Barrel (3)": LocationData("Random Food Item"),
            "Village Barrel (4)": LocationData("Random Food Item"),
            "Village Barrel (5)": LocationData("Random Food Item"),
            # Unobtainable urn near chest?
            "Village Urn (1)": LocationData("Random Minor Item"),
            "Village Urn (2)": LocationData("Random Minor Item"),
            "Village Urn (3)": LocationData("Random Minor Item"),
            "Village Urn (4)": LocationData("Random Minor Item"),
            "Village Urn (5)": LocationData("Random Minor Item"),
            "Village Urn (6)": LocationData("Random Minor Item"),
            "Village Crate (2)": LocationData("Random Minor Item"),
            # For these torches, add in a way to see what item is on the wall before using Tinderboxes
            "Torch (1)": LocationData("Torch"),
            "Torch (2)": LocationData("Torch"),
            "Torch (3)": LocationData("Torch"),
            "Torch (4)": LocationData("Torch"),
        },
        connections=["Level 6 - Mines (2)", "Level 6 - Altar of darkness", "Level 6 - Mines (Cave-in)", "Level 6 - Village Huts"],
    ),
    RegionData(
        "Level 6 - Altar of darkness",
        locations={
            # Has no items, what do we do?
        },
        # "Level 8 - The gauntlet"
        connections=["huts_village"],
    ),
    RegionData(
        "Level 6 - Village Huts",
        locations={
            # add Chests, enemies, etc
            "Hut Urn (1)": LocationData("Random Minor Item"),
            "Hut Urn (2)": LocationData("Random Minor Item"),
            "Hut Urn (3)": LocationData("Random Minor Item"),
            "Hut Urn (4)": LocationData("Random Minor Item"),
            "Hut Urn (5)": LocationData("Random Minor Item"),
            "Hut Urn (6)": LocationData("Random Minor Item"),
            "Hut Urn (7)": LocationData("Random Minor Item"),
            "Hut Urn (8)": LocationData("Random Minor Item"),
            "Hut Urn (9)": LocationData("Random Minor Item"),
            "Hut Urn (10)": LocationData("Random Minor Item"),
            "Hut Urn (11)": LocationData("Random Minor Item"),
            "Hut Urn (12)": LocationData("Random Minor Item"),
            "Hut Urn (13)": LocationData("Random Minor Item"),
            "Rope": LocationData("Rope"),
            "Lucky Coin": LocationData("Lucky coin"),
            "Hut Crate (1)": LocationData("Random Minor Item"),
            "Hut Crate (2)": LocationData("Random Minor Item"),
            "Hut Crate (3)": LocationData("Random Minor Item"),
            "Hut Crate (4)": LocationData("Random Minor Item"),
            "Hut Barrel (1)": LocationData("Random Food Item"),
            "Hut Barrel (2)": LocationData("Random Food Item"),
            # Change Cube of Depths investigate to say what it is and where its from. Already added the template, just need to finish it when we know variables
            "Cube of Depths": LocationData("Cube of depths"),
        },
    ),
    RegionData(
        "Level 6 - Mines (2)",
        locations={
            # Add chests, ghosts?
            # What do we do with blue sin? can't people just savescum it? add a trigger that only checks once you escape with it?
            # For the time being blue sin has been excluded, will add when figure out what to do with it
            # Remember, a lot of the crates and such here are empty
            "Minecart": LocationData("Stone"),
            "Diary of an Unknown Guard": LocationData("Diary of an unknown guard"),
            "Shark Teeth": LocationData("Shark teeth"),
        },
        connections=["Level 7 - Catacombs", "Level 6 - Mines (Cave-in)"],
    ),
    RegionData(
        "Level 6 - Mines (Cave-in)",
        locations={
            # Something to consider is that the player has to have a specific item to access this area, which is completely optional
            # I've added this area in as completely normal for now, but maybe we should treat it differently?
            # Consider adding blue sin here instead of mines (2) to prevent savescumming
            # Add lizardman, ghost loot(?)
            # I believe all of the items here have the same trigger as the non-cave in version, not sure how to handle that.
            # For now, they have not been added to here or RPGMaker side
            # "Minecart": LocationData("Stone"),
            # "Diary of an Unknown Guard": LocationData("Diary of an unknown guard"),
            # "Shark Teeth": LocationData("Shark teeth"),
            "Eastern Silk Robes": LocationData("Eastern silk robes"),
            "Jingasa Kabuto": LocationData("Jingasa kabuto"),
            "Charm of the Yggaegetsu": LocationData("Charm of the yggaegetsu"),
            "Cave Blue Herb (1)": LocationData("Blue herb"),
            "Cave Blue Herb (2)": LocationData("Blue herb"),
            "Cave Blue Herb (3)": LocationData("Blue herb"),
            "Cave Red Herb (1)": LocationData("Red herb"),
            "Cave Red Herb (2)": LocationData("Red herb"),
            "Cave Green Herb (1)": LocationData("Green herb"),
            "Cave Green Herb (2)": LocationData("Green herb"),
            "Cave Green Herb (3)": LocationData("Green herb"),
        },
        connections=["Level 7 - Catacombs", "deeper_thicket"],
    ),
    RegionData(
        "Staircase",
        locations={
            # Hanging corpse has no loot but moonless marks it
            # Eastern ghost appears here
            "Chair Room Crate (1)": LocationData("Random Minor Item"),
            "Chair Room Crate (2)": LocationData("Random Minor Item"),
            "Chair Room Barrel": LocationData("Random Food Item"),
        },
        connections=["Level 7 - Catacombs"],
    ),
    RegionData(
        "Level 7 - Catacombs",
        locations={
            # Enemies need to be added still
            # Enki is here, not sure if stuff needs to be done with him
            # Legarde is also here, I don't think he should be a check as it could make beating certain endings incredibly easy
            # The book of enlightenment does not work on hard mode. Maybe add an alternate use to it? Can we make it able to give archipelago hints?
            "Staircase Crate": LocationData("Random Minor Item"),
            "Entry Room Crate (1)": LocationData("Random Minor Item"),
            "Entry Room Crate (2)": LocationData("Random Minor Item"),
            "Entry Room Barrel": LocationData("Random Food Item"),
            "Enki Room Book of Enlightenment": LocationData("Book of enlightenment"),
            "West Hallway Crate": LocationData("Random Minor Item"),
            "West Hallway Barrel": LocationData("Random Food Item"),
            "East Hallway Barrel (1)": LocationData("Random Food Item"),
            "East Hallway Barrel (2)": LocationData("Random Food Item"),
        },
        connections=["Ancient city - The Tomb of the Gods"],
    ),
    RegionData(
        "Ancient city - The Tomb of the Gods",
        locations={
            # Miasma is here, do we need to do things with that?
            # Chest and maybe enemies need to be added
            # There's like a million events in this room, maybe I missed something
            "Locked Room Urn (1)": LocationData("Random Minor Item"),
            "Locked Room Urn (2)": LocationData("Random Minor Item"),
            "Left Wing Urn (1)": LocationData("Random Minor Item"),
            "Left Wing Urn (2)": LocationData("Random Minor Item"),
        },
        connections=["Ma'habre - The Tomb of the Gods", "Ancient city - Passageway", "The Tomb of the Gods - Level 2"],
    ),
    RegionData(
        "The Tomb of the Gods - Level 2",
        locations={
            "Scroll Storage Room Urn (1)": LocationData("Random Minor Item"),
            "Scroll Storage Room Urn (2)": LocationData("Random Minor Item"),
            "Scroll Storage Room Urn (3)": LocationData("Random Minor Item"),
            "Scroll Storage Room Urn (4)": LocationData("Random Minor Item"),
        },
    ),
    RegionData(
        "Ma'habre - The Tomb of the Gods",
        locations={
            # Chest and maybe enemies need to be added
            "Locked Room Urn (1)": LocationData("Random Minor Item"),
            "Locked Room Urn (2)": LocationData("Random Minor Item"),
            "Left Wing Urn (1)": LocationData("Random Minor Item"),
            "Left Wing Urn (2)": LocationData("Random Minor Item"),
        },
        connections=["Ma'habre - Passageway", "The Tomb of the Gods - Level 2"],
    ),
    RegionData(
        "The Tomb of the Gods - Level 2",
        locations={
            # Tons of bookshelves that need to be added, and lady of moon?
            "Scroll Storage Room Urn (1)": LocationData("Random Minor Item"),
            "Scroll Storage Room Urn (2)": LocationData("Random Minor Item"),
            "Scroll Storage Room Urn (3)": LocationData("Random Minor Item"),
            "Scroll Storage Room Urn (4)": LocationData("Random Minor Item"),
        },
    ),
    RegionData(
        "Ancient city - Passageway",
        locations={
            "Old Mahabre Entrance Urn (1)": LocationData("Random Minor Item"),
            "Old Mahabre Entrance Urn (2)": LocationData("Random Minor Item"),
            "Old Mahabre Entrance Urn (3)": LocationData("Random Minor Item"),
            "Old Mahabre Entrance Urn (4)": LocationData("Random Minor Item"),
            "Old Mahabre Entrance Dried Mushroom": LocationData("Random Minor Item"),
        },
        # Ancient passage is not an error, its mahabre interiors
        connections=["Ancient city - Inside (1)", "Ancient city - Old passage", "Ancient city - Center square"],
    ),
    RegionData(
        "Ancient city - Old passage",
        locations={
            "Blue Demon": LocationData("Blue demon powder"),
            # NOTE: if the renaming script is used, these aren't inside the old passage with the key
            "Ancient Mahabre Explosive Vial": LocationData("Explosive vial"),
            "Book Pages III": LocationData("Book pages III"),
            "Ancient Mahabre Bookshelf": LocationData("Random Minor Book (Ancient)"),
            "Ancient Mahabre Alchemy (1)": LocationData("Random Alchemy"),
            "Ancient Mahabre Alchemy (2)": LocationData("Random Alchemy"),
        },
    ),
    RegionData(
        "Ancient city - Center square",
        locations={
            # Pocketcat
            # Treasure chest that is empty? I don't remember whats there
            # I think one urn near pocketcat is inaccessible, didn't add it
            "Giant Statue Crate (1)": LocationData("Random Minor Item"),
            "Giant Statue Crate (2)": LocationData("Random Minor Item"),
            "Broken Statue Crate (1)": LocationData("Random Minor Item"),
            "Broken Statue Crate (2)": LocationData("Random Minor Item"),
            "Broken Statue Crate (3)": LocationData("Random Minor Item"),
            "Broken Statue Urn (1)": LocationData("Random Minor Item"),
            "Broken Statue Urn (2)": LocationData("Random Minor Item"),
            "Statue Dried Mushroom": LocationData("Dried mushroom"),
            "Temple Entrance Crate (1)": LocationData("Random Minor Item"),
            "Temple Entrance Urn (1)": LocationData("Random Minor Item"),
            "Temple Entrance Urn (2)": LocationData("Random Minor Item"),
        },
        connections=["Ancient city - Downtown", "Ancient city - Inside (1)", "Ancient city - Inside (2)"],
    ),
    RegionData(
        "Ancient city - Inside (1)",
        locations={
            # Cage scene? not sure what it does
            # Gaunt Knight
            # Chests, one of them you can like climb over some rubble or something?
            # Bookshelves
            # Snatcher enemies
            "Inside Ancient Mahabre Urn (Near Knight - 1)": LocationData("Random Minor Item"),
            "Inside Ancient Mahabre Urn (Near Knight - 2)": LocationData("Random Minor Item"),
            "Inside Ancient Mahabre Urn (Near Knight - 3)": LocationData("Random Minor Item"),
            "Inside Ancient Mahabre Urn (Near Knight - 4)": LocationData("Random Minor Item"),
            "Inside Ancient Mahabre Crate (Near Knight - 1)": LocationData("Random Minor Item"),
            "Inside Ancient Mahabre Crate (Near Knight - 2)": LocationData("Random Minor Item"),
            "Inside Ancient Mahabre Urn (Chest Room)": LocationData("Random Minor Item"),
            "Inside Ancient Mahabre Crate (Bookshelf Room - 1)": LocationData("Random Minor Item"),
            "Inside Ancient Mahabre Crate (Bookshelf Room - 2)": LocationData("Random Minor Item"),
            "Ancient Mahabre Prison Coin": LocationData("Lucky coin"),
            "Ancient Mahabre Prison Urn": LocationData("Random Minor Item"),
            "Upstairs Ancient Passage Crate (1)": LocationData("Random Minor Item"),
            "Upstairs Ancient Passage Crate (2)": LocationData("Random Minor Item"),
            "Upstairs Ancient Passage Urn": LocationData("Random Minor Item"),
        },
        # connections=["Ancient_passage", "Ancient_Center_square"],
    ),
    RegionData(
        "Ancient city - Temple district",
        locations={
            # The urns here share data between past mahabre and present mahabre?
        },
        connections=["Ancient city - Back alleys", "Grand library"],
    ),
    RegionData(
        "Grand library",
        locations={

        },
        connections=["Grand library - Inner sanctum"],
    ),
    RegionData(
        "Grand library - Inner sanctum",
        locations={

        },
    ),
    RegionData(
        "Ancient city - Back alleys",
        locations={

        },
        connections=["Ancient city - Underground cave", "Temple of Torment - Level 1 (Ancient)"],
    ),
    RegionData(
        "Temple of Torment - Level 1 (Ancient)",
        locations={

        },
        connections=["Temple of Torment - Level 2 (Ancient)"],
    ),
    RegionData(
        "Ancient city - Underground cave",
        locations={

        },
    ),
    RegionData(
        "Temple of Torment - Level 2 (Ancient)",
        locations={

        },
    ),
    RegionData(
        "Ancient city - Inside (2)",
        locations={

        },
    ),
    RegionData(
        "Ancient city - Downtown",
        locations={
            #chests need to be done
            "Lower Downtown Crate (1)": LocationData("Random Minor Item"),
            "Lower Downtown Crate (2)": LocationData("Random Minor Item"),
            "Lower Downtown Crate (3)": LocationData("Random Minor Item"),
            "Lower Downtown Crate (4)": LocationData("Random Minor Item"),
            "Lower Downtown Crate (5)": LocationData("Random Minor Item"),
            "Lower Downtown Urn (1)": LocationData("Random Minor Item"),
            "Lower Downtown Urn (2)": LocationData("Random Minor Item"),
            "Lower Downtown Urn (3)": LocationData("Random Minor Item"),
            "Lower Downtown Urn (4)": LocationData("Random Minor Item"),
            "Lower Downtown Urn (5)": LocationData("Random Minor Item"),
            "Lower Downtown Urn (6)": LocationData("Random Minor Item"),
            "Lower Downtown Urn (7)": LocationData("Random Minor Item"),
            "Lower Downtown Urn (8)": LocationData("Random Minor Item"),
            "Lower Downtown Urn (9)": LocationData("Random Minor Item"),
            "Lower Downtown Urn (10)": LocationData("Random Minor Item"),
            "Lower Downtown Urn (11)": LocationData("Random Minor Item"),
            "Lower Downtown Urn (12)": LocationData("Random Minor Item"),
            #Only stuff on the "upper level" have the shared variables
            #1408
            "Upper Downtown Crate (1)": LocationData("Random Minor Item"),
            #1409
            "Upper Downtown Crate (2)": LocationData("Random Minor Item"),
            #1288
            "Upper Downtown Crate (3)": LocationData("Random Minor Item"),
            #2352
            "Ancient Passage Downtown Crate": LocationData("Random Minor Item"),
            #Not given a variable for some reason?
            "Ancient Passage Downtown Urn": LocationData("Random Minor Item"),
            #1410
            "Upper Downtown Urn (1)": LocationData("Random Minor Item"),
            #1411
            "Upper Downtown Urn (2)": LocationData("Random Minor Item"),
            #1412
            "Upper Downtown Urn (3)": LocationData("Random Minor Item"),
            #1413
            "Upper Downtown Urn (4)": LocationData("Random Minor Item"),
            #1414
            "Upper Downtown Urn (5)": LocationData("Random Minor Item"),
        },
        connections=["Ancient city - The Tower of Endless"],
    ),
    RegionData(
        "Ancient city - The Tower of Endless",
        locations={
            #1421
            "Tower of the Endless Crate (1)": LocationData("Random Minor Item"),
            #1420
            "Tower of the Endless Crate (2)": LocationData("Random Minor Item"),
            #1419
            "Tower of the Endless Crate (3)": LocationData("Random Minor Item"),
            #1418
            "Tower of the Endless Crate (4)": LocationData("Random Minor Item"),
            #1415
            "Tower of the Endless Urn (1)": LocationData("Random Minor Item"),
            #1416
            "Tower of the Endless Urn (2)": LocationData("Random Minor Item"),
            #1417
            "Tower of the Endless Urn (3)": LocationData("Random Minor Item"),
            #1998
            "Tower of the Endless Barrel": LocationData("Random Food Item"),
        },
    ),
    RegionData(
        "Ma'habre - Passageway",
        locations={
            "Mahabre Entrance Urn (1)": LocationData("Random Minor Item"),
            "Mahabre Entrance Urn (2)": LocationData("Random Minor Item"),
            "Mahabre Entrance Urn (3)": LocationData("Random Minor Item"),
            "Mahabre Entrance Urn (4)": LocationData("Random Minor Item"),
        },
        # Ancient passage is not an error, its mahabre interiors
        # connections=["Mahabre_inside1", "Center_square"],
    ),
]


class FungerLocation(Location):
    game = "Fear & Hunger"


# def create_events(world: FungerWorld) -> None:
#     # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
#     # In our case, the player must press a button in the top left room to open the final boss door.
#     # AP has something for this purpose: "Event locations" and "Event items".
#     # An event location is no different than a regular location, except it has the address "None".
#     # It is treated during generation like any other location, but then it is discarded.
#     # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
#     # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
#     top_left_room = world.get_region("Top Left Room")
#     final_boss_room = world.get_region("Final Boss Room")
#
#     # One way to create an event is simply to use one of the normal methods of creating a location.
#     button_in_top_left_room = APQuestLocation(world.player, "Top Left Room Button", None, top_left_room)
#     top_left_room.locations.append(button_in_top_left_room)
#
#     # We then need to put an event item onto the location.
#     # An event item is an item whose code is "None" (same as the event location's address),
#     # and whose classification is "progression". Item creation will be discussed more in items.py.
#     # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
#     # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
#     # it is common practice to create the item when creating the location.
#     # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
#     # we'll create both the event location and the event item in our locations.py code.
#     button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
#     button_in_top_left_room.place_locked_item(button_item)
#
#     # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
#     # Luckily, we have another event we want to create: The Victory event.
#     # We will use this event to track whether the player can win the game.
#     # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
#     final_boss_room.add_event(
#         "Final Boss Defeated", "Victory", location_type=APQuestLocation, item_type=items.APQuestItem
#     )
#
#     # If you create all your regions and locations line-by-line like this,
#     # the length of your create_regions might get out of hand.
#     # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
#     # However, it is worth understanding how the actual creation of regions and locations works,
#     # That way, we're not just mindlessly copy-pasting! :)
