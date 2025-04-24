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





# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import google.generativeai as genai
# from google.api_core.exceptions import ResourceExhausted
# import os, itertools

# # ------------------------------------------------------------------
# # 1) مفاتيح Gemini – ضَعها في متغيّر بيئة أو مباشرة في القائمة
# # ------------------------------------------------------------------
# KEYS = os.getenv("GEMINI_KEYS", "").split(",") if os.getenv("GEMINI_KEYS") else [
#     "AIzaSyB5mX7Jckqt7STB57A_dMlxKRsJl3SOjpM",
#     "AIzaSyDL8oopr4R_z_9gRtYuYQxc5qjnE7hKvzA",
#     "AIzaSyCmfITvO_TU16wpfuyJ5DmhxFZUvT6s0do",
# ]
# if not KEYS or KEYS == [""]:
#     raise RuntimeError("No Gemini API keys found. Set GEMINI_KEYS env var or edit KEYS list.")

# key_cycle = itertools.cycle(KEYS)

# def get_model():
#     api_key = next(key_cycle)
#     genai.configure(api_key=api_key)
#     return genai.GenerativeModel("gemini-1.5-pro-latest")

# # ------------------------------------------------------------------
# # 2) FastAPI setup + CORS
# # ------------------------------------------------------------------
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # يمكنك استبدال * بدومين الفرونت‑إند
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ------------------------------------------------------------------
# # 3) Schema
# # ------------------------------------------------------------------
# class TranslationRequest(BaseModel):
#     text: str
#     accent: str  # مثال: "اللهجة المصرية بالعربية"

# # ------------------------------------------------------------------
# # 4) Translation endpoint
# # ------------------------------------------------------------------
# @app.post("/translate")
# def translate_text(req: TranslationRequest):
#     prompt = (
#         f"ترجم الجملة دي إلى ${req.accent} بدون مقدمة أو شرح: \"{req.text}\""
#     )

#     # جرّب بعدد المفاتيح المتاحة
#     for _ in range(len(KEYS)):
#         try:
#             model = get_model()
#             res = model.generate_content(prompt)
#             return {"translation": res.text.strip()}

#         except ResourceExhausted:
#             # المفتاح الحالي خلّص حصّته → جرّب التالي
#             continue
#         except Exception as e:
#             # أخطاء أخرى (مثل تحجيم البرومبت أو أخطاء إملائية)
#             raise HTTPException(status_code=500, detail=str(e))

#     # لو كل المفاتيح خلصت حصّتها
#     raise HTTPException(
#         status_code=429,
#         detail="All API keys exhausted. Please wait for the daily quota reset.",
#     )
