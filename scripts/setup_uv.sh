#!/bin/bash
set -eux

# Download and install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Setup completions for bash
grep -qxF 'eval "$(uv generate-shell-completion bash)"' ~/.bashrc || echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc

# Install Python and dependencies
[ -f pyproject.toml ] && uv sync

echo "UV has been successfully set up."
