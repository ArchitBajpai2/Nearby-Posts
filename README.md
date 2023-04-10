Overview
This is a Flask API that allows users to create and retrieve posts based on their location. Users can also retrieve weather data for a given location. The API uses a PostgreSQL database to store post information and utilizes the OpenWeatherMap API to retrieve weather data.

Installation and Setup
Install the required dependencies by running pip install -r requirements.txt.
Create a PostgreSQL database and update the DATABASE_URL environment variable in the .env file with your database connection information.
Sign up for an OpenWeatherMap API key and update the OPENWEATHERMAP_API_KEY environment variable in the .env file with your API key.
Usage
Create Post
To create a new post, send a POST request to the /posts endpoint with the following JSON format:
{
    "text": "testing 4",
    "lat": 26.9124,
    "lon": 75.7873
}

Upon successful creation of the post, the API will return a JSON response with a message:
{
    "message": "Post created successfully"
}

Retrieve Recent Posts
To retrieve the most recent posts for a given location, send a GET request to the /recent_posts endpoint with the following parameters:

lat: the latitude of the location (required)
lon: the longitude of the location (required)
page: the page number (optional, defaults to 1)
Example URL: http://127.0.0.1:5000/recent_posts?lat=12.9716&lon=77.5946&page=1

The API will return a JSON response with the following format:
{
    "has_next": true,
    "has_prev": false,
    "next_page": 2,
    "posts": [
        {
            "created_at": "just now",
            "id": 100,
            "location": "POINT(77.5946 12.9716)",
            "text": "testing 2"
        },
        {
            "created_at": "just now",
            "id": 99,
            "location": "POINT(77.5946 12.9716)",
            "text": "testing 2"
        },
        {
            "created_at": "just now",
            "id": 98,
            "location": "POINT(77.5946 12.9716)",
            "text": "testing 2"
        },
        {
            "created_at": "just now",
            "id": 97,
            "location": "POINT(75.7873 26.9124)",
            "text": "testing 1"
        },
        {
            "created_at": "just now",
            "id": 96,
            "location": "POINT(77.1025 28.7041)",
            "text": "testing 0"
        },
        {
            "created_at": "just now",
            "id": 95,
            "location": "POINT(75.7873 26.9124)",
            "text": "testing 1"
        },
        {
            "created_at": "just now",
            "id": 94,
            "location": "POINT(75.7873 26.9124)",
            "text": "testing 1"
        },
        {
            "created_at": "just now",
            "id": 93,
            "location": "POINT(77.5946 12.9716)",
            "text": "testing 2"
        },
        {
            "created_at": "just now",
            "id": 92,
            "location": "POINT(77.5946 12.9716)",
            "text": "testing 2"
        },
        {
            "created_at": "just now",
            "id": 91,
            "location": "POINT(77.5946 12.9716)",
            "text": "testing 2"
        }
    ],
    "prev_page": null
}

Retrieve Weather
To retrieve weather data for a given location, send a GET request to the /weather endpoint with the following parameters:

lat: the latitude of the location (required)
lon: the longitude of the location (required)
Example URL: http://127.0.0.1:5000/weather?lat=27.168567&lon=75.504915

The API will return a JSON response with the following format:
{
    "base": "stations",
    "clouds": {
        "all": 95
    },
    "cod": 200,
    "coord": {
        "lat": 27.1686,
        "lon": 75.5049
    },
    "dt": 1681125349,
    "id": 1258140,
    "main": {
        "feels_like": 32.87,
        "grnd_level": 963,
        "humidity": 7,
        "pressure": 1010,
        "sea_level": 1010,
        "temp": 35.69,
        "temp_max": 35.69,
        "temp_min": 35.69
    },
    "name": "Rīngas",
    "sys": {
        "country": "IN",
        "id": 9170,
        "sunrise": 1681087165,
        "sunset": 1681132743,
        "type": 1
    },
    "timezone": 19800,
    "visibility": 10000,
    "weather": [
        {
            "description": "overcast clouds",
            "icon": "04d",
            "id": 804,
            "main": "Clouds"
        }
    ],
    "wind": {
        "deg": 297,
        "gust": 5.44,
        "speed": 5.11
    }
}
