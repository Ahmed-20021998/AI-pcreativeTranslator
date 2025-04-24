# import google.generativeai as genai

# # # Set up API key
# genai.configure(api_key="AIzaSyB5mX7Jckqt7STB57A_dMlxKRsJl3SOjpM")  # Replace with your actual API key

# # # Create a model instance
# model = genai.GenerativeModel("gemini-1.5-pro-latest")

# # # Define input statements
# input_text = "posting more about this won't help you"
# language = "Egyptian Accent"

# # Ask Gemini to create a story
# prompt = f"Translate this text into ${language} please without any intro ${input_text}"

# response = model.generate_content(prompt)
# generated_story = response.text

# print("Translate:", generated_story)


import google.generativeai as genai

# Set up API key
genai.configure(api_key="AIzaSyDlbiCluy-T7XQjcFN8SmGIawGBoniJDk0")

# Create a model instance
model = genai.GenerativeModel("gemini-1.5-flash")

# Define input statements
input_text = "Instated of resorting to sarcasm , just try to think what can we do to find a sloution for this problem"
language = "اللهجة السعودية بالعربية"

# Ask Gemini to translate
prompt = f"ترجم الجملة دي إلى ${language} بدون مقدمة أو شرح: \"{input_text}\""

response = model.generate_content(prompt)
generated_translation = response.text

print("الترجمة:", generated_translation)


"""
Gemini API – Multi‑key round‑robin + graceful 429 retry
------------------------------------------------------
• استخدم أكثر من مفتاح لزيادة الحد اليومي (50 طلب لكل مفتاح فري).
• يشيل علامة $ من الـ prompt ويضمن خروج النص بالحروف العربية.
• يعيد المحاولة تلقائياً بمفتاح آخر لو طلع 429 (quota exceeded).
"""

# import os, itertools, time
# import google.generativeai as genai
# from google.api_core.exceptions import ResourceExhausted, InvalidArgument

# # ضع مفاتيحك مفصولة بفواصل أو خزّنها في متغيّر بيئة
# KEYS = [
#     "AIzaSyBHSBP37qTQ0qztvacWDwLjNVYrxsGdiQY",
#     "AIzaSyDL8oopr4R_z_9gRtYuYQxc5qjnE7hKvzA",
#     "AIzaSyCmfITvO_TU16wpfuyJ5DmhxFZUvT6s0do",
# ]
# key_cycle = itertools.cycle(KEYS)

# def get_model():
#     """يختار المفتاح التالي ويُرجع نموذج Gemini مهيّأ به."""
#     api_key = next(key_cycle)
#     genai.configure(api_key=api_key)
#     return genai.GenerativeModel("gemini-1.5-pro-latest")

# def translate(text: str, accent: str) -> str:
#     prompt = (
#         f"ترجم الجملة التالية إلى {accent} بالحروف العربية فقط "
#         f"وبدون أي مقدمة أو شرح:\n\"{text}\""
#     )

#     for _ in range(len(KEYS)):               # جرّب بعدد المفاتيح المتاحة
#         try:
#             model = get_model()
#             resp  = model.generate_content(prompt)
#             return resp.text.strip()

#         except ResourceExhausted:
#             # المفتاح ده خلّص حصّته → جرّب المفتاح التالي فورًا
#             print("Quota exceeded for this key, switching to next key…")
#             continue

#         except InvalidArgument as e:
#             raise RuntimeError(f"Prompt error: {e.message}") from None

#     # لو كل المفاتيح خلصت حصّتها
#     raise RuntimeError("All API keys exhausted. Please wait for quota reset.")

# # -------- استخدم الدالة ------------
# if __name__ == "__main__":
#     input_text = (
#         "Instead of resorting to sarcasm, just try to think what we can do "
#         "to find a solution for this problem."
#     )
#     accent      = "اللهجة السعودية بالعربية"

#     try:
#         result = translate(input_text, accent)
#         print("الترجمة:", result)

#     except RuntimeError as err:
#         print("خطأ:", err)
