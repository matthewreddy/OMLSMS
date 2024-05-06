# Design Document
Written by Jason Manning, Matthew Reddy, Grayson Clark, Connor Morin.
Updated May 5, 2024

## Architecture
![alt text](img/Final%20Architecture%20Diagram%20-%20Team%20F%20-%20Comp%20523.jpg)
Notes:
1. Python is the main language of this project used across almost the entirety of the application.
2. The computer application contains a frontend interface displayed by PyQt, which is also written in Python. This is the GUI.
3. Django is set up with a [model/view/template](/https://www.google.com/search?client=safari&rls=en&q=django+model+view+tempalte&ie=UTF-8&oe=UTF-8) arrangement which can be read about here. 
4. The application communicates with the server using Django MSSQL as an Object Relational Mapper(ORM). This allows you to use Python to edit the database backend which is run on Microsoft SQL Server. 

## Code Repository
1. https://github.com/matthewreddy/OMLSMS
2. The `README.md` is included in the top level of the directory. You can click [here](/README.md) to access it also.

## Detailed Data Definitions
1. A PDF of the database schema can be found [here](img/db_schema.pdf) (`img/db_schema.pdf`). It includes all tables, attributes and their respective types, and any constraints such as length, primary key, or foreign key constraints.
2. To see the definitions of each table in Python that can be understood by Django’s ORM, view [this file](web/omlweb/models.py) in the repository (`web/omlweb/models.py`). It includes all “models,” which are tables with all their attributes listed as fields. Types of all of the attributes are given, and constraints are also included.

## Design Rationale: Design Decisions
1. Most of the frameworks and languages that we used were already utilized and passed down to us, and we determined that it was easier to move forward with the preexisting technologies than start over and create new ones. To name them:
    * We continued to use Python as the primary programming language due to its ease of use and natural conjunction with Django. We simply updated the version that was implemented using Python 2to3 and it worked well.
    * We continued to use Django as an object-relational mapper since the relationships were already set up and we didn’t think there would be any benefit to switching it, since Django is relatively easy to understand and use, especially when being implemented in Python.
    * We continued to use PyQt as the designer for the user interface due to its easy incorporation with Python – we failed to find anything else that we were more comfortable with or felt was easier to develop in. Similar to Python, simply updated the version that it was implemented in, which seemed to work well.
    * We continued to use Microsoft SQL Server, which wasn’t really a choice for us, as it’s what the data is already stored in at the OML.
    * We continued to use Django-mssql as the means of communication between Django and Microsoft SQL Server, because it works well, can be installed easily using pip, and we didn’t find any reason to stop using it.
