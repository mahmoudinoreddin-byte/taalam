#!/bin/bash

echo ""
echo "╔═══════════════════════════════════════╗"
echo "║      Portfòlio Platform Setup         ║"
echo "╚═══════════════════════════════════════╝"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌  Python 3 not found. Please install Python 3.10+"
    exit 1
fi

echo "✓  Python found: $(python3 --version)"

# Create virtual environment
echo ""
echo "→  Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "→  Installing dependencies..."
pip install -q -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌  Dependency installation failed."
    exit 1
fi
echo "✓  Dependencies installed"

# Run migrations
echo ""
echo "→  Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser prompt
echo ""
echo "→  Create admin superuser"
python manage.py createsuperuser

# Collect static (optional for dev)
# python manage.py collectstatic --noinput

echo ""
echo "╔═══════════════════════════════════════════════════════╗"
echo "║  ✓  Setup complete! Run the server:                   ║"
echo "║                                                        ║"
echo "║     source venv/bin/activate                           ║"
echo "║     python manage.py runserver                         ║"
echo "║                                                        ║"
echo "║  Then open:  http://127.0.0.1:8000                     ║"
echo "║  Admin:      http://127.0.0.1:8000/admin               ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""
