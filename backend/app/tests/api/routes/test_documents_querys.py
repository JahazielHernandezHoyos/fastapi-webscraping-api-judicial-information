import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed

from fastapi.testclient import TestClient
from sqlmodel import Session

from backend.utils.scrape_judicial_processes import test_parallel_requests


def test_parallel_queries(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    test_parallel_requests()
