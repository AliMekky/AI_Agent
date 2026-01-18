# all the app components will be connected here. e.g, frontend and backend

# The `__init__.py` file plays a **foundational structural role** in this project rather than implementing business logic. Its main purpose is to define how Python treats directories and how different parts of the project are organized and accessed.

# At the most basic level, the presence of an `__init__.py` file tells Python that a directory should be treated as a **package** rather than just a regular folder. In this project, this is essential because tools like `setuptools` and `find_packages()` rely on package definitions to correctly discover and bundle the project’s modules during installation. Without `__init__.py`, those directories would not be recognized as part of the installable package.

# Beyond package recognition, `__init__.py` also helps establish **clear module boundaries**. By explicitly defining packages, it ensures that different components of the project—such as configuration code, API logic, agent logic, and utilities—can be cleanly imported using dotted paths (for example, `from app.core.config import settings`). This improves readability, maintainability, and scalability as the project grows.

# In many projects like this one, `__init__.py` is intentionally kept **empty**, and that is perfectly valid. Even an empty file still serves the crucial role of package initialization. However, it can also be used to execute initialization logic, define package-level variables, or re-export commonly used classes and functions to simplify imports. For example, core objects such as configuration settings or commonly used agents can be exposed at the package level through `__init__.py`.

# From an architectural perspective, `__init__.py` supports **modularity and encapsulation**. It allows the multi-AI agent system to be divided into logical components—such as agents, services, APIs, and utilities—while still functioning as a single coherent application. This is especially important in a project that integrates multiple frameworks like FastAPI, LangChain, and LangGraph, where clean separation of concerns is critical.

# In summary, the purpose of `__init__.py` in this project is to formally define Python packages, enable proper module discovery and imports, support packaging and deployment, and provide a clean structural foundation for a scalable and maintainable multi-AI agent application.


import subprocess
import threading
import time
import app.common.logger as logger  
import app.common.custom_exception as CustomException
from dotenv import load_dotenv

logger = logger.get_logger(__name__)

load_dotenv()  # Load environment variables from .env file
## when we are running this main.py file in production
## it will be triggered without settings.py this why we 
## need to load the .env file here


def run_backend():
    try:
        logger.info("Starting backend server...")
        subprocess.run(["uvicorn", "app.backend.api:app", "--host", "127.0.0.1", "--port", "9999"], check=True)

    except CustomException as e:
        logger.error(f"Backend server failed to start: {e}")
        raise CustomException("Backend server failed to start", e)

def run_frontend():
    try:
        logger.info("Starting frontend server...")
        subprocess.run(["streamlit", "run", "app/frontend/ui.py"], check=True)

    except CustomException as e:
        logger.error(f"Frontend server failed to start: {e}")
        raise CustomException("Frontend server failed to start", e)
    
if __name__ == "__main__":
    try:
        backend_thread = threading.Thread(target=run_backend)
        backend_thread.start()

        # Wait a moment to ensure the backend starts before the frontend
        time.sleep(5)

        frontend_thread = threading.Thread(target=run_frontend)
        frontend_thread.start()

        backend_thread.join()
        frontend_thread.join()

    except Exception as e:
        logger.error(f"Error in main application: {e}")
        raise CustomException("Error in main application", e)

