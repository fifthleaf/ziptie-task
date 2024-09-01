from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    """
    Configuration settings for the database connection.

        Attributes:
            database_host: The hostname or IP to use for the connection.
            database_name: The name of the database to connect to.
            database_password: The password of the database user.
            database_port: The port number to use for the connection.
            database_user: The username to use for the connection.
    """

    database_host: str = "127.0.0.1"
    database_name: str = "school"
    database_password: str = "root"
    database_port: int = 3306
    database_user: str = "root"

    def get_url(self) -> str:
        """
        Returns the URL for the database connection.

            Returns:
                 A string representing the database connection URL.
        """
        return (
            f"mysql+pymysql://{self.database_user}:{self.database_password}@"
            f"{self.database_host}:{self.database_port}/{self.database_name}"
        )
