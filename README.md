# Music-recommender

Music recommender using a graph database.

## Built With

- Neo4J - `provide description`.

- `tell which dataset we used + link`.

## Setup Development Environment

1. Create and activate the virtual environment.

```bash
$ python3 -m venv env
$ source env/bin/activate
```

2. Install all the requirements.

```bash
$ pip install -r requirements.txt
```

3. Do not forget to output the installed packages.

```bash
$ pip freeze > requirements.txt
```

## Setup Neo4j Environment

1. Create a Graph Database at `bolt://localhost:11003` with the password: `123mudar`

2. Create a database with the name: `musicrecommender`

## Running

Run the recommendation system. `<user_id>` is Id of the user. `<num_of_recomm>` is the quantity of tracks that will be recommended for the specified `<user_id>`.
```bash
$ python music.py <user_id> <num_of_recomm>
```

Populate the Neo4j database (must start the Neo4j database before running this command).
```bash
$ python music.py populate
```

Clean the Neo4j database (must start the Neo4j database before running this command).
`Warning: restart the database after cleanup. This will reset the Id.`
```bash
$ python music.py cleanup
```
## Folder Structure (changes will happen)

- `data`: `provide description`.

- `src`: stores the code for data processing + node labelling + etc...

- `src/process`: stores the code for data normalization + processing.

- `src/neo4j`: stores the code responsible to control operation on Neo4j

- `src/neo4j`: stores the models (Person, Music)

- `./music.py`: the heart of the application.
