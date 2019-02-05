# SQL Injection Showcase
This project was created as part of an assignment for my software security class. 
The purpose of this assignment is to demonstrate SQL injection vulnerabilities in a simple web app.

## How to install
Download the latest release from the [releases page](https://github.com/Mielzus/SQL-Injection-Showcase/releases).

Once the release is downloaded and extracted you should have the following file hierarchy:

```
| SQLInjectionShowcase/
|---+ data/
|   |---+ database.sqlite (Generated the first time the app is started)
|   |---+ statements.yml
|---+ templates/     
|   |---+ index.html
|   |---+ query.html
|   |---+ query-s.html
|---+ app.py
|---+ database.py
|---+ logic.py
|---+ README.md
|---+ requirements.txt
```

## How to run
The Flask app needs to be started by running `python app.py`. 
This will start the app running on `localhost:5000`.

There are three buttons on the landing page. `Unsafe Query`, `Safe Query`, and `Initialize Database`
`Initialize Database` needs to be pressed to populate the database as well as to reset the data if you've messed with it.

## Example Attack Queries
The following queries work by stopping the current select command with `";` and then providing a malicious SQL statement to execute.
These statements can be run on the unsafe query page and they will execute the malicious statement.
Running the statements against the safe query page will execute successfully and return no results.

A SQLite database browser can be used to view the changes to the database as statements are run.
I recommend [DB Browser for SQLite](https://sqlitebrowser.org/).

`"; DROP TABLE grades; /*` - This query will drop the table grades

`"; UPDATE grades SET grade='A+' WHERE student_id=2; /*` - This query will update all grade entries for student 2 to A+. 