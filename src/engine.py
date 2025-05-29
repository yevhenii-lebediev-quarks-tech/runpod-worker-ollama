import json
import os

from dotenv import load_dotenv
from ollama import Client
from utils import JobInput

client = Client(
    host='http://localhost:11434',
)


class OllamaEngine:
    def __init__(self):
        load_dotenv()

        print("OllamaEngine initialized")

    def generate(self, job_input: JobInput):
        # Get model from MODEL_NAME defauting to llama3.2:1b
        model = os.getenv("MODEL_NAME", "gemma3:1b")

        # Depending if prompt is a string or a list, we need to handle it differently and send it to the OpenAI API
        if job_input.prompt:
            response = client.generate(
                model=model,
                prompt=job_input.prompt,
                system=job_input.system,
                stream=job_input.stream,
                format=job_input.format,
            )
        else:
            # Buid new JobInput object with the OpenAI route and input
            response = client.chat(
                model=model,
                messages=job_input.messages,
                stream=job_input.stream,
                format=job_input.format,
            )

        print("Generating response for job_input:", job_input)

        if not job_input.stream:
            return self._convert_response(not job_input.prompt, response)

        content = ""
        last_message = None

        for chunk in response:
            last_message = chunk

            if job_input.prompt:
                content += chunk.response
            else:
                content += chunk.message.content

        if job_input.prompt:
            last_message.response = content
        else:
            last_message.message.content = content

        return self._convert_response(not job_input.prompt, last_message)

    @staticmethod
    def _convert_response(is_chat, response):
        result = {
            "model": response.model,
            "created_at": response.created_at,
            "done": response.done,
            "done_reason": response.done_reason,
            "total_duration": response.total_duration,
            "load_duration": response.load_duration,
            "prompt_eval_count": response.prompt_eval_count,
            "prompt_eval_duration": response.prompt_eval_duration,
            "eval_count": response.eval_count,
            "eval_duration": response.eval_duration,
        }

        if not is_chat:
            result["response"] = response.response
        else:
            result["message"] = {
                "content": response.message.content,
                "role": response.message.role,
                "images": response.message.images or [],
            }

        return result