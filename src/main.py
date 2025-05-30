import runpod
from handler import handler, adjust_concurrency

runpod.serverless.start(
    {
        "handler": handler,
        "return_aggregate_stream": True,
        "concurrency_modifier": adjust_concurrency,
    }
)
