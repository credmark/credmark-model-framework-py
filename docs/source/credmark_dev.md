# CLI credmark-dev

`credmark-dev` is a command-line tool installed with the `credmark-model-framework`. It can be used to list, run, and get docs for models.

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
