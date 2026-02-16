# This file has been written with help from https://github.com/NewSoupVi/Archipelago/blob/apquest/worlds/apquest/
# Comments have been left in from this, where needed, for the time being

from collections.abc import Mapping
from typing import Any

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, locations, options, regions, rules, web_world


class FungerWorld(World):
    """
    Fear & Hunger is a survival horror dungeon crawler made in RPGMaker.
    A terrifying presence has entered the room...
    """

    game = "Fear & Hunger"

    web = web_world.FungerWebWorld()

    options_dataclass = options.FungerOptions
    options: options.FungerOptions

    location_name_to_id = {}
    for region in locations.LOCATIONS:
        for key, value in locations.LOCATIONS[region].items():
            location_name_to_id[key] = value

    item_name_to_id = items.ITEMS

    # There is always one region that the generator starts from & assumes you can always go back to.
    # This defaults to "Menu", but you can change it by overriding origin_region_name.
    # TODO: Look into what "region" is best to use, is it the main menu or the first screen?
    origin_region_name = "Menu"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.FungerItem:
        return items.create_item_with_correct_classification(self, name)

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        # TODO: Change this and add in funger specific settings?
        return self.options.as_dict(
            "hard_mode", "hammer", "extra_starting_chest", "confetti_explosiveness", "player_sprite"
        )
