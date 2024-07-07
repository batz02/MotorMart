### Avvio del programma

- Avere sul proprio pc installato Python3 e PipEnv
- Posizionandosi nella cartella del progetto dove è presente il file `Pipfile` avviare la shell di PipEnv tramite il comando:
    ```
    pipenv shell
    ```  
- Entrando nella cartella `/MotorMart` dove è presente il file `manage.py` usare i seguenti comandi per creare e migrare le tabelle:
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
- Successivamente è possibile creare un utente admin con permessi completi per loggarsi e gestire alcuni aspetti dell'applicazione, come l'accesso al database, con il comando 
    ```
    python3 manage.py createsuperuser
    ```
    e successivamente inserendo le informazioni richieste
- Infine è possibile utilizzare l'applicazione eseguendo
    ```
    python3 manage.py runserver
    ```
    entrando nell'apposito url: `http://127.0.0.1:8000/`
