
# SweetSpot Dessert Parlour

Welcome to the official repository of SweetSpot Dessert Parlour, the go-to website for all dessert enthusiasts! Our website offers a delightful experience for users to explore our extensive menu of desserts, place orders online, and keep up with our latest sweet offerings and events.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing) 
- [Code Testing](#code-testing)
- [Credits](#credits)
- [Contributing](#contributing)
- [Feedback](#feedback)
- [License](#license)

## Introduction

SweetSpot Dessert Parlour brings the joy of sweet indulgence to your doorstep. With our intuitive and beautifully designed web platform, you can easily create recipes, create reservations and enjoy the delightful experience of being part of our service. 
## Features:

As of right now, our website is currently within its beta version. This means that whilst the current features are few and limited, it gives us room to expand and improve the overall User experience. Some of our current features include: 

- **Creating Reservations:** Users can create a reservation to come and visit our dessert parlour, in person. These reservations can be updated, edited or deleted, according to the user. 
- **Create recipes** Customize and create your own desserts that can be viewed on our public forum!.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8+
- pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/sweetspot-dessert-parlour.git
   ```
2. Navigate to the project directory:
   ```
   cd sweetspot-dessert-parlour
   ```
3. Create a virtual environment (optional):
   ```
   virtualenv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the development server:

```
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/` in your web browser to view the application.

## Testing Overview
We made sure that everything works well on our website by testing the Accounts, Desserts, and Reservations sections. We checked that every part works, is easy to use, and that there are no problems.

### Testing User Accounts
We did different tests to make sure that people can sign up, log in, and manage their profiles without any issues.

- **Sign-up Tests**: We checked that new users can create an account without any trouble.
- **Login Tests**: We tried different usernames and passwords to make sure that only the right users can log in.
- **Profile Tests**: We made sure that users can change their account information and that no one else can mess with it.

## Testing Overview
The application was thoroughly tested across the Accounts, Desserts, and Reservations sections to ensure optimal functionality, ease of use, and security.

### Testing User Accounts
Various checks were carried out to confirm that the processes of signing up, logging in, and managing user profiles were functioning correctly.

- **Sign-up Tests**: The account creation process was examined to validate successful registration for new users.
- **Login Tests**: Multiple username and password combinations were tested to verify that access is granted only to users with correct credentials.
- **Profile Tests**: It was confirmed that users could update their account details securely, and that these profiles could not be altered by unauthorized users.

### Testing Desserts
The display and management of dessert entries on the website underwent a series of tests.

- **Display Tests**: It was ensured that all dessert listings were presented accurately to users and that individual dessert details were accessible.
- **Add/Edit Tests**: The functionality to create and modify dessert entries through forms was automated and tested for correctness.
- **Delete Tests**: The ability to delete dessert entries was tested, with immediate reflection of these changes in the database confirmed.

### Testing Reservations
The reservation system was scrutinized for its capacity to handle creation, modification, and cancellation effectively.

- **Making Reservations**: The reservation form was tested for accuracy in capturing and recording new reservations.
- **Changing Reservations**: The system was tested to ensure that users could alter their reservations and that such changes were preserved correctly.
- **Cancelling Reservations**: The deletion of reservations was tested, ensuring that the system processed cancellations accurately and updated resource availability accordingly.

## Code Testing
- CSS passed with no errors using validator
- Python code passed with no errors using validator
- HTML code still needs to be tended to

## Credits
- Most templates/views/forms/models within SweetSpot app are credited to repository: Sweet_SpotV2 before modification. 
- All code written was orginally created by myself before being passed through AI assistant tools such as ChatGpt for seemless functionality and improved coding.  
- Most sections within read.me file was written originally before also being passed through ChatGpt for better formatting. 

## Contributing

We welcome contributions to SweetSpot Dessert Parlour! If you have suggestions or want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/NewFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some NewFeature'`).
5. Push to the branch (`git push origin feature/NewFeature`).
6. Open a pull request.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests to us.


## Feedback

If you have any feedback, please reach out to us at contact@sweetspot.com.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

