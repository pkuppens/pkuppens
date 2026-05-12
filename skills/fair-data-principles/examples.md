# FAIR Data Principles — Implementation Examples

Companion to [SKILL.md](SKILL.md). Contains platform-specific code patterns for C#/.NET and Python/FastAPI, organised by FAIR dimension.

---

## C#/.NET

### F — Findable

#### OpenAPI attributes for discoverability

```csharp
using Microsoft.AspNetCore.Mvc;
using Swashbuckle.AspNetCore.Annotations;

[ApiController]
[Route("api/v1/[controller]")]
[Produces("application/json")]
[SwaggerTag("Patients — demographics and identifiers")]
public class PatientsController : ControllerBase
{
    /// <summary>Search patients by name, identifier, or date of birth.</summary>
    [HttpGet]
    [SwaggerOperation(OperationId = "SearchPatients")]
    [SwaggerResponse(200, "Paginated list of patients")]
    [SwaggerResponse(400, "Invalid filter parameters")]
    public async Task<ActionResult<PagedResult<PatientDto>>> Search(
        [FromQuery] PatientSearchFilter filter,
        [FromQuery] int page = 1,
        [FromQuery] int pageSize = 25)
    {
        // Consistent pagination, filtering, and sorting
        var result = await _patientService.SearchAsync(filter, page, pageSize);
        return Ok(result);
    }
}
```

#### Metadata on Entity Framework models

```csharp
public class DatasetMetadata
{
    public Guid Id { get; set; }
    public string Title { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;

    [MaxLength(2048)]
    public string PersistentUri { get; set; } = string.Empty;

    public List<string> Keywords { get; set; } = [];
    public DateTimeOffset CreatedAt { get; set; }
    public DateTimeOffset ModifiedAt { get; set; }
    public string Version { get; set; } = "1.0.0";
}
```

### A — Accessible

#### JWT authentication middleware

```csharp
builder.Services
    .AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.Authority = builder.Configuration["Auth:Authority"];
        options.Audience = builder.Configuration["Auth:Audience"];
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
        };
    });

builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("DataReader", policy =>
        policy.RequireClaim("scope", "data:read"));
    options.AddPolicy("DataWriter", policy =>
        policy.RequireClaim("scope", "data:write"));
});
```

#### Audit logging middleware

```csharp
public class AuditLoggingMiddleware(RequestDelegate next, ILogger<AuditLoggingMiddleware> logger)
{
    public async Task InvokeAsync(HttpContext context)
    {
        var userId = context.User.FindFirst("sub")?.Value ?? "anonymous";
        var resource = context.Request.Path;
        var method = context.Request.Method;

        logger.LogInformation(
            "Access: {Method} {Resource} by {UserId} at {Timestamp}",
            method, resource, userId, DateTimeOffset.UtcNow);

        await next(context);

        logger.LogInformation(
            "Response: {StatusCode} for {Method} {Resource} by {UserId}",
            context.Response.StatusCode, method, resource, userId);
    }
}
```

### I — Interoperable

#### Content negotiation with multiple formats

```csharp
builder.Services.AddControllers(options =>
{
    options.RespectBrowserAcceptHeader = true;
    options.ReturnHttpNotAcceptable = true;
})
.AddJsonOptions(o => o.JsonSerializerOptions.PropertyNamingPolicy = JsonNamingPolicy.CamelCase)
.AddXmlSerializerFormatters();
```

#### Domain vocabulary references in DTOs

```csharp
public class DiagnosisDto
{
    public Guid Id { get; set; }

    /// <summary>ICD-10 code (e.g. "C61" for prostate cancer).</summary>
    public string IcdCode { get; set; } = string.Empty;

    /// <summary>SNOMED CT concept ID.</summary>
    public string? SnomedCtId { get; set; }

    /// <summary>Display name in the local language.</summary>
    public string DisplayName { get; set; } = string.Empty;

    /// <summary>Coding system URI for interoperability.</summary>
    public string CodingSystem { get; set; } = "http://hl7.org/fhir/sid/icd-10";
}
```

### R — Reusable

#### API versioning

```csharp
builder.Services.AddApiVersioning(options =>
{
    options.DefaultApiVersion = new ApiVersion(1, 0);
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.ReportApiVersions = true;
    options.ApiVersionReader = ApiVersionReader.Combine(
        new UrlSegmentApiVersionReader(),
        new HeaderApiVersionReader("X-Api-Version"));
});

builder.Services.AddApiExplorer(options =>
{
    options.GroupNameFormat = "'v'VVV";
    options.SubstituteApiVersionInUrl = true;
});
```

#### Deprecation via Sunset header

```csharp
[ApiVersion("1.0", Deprecated = true)]
[ApiController]
[Route("api/v{version:apiVersion}/patients")]
public class PatientsV1Controller : ControllerBase
{
    [HttpGet]
    public IActionResult GetAll()
    {
        Response.Headers.Append("Sunset", "Sat, 01 Nov 2025 00:00:00 GMT");
        Response.Headers.Append("Link",
            "</api/v2/patients>; rel=\"successor-version\"");
        return Ok(_service.GetAllLegacy());
    }
}
```

---

## Python / FastAPI

### F — Findable

#### Pydantic models with metadata fields

