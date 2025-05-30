import os

import runpod
from utils import JobInput
from engine import OllamaEngine

async def handler(job: any):
    # Just dump the whole input to the console and then return an {"ok": True} response
    print('Job:', job)

    job_input = JobInput(job["input"])

    engine = OllamaEngine()  # Instantiate the engine

    return await engine.generate(job_input)  # Call generate with job_input

def adjust_concurrency(current_concurrency):
    return int(os.getenv("OLLAMA_NUM_PARALLEL", 1))

runpod.serverless.start(
    {
        "handler": handler,
        "return_aggregate_stream": True,
        "concurrency_modifier": adjust_concurrency,
    }
)
