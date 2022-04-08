import pytest

from src.dice_bag import RollableDice, DiceBag


def test_default_dice_sides():
    dice = RollableDice()
    assert dice.sides == 6
    print("test run successfully")
    test_bag = DiceBag()
