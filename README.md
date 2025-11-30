# Flask Lab1 Application

A simple Flask application with health check endpoint.

## Project Structure

```
lab1/
├── app/
│   ├── __init__.py       # Flask app initialization
│   └── views.py          # Route definitions
├── docker-compose.yaml   # Docker Compose configuration
├── Dockerfile            # Docker image definition
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Requirements

- Python 3.11+
- Docker and Docker Compose (for containerized deployment)

## Local Development

### 1. Create and Activate Virtual Environment

```powershell
# Create virtual environment
python -m venv env

# Activate virtual environment
.\env\Scripts\Activate.ps1
```

If PowerShell blocks script execution:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
.\env\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Run the Application

```powershell
# Set Flask app environment variable
$Env:FLASK_APP = 'app:create_app'

# Run Flask development server
python -m flask run --host 0.0.0.0 --port 8000
```

The application will be available at:
- Local: http://127.0.0.1:8000
- Network: http://192.168.0.17:8000 (your local IP)

### 4. Test the Health Check Endpoint

```powershell
# Using curl
curl http://localhost:8000/healthcheck

# Or open in browser
# http://localhost:8000/healthcheck
```

Expected response:
```json
{
  "status": "ok"
}
```

## Docker Deployment

### Build and Run with Docker

```powershell
# Build Docker image
docker build -t flask-lab1 .

# Run container
docker run -p 8000:8000 flask-lab1
```

### Using Docker Compose (Recommended)

```powershell
# Build and start services
docker-compose up --build

# Run in detached mode (background)
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

The application will be available at http://localhost:8000

## API Endpoints

| Method | Endpoint       | Description              |
|--------|---------------|--------------------------|
| GET    | /healthcheck  | Returns application status |

## Environment Variables

- `FLASK_APP` - Flask application entry point (default: `app:create_app`)
- `PORT` - Application port (default: `8000`)

## Troubleshooting

### Error: "Could not import 'app.app'"
Make sure you're running Flask from the project root directory (`lab1`), not from inside the `app` folder.

### Error: "name 'app' is not defined"
Ensure that `from app import app` is present in `app/views.py`.

### PowerShell Script Execution Error
Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force`

## Development Notes

- The application uses Flask 3.1.2
- Python version: 3.11.3
- Development server should not be used in production
- For production, use a WSGI server like Gunicorn or uWSGI
