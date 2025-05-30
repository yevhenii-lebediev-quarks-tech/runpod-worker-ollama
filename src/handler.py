import runpod
from utils import JobInput
from engine import OllamaEngine

def handler(job: any):
    # Just dump the whole input to the console and then return an {"ok": True} response
    print('Job:', job)

    job_input = JobInput(job["input"])

    engine = OllamaEngine()  # Instantiate the engine

    return engine.generate(job_input)  # Call generate with job_input

runpod.serverless.start(
    {
        "handler": handler,
        "return_aggregate_stream": True,
    }
)
