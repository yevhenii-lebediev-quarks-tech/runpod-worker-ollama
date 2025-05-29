class JobInput:
    def __init__(self, job):
        self.messages = job.get("messages")
        self.prompt = job.get("prompt")
        self.format = job.get("format")
        self.options = job.get("options")
        self.system = job.get("system")
        self.keep_alive = job.get("keep_alive", -1)
        self.stream = job.get("stream", False)