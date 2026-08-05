# Agent Workflow Rules

When implementing new features for this project, the agent MUST strictly follow this end-to-end SDLC sequence:

1. **Requirement**: Gather full context.
2. **Acceptance Criteria**: Define exactly what done looks like.
3. **Data Model**: Design the schema first.
4. **API Contract**: Define the request/response payloads and routes.
5. **Backend Implementation**: Build the FastAPI logic.
6. **Backend Tests**: Write backend unit/integration tests.
7. **Frontend API Layer**: Wire up Axios/TanStack query wrappers.
8. **Frontend UI**: Build the React components.
9. **Frontend Tests**: Write frontend unit tests.
10. **E2E Flow**: Verify the system from frontend to backend.
11. **Security Review**: Check for vulnerabilities and RBAC enforcement.
12. **Performance Review**: Check for caching, lazy loading, optimized queries.
13. **Documentation**: Update `/docs` and inline comments.
14. **CI Verification**: Ensure lint, format, and tests pass.
15. **Definition of Done**: Feature is fully accepted.

The agent should pause and request user feedback at critical transitions (e.g., after API Contract, before Frontend UI) using the `implementation_plan.md` artifact.

## Software Architecture

All features MUST be designed and implemented adhering to the following layered architecture:

```text
          ┌─────────────┐
          │    Web      │
          │   Next.js   │
          └──────┬──────┘
                 │
          ┌──────▼──────┐
          │ API Client  │
          │ Query/State │
          └──────┬──────┘
                 │
          ┌──────▼──────┐
          │   FastAPI   │
          │ REST API    │
          └──────┬──────┘
                 │
    ┌────────────▼────────────┐
    │ Service / Repository    │
    └────────────┬────────────┘
                 │
          ┌──────▼──────┐
          │ PostgreSQL  │
          └─────────────┘
```

**Architecture Rules:**
1. **Frontend (Next.js)**: Handles presentation, server/client components, and routing.
2. **API Client Layer**: Handles all network requests, TanStack Query caching, and state management via Zustand.
3. **API Controllers (FastAPI)**: Responsible *only* for HTTP request/response validation, route definition, and payload formatting.
4. **Service / Repository Layer**: Contains all business logic (Services) and database interactions (Repositories). Controllers MUST NOT execute raw SQL or ORM queries directly.
5. **Database (PostgreSQL)**: The single source of truth for persistent relational data.