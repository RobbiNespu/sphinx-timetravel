# Publishing Guide for Sphinx TimeTravel

This guide explains how to publish the `sphinx-timetravel` extension to PyPI.

## Prerequisites

1. **PyPI Account**: Create an account on [PyPI](https://pypi.org/account/register/) if you don't have one
2. **TestPyPI Account** (optional but recommended): Create an account on [TestPyPI](https://test.pypi.org/account/register/) for testing
3. **API Tokens**: Generate API tokens for both PyPI and TestPyPI:
   - Go to Account Settings → API tokens
   - Create a new token with appropriate scope
   - Save the token securely (you'll need it for publishing)

## Development Dependencies

Install the required tools for building and publishing:

```bash
pip install build twine
```

Or install with dev dependencies:

```bash
pip install -e ".[dev]"
```

## Pre-Publication Checklist

Before publishing, ensure:

- [ ] Version number is updated in both `setup.py` and `pyproject.toml`
- [ ] `CHANGELOG.md` is updated with new version and changes
- [ ] All tests pass
- [ ] Documentation is up to date
- [ ] Code is clean and follows best practices
- [ ] `README.md` is accurate and complete
- [ ] License file is present and correct
- [ ] `MANIFEST.in` includes all necessary files

## Version Management

Update the version number in two places:

1. **setup.py**: Update the `version` parameter
2. **pyproject.toml**: Update the `version` field

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR** (1.0.0): Breaking changes
- **MINOR** (0.1.0): New features, backward compatible
- **PATCH** (0.1.1): Bug fixes, backward compatible

Example:
```python
# setup.py
version='0.1.2',

# pyproject.toml
version = "0.1.2"
```

## Building the Distribution

### 1. Clean Previous Builds

```bash
# Remove old build artifacts
rm -rf dist/
rm -rf build/
rm -rf *.egg-info
```

### 2. Build Source and Wheel Distributions

```bash
python -m build
```

This creates:
- `dist/sphinx_timetravel-X.X.X.tar.gz` (source distribution)
- `dist/sphinx_timetravel-X.X.X-py3-none-any.whl` (wheel distribution)

### 3. Verify the Build

Check the built files:

```bash
# List files in the distribution
tar -tzf dist/sphinx_timetravel-*.tar.gz

# Or on Windows
python -m zipfile -l dist/sphinx_timetravel-*.whl
```

## Testing on TestPyPI (Recommended)

Before publishing to the main PyPI, test on TestPyPI:

### 1. Upload to TestPyPI

```bash
python -m twine upload --repository testpypi dist/*
```

You'll be prompted for:
- Username: `__token__`
- Password: Your TestPyPI API token

### 2. Test Installation from TestPyPI

```bash
# Create a clean virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ sphinx-timetravel
```

### 3. Verify Installation

```bash
python -c "import sphinx_timetravel; print(sphinx_timetravel.__version__)"
```

## Publishing to PyPI

Once tested on TestPyPI, publish to the main PyPI:

### 1. Upload to PyPI

```bash
python -m twine upload dist/*
```

You'll be prompted for:
- Username: `__token__`
- Password: Your PyPI API token

### 2. Verify Publication

Check your package on PyPI:
- Visit: https://pypi.org/project/sphinx-timetravel/
- Verify version, description, and files are correct

### 3. Test Installation

```bash
# Create a clean virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from PyPI
pip install sphinx-timetravel
```

## Complete Publishing Workflow

Here's a complete workflow script:

```bash
#!/bin/bash
# publish.sh - Complete publishing workflow

set -e  # Exit on error

# 1. Clean previous builds
echo "Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info

# 2. Update version (manual step - edit setup.py and pyproject.toml)
echo "Please update version in setup.py and pyproject.toml"
read -p "Press Enter when version is updated..."

# 3. Build distributions
echo "Building distributions..."
python -m build

# 4. Check distributions
echo "Checking distributions..."
python -m twine check dist/*

# 5. Upload to TestPyPI
echo "Uploading to TestPyPI..."
python -m twine upload --repository testpypi dist/*

# 6. Test installation from TestPyPI
echo "Testing installation from TestPyPI..."
python -m venv test_env
source test_env/bin/activate
pip install --index-url https://test.pypi.org/simple/ sphinx-timetravel
deactivate
rm -rf test_env

# 7. Upload to PyPI
read -p "TestPyPI upload successful. Upload to PyPI? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    python -m twine upload dist/*
    echo "Published to PyPI!"
fi
```

## Using Environment Variables for Tokens

For automation, you can use environment variables:

```bash
# Set tokens
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-YourTokenHere  # For PyPI
export TWINE_REPOSITORY_URL=https://test.pypi.org/legacy/  # For TestPyPI

# Upload
python -m twine upload dist/*
```

## Troubleshooting

### Common Issues

1. **"File already exists"**
   - Version number must be incremented
   - Cannot re-upload the same version

2. **"Invalid distribution"**
   - Run `python -m twine check dist/*` to validate
   - Ensure `MANIFEST.in` includes all necessary files

3. **"Authentication failed"**
   - Verify API token is correct
   - Ensure token has appropriate scope
   - Use `__token__` as username, not your actual username

4. **"Package not found after upload"**
   - Wait a few minutes for PyPI to process
   - Check for any error messages in the upload output

### Validating Package

Before uploading, validate your package:

```bash
# Check package metadata
python -m twine check dist/*

# Verify package structure
python -m build --sdist --wheel
```

## Post-Publication

After successful publication:

1. **Create a Git Tag**
   ```bash
   git tag -a v0.1.2 -m "Release version 0.1.2"
   git push origin v0.1.2
   ```

2. **Create a GitHub Release**
   - Go to GitHub repository
   - Click "Releases" → "Create a new release"
   - Tag the version
   - Add release notes from CHANGELOG.md

3. **Update Documentation**
   - Update installation instructions if needed
   - Add any new features to README.md

4. **Announce (Optional)**
   - Post on social media
   - Update project website
   - Notify users if breaking changes

## Automated Publishing with GitHub Actions

You can automate publishing with GitHub Actions. Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [created]

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build twine
      
      - name: Build package
        run: python -m build
      
      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: python -m twine upload dist/*
```

Add `PYPI_API_TOKEN` to your GitHub repository secrets.

## Security Best Practices

1. **Never commit API tokens** to version control
2. **Use API tokens** instead of passwords
3. **Rotate tokens** periodically
4. **Use TestPyPI** for testing before main PyPI
5. **Review package contents** before uploading

## Additional Resources

- [PyPI Documentation](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Python Packaging Guide](https://packaging.python.org/)
- [Semantic Versioning](https://semver.org/)

## Quick Reference

```bash
# Build
python -m build

# Check
python -m twine check dist/*

# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Upload to PyPI
python -m twine upload dist/*

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ sphinx-timetravel

# Install from PyPI
pip install sphinx-timetravel
```

