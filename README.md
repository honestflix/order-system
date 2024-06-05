# Order system

# how to run main.py
1. Run main.py
    ```bash
    uvicorn main:main --host 0.0.0.0 --port 8000 --reload

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

# Running the App
1. To run the Flask app with Gunicorn in a development environment:
    ```bash
    gunicorn app:app --workers=4 --bind=0.0.0.0:8000
2. To run the Gradio interface, run the following command:
    ```bash
    python gradio_interface.py
# Running the Tests
1. To run all tests:
    ```bash
    pytest
2. To run a specific test file:
    ```bash
    pytest test_api.py
# Development
This project is designed to be deployed on platforms like Heroku, AWS, or Google Cloud Platform. The deployment_config.py file provides an example setup for deploying with Gunicorn.

