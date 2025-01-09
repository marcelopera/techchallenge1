class ValidationError(Exception):
    pass

class OptOutOfBounds(ValidationError):
    def __init__(self):
        super().__init__("Option must be between 2 and 6")

class SubOptOutOfBounds(ValidationError):
    def __init__(self):
        super().__init__("Sub-option is out of valid range for this option")

class YearOutOfBounds(ValidationError):
    def __init__(self):
        super().__init__("Year must be between 1970 and 2023")

def valida_entrada(opt: int, sub_opt: int, year: int):
    """
    Validates input parameters for Embrapa data queries.
    
    Args:
        opt: Main option (2-6)
        sub_opt: Sub option (varies based on main option)
        year: Year between 1970-2023
        
    Raises:
        OptOutOfBounds: If main option is invalid
        SubOptOutOfBounds: If sub-option is invalid for the given main option
        YearOutOfBounds: If year is outside valid range
    """
    if opt not in [2, 3, 4, 5, 6]:
        raise OptOutOfBounds()

    if opt in [2, 4] and sub_opt != 1:
        raise SubOptOutOfBounds()

    if opt in [3, 6] and sub_opt not in [1, 2, 3, 4]:
        raise SubOptOutOfBounds()

    if opt == 5 and sub_opt not in [1, 2, 3, 4, 5]:
        raise SubOptOutOfBounds()

    if year > 2023 or year < 1970:
        raise YearOutOfBounds()