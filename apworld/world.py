# This file has been written with help from https://github.com/NewSoupVi/Archipelago/blob/apquest/worlds/apquest/
# Comments have been left in from this, where needed, for the time being

from collections.abc import Mapping
from typing import Any

# Imports of base Archipelago modules must be absolute.
from BaseClasses import ItemClassification, Region
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import rules
from .items import ITEMS, FungerItem
from .locations import REGIONS
from .options import FungerOptions
from .web_world import FungerWebWorld


class FungerWorld(World):
    """
    Fear & Hunger is a survival horror dungeon crawler made in RPGMaker.
    A terrifying presence has entered the room...
    """

    game = "Fear & Hunger"

    web = FungerWebWorld()

    options_dataclass = FungerOptions
    options: FungerOptions

    # ruff: disable[RUF012]
    location_name_to_id = {
        location_name: location_data.id
        for region_data in REGIONS.values()
        for location_name, location_data in region_data.locations.items()
    }
    item_name_to_id = {item_name: item_data.id for item_name, item_data in ITEMS.items()}
    # ruff: enable[RUF012]

    # There is always one region that the generator starts from & assumes you can always go back to.
    # This defaults to "Menu", but you can change it by overriding origin_region_name.
    # TODO: Look into what "region" is best to use, is it the main menu or the first screen?
    origin_region_name = "Fortress"

    def create_regions(self) -> None:
        regions = [Region(region_name, self.player, self.multiworld) for region_name in REGIONS.keys()]
        self.multiworld.regions += regions

        for region_name, region_data in REGIONS.items():
            region = self.get_region(region_name)

            for to_name in region_data.connections:
                to_region = self.get_region(to_name)
                region.connect(to_region, f"{region_name} to {to_name}")

            region.add_locations(
                {location_name: location_data.id for location_name, location_data in region_data.locations.items()}
            )

        # create_events(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items = [
            self.create_item(location_data.item_name)
            for region_data in REGIONS.values()
            for location_data in region_data.values()
        ]
        self.multiworld.itempool += items

    def create_item(self, name: str) -> FungerItem:
        data = ITEMS[name]
        classification = data.classification
        id = data.id

        if name == "Torch" and (
            self.options.DifficultyChoice.terror_and_starvation or self.options.DifficultyChoice.hard_mode
        ):
            classification = ItemClassification.progression

        return FungerItem(name, classification, id, self.player)

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        # TODO: Change this and add in funger specific settings?
        return self.options.as_dict("ending", "difficulty", "skip_coin_flip", "start_with_dash")
