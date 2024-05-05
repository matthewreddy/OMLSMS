# Design Document
Written by Jason Manning, Matthew Reddy, Grayson Clark, Connor Morin.
Updated May 5, 2024

## Architecture
![alt text](/Final%20Architecture%20Diagram%20-%20Team%20F%20-%20Comp%20523.jpg)


## Code Repository
1. https://github.com/matthewreddy/OMLSMS
2. The README.md is included in the top level of the directory.

## Detailed Data Definitions
1. A PDF of the database schema can be found here (db_schema.pdf in the top level of the repository). It includes all tables, attributes and their respective types, and any constraints such as length, primary key, or foreign key constraints.
2. To see the definitions of each table in Python that can be understood by Django’s ORM, view this file in the repository (web/omlweb/models.py). It includes all “models,” which are tables with all their attributes listed as fields. Types of all of the attributes are given, and constraints are also included.

## Design Rationale: Design Decisions
1. Most of the frameworks and languages that we used were already utilized and passed down to us, and we determined that it was easier to move forward with the preexisting technologies than start over and create new ones. To name them:
- We continued to use Python as the primary programming language due to its ease of use and natural conjunction with Django. We simply updated the version that was implemented using Python 2to3 and it worked well.
- We continued to use Django as an object-relational mapper since the relationships were already set up and we didn’t think there would be any benefit to switching it, since Django is relatively easy to understand and use, especially when being implemented in Python.
We continued to use PyQt as the designer for the user interface due to its easy incorporation with Python – we failed to find anything else that we were more comfortable with or felt was easier to develop in. Similar to Python, simply updated the version that it was implemented in, which seemed to work well.
- We continued to use Microsoft SQL Server, which wasn’t really a choice for us, as it’s what the data is already stored in at the OML.
- We continued to use Django-mssql as the means of communication between Django and Microsoft SQL Server, because it works well, can be installed easily using pip, and we didn’t find any reason to stop using it.
