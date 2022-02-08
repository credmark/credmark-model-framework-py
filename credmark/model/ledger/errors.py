from typing import Union, List


class InvalidColumnException(Exception):
    def __init__(self, column: str, column_list: Union[List[str], None], message: str):
        self.name = column
        self.column_list = column_list
        super().__init__(message)

    def __str__(self):
        return f'Column {self.name} not a valid column. It must be in: {self.column_list}'
