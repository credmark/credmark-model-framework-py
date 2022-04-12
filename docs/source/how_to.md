# Run a Model

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


# Submit a Model

If you are a contributor external to credmark, you should create your folder in [credmark-models-py/models/contrib].

You should create and keep your models under this folder. Note that we have applied additional conditions for model slug names under this folder. Slug name must start with `contrib.<model-name>`, so for example: `Slug = ‘contrib.sample-model`.

If you are a contributor external to credmark, you should create your folder in [credmark-models-py/models/contrib].

You should create and keep your models under this folder. Note that we have applied additional conditions for model slug names under this folder. Slug name must start with `contrib.<model-name>`, so for example: `Slug = ‘contrib.sample-model`.

Once your model is ready to submit, simply create a pull request on the github repo and let us know in our [Discord](https://discord.com/invite/BJbYSRDdtr).
