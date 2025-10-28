"""Inventory Management System Module."""

import json
import logging
from datetime import datetime
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

DEFAULT_FILE = "inventory.json"


class Inventory:
    """Class to manage inventory operations."""

    def __init__(self) -> None:
        """Initialize an empty inventory."""
        self.stock_data: Dict[str, float] = {}

    def add_item(self, item: str, qty: float) -> None:
        """Add an item and its quantity to the inventory."""
        if not isinstance(item, str):
            logging.warning("Invalid item name: %s", item)
            return
        if not isinstance(qty, (int, float)):
            logging.warning("Invalid quantity for %s: %s", item, qty)
            return

        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        logging.info("Added %s of %s", qty, item)

    def remove_item(self, item: str, qty: float) -> None:
        """Remove a specified quantity of an item from the inventory."""
        try:
            self.stock_data[item] -= qty
            if self.stock_data[item] <= 0:
                del self.stock_data[item]
                logging.info("Removed item: %s (quantity zero or below)", item)
        except KeyError:
            logging.warning("Item '%s' not found in inventory.", item)
        except TypeError:
            logging.warning("Invalid quantity type for removal: %s", qty)

    def get_qty(self, item: str) -> float:
        """Return the current quantity of a given item."""
        return self.stock_data.get(item, 0)

    def check_low_items(self, threshold: float = 5) -> List[str]:
        """Return a list of items whose quantities are below the threshold."""
        return [item for item, qty in self.stock_data.items() if qty < threshold]

    def save_data(self, file_name: str = DEFAULT_FILE) -> None:
        """Save inventory data to a JSON file."""
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(self.stock_data, file, indent=4)
        logging.info("Data saved successfully to %s", file_name)

    def load_data(self, file_name: str = DEFAULT_FILE) -> None:
        """Load inventory data from a JSON file."""
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                self.stock_data = json.load(file)
            logging.info("Data loaded from %s", file_name)
        except FileNotFoundError:
            logging.warning("File '%s' not found. Starting with empty inventory.", file_name)
            self.stock_data = {}
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from '%s'. Starting fresh.", file_name)
            self.stock_data = {}

    def print_data(self) -> None:
        """Print a report of all inventory items and their quantities."""
        logging.info("Generating items report:")
        for item, qty in self.stock_data.items():
            print(f"{item} -> {qty}")


def main() -> None:
    """Main function for demonstrating inventory operations."""
    inventory = Inventory()
    inventory.add_item("apple", 10)
    inventory.add_item("banana", -2)
    inventory.add_item("orange", 3)
    inventory.remove_item("apple", 3)
    inventory.remove_item("orange", 1)
    print("Apple stock:", inventory.get_qty("apple"))
    print("Low items:", inventory.check_low_items())
    inventory.save_data()
    inventory.load_data()
    inventory.print_data()


if __name__ == "__main__":
    main()
