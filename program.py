from datetime import date

# ------- Domain section is here (domain = numbers, transactions, expenses, etc.) -------

# ---- getters / setters ----


def get_day(expense):
    '''
    Gets the day
    :param expense: the expense (type: dictionary)
    :return: the day (type: int)
    '''
    return expense.get("day")


def get_money(expense):
    '''
    Gets the money value
    :param expense: the expense (type: dictionary)
    :return: the amount of money (type: int)
    '''
    return expense.get("amount_of_money")


def get_type(expense):
    '''
    Gets the type of expense
    :param expense: the expense (type: dictionary)
    :return: the expense type (type: string)
    '''
    return expense.get("expense_type")


def set_money(expense, value):
    '''
    Gets the money value
    :param expense: the expense (type: dictionary)
    :param value: the value that needs to be added
    :return: Nothing
    '''
    expense["amount_of_money"] += value


def check_type(nr):
    '''
    -We check what type the variable is
    -To be correct, it need to be either a natural number or a string of the expense type
    -If not, it raises an error
    :param nr: the parameter that we want to check (type: string)
    :return: the type (type: string)
    '''
    try:  # if it is a number or not
        nr = float(nr)
    except ValueError:
        expense_dict = ['housekeeping', 'food', 'transport', 'clothing', 'internet', 'others']
        if nr not in expense_dict:
            raise ValueError("This is not an available type of expense or a number!\n\tAvailable types:"
                             "housekeeping, food, transport, clothing, internet, others\n"
                             "Please try again!")
        return 'string'

    if nr.is_integer():  # if it is int or float
        nr = int(nr)
        if nr >= 0:  # if it is positive or not
            return 'natural'
        else:
            raise ValueError("This is a negative number! Try again...")
    else:
        raise ValueError("This is a float number! Try again...")


def create_expense(day, money, type):
    '''
    -We check if the inserted expense is good
    -If it is good, we create the expense and return it. If not, errors will appear
    :param day: the day (type: int(positive))
    :param money: the amount of money (type: int(positive))
    :param type: the type of expense (type: string)
    :return: the expense (type: dictionary)
    '''

    # day: between 1 and 30, for simplicity
    if check_type(day) == 'natural':
        day = int(day)
    if day < 1 or day > 30:
        raise ValueError('The day is not in the interval [1,30]! Try again...')

    # amount of money :positive integer
    if check_type(money) == 'natural':
        money = int(money)

    # expense type: housekeeping, food, transport, clothing, internet, others)
    if check_type(type) == 'string':
        type = str(type)

    return {'day': int(day), 'amount_of_money': int(money), 'expense_type': str(type)}


# ---- UI functions ----


def display_by_days2(expenses):
    '''
    Dsiplays by days (p1)
    :param expenses: list of expenses( type: list)
    :return: Nothing
    '''
    for j in range(len(expenses)):
        print('In day' + str(get_day(expenses[j])) + ' : ' + str(get_money(expenses[j])) + ' RON for ' + str(get_type(expenses[j])))


def display_by_category2(expenses):
    '''
        Dsiplays by category (p2)
        :param expenses: list of expenses( type: list)
        :return: Nothing
        '''
    print('For ' + str(get_type(expenses[0])) + ':')
    for j in range(len(expenses)):
        print("\tIn day " + str(get_day(expenses[j])) + " -> " + str(get_money(expenses[j])) + ' RON;')


def display_none():
    '''
    If nothing needs to be displayed
    :return: Nothing
    '''
    print("\tThere are no expenses for " + str(category) + "in this month yet.")


def display_by_category_compare2(expenses, p, category, value):
    '''
        Dsiplays by days (p1)
        :param expenses: list of expenses( type: list)
        :param p : if it needs to be <,=,>
        :param category: from what category
        :param value :the value to compare
        :return: Nothing
        '''
    if p == 3:
        print('For ' + str(category) + ' < ' + str(value) + ' RON:')
    elif p == 4:
        print('For ' + str(category) + ' = ' + str(value) + ' RON:')
    else:
        print('For ' + str(category) + ' > ' + str(value) + ' RON:')

    for j in range(len(expenses)):
        print("\tIn day " + str(get_day(expenses[j])) + " -> " + str(get_money(expenses[j])) + ' RON;')


