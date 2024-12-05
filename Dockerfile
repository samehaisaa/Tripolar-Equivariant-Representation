# Step 1: Use a Python base image
FROM python:3.11-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt to the working directory
COPY requirements.txt .

# Step 4: Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the entire project into the container
COPY . .

# Step 6: Expose the port (if your app needs to be accessed externally)
# EXPOSE 5000  # Uncomment if needed, for example, if using Flask or FastAPI

# Step 7: Run the main Python script as the default command
CMD ["python", "main.py"]
