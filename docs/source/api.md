# Credmark API Client

For consumers of the API there exists a separate Credmark Client that includes a command-line tool and a SDK. The focus of this tool is for developing client-side apps and it is not needed for writing models.

### Install

```
$ pip install credmark-client
```

### Configuration

An API key can be set in the environment variable `CREDMARK_API_KEY`.

For example:

```
export CREDMARK_API_KEY=cmk-api-key-v1.YXVkOmZwaS5JcmVkbWFyay5jb20Kc2NvcGU6YWNjZXNzCm5mdDoxCmV4cDoxNjM2OTQ1ODI5MTY2.0xFCAd0B19bB29D4674531d6f115237E16AfCE377c.0x42971132bd11b2d8c4ca47e831e4e8f46d2b4eca1e1b6a6e5356293e3f8a7de759d8fb3ab4d2f51455942f796ac79bf7240d54bf2df3c4453e4d9432aaee519abc
```

### CLI Usage

This package includes a command-line tool `credmark`.

```
credmark --help
```

```
    usage: credmark [-h] [--log_level LOG_LEVEL] [--api_url API_URL]
                    {version,models,deployed-models,describe,describe-models,man,run,run-model} ...

    Credmark developer tool

    optional arguments:
    -h, --help            show this help message and exit
    --log_level LOG_LEVEL
                            Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    --api_url API_URL     Credmark API url. Defaults to the standard API gateway. You do not normally
                            need to set this.

    Commands:
    Supported commands

    {version,models,deployed-models,describe,describe-models,man,run,run-model}
                            additional help
        version             Show version of the package
        models (deployed-models)
                            List models deployed on server
        describe (describe-models, man)
                            Show documentation for models
        run (run-model)     Run a model
```

### Run a Model

```
credmark run cmk.total-supply
```

```
{"slug": "cmk.total-supply", "version": "1.0", "output": {"total_supply": 1e+26}, "dependencies": {"contract.metadata": {"1.0": 1}, "cmk.total-supply": {"1.0": 1}}, "runtime": 3108}
```

### SDK Usage

Create a client and call methods for API calls.

To run a model:

```

    try:
        client = CredmarkClient()

        result = client.run_model('cmk.total-supply')

        if 'output' in result:
            print(result['output'])
        else:
            # Model error
            print('Error', result['error'])

    except Exception as err:
        # requests/urllib exception
        print('Exception', str(err))

```

You can automatically raise model errors as exceptions:

```

    try:
        client = CredmarkClient()

        result = client.run_model('cmk.total-supply', raise_error_results=True)

        print(result['output'])

    except ModelBaseError as err:
        # model error
        print('Model Error:', str(err), err.data)

    except Exception as err:
        # requests/urllib exception
        print('Exception', str(err))

```
