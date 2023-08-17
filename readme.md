# Weather Forecasting
This repository contains a website project that displays the current weather of a city, along with a 5-day weather forecast.

## How It Works
The project is built around the Django framework, which handles backend logic and data management. The user interface is developed using HTML for structure, CSS for styling, and JavaScript for dynamic interactions. Python is used to fetch weather forecast data from an external API.

The project also utilizes the python-dotenv library to manage environment variables, enabling easy configuration of API keys and other sensitive information.

## Configuration
Follow the steps below to set up and run the project locally:

### Clone the repository:
```bash
git clone https://github.com/nuzael/weather.git
cd weather
```

### Create a virtual environment (optional but recommended):
On Linux:
```bash
python -m venv venv
source venv/bin/activate
```
On Windows: 
```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Configure environment variables:
Rename the `.env.example` file to `.env` and fill in the necessary information, such as API keys.

### Run database migrations:
```bash
python manage.py migrate
```

### Start the server:
```bash
python manage.py runserver
```

### Access the site:
Open your web browser and navigate to http://127.0.0.1:8000/ to see the site in action.

## Project Structure
static/: Contains static files, such as CSS and JavaScript files.

templates/: Stores the HTML files used to render the pages.

weather_app/: The main Django app that handles application logic.

urls.py: Defines the available URLs for the application.

views.py: Contains view functions that control the flow of data between the backend and frontend.

models.py: Defines the data models used in the app.

utils.py: Contains helper functions, such as API calls to fetch weather forecast data.

manage.py: Django management utility.

## Contribution
If you wish to contribute improvements to this project, feel free to create a pull request. Make sure to follow development best practices and document the changes you make.

## License
This project is under the MIT license. Refer to the LICENSE file for more information.
