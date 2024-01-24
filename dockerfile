# Use an official OpenJDK runtime as a parent image
FROM openjdk:11-jre-slim

# Set the working directory to /app
WORKDIR /app

# Copy the JAR file into the container at /app
COPY JMusicBot-X.Y.Z.jar /app/
COPY config.txt /app/

# Specify the command to run on container start
CMD ["java", "-Dnogui=true", "-jar", "JMusicBot-X.Y.Z.jar"]
