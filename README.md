# ContactManager
This project is a contact management application.
The programming language used is python, and pyqt5 was used for the graphic interface.

## Application structure
The project has been implemented following the Model–view–viewmodel (**MVVM**) pattern: this allows to have a separation 
between the application logic and the graphical user interface.

Here there are a Model `contactsModel.py` and three views (`allContactsView.py`, `detailContactView.py` and `newContactView.py`).


## Application features
The main features of the applications are:
- **Visualization of all contacts**: in the main view you can view the list of all the contacts saved in the database and sort them by name or surname.
It is also possible to select only a few contacts on the basis of tags assigned to each contact and to search for a term present in any field of any contact.

- **Adding a new contact**: a specific form can be filled with all the required fields. Here it' also possible to create and add a new tag.

- **Visualization of a specific contact**: here you can see (and not edit) all the filled fields of the selected contact, there are also two buttons for editing and delete the contact. 

- **Editing contact**: this view is the same as when a new contact is inserted, but in this case the fields already filled of the selected contact are kept and it is possible to modify each field
## Run the application
- from terminal go to the directory in which you have downloaded the project
- go inside the ContactManager folder using the command:  `cd ContactManager`
- then run the application with the command: `python main.py`
