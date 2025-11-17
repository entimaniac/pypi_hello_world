# Deployment Guide

This guide explains how to deploy the `entimaniac_hello_world` package to PyPI using GitHub Actions.

## Prerequisites

1. A PyPI account (create one at https://pypi.org/account/register/)
2. GitHub repository with the code pushed

## Setup Instructions

### Step 1: Configure PyPI Trusted Publishing

PyPI now supports "Trusted Publishing" which allows GitHub Actions to publish packages without needing API tokens.

1. Go to your PyPI account settings: https://pypi.org/manage/account/
2. Scroll down to "Publishing" section
3. Click "Add a new pending publisher"
4. Fill in the following details:
   - **PyPI Project Name**: `entimaniac_hello_world`
   - **Owner**: Your GitHub username (e.g., `entimaniac`)
   - **Repository name**: `pypi_hello_world`
   - **Workflow name**: `publish-to-pypi.yml`
   - **Environment name**: Leave blank (optional)
5. Click "Add"

### Step 2: Update Package Metadata

Before publishing, update the following in `pyproject.toml`:

- `name`: Change if you want a different package name (must be unique on PyPI)
- `version`: Update version number for each release
- `authors`: Add your name and email
- `project.urls`: Update with your actual GitHub repository URL

### Step 3: Create a Release

The GitHub Action is triggered when you create a new release:

1. Go to your GitHub repository
2. Click on "Releases" in the right sidebar
3. Click "Create a new release"
4. Click "Choose a tag" and create a new tag (e.g., `v0.1.0`)
5. Fill in the release title and description
6. Click "Publish release"

The GitHub Action will automatically:
- Run the tests
- Build the package
- Publish to PyPI

### Step 4: Manual Trigger (Optional)

You can also manually trigger the workflow:

1. Go to the "Actions" tab in your GitHub repository
2. Select "Publish Python Package to PyPI" workflow
3. Click "Run workflow"
4. Select the branch and click "Run workflow"

## Workflow Overview

The GitHub Actions workflow (`.github/workflows/publish-to-pypi.yml`) consists of three jobs:

1. **Test**: Runs the unit tests to ensure code quality
2. **Build**: Builds the source distribution and wheel
3. **Publish**: Publishes the package to PyPI using trusted publishing

## Version Management

To publish a new version:

1. Update the version in `entimaniac_hello_world/__init__.py`
2. Update the version in `pyproject.toml`
3. Commit the changes
4. Create a new release with a corresponding tag (e.g., `v0.2.0`)

## Troubleshooting

### Package name already exists
If the package name is already taken on PyPI, you'll need to choose a different name. Update the `name` field in `pyproject.toml`.

### Trusted publishing not configured
Make sure you've set up the trusted publisher on PyPI before creating a release.

### Tests failing
The workflow will not publish if tests fail. Check the Actions tab for error details.

## Testing Locally

Before publishing, you can test the build locally:

```bash
# Install build tools
pip install build

# Build the package
python -m build

# The built files will be in the dist/ directory
```

## Installing the Published Package

Once published, anyone can install your package:

```bash
pip install entimaniac_hello_world
```

And use it in Python:

```python
from entimaniac_hello_world import hello

print(hello("World"))  # Output: Hello World
```

