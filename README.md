# OMLSMS v2

> Oral Microbiology Lab's Sterilization Monitoring Service (OMLSMS) is used to monitor the functioning of dental sterilizers in offices across the region.

## Description

The original OMLSMS application was developed as part of a class capstone project at UNC Chapel Hill in 2014. At the time, it was coded in Python 2.7 and used PyQt4 as the GUI framework. Django was used for the database abstraction layer and template language. Django-mssql permitted the use of a SQL Server with Django. XHTML2PDF was used to convert HTML files into PDF files.

This project is focused on rewritting OMLSMS and updating all of its imports to the latest stable versions. Python 3 will be used along with PyQt5. The goal is to make the application more stable and up-to-date with current technologies along with implementing some changes requested by the clients.

## Usage

1. Make sure you are running Python 3 in the 64-bit architecture.
2. Install pip by running the following:
    ```
    python -m ensurepip --upgrade
    ```
3. Now we can use pip to install dependencies. Install PyQt5 by running: 
    ```
    pip install PyQt5
    ```
4. Install Django by running: 
    ```
    pip install Django
    ```
5. Install Django-mssql by running: 
    ```
    pip install Django-mssql
    ```

## Authors

### Original Authors

- [Maik Ruckauf](https://github.com/MaikRuckauf)

- [Kemani Simms](https://github.com/Kasmanian)

### Current Authors

- [Matthew Reddy](https://github.com/matthewreddy)

- [Grayson Clark](https://github.com/graysonjclark1)

- [Connor Morin](https://github.com/connor2702)

- [Jason Manning](https://github.com/jasonmanning27)