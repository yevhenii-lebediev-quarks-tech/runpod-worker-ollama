# Runpod serverless runner for ollama

## How to use

Start a runpod serverless with the docker container ``svenbrnn/runpod-ollama:0.5.7``. Set ``MODEL_NAME`` environment to a model from ollama.com to automatically download a model.
A mounted volume will be automatically used.

## Environment variables

| Variable Name | Description                              | Default Value       |
|---------------|------------------------------------------|---------------------|
| `MODEL_NAME`  | The name of the model to download        | NULL                |

## Test requests for runpod.io console

See the [test_inputs](./test_inputs) directory for example test requests. 


## Streaming

Streaming for openai requests are fully working.

## Licence

This project is licensed under the Creative Commons Attribution 4.0 International License. You are free to use, share, and adapt the material for any purpose, even commercially, under the following terms:

- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **Reference**: You must reference the original repository at [https://github.com/svenbrnn/runpod-ollama](https://github.com/svenbrnn/runpod-ollama).

For more details, see the [license](https://creativecommons.org/licenses/by/4.0/).