# Citi Data Analytics Academy

## A Python Django API to retrieve and present Stock data

After running the following code in Visual Code you should be able to do the following.

* Launch a Python Web Server with the Django Framework
* Use the default Django SQLite database as a Database Server
* Download historic Stock Market data for the Shares you choose
* Display the downloaded Stock Market data as an API using your Django Web Server

---

### Requirements

* Microsoft Windows 10/11
* Visual Studio Code
* Python

### Getting setup

* Install Python on your computer, https://www.python.org/downloads/.
* Install Visual Studio Code on your computer, https://code.visualstudio.com/download.
* Download this repository as a zip folder to your computer.
* Unzip the folder and copy the folder to your Documents folder

> Do not copy a folder inside a folder to your Documents.
> You should have one folder called **met-citi-django** in your Documents.

---

### Installing the Python Packages

* Go to File > Open Folder in Visual Studio Code and open the met-citi-django folder.
* Go to Terminal > New Terminal to open a new terminal.
* Run the following command in the new terminal to install the necessary Python packages.

```
pip install -r requirements.txt
```

---

### Setting up the Django database

* Run the following command in the terminal to create the Django database.
* This commands creates a new file called db.sqlite3 which is a very simple database.

```
python manage.py migrate
```

```
python manage.py makemigrations hello
```

```
python manage.py migrate hello
```

---

### Setting up the Django Admin user

* Run the following command to create the Django admin user.
* You can use these admin user details to login to the Admin interface of your Django Web Server.

```
python manage.py createsuperuser
```

---

### Add Stock data from Yahoo Finance to your database

* In the scripts folder in your project there is a file called, fetch_stock.
* Open the file in Visual Studio Code.
* Go to Run > Run Without Debugging to run the code.
* This will download last year's Stock data from Yahoo Finance for the shares specified in the code.

If you want to change the Share's being downloaded change this line in the code, using valid Stock symbols.

```
STOCKS = ["AAPL", "MSFT", "GOOGL"]
```

You need to change this line to point to the path of your own met-citi-django folder, as it will be different.

```
sys.path.insert(0, 'C:\\Users\\chris\\Documents\\code\\met-citi-django')
```

---

### Visualizing your Database

* Download this software if you want a graphical interface to look at the Stock data you downloaded.
* https://sqlitebrowser.org/dl/


---

### Run your Django Project

* When you run your Django Project it will create a web server with an API.
* The API will load the Stock data in JSON format.
* You can use this API as a data source for Microsoft PowerBI.

Run this in the terminal to run your project and create the API.

```
python manage.py runserver
```

You can access the API and Stock data by going to the following URL in your Browser.

```
http://localhost:8000/api/v1/stocks/
```



