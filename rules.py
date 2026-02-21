from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import FungerWorld


def set_all_rules(world: FungerWorld) -> None:
    # Two of these are not yet implemented for the test, look up apquest info when you need to add them
    # set_all_entrance_rules(world)
    # set_all_location_rules(world)
    set_completion_condition(world)


# def set_all_entrance_rules(world: APQuestWorld) -> None:
# fortress_to_level1_basement_a = world.get_entrance("Fortress to Level 1: Left Entrance")


def set_completion_condition(world: FungerWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has_all(
        ("Dried mushroom"), world.player
    )

    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    # world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
