from typing import List, Union

from credmark.cmf.model.errors import ModelRunError


class InvalidColumnException(ModelRunError):
    def __init__(self,
                 model_slug: str,
                 column: str,
                 column_list: Union[List[str], None],
                 message: str):
        self.model_slug = model_slug
        self.name = column
        self.column_list = column_list
        super().__init__(message)

    def __str__(self):
        return f'Column {self.name} not a valid column for {self.model_slug}. ' \
            f' It must be in: {self.column_list}'


class InvalidQueryException(ModelRunError):
    def __init__(self, model_slug: str, message: str):
        self.model_slug = model_slug
        super().__init__(message)
