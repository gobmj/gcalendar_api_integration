# Python on Replit

Welcome to Python on Replit! This README provides you with a quick start guide to get your Python projects up and running seamlessly.

## Getting Started

1. **Secret Key Setup**
   To enhance the security of your project, we recommend setting up a secret environment variable for sensitive data. Follow these steps to generate a secure random token for your `SECRET_KEY`:

   - Open the shell by clicking on the shell icon.
   - Type the following Python code and press Enter:

     ```python
     import secrets
     secrets.token_urlsafe(32)
     ```

   - Copy the generated token and create a new secret environment variable named `SECRET_KEY`, then paste the token as its value.

2. **Running Your Project**
   With your `SECRET_KEY` in place, simply hit the run button, and your Python code will start executing.

If you prefer visual guidance, check out our [1-minute walkthrough video](https://www.loom.com/share/341b5574d12040fb9fcbbff150777f1c) for a step-by-step demonstration.

## Installing Packages

Adding external packages to your project is a breeze on Replit. You have two options:

1. **Import Directly in Your Code**
   - To use a package, import it directly in the Python file where you need it.
   - When you hit the run button, Replit will automatically install the required packages for you.

   Example:
   ```python
   import math
   import pandas as pd
   ```

2. **Use the Replit Packager Interface**
   - Alternatively, you can manage your project's packages using the Replit packager interface located in the left sidebar.

## Need Help?

If you encounter any issues or need assistance, we've got you covered:

- Explore our comprehensive [documentation](https://docs.replit.com) for answers to common questions and detailed information about Replit's features.
- Don't hesitate to report any bugs or provide feedback; we value your input. Visit our [support page](https://replit.com/support) to get in touch with us.
