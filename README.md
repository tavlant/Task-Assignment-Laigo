# Invoice Processing Microservice

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/invoice-processing.git
    cd invoice-processing
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

## Usage

- Open your browser and navigate to `http://127.0.0.1:8000`.
- Upload a PDF or image file.
- The processed data will be displayed automatically and saved in your Downloads folder.

## Testing

To run the unit tests:
```bash
pytest tests/
