from abc import abstractmethod
import logging
from .context import ModelContext


class Model:
    """
    The base model class.

    Models should subclass this class and override the
    run() method. They may also override init().

    Available instance variables:

    slug - model slug
    version - model version
    logger - a logger for messages related to the model

    """

    # If loading with a model manifest file, these class
    # variables will be set automatically by the loader.
    slug: str
    version: str
    _manifest: dict

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
    def run(self, input) -> dict:
        """Subclasses must override this method to run
        the model.

        Model instances may be reused if the context does not change
        so keep in mind that run() may be called multiple times.
        """
