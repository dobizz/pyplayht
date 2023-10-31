# Define the path to the requirements file
if [ -f "requirements-dev.txt" ]; then
    requirements_file="requirements-dev.txt"
elif [ -f "../requirements-dev.txt" ]; then
    requirements_file="../requirements-dev.txt"
else
    echo "No requirements file found. Please make sure requirements-dev.txt exists in the current directory or one level up."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip is not installed. Please install Python and try again."
    exit 1
fi

# Install requirements
pip install -r "$requirements_file"

# Check if the installation was successful
if [ $? -eq 0 ]
then
    echo "Requirements installed successfully."
else
    echo "Failed to install requirements."
fi

# Install pre-commit hooks
pre-commit install
pre-commit install --hook-type commit-msg --hook-type pre-push
