# HyperForms

A simple Django project for handling requests and rendering templates of web pages. Learning how to save and retrieve data from a database.

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AstronauticalCodes/HyperForms.git
   ```

2. Navigate to the project directory:
   ```bash
   cd HyperForms
   ```

3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply the migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

Navigate to `http://127.0.0.1:8000/` in your web browser to access the application. The homepage provides a link to visit the forms.

## Features

- **Register Form**: Users can register by filling out their name, age, and favorite book.
- **Admin Management**: Admins can manage the forms and view submitted data.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
