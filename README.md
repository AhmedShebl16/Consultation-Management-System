# Consultation Management System (AI-Powered)

A production-ready Full-Stack Django application for managing patient consultations with AI-generated medical summaries.

## 🚀 Features
- **Patient Management**: Create and list patients.
- **Consultation Tracking**: Record symptoms and diagnoses.
- **AI Summarization**: Integrates with **Google Gemini 2.5 Flash** to generate professional medical summaries.
- **Modern Dashboard**: Responsive UI built with Bootstrap 5 and Axios.
- **API Documentation**: Automated Swagger/OpenAPI documentation.

## 🛠️ Tech Stack
- **Backend**: Django, Django REST Framework (DRF).
- **Frontend**: HTML5, Bootstrap 5, JavaScript (Axios).
- **AI**: Google Generative AI (Gemini API).
- **Docs**: drf-spectacular (Swagger UI).

## ⚙️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <your-repo-link>
   cd Consultation-Management-System
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your Gemini API Key and Django config:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```
   *Note: Check `.env.example` for reference.*

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

## 🌐 Access the App

- **Frontend Dashboard**: `http://127.0.0.1:8000/`
- **Swagger API Docs**: `http://127.0.0.1:8000/api/schema/swagger-ui/`

## 📝 Assumptions
- The AI summary is generated based on provided symptoms and diagnosis.
- If the AI service is unavailable, a structured fallback summary is provided.
