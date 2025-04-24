from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware


# Configure Gemini
genai.configure(api_key="AIzaSyDlbiCluy-T7XQjcFN8SmGIawGBoniJDk0")

# Create the model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# FastAPI app
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body model
class TranslationRequest(BaseModel):
    text: str
    accent: str  # مثل: "اللهجة المصرية", "اللهجة المغربية", "الفصحى", إلخ

# Translation endpoint
@app.post("/translate")
def translate_text(request: TranslationRequest):
    try:
        prompt = (
            f"ترجم الجملة دي إلى ${request.accent} بدون مقدمة أو شرح: \"{request.text}\""
        )
        response = model.generate_content(prompt)
        return {"translation": response.text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




