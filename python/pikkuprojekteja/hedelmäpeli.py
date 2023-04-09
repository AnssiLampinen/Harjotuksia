import random
ROW_QUANTITY = 5
COLUMN_QUANTITY = 5

symbol_count = {"A": 2, "B": 4, "C": 8, "D":16}
symbol_multipliers = {"A": {1: 0, 2: 0, 3: 2, 4: 4, 5: 8}, "B": {1: 0, 2: 0, 3: 2, 4: 4, 5: 8}, 
                      "C": {1: 0, 2: 0, 3: 2, 4: 4, 5: 8}, "D": {1: 0, 2: 0, 3: 2, 4: 4, 5: 8}}
symbol_list = [] 

def dictionary_to_list(dict_to_convert: dict):
    """
    Converts dictionary of keys and multipliers to list with the multipliers amount of keys.
    {A: 1, B: 2, C: 3} -> [A, B, B, C, C, C]
    """
    output_list = []
    for i in range(0, len(dict_to_convert)):
        values = list(dict_to_convert.values()) # List of values
        keys = list(dict_to_convert.keys()) # List of keys
        for _ in range(0, values[i]):
            output_list.append(keys[i])
    return output_list
 


def get_column():
    """
    Outputs single column with ROW_QUANTITY amount of symbols.
    """
    symbol_list = dictionary_to_list(symbol_count)
    column = []
    symbols = symbol_list.copy()
    for _ in range(ROW_QUANTITY):
        symbol = symbols[random.randint(0, len(symbols)-1)]
        column.append(symbol)
        symbols.remove(symbol)
    return column


def get_all_columns():
    """
    Outpust list containing COLUMN_QUANTITY amount of columns (lists).
    """
    all_columns = []
    for _ in range(COLUMN_QUANTITY):
        all_columns.append(get_column())
    return all_columns


columns = get_all_columns()





def get_line_symbol(row_index):
    """
    Outputs symbols for row, 1 from every column.
    """
    for i in range(COLUMN_QUANTITY):
        yield columns[row_index][i] # Palauttaa symbolit 1 kerrallaan



def line_symbols(line_index):
    """
    Creates a list of the symbols contained by specific lane. Lanes can be horizontal or from corner to corner.
    """
    if line_index in range(ROW_QUANTITY): # suorat rivit
        line = [x for x in get_line_symbol(line_index)]
    # elif line_number == ROW_QUANTITY + 1: # vasen ala - oikea ylä

    # elif line_number == ROW_QUANTITY + 2: # asen ylä - oikea ala
    return line
        
line1 = line_symbols(0)

['C', 'D', 'D', 'D', 'B']

def lane_multiplier(line_index):
    """
    Returns the multiplier for specific lane.
    """
    line = line_symbols(line_index)
    symbol = line[0]
    current_symbol = line[0]
    count = -1
    i = -1
    while current_symbol == symbol:
        count += 1
        i += 1
        if i > len(line)-1:
            break
        else:
            current_symbol = line[i]
    multiplier = symbol_multipliers[symbol][count]
    return multiplier



def print_grid():
    """
    Prints out the grid of symbols and multipliers for every lane.
    """
    for i in range(ROW_QUANTITY):
        for j in range(COLUMN_QUANTITY):
            print(columns[i][j], end = " ")
        print("Multiplier: " + str(lane_multiplier(i)))

print_grid()