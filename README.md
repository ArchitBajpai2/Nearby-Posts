# Twitter_api documentation

Please install all the dependies and connect to the postgres database and make the post table
Also enter your openweatherrmap api key in place to use the weather endpoint

to test eh api(s) use the following endpoints and formats
1)For posting (use POST method)
  http://127.0.0.1:5000/posts
  and pass json of format
  {
    "text": "testing 4",
    "lat": 26.9124,
    "lon": 75.7873
  }
output{
    "message": "Post created successfully"
}

2) To get recent_posts (use GET method)
  http://127.0.0.1:5000/recent_posts
  and pass lat and lon and page as parameters Eg. http://127.0.0.1:5000/recent_posts?lat=12.9716&lon=77.5946&page=1
  output {
    "has_next": true,
    "has_prev": false,
    "next_page": 2,
    "posts": [
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
        },
        {
            "created_at": "just now",
            "id": 90,
            "location": "POINT(75.7873 26.9124)",
            "text": "testing 1"
        }
    ],
    "prev_page": null
}
  
3)To get weather (use GET method)
  http://127.0.0.1:5000/weather
  and pass lat and lon as parameters Eg. http://127.0.0.1:5000/weather?lat=27.168567&lon=75.504915
  output {
    "base": "stations",
    "clouds": {
        "all": 95
    },
    "cod": 200,
    "coord": {
        "lat": 27.1686,
        "lon": 75.5049
    },
    "dt": 1681123403,
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
