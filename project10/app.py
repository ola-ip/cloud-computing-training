# ==============================================================================
# SECTION 1: MODULE IMPORTS
# Import FastAPI core class and Request header inspector
# ==============================================================================
from fastapi import FastAPI, Request
import datetime


# ==============================================================================
# SECTION 2: APPLICATION INITIALIZATION
# Initialize FastAPI application instance
# ==============================================================================
app = FastAPI(title="Intern Web App")


# ==============================================================================
# SECTION 3: API ENDPOINT DEFINITION
# Define root endpoint '/' returning backend details and received headers
# ==============================================================================
@app.get("/")
def read_root(request: Request):
    return {
        "status": "Success",
        "message": "Hello Intern! You reached the Python FastAPI backend.",
        "server_time": str(datetime.datetime.now()),

        # Return headers to verify Proxy Header forwarding in Step 3
        "headers_received_by_backend": {
            "host": request.headers.get("host"),
            "x_real_ip": request.headers.get("x-real-ip"),
            "x_forwarded_for": request.headers.get("x-forwarded-for"),
            "x_forwarded_proto": request.headers.get("x-forwarded-proto")
        }
    }


# ==============================================================================
# SECTION 4: SERVER EXECUTION BLOCK
# Run app locally on internal port 8000 when executed directly
# ==============================================================================
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
