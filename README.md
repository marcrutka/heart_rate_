# Heart Rate Monitoring Application

The application monitors the user's heart rate, analyzes the data, and generates reports on trends and potential health risks.

## Prerequisites
1. Install **Docker Desktop** (https://www.docker.com/products/docker-desktop).
2. Install **Python** version 3.8+ and the modules listed in `requirements.txt`.

## How to run the application?

### 1. Set up the environment
1. Download the project and navigate to the folder:
   ```bash
   cd ~\Heartrate
   ```
2. Run `docker-compose`:
   ```bash
   docker compose up
   ```
3. Build the image from the Dockerfile:
   ```bash
   docker build -t heartrate_image -f Dockerfile.dockerfile .
   ```
4. Check the running containers:
   ```bash
   docker ps
   ```
   You should see a container with three images.

### 2. Running the scripts
1. Run the **producer**:
   ```bash
   python producer.py
   ```
   If everything works correctly, you should see the message:
   ```
   Already working
   ```
2. Run the **consumer**:
   ```bash
   python consumer.py
   ```
   The terminal should display messages about receiving signals regarding the measured heart rate every 2 seconds.

### 3. Generating reports
- Every 20 signals, the program will automatically generate a report in an Excel file. The report contains analysis of trends, z-score, and potential health risks.

## Troubleshooting
1. If an error occurs in `producer.py` or `consumer.py`, stop the program by pressing `Ctrl + C`.
2. Then create the Kafka topic with the following command:
   ```bash
   kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic heartrate
   ```
3. Restart the application by entering the appropriate commands.

## Notes
- All logs and data will be saved in real-time in the relevant project files.
- If you have any further questions, please contact the project author.
