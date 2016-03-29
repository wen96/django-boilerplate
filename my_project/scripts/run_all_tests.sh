. "$(dirname "$0")/init.sh"

. "$SCRIPTS_DIR/pylint.sh"
python manage.py test
