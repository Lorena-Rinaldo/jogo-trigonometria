"""Configura o cliente do Supabase usado pelos services."""

import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()


def get_supabase_client():
    """Cria o cliente Supabase a partir das variáveis do arquivo .env."""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SECRET_KEY") or os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise RuntimeError(
            "Configure SUPABASE_URL e SUPABASE_SECRET_KEY no arquivo .env."
        )

    return create_client(url, key)


supabase = get_supabase_client()