def display_none2(p, category, value):
    '''
    If nothing needs to be displayed
    :param p : if it needs to be <,=,>
    :param category: from what category
    :param value :the value to compare
    :return : Nothing
    '''
    if p == 3:
        print("\tThere are no expenses for the category -" + str(category) +
              "- which are smaller than " + str(value) + " RON in this month yet.")
    elif p == 4:
        print("\tThere are no expenses for the category -" + str(category) +
              "- which are equal to " + str(value) + " RON in this month yet.")
    else:
        print("\tThere are no expenses for the category -" + str(category) +
              "- which are greater than " + str(value) + " RON in this month yet.")


def print_menu():
    '''
    Prints the menu with the commands
    :return: Nothing
    '''
    print("\n(A) Add a new expense")
    print("\t\tadd <sum> <category>\n\t\tinsert <day> <sum> <category>")
    print("(B) Modify expenses")
    print("\t\tremove <day>\n\t\tremove <start day> to <end day>\n\t\tremove <category>")
    print("(C) Display expenses with different properties")
    print("\t\tlist\n\t\tlist <category>\n\t\tlist <category> [ < | = | > ] <value>. Condition:"
          "the value has to be a positive natural number")


def print_goodbye():
    '''
    A goodbye message
    :return: Nothing
    '''
    print('Goodbye! ^_^')


def print_bad_command():
    '''
    Called when the command that was written isn't good
    :return: Nothing
    '''
    print('Oops ... bad command! Please try again!')


def print_error(error):
    '''
    Prints the customized text for the error
    :param error: the text of the error
    :return: Nothing
    '''
    print(str(error))


# ------ Functionalities section ------

# ---- add functions ----
def is_in_list(day, money, type, expenses):
    for i in range(len(expenses)):
        if get_day(expenses[i]) == int(day):
            if get_type(expenses[i]) == type:
                set_money(expenses[i], int(money))
                return True
    return False


def add_new_expense(expenses, command_param):
    '''
    We add a new expense to the list
    :param expenses: the list of expenses (type: list)
    :param command_param: the parameters of the command (type: list)
    :return: Nothing
    '''

    if len(command_param) == 2:
        day = str(date.today())
        tokens = day.split("-")
        day = int(tokens[2])  # current day
        if not is_in_list(day, command_param[0], command_param[1], expenses):
            expenses.append(create_expense(day, command_param[0], command_param[1]))
    else:
        raise ValueError("Wrong input! See the available options:\n"
                         "\tadd <sum> <category>\n")


def insert_new_expense(expenses, command_param):
    if len(command_param) == 3:
        if not is_in_list(command_param[0], command_param[1], command_param[2], expenses):
            expenses.append(create_expense(command_param[0], command_param[1], command_param[2]))
    else:
        raise ValueError("Wrong input! See the available options:"
                         "\n\tinsert <day> <sum> <category>\n")


# ---- modify functions ----
def m_what_command(command_param):
    '''
    -We check if the parameters for the modify functions are correct.
    -If they are, we find out what command the user wants (from the 3 available commands)
    :param command_param: list of parameters (type: list)
    :return: the number of the command (type: int)
    '''

    if len(command_param) == 1:
        type = check_type(command_param[0])
        if type == 'natural':
            return 1
        elif type == 'string':
            return 3
    elif len(command_param) == 3:
        type1 = check_type(command_param[0])
        type2 = check_type(command_param[2])
        if command_param[1] == 'to' and type1 == type2 == 'natural':
            if 0 < int(command_param[0]) < 31 and 0 < int(command_param[2]) < 31:
                return 2
            else:
                raise ValueError("The days are in the interval [1, 30]! Try again...")
        else:
            raise ValueError("Wrong parameters!")
    else:
        raise ValueError("Wrong input! See the available options:"
                         "\n\tremove <day>\n\tremove <start day> to <end day>"
                         "\n\tremove <category>")


def remove(begin, end, step, expenses, x_to_delete, x):
    '''
    Does the deleting from the list
    :param begin: the beginning of the "for" index (type:int)
    :param end: the end of the "for" index (type:int)
    :param step: the step of the "for" index (type:int)
    :param expenses: the list of the expenses
    :param x_to_delete: the value we looking for to delete
    :param x: the element(day,money,category) that we are looking for so we can delete
    :return: Nothing
    '''
    if x == 'day':
        for i in range(begin, end, step):  # remove from list the dict
            if get_day(expenses[i]) == x_to_delete:
                expenses.pop(i)
    else:
        for i in range(begin, end, step):  # remove from list the dict
            if get_type(expenses[i]) == x_to_delete:
                expenses.pop(i)


