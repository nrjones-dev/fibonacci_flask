# Fibonacci Web App

Update the number in the fibonacci sequence based on the refresh count of the web app.

## Installation

### Requirements

- Docker

### Usage

- Open the terminal in the root directory of this project
- Run `docker build -t my_flask_app .`
- Run `docker run -p 8000:8000 my_flask_app`
- Now load up a browser and navigate to `http://localhost:8000`

  You should now see the counter update each time the screen is refreshed, showing the amount of times you've refreshed the page and the related fibonacci number.
