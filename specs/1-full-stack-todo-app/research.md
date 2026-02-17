# Research Findings: Full-Stack Todo Web Application

## Decision 1: Better Auth + FastAPI JWT Integration

**Decision**: Use python-jose library to verify Better Auth JWT tokens in FastAPI

**Rationale**: Better Auth generates standard JWT tokens that can be verified using industry-standard libraries. Python-jose is compatible with Better Auth's token format and provides secure verification capabilities.

**Alternatives considered**:
- PyJWT: Also compatible but python-jose is recommended for async environments
- Custom verification: Would be complex and error-prone
- Using HTTP-only cookies only: Still requires backend verification for API endpoints

## Decision 2: Neon PostgreSQL Configuration

**Decision**: Use environment-specific connection strings with appropriate pool settings

**Rationale**: Neon Serverless handles connection pooling effectively, so we don't need aggressive local pooling. Standard connection parameters will work across environments.

**Configuration**:
- For development: Standard PostgreSQL connection string format
- Pool settings: Conservative settings (min 1, max 10) to work well with Neon's serverless model
- Connection timeout: 30 seconds for development, 10 seconds for production

**Alternatives considered**:
- Aggressive connection pooling: Could overwhelm serverless database
- Connection strings with embedded credentials: Less secure than environment variables

## Decision 3: JWT Secret Management

**Decision**: Use a shared environment variable for BETTER_AUTH_SECRET used by both frontend and backend

**Rationale**: Better Auth uses the same secret for generating tokens on the frontend and verifying them elsewhere. The secret must be available to both the Next.js frontend (for auth) and FastAPI backend (for verification).

**Implementation**:
- Store secret in environment: `BETTER_AUTH_SECRET`
- Frontend: NEXT_PUBLIC_BETTER_AUTH_SECRET (Next.js prefixes public variables)
- Backend: BETTER_AUTH_SECRET (regular environment variable)
- Both values must be identical

**Alternatives considered**:
- Separate secrets: Would break the authentication flow
- Dynamic secret exchange: Too complex for this use case
- Public key cryptography: Not supported by Better Auth's basic configuration

## Implementation Notes

### JWT Verification Process
1. Better Auth generates JWT tokens with user information
2. Frontend stores these tokens in cookies (httpOnly for security)
3. API requests include tokens in Authorization header
4. FastAPI backend verifies JWT using the shared secret
5. Verified user information is extracted and used for authorization checks

### Security Considerations
- JWT tokens should have short expiration times
- Refresh token mechanism should be implemented for better UX
- All sensitive operations must validate user ownership
- No user should be able to access another user's data through any endpoint

## Next Steps

With these clarifications resolved, we can proceed to implement:
1. Database models using SQLModel
2. JWT verification middleware in FastAPI
3. Better Auth integration in Next.js
4. Task CRUD endpoints with proper authorization
5. Frontend components for task management