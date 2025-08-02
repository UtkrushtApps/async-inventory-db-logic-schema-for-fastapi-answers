# Solution Steps

1. Design a normalized products table schema suitable for inventory, including id, name, sku, description, price, quantity, created_at, updated_at. Ensure strong types, not null, and unique constraints for SKU. Add indexes on 'name' and 'sku'. Write the schema as PostgreSQL DDL in schema.sql.

2. Implement the SQLAlchemy async Product model (models.py) with fields mapped to match the Postgres types. Ensure that best practices (unique constraint, indexes, appropriate field types) are followed.

3. Write async CRUD functions in crud.py for creating a product (inserting, returning the created Product, handling IntegrityError for uniqueness) and retrieving all products (get_products). Ensure all DB calls are async and compatible with FastAPI dependency-injected sessions.

4. Add an optional utility function in crud.py for fetching a product by SKU, to demonstrate enforced uniqueness and serve future use-cases.

5. Make sure the CRUD operations are fully async (awaited properly), aligning with SQLAlchemy async best practices.

6. Verify that constraints are declared both in the Python model and the schema.sql.

7. Check that the model, CRUD functions, and schema are ready to be used with FastAPI routes and startup DB migration/init logic.

