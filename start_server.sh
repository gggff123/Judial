curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
python start_server.py