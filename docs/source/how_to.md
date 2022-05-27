# How To...

Check out how to create, run and submit a Model based on the Credmark Model Framework. Additionally, before submitting your final model, check our model guidelines and how to build a good model and create a good PR.

## Create a Model

A model is simply a decorated class that inherits from {class}`credmark.cmf.model.Model` and implements a `run()` method that takes an input and returns an output.

To get started, you can use the {doc}`credmark_dev` command to create a new model skeleton python file using something like:

```
credmark-dev create my_models hello_world
```

This will create a model in the folder `models/contrib/my_models/hello_world.py`.

In the command above you can replace `my_models` with your username or a unique folder name for your models and replace `hello_world` with the name you wish to use for the file.

The skeleton file will contain a subclass of {class}`credmark.cmf.model.Model` decorated with the {meth}`credmark.cmf.model.Model.describe` decorator `@Model.describe`, something like the following example:

```python
from credmark.cmf.model import Model, EmptyInput

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

## Model Guidelines

What makes a good model? In general, good Models Should be:

- Generalized
- Short
- Legible
- Strict

**NOTICE:** These checks either **ARE** or **WILL** be added as automated Checks on PRs.

Here’s a [passing test](https://github.com/credmark/credmark-models-py/runs/5975564564?check_suite_focus=true) on github: ✅

Here’s a [failing test](https://github.com/credmark/credmark-models-py/runs/5844626780?check_suite_focus=true) on github: ❌

### The Good Model Checklist

**Check your model.describe() decorator**

- [ ] Increment the Version Number when you update your model
- [ ] The Slug is Unique
- [ ] The Slug is correctly Namespaced
- [ ] The Display Name is descriptive but not too long
- [ ] The Description describes what the model does
- [ ] The DTOs describe the Inputs and Outputs schemas

**Check the model’s content**

- [ ] It does one thing, and it does it well
- [ ] It conforms to it’s type definition
- [ ] Does the client have the ability to ask for what they want?
- [ ] Do you set good default inputs?
- [ ] Don’t make historical calls within models unless absolutely necessary.

**Check the code**

- [ ] It raises ModelDataError instead of returning None or 0
- [ ] It returns a DTO, and uses a framework DTO if it exists.
- [ ] It doesn’t have any print() statements.
- [ ] It passes linting tests.
- [ ] There are no global functions that aren’t models.

**Check the legibility**

- [ ] It is a minimal number of lines of code to get the job done
- [ ] It uses descriptive variable names

**Check for repetition**

- [ ] It calls other models if they exist
- [ ] It uses the framework tools if they exist

**Check that your actions are allowed on your model type:**

|                                          | Calls Contract Functions | Calls Database |    Calls other Models    | Has hard-coded Data | Transforms Input Data |
| ---------------------------------------- | :----------------------: | :------------: | :----------------------: | :-----------------: | :-------------------: |
| Models that fetches data                 |            ✅            |       ✅       |            ⚠️            |         ❌          |          ❌           |
| Algorithmic models                       |            ❌            |       ❌       | ⚠️ only other algorithms |         ❌          |          ✅           |
| Models that stitch together other models |            ❌            |       ❌       |            ✅            |         ❌          |          ❌           |
| Models that have hardcoded configuration |            ❌            |       ❌       |            ❌            |         ✅          |          ❌           |

### The Good PR Checklist

- [ ] It has no merge conflicts
- [ ] It doesn’t break other models
- [ ] It builds and runs
- [ ] It passes github tests
  - Pylint settings: https://github.com/credmark/credmark-models-py/blob/main/.pylintrc
  - At the command-line, run: pylint models
- [ ] It is under the maximum PR size:
  - 2 files changed
  - 4 models changed
  - 200 lines of code changed
- [ ] For each model
  - Does it pass the checklist
- [ ] For each DTO
  - Does it already exist in the Framework?
  - Is it materially different from the existing DTOs

## Bugs, Issues, and Support

The Credmark Model Framework is under active development, thus there will be some bugs or issues that may cause problems.

We encourage all modelers to join our [Discord](https://discord.com/invite/3dSfMqP3d4), pick the role "Engineering" and post any issues the in the channel [#framework-help](https://discord.com/channels/827615638540910622/965655586513485835). The Discord shall be the place to ask general questions about how to do something or if you have data-related questions.

If you want to report a bug, unexpected behavior, or feature request, you can raise an issue in Github directly but we encourage you in this case as well to notify the community in Discord.
