from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import base64
from pydantic import BaseModel
import os

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://intellect7-ai.web.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return FileResponse("index.html")

@app.get("/result.html")
async def get_result_page():
    return FileResponse("result.html")

def get_mock_analysis():
    return {
        "analysis": {
            "skills_match": {
                "matching_skills": [
                    "Python",
                    "FastAPI",
                    "REST APIs",
                    "Database Design"
                ],
                "missing_skills": [
                    "Docker",
                    "Kubernetes"
                ],
                "match_percentage": 75
            },
            "experience_match": {
                "years_experience": 3,
                "required_experience": 2,
                "match_percentage": 100
            },
            "education_match": {
                "degree": "Bachelor's in Computer Science",
                "required_degree": "Bachelor's in Computer Science or related field",
                "match_percentage": 90
            },
            "overall_assessment": {
                "score": 85,
                "recommendation": "Strong candidate",
                "key_strengths": [
                    "Strong technical skills",
                    "Relevant experience",
                    "Good educational background"
                ],
                "areas_for_improvement": [
                    "Could benefit from containerization experience",
                    "Consider adding cloud platform experience"
                ]
            }
        },
        "metadata": {
            "analysis_timestamp": "2024-03-14T10:30:00Z",
            "version": "1.0"
        }
    }

@app.post("/analyze-resume")
async def analyze_resume(
    resume_file: UploadFile = File(...),
    job_description_file: UploadFile = File(None),
    job_description_text: str = File(None)
):
    # For now, ignore the file/text contents and return the mock response
    mock_response = get_mock_analysis()
    return {
        "status": "success",
        "message": "Analysis completed successfully (MOCK RESPONSE)",
        "data": mock_response
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)