```python
from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class DatasetMetadata(BaseModel):
    """Rich metadata attached to every dataset for catalogue discovery."""

    id: UUID = Field(default_factory=uuid4, description="Globally unique identifier")
    title: str = Field(..., max_length=256, description="Human-readable title")
    description: str = Field(..., description="What the dataset contains")
    persistent_uri: str = Field(..., description="Permanent URI (DOI or handle)")
    keywords: list[str] = Field(default_factory=list, description="Search terms")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    modified_at: datetime = Field(default_factory=datetime.utcnow)
    version: str = Field(default="1.0.0", pattern=r"^\d+\.\d+\.\d+$")
```

#### Searchable catalogue endpoint

```python
from fastapi import APIRouter, Query

router = APIRouter(prefix="/api/v1/datasets", tags=["Datasets"])


@router.get("/", summary="Search datasets by keyword, tag, or date range")
async def search_datasets(
    q: str | None = Query(None, description="Free-text search"),
    keyword: str | None = Query(None, description="Filter by keyword tag"),
    page: int = Query(1, ge=1),
    page_size: int = Query(25, ge=1, le=100),
) -> dict:
    results = await dataset_service.search(q=q, keyword=keyword, page=page, page_size=page_size)
    return {
        "items": results.items,
        "total": results.total,
        "page": page,
        "page_size": page_size,
    }
```

### A — Accessible

#### OAuth2 dependency injection

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """Validate JWT and return user claims."""
    payload = decode_jwt(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload


async def require_scope(scope: str):
    """Factory for scope-checking dependencies."""

    async def _check(user: dict = Depends(get_current_user)) -> dict:
        if scope not in user.get("scopes", []):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Missing scope: {scope}")
        return user

    return _check
```

#### Audit logging middleware

```python
import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

logger = logging.getLogger("audit")


class AuditLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        user_id = request.state.user.get("sub", "anonymous") if hasattr(request.state, "user") else "anonymous"
        start = time.monotonic()

        logger.info("Access: %s %s by %s", request.method, request.url.path, user_id)
        response = await call_next(request)
        elapsed_ms = (time.monotonic() - start) * 1000

        logger.info(
            "Response: %s for %s %s by %s (%.0f ms)",
            response.status_code, request.method, request.url.path, user_id, elapsed_ms,
        )
        return response
```

### I — Interoperable

#### OpenAPI customisation

```python
from fastapi import FastAPI

app = FastAPI(
    title="Healthcare Data Platform",
    version="1.0.0",
    description="FAIR-compliant API for clinical datasets",
    contact={"name": "Data Platform Team", "email": "data-platform@example.org"},
    license_info={"name": "CC BY 4.0", "url": "https://creativecommons.org/licenses/by/4.0/"},
    servers=[
        {"url": "https://api.example.org", "description": "Production"},
        {"url": "https://staging-api.example.org", "description": "Staging"},
    ],
)
```

#### Domain vocabulary references in models

```python
from pydantic import BaseModel, Field


class Diagnosis(BaseModel):
    """Clinical diagnosis coded with ICD-10 and optionally SNOMED CT."""

    id: str = Field(..., description="Unique diagnosis record ID")
    icd_code: str = Field(..., description="ICD-10 code, e.g. 'C61'")
    snomed_ct_id: str | None = Field(None, description="SNOMED CT concept ID")
    display_name: str = Field(..., description="Human-readable diagnosis name")
    coding_system: str = Field(
        default="http://hl7.org/fhir/sid/icd-10",
        description="URI of the coding system for interoperability",
    )
```

### R — Reusable

#### API versioning via URL path

```python
from fastapi import APIRouter, FastAPI

app = FastAPI()

v1_router = APIRouter(prefix="/api/v1")
v2_router = APIRouter(prefix="/api/v2")


@v1_router.get("/patients", tags=["Patients v1"], deprecated=True)
async def list_patients_v1():
    """Deprecated: use v2. Sunset: 2025-11-01."""
    return {"items": [], "_sunset": "2025-11-01", "_successor": "/api/v2/patients"}


@v2_router.get("/patients", tags=["Patients v2"])
async def list_patients_v2():
    return {"items": [], "total": 0, "page": 1}


app.include_router(v1_router)
app.include_router(v2_router)
```

#### HATEOAS links for discoverability and reusability

```python
from pydantic import BaseModel, Field


class Link(BaseModel):
    href: str
    rel: str
    method: str = "GET"


class PatientResponse(BaseModel):
    id: str
    name: str
    links: list[Link] = Field(default_factory=list)


def build_patient_response(patient_id: str, name: str) -> PatientResponse:
    base = f"/api/v2/patients/{patient_id}"
    return PatientResponse(
        id=patient_id,
        name=name,
        links=[
            Link(href=base, rel="self"),
            Link(href=f"{base}/diagnoses", rel="diagnoses"),
            Link(href=f"{base}/observations", rel="observations"),
            Link(href="/api/v2/patients", rel="collection"),
        ],
    )
```

#### Data lineage in response metadata

```python
from datetime import datetime

from pydantic import BaseModel, Field


class LineageMetadata(BaseModel):
    """Provenance and lineage information attached to dataset responses."""

    source_system: str = Field(..., description="Origin system identifier")
    source_version: str = Field(..., description="Version in the source system")
    ingested_at: datetime = Field(..., description="When data was ingested")
    transformations: list[str] = Field(
        default_factory=list,
        description="Ordered list of transformations applied",
    )
    licence: str = Field(default="proprietary", description="Usage licence identifier")
    quality_score: float | None = Field(None, ge=0.0, le=1.0, description="Data quality score (0-1)")
```
