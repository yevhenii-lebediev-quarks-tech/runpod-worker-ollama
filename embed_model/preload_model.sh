#!/bin/sh

# Start the Ollama server in the background
echo "Starting Ollama server to preload model: $MODEL_NAME"
ollama serve &

# Capture the PID of the Ollama server
OLLAMA_PID=$!

# Wait for the server to be ready (adjust if necessary)
echo "Waiting for Ollama server to start..."
sleep 5

# Pull the specified model
echo "Pulling model: $MODEL_NAME"
if ollama pull "$MODEL_NAME"; then
  echo "Successfully pulled model: $MODEL_NAME"
else
  echo "Failed to pull model: $MODEL_NAME"
  kill $OLLAMA_PID
  exit 1
fi

# Stop the Ollama server
echo "Stopping Ollama server..."
kill $OLLAMA_PID

# Wait for the server to terminate
wait $OLLAMA_PID

echo "Model preloading complete."
