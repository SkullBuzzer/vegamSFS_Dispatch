import random
import string


def random_generator(size=100, chrs=string.digits):
    return ''.join(random.choice(chrs) for x in range(size))


class TestDataAddNewGroup:
    testData_newGroup = [{'Username': 'cc', 'Password': '1', 'Groupname': 'RelabelGroup' + random_generator(),
                          'OperationType': 'Relabel', 'OperatorName': 'Guru Patil', 'OperationType1': 'Delivery Order',
                          'OperatorName1': 'an'}]

    testData_search = [{'Username': 'cc', 'Password': '1', 'Groupname': 'Relabel Group 1', 'OperationType': 'Relabel',
                        'OperatorName': 'Guru Patil'}]
