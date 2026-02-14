from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import FungerWorld

def create_and_connect_regions(world: FungerWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: FungerWorld) -> None:
    # Using the RPGMaker map names as the region names
    fortress = Region("Fortress", world.player, world.multiworld)
    level1_basement_a = Region("Level 1: Left Entrance", world.player, world.multiworld)

    regions = [fortress, level1_basement_a]

    world.multiworld.regions += regions


def connect_regions(world: APQuestWorld) -> None:
    fortress = world.get_region("Fortress")
    level1_basement_a = world.get_region("Level 1: Left Entrance")

    fortress.connect(level1_basement_a, "Fortress to Level 1: Left Entrance")
