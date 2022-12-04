from enum import Enum


class Category(Enum):

    PHONES = 'Phones'
    LAPTOPS = 'Laptops'
    TV = 'TV'
    COMPUTERS_AND_COMPONENTS = 'Computers & Computer components'
    SMART_WATCHES = 'Smart Watches'
    PHOTOGRAPHY = 'Photography'
    GAMING_CONSOLES = 'Gaming consoles'
    HEADPHONES = 'Headphones'
    TABLETS = 'Tablets'
    AUDIO = 'Audio'
    STORAGE = 'Storage'

    @classmethod
    def choices(cls):
        return [(category.name, category.value) for category in cls]
