from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from .world import FungerWorld

# This is currently a test for the first room in the game, where you loot the barrels going into the dungeon.
# A better solution will be found for the full game
# Test map name in rpgmaker is "Fortress"
LOCATIONS = {
    "Fortress": {
        "Bottom Right Crate": 1,
        "Right Crate (Left)": 2,
        "Right Crate (Top)": 3,
        "Right Crate (Right)": 4,
        "Right Barrel": 5,
        "Left Barrel (Left)": 6,
        "Left Barrel (Right)": 7,
    },
    "Level 1: Left Entrance": {
        "Entrance Barrel (Left)": 8,
        "Entrance Barrel (Right)": 9,
        "Dried Mushroom (Left Entrance)": 10,
    },
}


class FungerLocation(Location):
    game = "Fear & Hunger"

# def get_locations(location_names: list[str]) -> dict[str, int | None]:
    # return {location_name: LOCATIONS[location_name] for location_name in location_names}

def create_all_locations(world: FungerWorld) -> None:
    create_regular_locations(world)
    # create_events(world)


def create_regular_locations(world: FungerWorld) -> None:
    # Using the RPGMaker map names as the region names
    fortress = world.get_region("Fortress")
    level1_basement_a = world.get_region("Level 1: Left Entrance")

    fortress.add_locations(LOCATIONS["Fortress"], FungerLocation)
    level1_basement_a.add_locations(LOCATIONS["Level 1: Left Entrance"], FungerLocation)


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
