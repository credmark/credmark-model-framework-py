from abc import abstractmethod
import logging
from typing import Type, Union

from credmark.model.errors import ModelDataError
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
    context - a model context instance
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
        """
        Subclasses may override this method to do
        any model instance initiation
        """

    @abstractmethod
    def run(self, input: Union[dict, DTO]) -> Union[dict, DTO]:
        """
        Subclasses must override this method to run
        the model.

        Model instances may be reused so keep in mind that run()
        may be called multiple times. If you are using global
        data structures, make sure they are reset or cleared
        after each model run.
        """

    def raise_data_error(self, message: str,
                         code: str = ModelDataError.ErrorCodes.GENERAL,
                         data: Union[dict, list, str, int, float, None] = None):
        """
        Raise a ModelDataError.

        Call this method during a model run to signify a deterministic,
        permanent error exists, based on the input, context,
        and blockchain data.

        For example:
        self.raise_data_error('Conflicting data in calculation',
                              ModelDataError.ErrorCodes.CONFLICT,
                              data)

        See ModelDataError for more details.

        See also convenience methods for common data errors:
            self.raise_no_data()
            self.raise_invalid_input()
        """
        ctxt = self.context
        raise ModelDataError(message, code, ctxt.chain_id,
                             ctxt.block_number, data)

    def raise_no_data(self,
                      message: str,
                      data: Union[dict, list, str, int, float, None] = None):
        """
        A convenience method to call raise_data_error() with
        ModelDataError.ErrorCodes.NO_DATA

        Example:
          self.raise_no_data('No contract at address')
        """
        self.raise_data_error(message, ModelDataError.ErrorCodes.NO_DATA, data)

    def raise_invalid_input(self,
                            message: str,
                            data: Union[dict, list, str, int, float, None] = None):
        """
        A convenience method to call raise_data_error() with
        ModelDataError.ErrorCodes.INVALID_INPUT

        Example:
          self.raise_invalid_input('Invalid interval string')
        """
        self.raise_data_error(message, ModelDataError.ErrorCodes.INVALID_INPUT, data)

    def convert_dict_to_dto(self,
                            data: dict,
                            dto_class: Type[DTO]):
        """
        A model can call this method to convert a dict
        of data in a known format into a DTO instance.
        """
        return transform_data_for_dto(data, dto_class, self.slug, 'transform')
