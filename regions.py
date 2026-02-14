from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import FungerWorld

def create_and_connect_regions(world: FungerWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: FungerWorld) -> None:
    fortress = Region("Fortress", world.player, world.multiworld)

    regions = [fortress]

    world.multiworld.regions += regions


# def connect_regions(world: APQuestWorld) -> None:
#     fortress = world.get_region("Fortress")
#
#     # Okay, now we can get connecting. For this, we need to create Entrances.
#     # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
#     # One way to create an Entrance is by calling the Entrance constructor.
#     overworld_to_bottom_right_room = Entrance(world.player, "Overworld to Bottom Right Room", parent=overworld)
#     overworld.exits.append(overworld_to_bottom_right_room)
#
#     # You can then connect the Entrance to the target region.
#     overworld_to_bottom_right_room.connect(bottom_right_room)
#
#     # An even easier way is to use the region.connect helper.
#     overworld.connect(right_room, "Overworld to Right Room")
#     right_room.connect(final_boss_room, "Right Room to Final Boss Room")
#
#     # The region.connect helper even allows adding a rule immediately.
#     # We'll talk more about rule creation in the set_all_rules() function in rules.py.
#     overworld.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))
#
#     # Some Entrances may only exist if the player enables certain options.
#     # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
#     # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
#     if world.options.hammer:
#         top_middle_room = world.get_region("Top Middle Room")
#         overworld.connect(top_middle_room, "Overworld to Top Middle Room")
