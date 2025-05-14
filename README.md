# AI-Powered Password Strength Checker with Feedback

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ## Overview

This project is a simple password strength checker that goes beyond just scoring your password. It uses a rule-based system, informed by common password weaknesses identified through AI research, to provide specific and actionable feedback on how to improve your password's security. This was created as part of the 3MTT Learning Community challenge.

## Features

* **Strength Assessment:** Determines if a password is weak, medium, or strong.
* **Detailed Feedback:** Provides specific suggestions on how to make a password more secure (e.g., increasing length, adding different character types, avoiding common patterns).
* **AI-Informed Rules:** The assessment logic incorporates insights from AI analysis of prevalent password cracking techniques.
* **Simple Command-Line Interface:** Easy to run using Python in a terminal (like the one in Pydroid 3).

## How to Use

1.  **Prerequisites:** You need to have Python 3 installed on your system (Pydroid 3 on Android).
2.  **Download the Script:** Download the `password_checker.py` file from this repository.
3.  **Run the Script:** Open a terminal or the Pydroid 3 terminal and navigate to the directory where you saved the file. Run the script using the command:
    ```bash
    python password_checker.py
    ```
4.  **Enter Password:** The script will prompt you to enter a password. Type your password and press Enter.
5.  **View Results:** The script will display the strength of your password and provide suggestions for improvement, if any.

## AI in Action (Explanation for Users)

While this version primarily uses a rule-based system, the rules themselves are designed based on patterns and weaknesses that AI algorithms have identified in large datasets of cracked passwords. This allows for more intelligent feedback than simple length or character checks. Future versions could incorporate actual machine learning models for more sophisticated analysis.

## 3MTT Learning Community

This project was created as part of the 3MTT (Three Million Technical Talent) Learning Community initiative in Nigeria.

## Collaborators

* [Name Ahmad Ibrahim]
* [Fellow ID FE/23/31537538 ] (if applicable)

## License

[Specify your license here, e.g., MIT License](https://opensource.org/licenses/MIT) ## Acknowledgements

* [Optional: Mention any resources or research that inspired your rules.]

