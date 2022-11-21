from enum import Enum


class Category(Enum):

    PHONES = 'Phones'
    LAPTOPS = 'Laptops'
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

#     @classmethod
#     def get_max_name_length(cls):
#         return max([len(category[1]) for category in cls])
#
# #
# for category in Category.choices():
#     print(category)
#     print(category[1])