def modify_expenses(expenses, command_param):
    '''
    It modifies the expenses. For:
    - p=1 : remove <day>
    - p=2 : remove <start day> to <end day>
    - p=3 : remove <category>
    :param expenses: list of expenses (type: list)
    :param command_param: parameters (type: list)
    :return: Nothing
    '''
    p = m_what_command(command_param)
    if p == 1:
        # remove < day >
        day_to_delete = int(command_param[0])  # what day to remove
        remove(len(expenses)-1, -1, -1, expenses, day_to_delete, 'day')  # do the removing

    elif p == 2:
        # remove <start day> to <end day>
        from_day = int(command_param[0])  # from what day
        to_day = int(command_param[2])  # until that day
        for day_to_delete in range(from_day, to_day+1):
            remove(len(expenses)-1, -1, -1, expenses, day_to_delete, 'day')  # do the removing

    elif p == 3:
        # remove <category>
        category_to_delete = command_param[0]
        remove(len(expenses)-1, -1, -1, expenses, category_to_delete, 'category')  # do the removing


def d_what_command(command_param):
    '''
    -We check if the parameters for the display functions are correct.
    -If they are, we find out what command the user wants (from the 5 available commands)
    :param command_param: list of parameters (type: list)
    :return: the number of the command (type: int)
    '''
    if len(command_param) == 0:
        return 1
    if len(command_param) == 1 and check_type(command_param[0]) == 'string':
        return 2
    if len(command_param) == 3 and check_type(command_param[0]) == 'string' and\
            check_type(command_param[2]) == 'natural':
        if command_param[1] == '<':
            return 3
        elif command_param[1] == '=':
            return 4
        elif command_param[1] == '>':
            return 5
        else:
            raise ValueError("Choose from <,=,>")
    else:
        raise ValueError("Wrong input! See the available options:"
                         "\n\tlist\n\tlist <category>"
                         "\n\tlist <category> [ < | = | > ] <value>")

# ---- display function ----


def display_by_days(expenses):
    '''
    We display the expenses ordered by the day
    :param expenses: list of expenses (type: list)
    :return: Nothing
    '''
    expenses2 = []
    for i in range(1, 31):
        day_print = False  # if the day was not printed
        for j in range(len(expenses)):
            if get_day(expenses[j]) == i:
                if not day_print:
                    expenses2.append(expenses[j])
    display_by_days2(expenses2)


def display_by_category(category, expenses):
    '''
    We display the expenses ordered by the category
    :param expenses: list of expenses (type: list)
    :param category: the category we are looking for (type: string)
    :return: Nothing
    '''
    expenses2 = []
    exists = False
    for i in range(1, 31):
        for j in range(len(expenses)):
            if get_day(expenses[j]) == i and get_type(expenses[j]) == category:
                expenses2.append(expenses[j])
                exists = True

    if not exists:
        display_none()
    else:
        display_by_category2(expenses2)


def display_by_category_compare(category, value, expenses, p):
    '''
    We display the expenses ordered by the category
    :param expenses: list of expenses (type: list)
    :param value: the value we use to compare
    :param category: the category we are looking for (type: string)
    :param p: - for p=3 -> we use '<'
              - for p=4 -> we use '='
              - for p=5 -> we use '>'
    :return: Nothing
    '''
    expenses2 = []
    exists = False

    for i in range(1, 31):
        for j in range(len(expenses)):
            if get_day(expenses[j]) == i and get_type(expenses[j]) == category:
                if p == 3 and get_money(expenses[j]) < int(value):
                    expenses2.append(expenses[j])
                    exists = True
                elif p == 4 and get_money(expenses[j]) == int(value):
                    expenses2.append(expenses[j])
                    exists = True
                elif p == 5 and get_money(expenses[j]) > int(value):
                    expenses2.append(expenses[j])
                    exists = True

    if not exists:
        display_none2(p, category, value)
    else:
        display_by_category_compare2(expenses2, p, category, value)


