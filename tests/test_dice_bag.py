import pytest

from src.dice_bag import RollableDice


def test_default_dice_sides():
    dice = RollableDice()
    assert dice.sides == 6
