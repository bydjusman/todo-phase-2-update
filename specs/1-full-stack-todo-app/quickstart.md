# Quickstart Guide: Full-Stack Todo Web Application

## Development Setup

### Prerequisites
- Node.js (v18 or higher)
- Python (3.9 or higher)
- PostgreSQL-compatible database (Neon recommended)
- bun package manager (or npm/yarn)

### Initial Setup

1. **Clone and prepare the repository:**
   ```bash
   # Navigate to your project root
   cd todo-app-phase-2
   ```

2. **Install dependencies:**
   ```bash
   # Install frontend dependencies
   cd apps/client
   bun install

   # Install backend dependencies
   cd ../server
   pip install -r requirements.txt
   # If no requirements.txt exists yet, create it:
   pip install fastapi uvicorn sqlmodel python-jose python-dotenv python-multipart
   ```

3. **Set up environment variables:**
   ```bash
   # Create .env file in both frontend and backend
   # Backend .env (apps/server/.env):
   DATABASE_URL="postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname"
   BETTER_AUTH_SECRET="your-super-secret-jwt-key-here"

   # Frontend .env (apps/client/.env):
   NEXT_PUBLIC_API_URL="http://localhost:8000"
   NEXT_PUBLIC_BETTER_AUTH_URL="http://localhost:3000"
   BETTER_AUTH_SECRET="your-super-secret-jwt-key-here"
   ```

4. **Set up the database:**
   ```bash
   cd apps/server
   # Run initial migrations or create tables
   python -c "
   from sqlmodel import create_engine, SQLModel
   from models.task import Task
   engine = create_engine('postgresql://...')  # Use your DATABASE_URL
   SQLModel.metadata.create_all(engine)
   "
   ```

## Running the Application

### Development Mode

1. **Start the backend server:**
   ```bash
   cd apps/server
   uvicorn main:app --reload --port 8000
   ```

2. **Start the frontend server:**
   ```bash
   cd apps/client
   bun run dev
   ```

3. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000/api/
   - API Documentation: http://localhost:8000/docs

### Production Mode

1. **Build the frontend:**
   ```bash
   cd apps/client
   bun run build
   ```

2. **Run the backend:**
   ```bash
   cd apps/server
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Key Features and Endpoints

### Authentication Endpoints
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `GET /api/auth/me` - Get current user info

### Task Management Endpoints
- `GET /api/tasks` - Get user's tasks with filtering/pagination
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/{id}` - Get specific task
- `PUT /api/tasks/{id}` - Update task completely
- `PATCH /api/tasks/{id}` - Partially update task
- `DELETE /api/tasks/{id}` - Delete task

### Security Features
- JWT token-based authentication for all task operations
- User data isolation - each user can only access their own tasks
- Input validation and sanitization
- Proper error handling with appropriate HTTP status codes

## Testing the Application

### Manual Testing
1. Register a new user via the frontend
2. Log in and create a few tasks
3. Verify you can edit, complete, and delete your tasks
4. Log out and log in as a different user (if possible) to verify isolation
5. Test error cases (invalid credentials, missing tokens, etc.)

### API Testing
Use a tool like Postman or curl to test API endpoints directly, ensuring:
- Authentication is required for all task operations
- Users can only access their own tasks
- Proper error responses are returned for invalid requests

## Troubleshooting

### Common Issues

**Issue:** Cannot connect to database
- Solution: Verify DATABASE_URL is correct in backend .env file
- Check that Neon project is active and accessible

**Issue:** JWT authentication failing
- Solution: Ensure BETTER_AUTH_SECRET is identical in both frontend and backend .env files

**Issue:** CORS errors
- Solution: Configure CORS middleware in FastAPI to allow your frontend origin

**Issue:** Frontend cannot reach backend
- Solution: Verify NEXT_PUBLIC_API_URL is set correctly in frontend .env file

## Next Steps

1. **Complete the implementation** following the technical plan
2. **Add more tests** to ensure reliability
3. **Deploy to production** with proper environment configuration
4. **Monitor performance** and optimize as needed
5. **Add additional features** as defined in the roadmap