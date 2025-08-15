# Use official MySQL image
FROM mysql:8.0

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=Maroon5maps$
ENV MYSQL_DATABASE=loan_risk_db
ENV MYSQL_USER=loan_user
ENV MYSQL_PASSWORD=loan_password

# Copy SQL dump(s) into container
COPY loan_risk_db.sql /docker-entrypoint-initdb.d/
COPY loan_risk_db_prediction_record.sql /docker-entrypoint-initdb.d/

# Expose default MySQL port
EXPOSE 3306
