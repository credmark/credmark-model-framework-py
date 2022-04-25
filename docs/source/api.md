# Credmark API

The Credmark Framework provides access to remote models and access to on-chain data via [Credmark API](https://gateway.credmark.com/api/).

## Interactive HTTP requests

If you go to the popup in the top right of the window you can now choose between the different model groups:

- [Credmark Models](https://gateway.credmark.com/api/?urls.primaryName=Credmark%20Models)
- [Utility Models](https://gateway.credmark.com/api/?urls.primaryName=Utility%20Models)
- [Contributor Models](https://gateway.credmark.com/api/?urls.primaryName=Contributor%20Models)
- [Example Models](https://gateway.credmark.com/api/?urls.primaryName=Example%20Models)

For each group, you will get the docs for all the models within the group and you are able to run them interactively. Note that not all models are fully documented yet.

## API client for consumers

For consumers of the API there exists a separate Credmark Client that includes a command-line tool and a SDK. The focus of this tool is for developing client-side apps and it is not needed for writing models.


### Install
```
$ pip install credmark-client
```

### Configuration

An API key can be set in the environment variable ``CREDMARK_API_KEY``.

For example:
```
export CREDMARK_API_KEY=cmk-api-key-v1.YXVkOmZwaS5JcmVkbWFyay5jb20Kc2NvcGU6YWNjZXNzCm5mdDoxCmV4cDoxNjM2OTQ1ODI5MTY2.0xFCAd0B19bB29D4674531d6f115237E16AfCE377c.0x42971132bd11b2d8c4ca47e831e4e8f46d2b4eca1e1b6a6e5356293e3f8a7de759d8fb3ab4d2f51455942f796ac79bf7240d54bf2df3c4453e4d9432aaee519abc
```

### CLI Usage

This package includes a command-line tool ``credmark``.
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
credmark run example.echo
```

```
{"slug": "example.echo", "version": "1.0", "output": {"message": "Hello"}, "dependencies": {"example.echo": {"1.0": 1}}, "runtime": 3418}
```


### SDK Usage


Create a client and call methods for API calls.

To run a model:

```
    try:
        client = CredmarkClient()

        result = client.run_model('example.echo')

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

        result = client.run_model('example.echo', raise_error_results=True)

        print(result['output'])

    except ModelBaseError as err:
        # model error
        print('Model Error:', str(err), err.data)

    except Exception as err:
        # requests/urllib exception
        print('Exception', str(err))
```
