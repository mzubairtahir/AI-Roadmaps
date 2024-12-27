#!/bin/bash

# Check if a message was provided
if [ -z "$1" ]; then
    echo "Usage: source makemigrations.sh <migration_message>"
    return  
fi

# Generate the migration
alembic revision --autogenerate -m "$1"

# Inform the user that the migration has been created
echo "Migration created with message: '$1'"
