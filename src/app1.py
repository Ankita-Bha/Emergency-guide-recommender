from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
import google.generativeai as genai

app = FastAPI()

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='2004',  # Your MySQL password
        database='golden_hours'  # Your database name
    )

# Generative AI setup (Gemini API)
genai.configure(api_key='AIzaSyAJZLxr9aoFRCWrh_0JXU-abaWYSyHjFnA')  # Replace with your actual Gemini API key

# Models for API
class UserDetails(BaseModel):
    name: str
    age: int
    gender: str
    phone: str
    address: str

class ParentDetails(BaseModel):
    user_id: int
    name: str
    medical_history: str

class EmergencyContact(BaseModel):
    user_id: int
    contact_name: str
    phone: str
    relationship: str

# API to add user details
@app.post("/add_user/")
async def add_user(user: UserDetails):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO user_details (name, age, gender, phone, address) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (user.name, user.age, user.gender, user.phone, user.address))
        conn.commit()
        return {"message": "User added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# API to add parent details
@app.post("/add_parent/")
async def add_parent(parent: ParentDetails):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO parent_details (user_id, name, medical_history) VALUES (%s, %s, %s)"
        cursor.execute(query, (parent.user_id, parent.name, parent.medical_history))
        conn.commit()
        return {"message": "Parent details added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# API to add emergency contact
@app.post("/add_contact/")
async def add_contact(contact: EmergencyContact):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO emergency_contacts (user_id, contact_name, phone, relationship) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (contact.user_id, contact.contact_name, contact.phone, contact.relationship))
        conn.commit()
        return {"message": "Emergency contact added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# Generative AI Prediction using Gemini
@app.get("/predict_suggestions/{user_id}")
async def predict_suggestions(user_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_details WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        conn.close()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        prompt = f"Provide medical guidance based on the following data: {user}"
        response = genai.generate_text(model="gemini-1.5-pro", prompt=prompt)

        return {"suggestions": response.text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app1:app", host="0.0.0.0", port=8000, reload=True)
