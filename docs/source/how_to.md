# How To...
Check out how to create, run and submit a Model based on the Credmark Model Framework.

## Create a Model

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

## Run a Model

To see a list of all models available, use the command:

```
credmark-dev list
```

You can then pick a model name (slug) and run the model by using the command:

```
credmark-dev run <Specify Slug> -b <Specify block number>  -i <Specify Input>
```

so for example

```
credmark-dev run cmk.circulating-supply -b 14000000  -i “{}”
```

Tip: you can run the command

```
credmark-dev list --manifests
```

to see the input data format required for each model. It will also show the output formats.


## Submit a Model

If you are a contributor external to credmark, you should create your folder in [credmark-models-py/models/contrib].

You should create and keep your models under this folder. Note that we have applied additional conditions for model slug names under this folder. Slug name must start with `contrib.<model-name>`, so for example: `Slug = ‘contrib.sample-model`.

If you are a contributor external to credmark, you should create your folder in [credmark-models-py/models/contrib].

You should create and keep your models under this folder. Note that we have applied additional conditions for model slug names under this folder. Slug name must start with `contrib.<model-name>`, so for example: `Slug = ‘contrib.sample-model`.

Once your model is ready to submit, simply create a pull request on the github repo and let us know in our [Discord](https://discord.com/invite/BJbYSRDdtr).
