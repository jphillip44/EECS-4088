# EECS-4088

#### Basic structure of the project:
The main folder has two directories, flask and react-base-files. Flask is the working server code and includes a compiled version of the files in the react-based-files folder. The react-base-files folder is there for reference purposes, since the compiled code is impossible to read, or changed need to be made.

#### Organization of the Flask code
The primary app responsible for running the program is `app.py`. It is a Flask-socketio app that launches the server and facilitates communication with the controllers and front-end. It communicates with the controllers via a variable called `SOCKETIO` and the front-end via a variable called `DISPLAY`. These get passed as parameters to the games themselves under the names `socketio` and `display_game` respectively, allowing their various functionality to be called from any of the games.

#### Socketio component
Flask-socketio is a framework that is available for public use. More details can be found here: https://flask-socketio.readthedocs.io/en/latest/. The server and controllers connect using the socketio protocol, they communicate through a series of emits and listeners.

#### Display component
The display component is attached to all the games through `display_game.py`. Whenever some component of the project needs to update the display, it simply calls the `display_game` object it was given passing the object that needs to be updated. Depending on the object that is passed, the `update` function calls the corresponding function and delegates to the `desktop` package that is in the `desktop` folder. 

#### Game component
The game component is somewhat similar to display though it calls the game directly and does not delegate to an intermediate function. The primary difference is games are simpler to launch requiring less parameter setup as they do not need to share anything in common. The `select_game` function in `game_list.py` is used to launch the game that is selected from the `games` package inside the `games` folder.

#### Installing the project
The project runs using `Python3`. To install the existing dependencies, it is recommended to use `pip install -U -r requirement.txt` or `pip3` if that is your correct alias for `pip`. Some variants of `numpy` do not play nicely with the application so its exclusion from `requirements.txt` was intentional. It may need to be installed with `pip` as well. On some systems, the `eventlet` packages seems to be problematic but it is the preferred server. If it is being problematic, install `gevent` and `gevent-websocket` with `pip` and uninstall `eventlet`.

#### Running the application
Once the correct python dependencies are installed, the project can be launched using `python3 app.py` or in some variants of Powershell, the correct term for launching a python project is `py app.py`. The controller can be connected from any web-enabled device using the IP and listed port on the GUI or by scanning the QR code on the display. Obtaining a local IP is not an exact science and may differ on certain machines though so there is a possibility that the attempt to grab the IP is incorrect. If so, the server can always be reached using the `<local IP>:5000` or forwarded to a `<public IP>:port`.

#### Closing the application
The application can be closed by pressing `ctrl + c` from the terminal window. 




