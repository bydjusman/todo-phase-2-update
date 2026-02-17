# Architecture Specification: Phase 2 Todo Web App

## 1. Monorepo Folder Structure

```
todo-app/
├── .specify/                     # SpecKit Plus configuration and templates
├── apps/
│   ├── client/                   # Next.js frontend application
│   │   ├── components/           # React components
│   │   ├── pages/                # Next.js pages
│   │   ├── lib/                  # Client utilities and API calls
│   │   ├── public/               # Static assets
│   │   └── styles/               # Global styles
│   └── server/                   # FastAPI backend application
│       ├── api/                  # API routes
│       ├── models/               # Database models
│       ├── schemas/              # Pydantic schemas
│       ├── services/             # Business logic
│       ├── middleware/           # Authentication and other middleware
│       ├── database/             # Database connection and setup
│       └── tests/                # Backend tests
├── packages/                     # Shared packages and utilities
│   ├── types/                    # Shared TypeScript types
│   └── common/                   # Shared utilities
├── specs/                        # Feature specifications and architecture docs
│   └── architecture.md           # This document
├── history/                      # Prompt history and ADRs
├── .env                          # Environment variables
├── docker-compose.yml            # Docker configuration
└── README.md                     # Project documentation
```

## 2. High-Level Data Flow Diagram

```mermaid
graph TD
    A[User] --> B[Next.js Frontend]
    B --> C{API Request}
    C --> D[Better Auth JWT]
    C --> E[REST Endpoints /api/tasks]
    D --> F[FastAPI Backend]
    E --> F
    F --> G[Neon Database]
    G --> F
    F --> B
    B --> A
```

### Data Flow Steps:
1. User interacts with Next.js frontend
2. Frontend makes authenticated requests to backend
3. Better Auth provides JWT token validation
4. FastAPI processes requests and interacts with Neon database
5. Data flows back to frontend for display

## 3. Authentication Flow (Better Auth → JWT → FastAPI)

### Authentication Process:
1. **User Registration/Login**: Better Auth handles user registration and authentication
2. **JWT Token Generation**: Better Auth generates JWT tokens upon successful authentication
3. **Token Storage**: Tokens stored in httpOnly cookies for security
4. **Request Authentication**: Frontend includes JWT in API requests
5. **Token Validation**: FastAPI middleware validates JWT tokens
6. **User Context**: Validated user context passed to API endpoints

### Implementation Details:
- Use Better Auth with Next.js middleware
- JWT tokens with proper expiration times
- FastAPI dependency to extract and validate user from JWT
- Refresh token mechanism for seamless experience

## 4. Recommended REST Endpoints (clean /api/tasks style)

### Task Management Endpoints:
```
GET    /api/tasks          # Get all tasks for authenticated user
GET    /api/tasks/{id}     # Get specific task by ID
POST   /api/tasks          # Create new task
PUT    /api/tasks/{id}     # Update existing task
DELETE /api/tasks/{id}     # Delete specific task
```

### User Management Endpoints:
```
POST   /api/auth/register  # User registration (handled by Better Auth)
POST   /api/auth/login     # User login (handled by Better Auth)
GET    /api/auth/me        # Get current user info
POST   /api/auth/logout    # User logout
```

### Additional Endpoints:
```
GET    /api/health         # Health check endpoint
GET    /api/meta           # System metadata
```

### API Response Format:
```json
{
  "success": true,
  "data": {},
  "message": "Success message"
}
```

## 5. Database Connection Strategy for Neon

### Neon Configuration:
- Use Neon's PostgreSQL database as primary data store
- Connection pooling configuration with pgBouncer
- Environment-based configuration for dev/prod
- SSL encryption for all connections

### Connection Management:
- SQLAlchemy async engines with Neon connection string
- Connection pooling with min/max size configuration
- Automatic reconnection logic
- Health check endpoints for database connectivity

### Environment Variables for Neon:
```
NEON_DATABASE_URL=postgresql://user:password@ep-xxx.us-east-1.aws.neon.tech/dbname
NEON_POOL_MIN_SIZE=1
NEON_POOL_MAX_SIZE=10
NEON_SSL_MODE=require
```

### Table Structure:
- Users table for authentication data
- Tasks table with foreign key to users
- Indexes on frequently queried fields
- Proper constraints and relationships

## 6. Key Security Decisions

### Authentication Security:
- JWT tokens with short expiration (15 minutes)
- Refresh tokens with longer expiration (7 days)
- HttpOnly, Secure, SameSite cookies for token storage
- CSRF protection using double-submit cookies

### API Security:
- Rate limiting on authentication endpoints
- Input validation using Pydantic schemas
- SQL injection prevention via SQLAlchemy ORM
- XSS prevention with Content Security Policy

### Data Security:
- Password hashing using bcrypt
- Data encryption at rest with Neon features
- Audit logging for sensitive operations
- Regular security scanning and dependency updates

### Transport Security:
- HTTPS enforcement
- HTTP security headers
- CORS policy allowing only frontend origin
- HSTS header for secure connections

### Monitoring and Logging:
- Structured logging for security events
- Failed authentication attempt tracking
- Unusual activity detection
- Log retention and rotation policies

## 7. Additional Architecture Considerations

### Performance:
- Caching layer using Redis for frequently accessed data
- Database query optimization with proper indexing
- CDN for static assets
- Lazy loading for UI components

### Scalability:
- Stateless API design
- Horizontal scaling capability
- Database read replicas support
- Microservice readiness (if needed in future)

### Testing Strategy:
- Unit tests for business logic
- Integration tests for API endpoints
- End-to-end tests for critical user flows
- Security testing for authentication flow