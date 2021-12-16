from website import app
import sys

app = app()

if __name__ == "__main__":
    app.run(debug=True)
    sys.exit(0)