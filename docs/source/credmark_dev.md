# CLI credmark-dev

`credmark-dev` is a command-line tool installed with the `credmark-model-framework`. It can be used to list, run, and get docs for models.

## `help` command

```
$ credmark-dev --help

usage: credmark-dev [-h] [--log_level LOG_LEVEL] [--model_path MODEL_PATH]
                    [--manifest_file MANIFEST_FILE]
                    {version,list,list-models,models,deployed-models,describe,describe-models,man,run,run-model,build,build-manifest,clean,remove-manifest}
                    ...

Credmark developer tool

optional arguments:
  -h, --help            show this help message and exit
  --log_level LOG_LEVEL
                        Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
  --model_path MODEL_PATH
                        Semicolon separated paths to the model folders (or parent) or model
                        python file. Defaults to models folder.
  --manifest_file MANIFEST_FILE
                        Name of the built manifest file. Defaults to models.json. [Not
                        required during development]

Commands:
  Supported commands

  {version,list,list-models,models,deployed-models,describe,describe-models,man,run,run-model,build,build-manifest,clean,remove-manifest}
                        additional help
    version             Show version of the framework
    list (list-models)  List models in this repo
    models (deployed-models)
                        List models deployed on server
    describe (describe-models, man)
                        Show documentation for local and deployed models
    run (run-model)     Run a model
    build (build-manifest)
                        Build model manifest [Not required during development]
    clean (remove-manifest)
                        Clean model manifest
```

## `run` command

Below -h command shows the details of options available for run commands.

```
$ credmark-dev run -h

usage: credmark-dev run [-h] [-b BLOCK_NUMBER] [-c CHAIN_ID] [-i INPUT] [-v MODEL_VERSION]
                        [-j] [-l USE_LOCAL_MODELS] [--provider_url_map PROVIDER_URL_MAP]
                        [--api_url API_URL]
                        model-slug

positional arguments:
  model-slug            Slug for the model to run.

optional arguments:
  -h, --help            show this help message and exit
  -b BLOCK_NUMBER, --block_number BLOCK_NUMBER
                        Block number used for the context of the model run. If not
                        specified, it is set to the latest block of the chain.
  -c CHAIN_ID, --chain_id CHAIN_ID
                        Chain ID. Defaults to 1.
  -i INPUT, --input INPUT
                        Input JSON or if value is "-" it will read input JSON from stdin.
  -v MODEL_VERSION, --model_version MODEL_VERSION
                        Version of the model to run. Defaults to latest.
  -j, --format_json     Format output json to be more readable
  -l USE_LOCAL_MODELS, --use_local_models USE_LOCAL_MODELS
                        Comma-separated list of model slugs for models that should favor
                        use of the local version. This is only required when a model is
                        calling another model.
  --provider_url_map PROVIDER_URL_MAP
                        JSON object of chain id to Web3 provider HTTP URL. Overrides
                        settings in env vars.
  --api_url API_URL     Credmark API url. Defaults to the standard API
                        gateway. You do not normally need to set this.
```

To call any model we can specify the output by providing below parameters (they're not necessarily required):

- `-b` or `–block_number` : to define against which block number the model should run. If not specified, it uses the "latest" block from our ledger db.
- `-i` or `–input` : to provide input for a model in a predefined structure.(you can run command `credmark-dev list --manifests` to see the input format required for each model. See example below). If not provided it will default to “{}”.
  Model-slug: Name of the model (slug) to call the model.

Note: if chain ID is not mentioned explicitly in the parameter, it defaults to 1. If the model is using web 3 instance then chain id (and blockchain) will be picked from the .env file we defined during setup (refer to “configure environment variable” section). If the model is using Credmark database then, by default, it will refer to the Ethereum blockchain.

See the example below. Here, we are running the model “cmk.circulating-supply” at block_number 14000000.

```
$ credmark-dev run -b 14000000 cmk.circulating-supply -i "{}"

{"slug": "cmk.circulating-supply", "version": "1.0", "output": {"result": 28314402605762084044696668}, "dependencies": {"cmk.total-supply": {"1.0": 1}, "cmk.circulating-supply": {"1.0": 1}}}
```

## `list` command

Below `-h` command shows the details of options available for list commands.

```
$ credmark-dev list -h

usage: credmark-dev list [-h] [--manifests] [--json]

optional arguments:
  -h, --help   show this help message and exit
  --manifests
  --json
```

Note: You can also run `list-models` command alternatively.

Example below shows simple output (list of all models and their version) of list command:

```
$ credmark-dev list

Loaded models:

 - var: ['1.0']
 - cmk.total-supply: ['1.0']
 - cmk.circulating-supply: ['1.0']
 - xcmk.total-supply: ['1.0']
[...]
```

You can also get the list result in different formats using `--json` or `--manifest`.

## `describe` command

The describe command shows details on one or more models.

```
credmark-dev describe [model-slug]
```

The model-slug can be a slug or slug prefix string.

For example:

```
$ credmark-dev describe example.echo

example.echo
 - slug: example.echo
 - version: 1.0
 - display_name: Echo
 - description: A test model to echo the message property sent in input.
 - developer: Credmark
 - tags: None
 - input schema (* for required field):
   EchoDto(EchoDto(*))
     └─message(string)
 - input example:
   #01: {"message": "string"}
 - output schema (* for required field):
   EchoDto(EchoDto(*))
     └─message(string)
 - output example:
   #01: {"message": "string"}
 - errors:
   No defined errors
 - class: models.examples.echo_example.EchoModel
```

## `version` command

The version command shows the current version of the `credmark-model-framework`:

```
$ credmark-dev version
credmark-model-framework version 0.0.0
```

**Note:** the commands `build` and `clean` do not need to be used during model development.
