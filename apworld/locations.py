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
                "Entrance Crate (1)":  LocationData("Random Minor Item"),
                "Entrance Crate (2)":  LocationData("Random Minor Item"),
                "Entrance Crate (3)":  LocationData("Random Minor Item"),
                "Entrance Crate (4)":  LocationData("Random Minor Item"),
                "Storeroom Crate":  LocationData("Random Minor Item"),
                "Storeroom Shelf":  LocationData("Random Minor Item"),
                "Storeroom Barrel":  LocationData("Random Food Item"),
                "Hallway Crate (1)":  LocationData("Random Minor Item"),
                "Hallway Crate (2)":  LocationData("Random Minor Item"),
                "Hallway Crate (3)":  LocationData("Random Minor Item"),
                "Hallway Crate (4)":  LocationData("Random Minor Item"),
                "Hallway Crate (5)":  LocationData("Random Minor Item"),
                "Statue Crate":  LocationData("Random Minor Item"),
                "Hidden Room Barrel (1)":  LocationData("Random Food Item"),
                "Hidden Room Barrel (2)":  LocationData("Random Food Item"),
                "Hidden Room Crate":  LocationData("Random Minor Item"),
                "Library Minor Bookshelf":  LocationData("Random Minor Book"),
                "Library Mockup Bookshelf":  LocationData("Mockup book"),
                "Kitchen Shelf (1)":  LocationData("Random Minor Item"),
                "Rondon Flag":  LocationData("Cloth fragment"),
                "Book of Fears":  LocationData("Book of Fears"),
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
                "West Hallway Crate (1)":  LocationData("Random Minor Item"),
                "West Hallway Crate (2)":  LocationData("Random Minor Item"),
                "West Hallway Crate (3)":  LocationData("Random Minor Item"),
                "West Hallway Crate (4)":  LocationData("Random Minor Item"),
                "East Hallway Crate (1)":  LocationData("Random Minor Item"),
                "East Hallway Crate (2)":  LocationData("Random Minor Item"),
                "East Hallway Crate (3)":  LocationData("Random Minor Item"),
                "North Hallway Crate (1)":  LocationData("Random Minor Item"),
                "North Hallway Crate (2)":  LocationData("Random Minor Item"),
                "North Hallway Crate (3)":  LocationData("Random Minor Item"),
                "North Hallway Crate (4)":  LocationData("Random Minor Item"),
                "North Hallway Barrel":  LocationData("Random Food Item"),
                "Northeast Hallway Barrel (1)":  LocationData("Random Food Item"),
                "Northeast Hallway Barrel (2)":  LocationData("Random Food Item"),
                "Hidden Room Barrel (1)":  LocationData("Random Food Item"),
                "Hidden Room Barrel (2)":  LocationData("Random Food Item"),
                "Hidden Room Crate":  LocationData("Random Minor Item"),
                "Kitchen Barrel (1)":  LocationData("Random Food Item"),
                "Kitchen Barrel (2)":  LocationData("Random Food Item"),
                "Torture Room Crate (1)":  LocationData("Random Minor Item"),
                "Torture Room Crate (2)":  LocationData("Random Minor Item"),
                "Torture Room Crate (3)":  LocationData("Random Minor Item"),
                "Book of Fears":  LocationData("Book of Fears"),
                "Library Minor Bookshelf":  LocationData("Random Minor Book"),
                "Library Mockup Bookshelf":  LocationData("Mockup book"),
                "Rondon Flag":  LocationData("Cloth fragment"),
                "North Entrance Barrel":  LocationData("Random Food Item"),
                "North Entrance Shelf (1)":  LocationData("Random Food Item"),
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
                "Rondon Flag":  LocationData("Cloth fragment"),
                "Book of Fears":  LocationData("Book of Fears"),
                "Entrance Crate (1)":  LocationData("Random Minor Item"),
                "Entrance Crate (2)":  LocationData("Random Minor Item"),
                "Left Hidden Room Barrel (1)":  LocationData("Random Food Item"),
                "Left Hidden Room Barrel (2)":  LocationData("Random Food Item"),
                "Left Hidden Room Barrel (3)":  LocationData("Random Food Item"),
                "Left Hidden Room Barrel (4)":  LocationData("Random Food Item"),
                "Left Hidden Room Crate":  LocationData("Random Minor Item"),
                "Kitchen Shelf (1)":  LocationData("Random Minor Item"),
                "Right Hidden Room Barrel (1)":  LocationData("Random Food Item"),
                "Right Hidden Room Barrel (2)":  LocationData("Random Food Item"),
                "Right Hidden Room Shelf":  LocationData("Random Minor Item"),
                "Right Hidden Room Crate":  LocationData("Random Minor Item"),
                "Right Storeroom Barrel (1)":  LocationData("Random Food Item"),
                "Right Storeroom Barrel (2)":  LocationData("Random Food Item"),
                "Right Storeroom Shelf":  LocationData("Random Minor Item"),
                "Right Storeroom Crate (1)":  LocationData("Random Minor Item"),
                "Right Storeroom Crate (2)":  LocationData("Random Minor Item"),
                "Right Storeroom Crate (3)":  LocationData("Random Minor Item"),
                "Right Storeroom Crate (4)":  LocationData("Random Minor Item"),
                "Right Storeroom Crate (5)":  LocationData("Random Minor Item"),
                "Right Storeroom Crate (6)":  LocationData("Random Minor Item"),
                "Right Storeroom Crate (7)":  LocationData("Random Minor Item"),
                "Right Storeroom Crate (8)":  LocationData("Random Minor Item"),
                "Left Storeroom Barrel":  LocationData("Random Food Item"),
                "Left Storeroom Crate (1)":  LocationData("Random Minor Item"),
                "Left Storeroom Crate (2)":  LocationData("Random Minor Item"),
                "Left Storeroom Crate (3)":  LocationData("Random Minor Item"),
                "Left Storeroom Shelf":  LocationData("Random Minor Item"),
                "Library Mockup Bookshelf":  LocationData("Mockup book"),
                "Library Minor Bookshelf":  LocationData("Random Minor Book"),
                "Captain's Crate":  LocationData("Random Minor Item"),
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
                "Book of Fears":  LocationData("Book of Fears"),
                "Entrance Storeroom Crate (1)":  LocationData("Random Minor Item"),
                "Entrance Storeroom Crate (2)":  LocationData("Random Minor Item"),
                "Entrance Storeroom Barrel":  LocationData("Random Food Item"),
                "Entrance Crate (1)":  LocationData("Random Minor Item"),
                "Entrance Crate (2)":  LocationData("Random Minor Item"),
                "Entrance Crate (3)":  LocationData("Random Minor Item"),
                "Kitchen Crate (1)":  LocationData("Random Minor Item"),
                "Kitchen Crate (2)":  LocationData("Random Minor Item"),
                "Kitchen Crate (3)":  LocationData("Random Minor Item"),
                "Kitchen Barrel (1)":  LocationData("Random Food Item"),
                "Kitchen Barrel (2)":  LocationData("Random Food Item"),
                "Storeroom Crate (1)":  LocationData("Random Minor Item"),
                "Storeroom Barrel":  LocationData("Random Food Item"),
                "Storeroom Shelf":  LocationData("Random Minor Item"),
                "Hallway Crate (1)":  LocationData("Random Minor Item"),
                "Hallway Crate (2)":  LocationData("Random Minor Item"),
                "North Hallway Shelf":  LocationData("Random Minor Item"),
                "North Hallway Barrel":  LocationData("Random Food Item"),
                "Captain's Barrel":  LocationData("Random Food Item"),
                "Captain's Bookshelf":  LocationData("Random Minor Book"),
                "Library Mockup Bookshelf":  LocationData("Mockup book"),
                "Hidden Room Barrel (1)":  LocationData("Random Food Item"),
                "Hidden Room Barrel (2)":  LocationData("Random Food Item"),
                "Hidden Room Crate":  LocationData("Random Minor Item"),
            },
        },
        connections=["Level 1 - Courtyard"]
    ),
    RegionData(
        "Level 1 - Courtyard",
        variants={
            "A": {
                "Courtyard Green Herb":  LocationData("Green herb"),
                "Courtyard Blue Herb":  LocationData("Blue herb"),
                "Courtyard Stick":  LocationData("Stick"),
            },
            "B": {
                "Courtyard Green Herb":  LocationData("Green herb"),
                "Courtyard Blue Herb":  LocationData("Blue herb"),
                "Courtyard Stick":  LocationData("Stick"),
                "Courtyard Barrel (1)":  LocationData("Random Food Item"),
                "Courtyard Barrel (2)":  LocationData("Random Food Item"),
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
                # Double check to see if anything is missing

                "Rondon Flag (1)":  LocationData("Cloth fragment"),
                "Rondon Flag (2)":  LocationData("Cloth fragment"),
                "Captain's Inner Room Shelf (1)":  LocationData("Random Minor Item"),
                "Captain's Inner Room Shelf (2)":  LocationData("Random Minor Item"),
                "Captain's Inner Room Bookshelf (1)":  LocationData("Random Minor Book"),
                "Torture Room Skinning Knife":  LocationData("Skinning knife"),
                "Torture Room Bonesaw":  LocationData("Bonesaw"),
                "Trortur Room Skinning Knife":  LocationData("Skinning knife"),
                "Library Hallway Crate (1)":  LocationData("Random Minor Item"),
                "Library Hallway Crate (2)":  LocationData("Random Minor Item"),
                "Library Hallway Crate (3)":  LocationData("Random Minor Item"),
                "Library Hallway Barrel":  LocationData("Random Minor Food"),
                "Library Bookshelf (1)":  LocationData("Random Minor Book"),
                "Library Bookshelf (2)":  LocationData("Random Minor Book"),
                "Library Bookshelf (3)":  LocationData("Random Minor Book"),
                "Library Bookshelf (4)":  LocationData("Random Minor Book"),
                "Book Pages I":  LocationData("Book pages I"),
                "Torture Hallway Barrel":  LocationData("Random Minor Food"),
                "Trortur Room Barrel":  LocationData("Random Minor Food"),

            },
            "B": {
                # List of things that need proper implementation:
                # Captain's desk doesn't have conditionals but gives a key and diary at the same time, does this work?
                # Buckman stuff, not sure if it gives any items though
                # Bookcase in captain's room and library
                # does the human hydra do anything?
                # Enemies, etc
                # Should we make the sacrifice a location? (same for the praying and orgy?)
                # Double check to see if anything is missing

                "Rondon Flag (1)":  LocationData("Cloth fragment"),
                "Rondon Flag (2)":  LocationData("Cloth fragment"),
                "Sacrifice Room Bookshelf (1)":  LocationData("Random Minor Book"),
                "Sacrifice Room Shelf (1)":  LocationData("Random Minor Item"),
                "Sacrifice Room Shelf (2)":  LocationData("Random Minor Item"),
                "Hydra Hallway Crate (1)":  LocationData("Random Minor Item"),
                "Hydra Hallway Crate (2)":  LocationData("Random Minor Item"),
                "Library Hallway Crate (1)":  LocationData("Random Minor Item"),
                "Library Hallway Crate (2)":  LocationData("Random Minor Item"),
                "Torture Hallway Barrel":  LocationData("Random Minor Food"),
                "Trortur Room Barrel":  LocationData("Random Minor Food"),
                "Torture Room Skinning Knife":  LocationData("Skinning knife"),
                "Torture Room Bonesaw":  LocationData("Bonesaw"),
                "Trortur Room Skinning Knife":  LocationData("Skinning knife"),
                "Library Bookshelf (1)":  LocationData("Random Minor Book"),
                "Library Bookshelf (2)":  LocationData("Random Minor Book"),
                "Library Bookshelf (3)":  LocationData("Random Minor Book"),
                "Library Bookshelf (4)":  LocationData("Random Minor Book"),
                "Library Bookshelf (5)":  LocationData("Random Minor Book"),
                "Library Bookshelf (6)":  LocationData("Random Minor Book"),
            },
            "C": {},
        },
        connections=["Level 2 - Blood pit", "Level 1 - Backyard"],
    ),
    RegionData(
        "Level 1 - Backyard",
        locations={
            "Backyard Stick":  LocationData("Stick"),
            # Weird huge conditional tree on the dagger but it might not be that relevant?
            # "Backyard Dagger": LocationData("Dagger"),
            "Orgy Stick":  LocationData("Stick"),
            "Orgy Red Herb":  LocationData("Stick"),
            "Backyard Blue Herb (West)":  LocationData("Blue herb"),
            "Backyard Blue Herb (East)":  LocationData("Blue herb"),
            "Backyard Green Herb":  LocationData("Green herb"),
            "Backyard Barrel (1)":  LocationData("Random Food Item"),
            "Backyard Barrel (2)":  LocationData("Random Food Item"),
            "Backyard Barrel (3)":  LocationData("Random Food Item"),
            "Backyard Crate":  LocationData("Random Minor Item"),
            "Butterfly Soul":  LocationData("Butterfly soul"),
        },
        connections=["Level 1 - Hidden backyard"],
    ),
    RegionData(
        "Level 1 - Hidden backyard",
        locations={
            # Dog has no loot
            "Hidden Backyard Stick (1)":  LocationData("Stick"),
            "Hidden Backyard Stick (2)":  LocationData("Stick"),
        },
        connections=["Tree of the Depths - Thicket Level 1"],
    ),
    RegionData(
        "Level 2 - Basement",
        variants={
            "A": {
                locations={
                    "Rune Room Dried Mushroom (West)": LocationData("Dried Mushroom"),
                    "Rune Room Dried Mushroom (North)": LocationData("Dried Mushroom"),
                    "Rune Room Dried Mushroom (Northeast)": LocationData("Dried Mushroom"),
                    "Rune Room Dried Mushroom (East)": LocationData("Dried Mushroom"),
                    "Hallway Dried Mushroom": LocationData("Dried Mushroom"),
                    "Miasma": LocationData("Miasma"),
                    "Rune Room Barrel (1)":  LocationData("Random Food Item"),
                    "Rune Room Barrel (2)":  LocationData("Random Food Item"),
                    "Rune Room Barrel (3)":  LocationData("Random Food Item"),
                    "Rune Room Crate":  LocationData("Random Minor Item"),
                    "Rune Room Blue Herb":  LocationData("Blue Herb"),
                    "Rune Room Green Herb":  LocationData("Green Herb"),
                    "Keg Room Barrel (Left)":  LocationData("Random Food Item"),
                    "Keg Room Barrel (Right)":  LocationData("Random Food Item"),
                    # Note: Change the description text/pickup text for this one?
                    "Keg Room Rotten Meat":  LocationData("Rotten meat"),
                    "Vertical Hallway Crate (1)":  LocationData("Random Minor Item"),
                    "Vertical Hallway Crate (2)":  LocationData("Random Minor Item"),
                    "Vertical Hallway Crate (3)":  LocationData("Random Minor Item"),
                    "Vertical Hallway Crate (Right)":  LocationData("Random Minor Item"),
                    "Corpse Pile Hallway Crate":  LocationData("Random Minor Item"),
                    "Corpse Pile Hallway Crate (2)":  LocationData("Random Minor Item"),
                    "Corpse Pile Hallway Barrel (Left)":  LocationData("Random Food Item"),
                    "Corpse Pile Hallway Barrel (Right)":  LocationData("Random Food Item"),
                    # TODO: Armour racks/Weapon Racks/the chest are not common events. They have not been added in because of that, fix them first
                }
            },
            "B": {
                locations={
                    "Entryway Dried Mushroom": LocationData("Dried Mushroom"),
                    "Rune Room Dried Mushroom (Southwest)": LocationData("Dried Mushroom"),
                    "Rune Room Dried Mushroom (West)": LocationData("Dried Mushroom"),
                    "Rune Room Dried Mushroom (Northeast)": LocationData("Dried Mushroom"),
                    "Rune Room Dried Mushroom (East)": LocationData("Dried Mushroom"),
                    "Rune Room Blue Herb": LocationData("Blue herb"),
                    "Hallway Blue Herb": LocationData("Blue herb"),
                    "Hallway Green Herb": LocationData("Green herb"),
                    "Kitchen Rotten Meat":  LocationData("Rotten meat"),
                    "Kitchen Barrel":  LocationData("Random Food Item"),
                    "Miasma": LocationData("Miasma"),
                    "Armory Hallway Barrel":  LocationData("Random Food Item"),
                    "Armory Hallway Crate (1)":  LocationData("Random Minor Item"),
                    "Armory Hallway Crate (2)":  LocationData("Random Minor Item"),
                    "Armory Hallway Crate (3)":  LocationData("Random Minor Item"),
                    "Armory Hallway Crate (4)":  LocationData("Random Minor Item"),
                    "Armory Hallway Crate (5)":  LocationData("Random Minor Item"),
                    "Armory Hallway Crate (6)":  LocationData("Random Minor Item"),
                    "Armory Hallway Crate (7)":  LocationData("Random Minor Item"),
                    "Centre Hallway Crate (1)":  LocationData("Random Minor Item"),
                    "Centre Hallway Crate (2)":  LocationData("Random Minor Item"),
                    "Moss Hallway Dried Mushroom (1)": LocationData("Dried Mushroom"),
                    "Moss Hallway Dried Mushroom (2)": LocationData("Dried Mushroom"),
                    "Moss Hallway Dried Mushroom (3)": LocationData("Dried Mushroom"),
                    "Right Hallway Crate":  LocationData("Random Minor Item"),
                    # TODO: Armour racks/Weapon Racks/the chest are not common events. They have not been added in because of that, fix them first
                }
            },
        },
        connections=["Flip side - Basement", "Level 3 - Basement"],
    ),
    RegionData( # TODO: Can only enter once, items not added yet in RPGMaker
        "Flip side - Basement" #,
        # locations = {
        #     "Flipside Basement - Room 3 Barrel (Left)": LocationData("Random Food Item"),
        #     "Flipside Basement - Room 3 Barrel (Right)": LocationData("Random Food Item"),
        #     "Flipside Basement - Room 5 Crate (Left)": LocationData("Random Minor Item"),
        #     "Flipside Basement - Room 5 Crate (Left)": LocationData("Random Minor Item"),
        # }
    ),
    RegionData(
        "Level 3 - Basement",
        locations = {

        },
        connections=["Level 3 - Prisons"],
        ),
    RegionData(
        "Level 3 - Prisons",
        variants={
            "A": {},
            "B": {},
            "C": {},
        }),
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
