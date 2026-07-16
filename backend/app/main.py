from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.user import router as user_router
from app.routers.post import router as post_router
from app.routers.comment import router as comment_router
from app.routers.follow import router as follow_router
from app.routers.like import router as like_router

from app.core.database import Base, engine


from app.models.user import User
from app.models.post import Post
from app.models.comment import Comment
from app.models.like import Like
from app.models.follow import Follow


app = FastAPI(
    title="LinkedIn Lite API",
    description="Backend API for LinkedIn Lite",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

Base.metadata.create_all(bind=engine)

# -----------------------------
# CORS Configuration
# -----------------------------

'''app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)'''


# -----------------------------
# Root Endpoint
# -----------------------------

@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to LinkedIn Lite API",
        "status": "Running"
    }


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health", tags=["Health"])
async def health():
    return {
        "status": "healthy"
    }


# -----------------------------
# Register Routers
# -----------------------------

app.include_router(
    user_router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    post_router,
    prefix="/posts",
    tags=["Posts"]
)

app.include_router(
    comment_router,
    prefix="/comments",
    tags=["Comments"]
)


app.include_router(
    follow_router,
    prefix="/follow",
    tags=["Follow"]
)

app.include_router(
    like_router,
    prefix="/likes",
    tags=["Likes"]
)