# Order system ☕

# how to run main.py
1. Run main.py
    ```bash
    python app/main.py

## Setup and Installation
1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/honestflix/order-system.git

2. Set up a virtual environment and activate it.

    ```bash
    apt install python3.10-venv
    python3 -m venv my-env
    . my-env/bin/activate
    
3. Install the required dependencies:

   ```bash
   python3 -m pip install -e .
   python3 -m pip install -r requirements.txt

### Docker Setup
1. **Build the Docker image:**
    ```sh
    docker build -t caffeinated-odyssey .
    ```

2. **Run the Docker container:**
    ```sh
    docker run -d -p 8000:8000 caffeinated-odyssey
    ```

## API Endpoints

- **POST /order/**: Place an order for americano.
- **GET /start/**: Baristas start preparing the orders.
- **POST /finish/**: Baristas finish preparing the orders.

## Notes
- Ensure to protect the service against DDoS attacks.
- Clients and baristas interact with different FastAPI servers on separate ports.

# Running the App
To run the Flask app with Gunicorn in a development environment:
    ```bash
    gunicorn main:main --workers=4 --bind=0.0.0.0:8000

# Development
This project is designed to be deployed on platforms like Heroku, AWS, or Google Cloud Platform. The deployment_config.py file provides an example setup for deploying with Gunicorn.

