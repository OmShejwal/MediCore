from database import engine, Base, Prediction
from sqlalchemy import inspect, text

def update_schema():
    inspector = inspect(engine)
    
    # Update predictions table
    columns = [col['name'] for col in inspector.get_columns('predictions')]
    if 'ai_advice' not in columns:
        print("Adding 'ai_advice' column to 'predictions' table...")
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE predictions ADD COLUMN ai_advice TEXT"))
            conn.commit()
        print("Column 'ai_advice' added successfully.")
    
    # Update users table
    user_columns = [col['name'] for col in inspector.get_columns('users')]
    if 'preferred_language' not in user_columns:
        print("Adding 'preferred_language' column to 'users' table...")
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE users ADD COLUMN preferred_language VARCHAR(20) DEFAULT 'English'"))
            conn.commit()
        print("Column 'preferred_language' added successfully.")
    
    if 'streak_count' not in user_columns:
        print("Adding 'streak_count' column to 'users' table...")
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE users ADD COLUMN streak_count INTEGER DEFAULT 0"))
            conn.commit()
        print("Column 'streak_count' added successfully.")
        
    if 'last_checkin' not in user_columns:
        print("Adding 'last_checkin' column to 'users' table...")
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE users ADD COLUMN last_checkin DATETIME"))
            conn.commit()
        print("Column 'last_checkin' added successfully.")

    # Update chat_messages table
    chat_columns = [col['name'] for col in inspector.get_columns('chat_messages')]
    if 'rating' not in chat_columns:
        print("Adding 'rating' column to 'chat_messages' table...")
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE chat_messages ADD COLUMN rating INTEGER"))
            conn.commit()
        print("Column 'rating' added successfully.")

if __name__ == "__main__":
    update_schema()
