# Weather App with Flask & OpenWeatherMap API

This project is a simple web application that lets you:

- Add counties/cities to track their weather
- View current temperature, humidity, and wind speed
- Update weather data
- Remove locations

## 📁 Project Structure

```
weather-app/
├── app.py             # Flask backend code
├── config.py          # Stores API key (keep this secret!)
├── templates/
│   └── weather.html   # Frontend HTML/JavaScript
└── README.md          # This file
```

## 🔧 Setup Instructions

### Get an API Key

1. Sign up at OpenWeatherMap
2. Get your free API key
3. Create config.py

```python
API_KEY = "your_api_key_here"  # From OpenWeatherMap
```

### Install Requirements

```bash
pip install flask flask-cors requests
pip install requests
```

### Run the App

```bash
python app.py
```

Open: http://localhost:5000

## 💻 Code Explanation

### 🌐 Backend (app.py)

Handles weather data fetching and CRUD operations.

Key Features:
- CORS(app) → Allows frontend-backend communication
- Stores data in counties_data dictionary
- Uses OpenWeatherMap API

Endpoints:

| Route | Method | Action |
|-------|--------|--------|
| / | GET | Shows the HTML page |
| /counties | GET | Lists all tracked counties |
| /counties | POST | Add new county |
| /counties/<county> | PUT | Update county's weather |
| /counties/<county> | DELETE | Remove county |

### 🖥️ Frontend (weather.html)

Simple interactive UI with jQuery.

Features:
- Add counties via input box
- Auto-refreshes the list
- Update/Delete buttons for each entry

Key Functions:

```javascript
fetchCounties()      // Loads all counties
addCounty()          // Adds new county
updateCounty(name)   // Refreshes weather data  
deleteCounty(name)   // Removes a county
```

## 🚦 Common Issues & Fixes

### CORS Errors
- Always access via http://localhost:5000 (not file://)

### API Key Not Working
- Wait 10-15 mins after getting a new key
- Check config.py has the correct key

### Can't Delete "County Laois"
- The backend now handles variations ("Laois" vs "County Laois")

## 📚 References

### Documentation & Tutorials
- [OpenWeatherMap API Documentation](https://openweathermap.org/current) - Official documentation for the current weather data API
- [API Integration in Python (Real Python)](https://realpython.com/api-integration-in-python/) - Tutorial on integrating APIs in Python applications
- [WSAA 6.5 REST for project](https://atlantictu-my.sharepoint.com/personal/andrew_beatty_atu_ie/_layouts/15/stream.aspx?id=%2Fpersonal%2Fandrew%5Fbeatty%5Fatu%5Fie%2FDocuments%2FWSAA%202025%20%28private%29%2Fvideos%2FWSAA6%2E5%20REST%20for%20project%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E3ffb2ea5%2D0031%2D4880%2Dbb82%2D42459b1ac031) - Video tutorial on REST implementation for projects
- [WSAA 10.1 PythonAnywhere](https://atlantictu-my.sharepoint.com/personal/andrew_beatty_atu_ie/_layouts/15/stream.aspx?id=%2Fpersonal%2Fandrew%5Fbeatty%5Fatu%5Fie%2FDocuments%2FWSAA%202025%20%28private%29%2Fvideos%2FWSAA10%2E1%2Dpythonanywhere%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Eaebfbe13%2Da10e%2D4d58%2D938c%2D7322e839825d) - Guide on deploying Flask applications on PythonAnywhere
- [WSAA 6.2 Flask Introduction](https://atlantictu-my.sharepoint.com/personal/andrew_beatty_atu_ie/_layouts/15/stream.aspx?id=%2Fpersonal%2Fandrew%5Fbeatty%5Fatu%5Fie%2FDocuments%2FWSAA%202025%20%28private%29%2Fvideos%2FWSAA6%2E2%20Flask%20introduction%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E8b5bb6ab%2D829c%2D403d%2D9002%2D52a3f87895b3) - Introduction to Flask web framework
- [DR 6.3 AJAX jQuery](https://atlantictu-my.sharepoint.com/personal/andrew_beatty_atu_ie/_layouts/15/stream.aspx?id=%2Fpersonal%2Fandrew%5Fbeatty%5Fatu%5Fie%2FDocuments%2Farchive%2Fwsaa%202024%20%28private%29%2FVideos%2FDR6%2E3%20AJAX%20JQuery%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E5d78a4de%2Ddfc4%2D4d44%2D91a1%2D86e3956f963f) - Tutorial on using AJAX with jQuery for dynamic web applications

### AI Tools & Assistants
- [ChatGPT](https://chat.openai.com) - OpenAI's conversational AI assistant for natural language processing and code generation
- [Claude.AI](https://claude.ai) - Anthropic's AI assistant with strong reasoning and document analysis capabilities
- [DeepSeek](https://deepseek.com) - AI platform with advanced search and language understanding features
- [Manus.im](https://manus.im) - AI agent platform for task automation and assistance
