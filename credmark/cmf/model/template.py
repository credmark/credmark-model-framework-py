from credmark.cmf.model import Model
from credmark.dto import EmptyInput

# Next Steps:

# Set the slug, display_name, and description for your model below.
# Add code to the run() method.


@Model.describe(slug='contrib.my-model',
                version='1.0',
                display_name='My Model',
                description="Description of the model.",
                input=EmptyInput,
                output=dict)
class ContribModel(Model):
    """
    If the description is not set in the decorator above,
    this doc string is used as the model description.
    """

    def run(self, input: EmptyInput) -> dict:

        # Add your model code here.

        # Access utilities with self.context
        # Log using self.logger

        # Input:
        # If you require input, use an existing DTO class or
        # create your own and set the class as the "input" arg
        # in the decorator and set the "input" arg type in this function.

        # Output:
        # It is recommended to use an existing DTO class or
        # create your own to use as the model output (return value.)
        # Set the "output" arg in the decorator and the return type
        # of this function. Then change this function to return an
        # instance of the DTO class.

        return {}
