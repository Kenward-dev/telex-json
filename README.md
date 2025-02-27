# Telex JSON API

This is a simple FastAPI-based API that serves the contents of `integration.json` containing telex integration configurations.

## Project Structure
```
telex-json/
    ├── integration.json
    ├── main.py
    ├── README.md
    ├── requirements.txt
    ├── vercel.json
```

## Installation & Setup

1. **Clone the Repository**
   ```sh
   git clone https://github.com/Kenward-dev/telex-json
   cd telex-json
   ```

2. **Create a Virtual Environment** (optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Running the FastAPI App

Start the FastAPI server:
```sh
uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| GET    | `/`     | Returns the contents of `integration.json` |

Once the server is running, visit:
```
http://127.0.0.1:8000/
```
to see the JSON response.

## Deployment

This project is configured for deployment on [Vercel](https://vercel.com/).

### Deploy to Vercel

1. **Install Vercel CLI (if not installed):**
   ```sh
   npm install -g vercel
   ```
2. **Login to Vercel:**
   ```sh
   vercel login
   ```
3. **Deploy the project:**
   ```sh
   vercel
   ```

## License

This project is open-source and available for modification.

