import random
import string


def random_generator_key(size=3, chrs=string.digits):
    return ''.join(random.choice(chrs) for x in range(size))


def random_generator_sub(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))


def random_generator_sold_ship(size=10, chars=string.digits):
    return "".join(random.choice(chars) for x in range(size))


class TestData_CustomerAccount:
    test_data_addCust = [{'UserName': 'cc', 'Password': '1', 'KeyAccountName': random_generator_key() + ' Ford',
                          'CustomerName': random_generator_sub(), 'SoldToNumber': random_generator_sold_ship(),
                          'ShipToNumber': random_generator_sold_ship()}]

    test_data_add_Exst = [
        {'UserName': 'cc', 'Password': '1', 'KeyAccountName': '04 FIAT', 'CustomerName': 'GAC FIAT-Guangzhou-1P',
         'SoldToNumber': '0003965740', 'ShipToNumber': '0003965740'}]

    test_data_edit = [
        {'UserName': 'cc', 'Password': '1', 'KeyAccountName': '08 BAONENG',
         'CustomerName': random_generator_key() + 'BAONENG',
         'SoldToNumber': random_generator_sold_ship(), 'ShipToNumber': random_generator_sold_ship(),
         'KeyAccountName1': '04 DAIMLER'}]
