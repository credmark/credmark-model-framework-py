# Create a Model

A model is simply a decorated class that inherits from {class}`credmark.cmf.model.Model` and implements a `run()` method that takes an input and returns an output.

Create a new class as a subclass of {class}`credmark.cmf.model.Model` and then decorate it with the `@Model.describe` decorator:

```python
@Model.describe(slug='contrib.hello-world',
                version='1.0',
                display_name='Hello World',
                description="A test model to say hi.",
                developer='Credmark',
                input=EmptyInput,
                output=dict)
class HelloModel(Model):
    def run(self, input: EmptyInput) -> dict:
        return {'message': 'Hello world!'}
```

From your model's `run()` method, you can access `self.context` which gives you access to the context chain id, block number, a configured web3 instance, ledger data access, the ability to call other models, and more. See {class}`credmark.cmf.model.context.ModelContext` for more details.

Here is more info on the {class}`credmark.cmf.model.Model` class:

```{eval-rst}
.. autoclass:: credmark.cmf.model.Model
   :members:
   :noindex:
```
