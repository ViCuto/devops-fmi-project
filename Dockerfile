FROM python:3.14-slim

# Create a non-root user for security purposes
RUN useradd -m appuser

WORKDIR /app

# Copy dependencies first (cache optimization)
COPY src/requirements.txt .

# Install dependencies without cache to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ .

# Change ownership of the files to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]