# 📽Movie Rentals
Application that manages a movie rental store.

## Used Concepts and Several Application Features
- Console User Interface
- Graphical User Interface, built using ```Tkinter```
- Layered Architecture: ```presentation layer``` (application UI), ```business layer``` (application service), ```persistence layer``` (application repositories)
- Usage of OOP concepts such as ```inheritance```, ```encapsulation```, ```polymorphism``` and ```abstraction```.
- Tests coverage 96% except the UI
- Several ways of storing the data persistently - json file, binary file and text file - selectable within a settings file 
- Exceptions handling

  ## Design Patterns Used
- ```Command``` design pattern, used for the undo/redo functionality.
- ```Data Access Object``` pattern, used for reading the data in the text files.

## Other Application Features
- Adding, removing, updating and listing all movies, clients.
- Renting or returning a movie with a given client. The client is not allowed to rent new movies if they have any overdue movies to return.
- Searching for movies, clients or rentings by any attributes, or by all of them at once.
- Getting statistics for the most rented movies, the most active clients and the overdue movies.
- Letting the user select the data storage mode and the user interface using the settings file.
- Undo and Redo functionality for all data-modifying features.
