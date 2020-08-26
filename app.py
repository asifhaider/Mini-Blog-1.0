### The root level python file 
### for executing the main app

# imports the 'app' object from __init__.py under the root directory sub folder blogsite

from blogsite import app

# start running the app

if __name__ == '__main__':
    app.run(debug=True)