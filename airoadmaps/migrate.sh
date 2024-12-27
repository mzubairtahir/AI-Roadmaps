
#!/bin/bash

# Apply the latest migration
alembic upgrade head

# Inform the user that the migration has been applied
echo "Migrated to the latest version."
