FROM maven:3.8.4-openjdk-17 AS build
WORKDIR /app
COPY . . 
RUN mvn clean package -DskipTests

FROM openjdk:17-jdk-slim
WORKDIR /app
COPY --from=build /app/target/art_gal-0.0.1-SNAPSHOT.war art_gal.war
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "art_gal.war"]
