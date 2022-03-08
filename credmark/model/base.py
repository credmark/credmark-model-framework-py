from abc import abstractmethod
import logging
from typing import Type, Union
from .context import ModelContext
from credmark.types.dto import DTO
from .transform import transform_data_for_dto


class Model:
    """
    The base model class.

    Models should subclass this class and override the
    run() method. They may also override init().

    Available instance variables:

    logger - a logger for messages related to the model
    """

    # These class variables will be set automatically by
    # the loader or decorator
    slug: str
    version: str
    _manifest: dict
    inputDTO: Union[Type[DTO], None]
    outputDTO: Union[Type[DTO], None]

    def __init__(self, context: ModelContext):
        self.context = context
        # Configure our logger.
        self.logger = logging.getLogger(
            'credmark.models.{0}'.format(self.slug))
        self.init()

    def init(self):
        """Subclasses may override this method to do
        any model instance initiation
        """

    @abstractmethod
    def run(self, input: Union[dict, DTO]) -> Union[dict, DTO]:
        """Subclasses must override this method to run
        the model.

        Model instances may be reused if the context does not change
        so keep in mind that run() may be called multiple times.
        """

    def convert_dict_to_dto(self,
                            data: dict,
                            dto_class: Type[DTO]):
        """
        A model can call this method to convert a dict
        of data in a known format into a DTO instance.
        """
        return transform_data_for_dto(data, dto_class, self.slug, 'transform')
