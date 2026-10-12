# This file has been written with help from https://github.com/NewSoupVi/Archipelago/blob/apquest/worlds/apquest/
# Comments have been left in from this, where needed, for the time being

from collections.abc import Mapping
from typing import Any
import json

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

    location_name_to_id = {}  # noqa: RUF012
    for region_data in REGIONS:
        if region_data.locations:
            for location_name, location_data in region_data.locations.items():
                location_name_to_id[f"{region_data.name}: {location_name}"] = location_data.id
        else:
            for variant_name, locations in region_data.variants.items():
                for location_name, location_data in locations.items():
                    location_name_to_id[f"{region_data.name} ({variant_name}): {location_name}"] = location_data.id

    item_name_to_id = {item_name: item_data.id for item_name, item_data in ITEMS.items()}  # noqa: RUF012

    # There is always one region that the generator starts from & assumes you can always go back to.
    # This defaults to "Menu", but you can change it by overriding origin_region_name.
    origin_region_name = "Fortress"

    def create_regions(self) -> None:
        regions = [Region(region_data.name, self.player, self.multiworld) for region_data in REGIONS]
        self.multiworld.regions += regions

        funger_json = { "Variants":{}, "Options":{}}
        for region_data in REGIONS:
            region = self.get_region(region_data.name)

            for to_name in region_data.connections:
                to_region = self.get_region(to_name)
                region.connect(to_region, f"{region_data.name} to {to_name}")

            region_name = region_data.name
            if region_data.variants:
                if region_name == "Level 1 - Courtyard":
                    if funger_json["Variants"]["Level 1 - Entrance"] == "A":
                        funger_json["Variants"][region_name] = "A"
                    else:
                        funger_json["Variants"][region_name] = "B"
                else:
                    variant = self.random.choice(list(region_data.variants.keys()))
                    funger_json["Variants"][region_name] = variant
                region_data.locations = region_data.variants[variant]
                region_name = f"{region_data.name} ({variant})"

            region.add_locations(
                {
                    f"{region_name}: {location_name}": location_data.id
                    for location_name, location_data in region_data.locations.items()
                }
            )

        #Probably put this in its own function, just writing this out here for now
        funger_json["Options"]["Character"] = str(self.options.character)

        with open('fungerpelago_data.json', 'w', encoding='utf-8') as f:
            json.dump(funger_json, f, ensure_ascii=False, indent=4)

        # create_events(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def randomize_common(self, name: str) -> str:
        # Default to Torch if something goes wrong
        item = "Torch"
        if name == "Random Minor Item":
            # Multiple of the same item are not errors, some items are just weighted higher
            choices = ["Tinderbox x5", "Cloth fragment", "Glass vial", "Tobacco x2", "Pipe", "Opium powder",
                "Bottle of whiskey", "Nitroglycerin powder", "Red vial", "Ale", "Pinecone", "Small key",
                "Blue vial", "Nothing", "Stick", "Blue vial", "Ale", "Red vial", "Cloth hood", "Leather helmet",
                "Oil", "Silver coin x5", "Dirt x5", "Iron arrow", "White vial", "Quill", "Water vial",
                "Wooden buckler", "Explosive vial", "Bear trap", "Purifying talisman", "Red herb", "Blue herb",
                "Green herb", "Silver coin x12", "Silver coin x6", "Silver coin x3", "Raw meat", "Bonesaw",
                "Throwing knife", "Worm juice", "Throwing dart", "Random Rare Item", "Random Rare Item",
                "Lucky coin", "Torch", "Tinderbox x5", "Cloth fragment and Stick"]
            # These choices are given a 50% chance to reroll, same as base funger
            # Some are even rarer than that, green herb is 1/5, lucky coin is 1/3
            rare_choices = ["Opium powder", "Bottle of whiskey", "Red vial", "Small key", "Purifying talisman",
                "Green herb", "Lucky coin"]
            item = self.random.choice(choices)
            while item in rare_choices:
                if item == "Green herb":
                    if self.random.randrange(1,5) == 1:
                        break
                    else:
                        item = self.random.choice(choices)
                if item == "Lucky coin":
                    if self.random.randrange(1,3) == 1:
                        break
                    else:
                        item = self.random.choice(choices)
                else:
                    if self.random.randrange(1,2) == 1:
                        break
                    else:
                        item = self.random.choice(choices)
        # Don't elif, since random minor item can turn into random rare item
        
        return item

    def create_items(self) -> None:
        items = [
            self.create_item(location_data.item_name)
            for region_data in REGIONS
            for location_data in region_data.locations.values()
        ]
        self.multiworld.itempool += items

    def create_item(self, name: str) -> FungerItem:
        data = ITEMS[name]
        classification = data.classification
        id = data.id


        random_types = ["Random Minor Item", "Random Minor Book", "Random Food Item", "Random Minor Book (Ancient)",
             "Random Alchemy"]
        # coinflip items: "Random Scroll Item", "Random Good Armor", "Random Rare Item", "Random Rare Book",
        #   "Random Rare Book (Ancient)", "Random Weapon", "Random Minor Weapon"(?),
        # Haven't added any enemy loot either
        # if name in random_types:


        if name == "Torch" and (
            self.options.difficulty.option_terror_and_starvation or self.options.difficulty.option_hard_mode
        ):
            classification = ItemClassification.progression

        return FungerItem(name, classification, id, self.player)

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        # TODO: Change this and add in funger specific settings?
        return self.options.as_dict("ending", "difficulty", "skip_coin_flip")
