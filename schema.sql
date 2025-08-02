-- PostgreSQL DDL for products table
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    sku VARCHAR(64) NOT NULL UNIQUE,
    description TEXT,
    price NUMERIC(12,2) NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Index for searching by name
CREATE INDEX IF NOT EXISTS idx_products_name ON products (name);
-- Unique index is implicit in UNIQUE constraint on sku