def display_expenses(expenses, command_param):
    '''
    Displays what you asked based on the input
    p1: list
    p2: list <category>
    [ p3 | p4 | p5 ]: list <category> [ < | = | > ] <value>
    :param expenses: list of expenses (type: list)
    :param command_param: list of parameters (type: list)
    :return: Nothing
    '''
    p = d_what_command(command_param)
    if p == 1:
        display_by_days(expenses)
    elif p == 2:
        display_by_category(command_param[0], expenses)
    else:
        display_by_category_compare(command_param[0], command_param[2], expenses, p)


# ---- other ---
def split_command(command):
    '''
    It splits the command into multiple words and it transforms them into lower cases
    :param command: what it was inserted (type: string)
    :return: the command word and parameters (type: string and list)
    '''
    tokens = command.strip().split()
    command_word = tokens[0].lower()
    command_param = []
    for i in range(len(tokens)-1):
        command_param.append(tokens[i+1].lower())
    return command_word, command_param


def test_init(expenses_list):
    '''
    Include at least 10 items in the application at startup
    :param expenses_list: the list of expenses (type: list)
    :return: Nothing
    '''
    expenses_list.append(create_expense(3, 100, 'internet'))
    expenses_list.append(create_expense(3, 50, 'others'))
    expenses_list.append(create_expense(4, 50, 'others'))
    expenses_list.append(create_expense(10, 50, 'others'))
    expenses_list.append(create_expense(20, 1000, 'housekeeping'))
    expenses_list.append(create_expense(5, 44, 'transport'))
    expenses_list.append(create_expense(7, 350, 'clothing'))
    expenses_list.append(create_expense(4, 50, 'food'))
    expenses_list.append(create_expense(10, 50, 'food'))
    expenses_list.append(create_expense(20, 500, 'transport'))


def test_create_expense():
    '''
    We test the create function
    :return:
    '''
    try:
        create_expense(-3, 67, 'food')
        assert False
    except ValueError:
        pass

    try:
        create_expense(4.5, 67, 'food')
        assert False
    except ValueError:
        pass

    try:
        create_expense(35, 67, 'food')
        assert False
    except ValueError:
        pass

    try:
        create_expense(20, 55, 'greh')
        assert False
    except ValueError:
        pass


def test_modify(expenses):
    '''
    We test the modify function
    :param expenses:
    :return:
    '''
    try:
        modify_expenses(expenses, [-3, 'to',10])
        assert False
    except ValueError:
        pass

    try:
        modify_expenses(expenses, [3, 'to',10])
        assert True
    except ValueError:
        pass


def test_display(expenses):
    # ---- display_expenses(expenses, ['food']) ----
    list_expected1 = [{'day': 4, 'amount_of_money': 50, 'expense_type': 'food'}, {'day': 10, 'amount_of_money': 50, 'expense_type': 'food'}]
    actual_expenses1 = []
    for i in range(1, 31):
        for j in range(len(expenses)):
            if get_day(expenses[j]) == i and get_type(expenses[j]) == 'food':
                actual_expenses1.append(expenses[j])
    assert list_expected1 == actual_expenses1

    # ---- display_expenses(expenses, ['others', '=' , 50]) ----
    list_expected2 = [{'day': 3, 'amount_of_money': 50, 'expense_type': 'others'}, {'day': 4, 'amount_of_money': 50, 'expense_type': 'others'},
                      {'day': 10, 'amount_of_money': 50, 'expense_type': 'others'}]
    actual_expenses2 = []
    for i in range(1, 31):
        for j in range(len(expenses)):
            if get_day(expenses[j]) == i and get_type(expenses[j]) == 'others':
                if get_money(expenses[j]) == 50:
                    actual_expenses2.append(expenses[j])
    assert list_expected2 == actual_expenses2




if __name__ == '__main__':
    print_menu()
    expenses = []
    test_init(expenses)
    #test_create_expense()
    #test_modify(expenses)
    test_display(expenses)
    command_dict = {'add': add_new_expense, 'insert': insert_new_expense,
                    'remove': modify_expenses, 'list': display_expenses}
    done = False

    while not done:
        command = input('\ncommand> ')
        command_word, command_param = split_command(command)

        if command_word in command_dict:
            try:
                command_dict[command_word](expenses, command_param)
            except ValueError as val_error:
                print_error(val_error)
        elif command_word == 'exit':
            done = True
            print_goodbye()
        else:
            print_bad_command()
