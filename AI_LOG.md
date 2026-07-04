# AI Collaboration Log

## AI Tech Stack

The following AI tools were used throughout the development of this project:

* **GitHub Copilot (VS Code Integration)** – Used during implementation to generate code suggestions, autocomplete repetitive code, identify syntax issues, and assist with debugging while coding.
* **ChatGPT (GPT-5.5)** – Used for system design discussions, backend architecture, Docker setup, debugging, frontend implementation guidance, and documentation.
* **Claude** – Used to cross-check implementation ideas, validate approaches, and compare alternative solutions for certain components.

Each tool served a different purpose throughout the development process, helping accelerate implementation while maintaining understanding of the generated code.

---

# How AI Was Used

## Backend Development

AI assisted in:

* Designing the FastAPI project structure.
* Creating REST API endpoints.
* Designing SQLAlchemy models.
* Configuring SQLite database integration.
* Implementing APScheduler for periodic URL health checks.
* Handling HTTP request timeouts and exceptions.
* Measuring response time and recording HTTP status codes.
* Structuring the backend into routers, services, models, and database layers.

Example prompt:

> "Create a FastAPI backend that stores monitored URLs in SQLite and periodically checks each URL every minute, recording HTTP status code, response time, and timestamp."

---

## Frontend Development

AI assisted in:

* Creating the React + Vite project structure.
* Designing reusable React components.
* Implementing URL registration.
* Displaying monitored URLs in a dashboard.
* Auto-refreshing monitoring results.
* Managing API communication with Axios.
* Displaying status badges for UP and DOWN states.

Example prompt:

> "Build a React dashboard that displays monitored URLs with their current status, latest response time, status code, and last checked timestamp."

---

## Docker & Deployment

AI assisted in:

* Creating Dockerfiles for both frontend and backend.
* Configuring Docker Compose.
* Connecting frontend and backend containers.
* Preparing the application to run using a single `docker compose up --build` command.
* Discussing a simple cloud deployment architecture suitable for an MVP.

Example prompt:

> "Containerize a FastAPI backend and React frontend using Docker Compose so the entire application can be started with a single command."

---

# GitHub Copilot Usage

GitHub Copilot was used directly inside Visual Studio Code during development for:

* Code completion and boilerplate generation.
* Suggesting FastAPI route implementations.
* Assisting with React component structure.
* Writing repetitive CRUD operations.
* Detecting syntax mistakes while typing.
* Suggesting fixes for common coding errors.
* Speeding up development through inline code suggestions.

Copilot was primarily used as an in-editor coding assistant, while architectural decisions and debugging were guided using ChatGPT and Claude.

---

# Course Corrections

AI-generated code was not accepted blindly. Several iterations required debugging and manual corrections.

### 1. React Callback Issue

An early implementation incorrectly handled the callback after adding a new URL, causing the dashboard not to refresh correctly.

The callback logic was corrected so that the URL list refreshes only after a successful API request.

---

### 2. React State Error

During development, the dashboard crashed with the error:

> `urls.map is not a function`

Using browser debugging tools together with AI assistance, the issue was traced to an API response returning HTML instead of JSON because of an incorrect frontend API configuration. After correcting the API endpoint configuration, the application functioned correctly.

---

### 3. Docker Networking Configuration

An initial Docker configuration incorrectly configured the frontend API URL to use:

```
http://backend:8000
```

Since React executes in the user's browser rather than inside the Docker container, the browser could not resolve the Docker service name.

The configuration was corrected to use:

```
http://localhost:8000
```

for browser-based API communication while preserving Docker container networking.

---

### 4. Environment Variable Configuration

Environment variables were introduced to avoid hardcoded API URLs.

During development, the frontend initially failed because the environment variables were not being loaded correctly by Vite. After validating the build configuration and rebuilding the frontend image, the environment variables were successfully integrated.

---

# Development Philosophy

AI was used as a productivity and learning assistant rather than a replacement for engineering decisions.

Generated code was:

* Reviewed before integration.
* Tested locally.
* Debugged when necessary.
* Refactored for readability and maintainability.
* Modified to fit the project architecture.

All final implementation decisions, testing, and integration were performed manually.

---

# Outcome

Using AI-assisted development significantly accelerated implementation while allowing focus on architecture, debugging, integration, and validating the overall end-to-end system. The collaboration enabled rapid iteration across backend development, frontend implementation, containerization, and documentation while maintaining a clear understanding of the resulting codebase.
