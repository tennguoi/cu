FROM maven:3.8.4-openjdk-17 AS build
WORKDIR /app
COPY . ./
RUN mvn clean package -DskipTests
# COPY src ./src
FROM openjdk:17-jdk-slim

COPY --from=build /app/target/art-gal-0.0.1-SNAPSHOT.war /app/art-gal.war
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "art-gal.war"]
