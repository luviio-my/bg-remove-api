from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    from rembg import remove

    input_data = await file.read()
    output_data = remove(input_data)

    return Response(content=output_data, media_type="image/png")
