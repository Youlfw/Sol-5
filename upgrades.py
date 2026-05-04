class UpgradeCard:
    def __init__(self, name: str, rarity: str):
        self.name = name
        self.rarity = rarity

    def __repr__(self):
        return f"{self.name} (Rarity: {self.rarity})"


class CardSelectionScreen:
    def __init__(self):
        self.upgrade_cards = {
            'Common': [],
            'Uncommon': [],
            'Rare': [],
            'Epic': [],
            'Legendary': []
        }

    def add_card(self, card: UpgradeCard):
        if card.rarity in self.upgrade_cards:
            self.upgrade_cards[card.rarity].append(card)
        else:
            print(f"Rarity {card.rarity} is not a valid tier.")

    def display_cards(self):
        for rarity, cards in self.upgrade_cards.items():
            print(f"{rarity} Cards:")
            for card in cards:
                print(f"  - {card}")
