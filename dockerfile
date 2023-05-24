# Use the official MariaDB image as base
FROM mariadb:latest

# Environment variables for the MariaDB server
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=myDatabase
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=root

# Expose the MySQL/MariaDB port
EXPOSE 3306

# Initialize the database
#COPY ./scripts/ 

# Start the MariaDB server
CMD ["mysqld"]