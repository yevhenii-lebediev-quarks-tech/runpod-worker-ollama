FROM svenbrnn/runpod-ollama:0.5.7

ARG MODEL_NAME
ENV MODEL_NAME=$MODEL_NAME
ADD preload_model.sh /preload_model.sh
RUN chmod +x /preload_model.sh && /preload_model.sh

# Copy the model to the volume
FROM svenbrnn/runpod-ollama:0.5.7
COPY --from=0 /runpod-volume /runpod-volume