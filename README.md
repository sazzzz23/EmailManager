Email Manager

A Python desktop email management simulator built with Tkinter. The project provides a graphical interface for viewing, creating, labelling, prioritising, and deleting simulated email messages.

Originally developed as a university project, the project has been cleaned up and documented to be used on github portfolio.

##Features

* List Messages — View all stored messages with their ID, priority, sender, label, and subject.
* Read Messages — Open an individual message using its message ID.
* Create Messages — Create new messages with sender, recipient, subject, and content.
* Label Messages — Add labels to messages and filter messages by label.
* Message Priority — Assign a priority from 1–5, displayed using stars.
* Delete Messages — Delete messages from the simulator.
* Automated Testing — Includes pytest tests covering the message model and message creation functionality.

##Technologies

* Python 3
* Tkinter — Graphical user interface
* pytest — Automated testing
* Object-Oriented Programming
* Git / GitHub — Version control

##Project Structure
<img width="970" height="630" alt="image" src="https://github.com/user-attachments/assets/d0fb866b-4ac0-4084-ad37-1ac621f4723c" />


##Running the Application

Clone the repository and navigate into the project directory:

git clone https://github.com/sazzzz23/EmailManager.git
cd EmailManager

Run the application with:

python3 src/email_manager.py

The Email Manager window should open.




<br>
##Running the Tests

Install pytest if it is not already installed:

python3 -m pip install pytest

Then run:

python3 -m pytest -q

The current test suite contains 6 tests.





<br>
##How It Works

The application uses a simple separation between the graphical interface and the message-management logic.

message.py defines the Message class and stores information such as the sender, recipient, subject, content, label, and priority.

message_manager.py manages the collection of messages and provides functions for retrieving, creating, updating, labelling, and deleting messages.

The Tkinter GUI modules provide the different user interfaces for interacting with these messages.

Messages are stored in memory, so newly created or modified messages are not persisted after the application is closed. This project is intended as an email-management simulation, rather than a connection to a real email service.




<br>
##Testing

The project uses pytest for automated testing.

The tests currently cover:

* Message initialisation
* Default message priority
* Priority/star formatting
* Message information formatting
* Label assignment
* New message creation
