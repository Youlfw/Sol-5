class Item:
    def __init__(self, name, rarity, effects):
        self.name = name
        self.rarity = rarity
        self.effects = effects

    def display_info(self):
        return f'Item: {self.name}, Rarity: {self.rarity}, Effects: {', '.join(self.effects)}'


class ItemSelectionScreen:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def select_item_by_rarity(self, rarity):
        selected_items = [item for item in self.items if item.rarity == rarity]
        return selected_items

    def display_items(self):
        for item in self.items:
            print(item.display_info())


# Example items
common_item = Item('Common Sword', 'Common', ['Basic Attack', 'No Special Effects'])
rare_item = Item('Rare Shield', 'Rare', ['Defense Boost', 'Reflect Damage'])
legendary_item = Item('Legendary Bow', 'Legendary', ['Critical Hit', 'Increased Range'])
mythical_item = Item('Mythical Staff', 'Mythical', ['Magic Power', 'Mana Regeneration'])
epic_item = Item('Epic Axe', 'Epic', ['High Damage', 'Slow Attack Speed'])

item_screen = ItemSelectionScreen()
item_screen.add_item(common_item)
item_screen.add_item(rare_item)
item_screen.add_item(legendary_item)
item_screen.add_item(mythical_item)
item_screen.add_item(epic_item)

# Display all items
item_screen.display_items()