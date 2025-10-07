### Program Startup

- Have Python3 and PipEnv installed on your PC  
- Navigate to the project folder where the `Pipfile` is located and start the PipEnv shell using the command:  
    ```
    pipenv shell
    ```  
- Enter the `/MotorMart` folder where the `manage.py` file is located and use the following commands to create and migrate the tables:  
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```  
- Next, you can create an admin user with full permissions to log in and manage certain aspects of the application, such as database access, using the command:  
    ```
    python3 manage.py createsuperuser
    ```  
    and then enter the requested information  
- Finally, you can run the application by executing:  
    ```
    python3 manage.py runserver
    ```  
    and going to the URL: `http://127.0.0.1:8000/`
