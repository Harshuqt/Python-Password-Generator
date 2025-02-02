# Python Password Generator

## Introduction
This Python application allows users to generate secure and customized passwords based on user preferences. The password generator features a visual interface, customizable options, and easy customization.

## UI Elements
The application features a modern, intuitive UI with the following key components:
- **Password Display**: A text area where the generated password will be displayed.
- **Password Length**: A slider to set the desired length of the password between 1 and 50 characters.
- **Character Options**: checkboxes to select from uppercase letters, lowercase letters, numbers, and symbols.
- **Generate Button**: Click the button to generate a password with selected character options and length.

## Main Features
1. **Password Length Customization**:
   - Users can set their preferred password length (between 1 and 50 characters).

2. **Character Type Customization**:
   - Users can choose from uppercase letters, lowercase letters, numbers, or symbols to customize the generated password.

3. **Ease of Use**:
   - The interface is intuitive with visual feedback for each input field.
   - Generates a new password by default but allows users to generate and copy their own passwords.

4. **Output Options**:
   - Shows the current password being typed in the display area below the button.
   - Automatically copies the generated password to the clipboard using the "Copy Password" button.

## Customization Notes
The generator is highly customizable with the following options:
1. **Password Length**: Set directly in the slider or change it from the text field.
2. **Character Options**: Toggle between uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), or symbols (!@#$%^&*())
3. **Password Generation**: Generate a new password immediately by clicking the "Generate Password" button.

## Setup Instructions
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Script**:
   ```bash
   python3 pass_gen.py
   ```

## Usage Tips
1. Select at least one character type in the options to ensure security.
2. Use the slider or text field to set your preferred password length.
3. Click the "Copy Password" button and select characters from the UI if you want to generate a new password manually.
4. The "Generate Password" button creates a new password each time it's clicked.

## Notes
- This is the default implementation. To make the generator more powerful or flexible, users could:
  - Add more character options (e.g., symbols, special characters).
  - Implement features like password strength calculation.
  - Add persistence for stored passwords in the future.



## License Information  
his project is licensed under the [GNU General Public License v3.0](https://github.com/Harshuqt/Python-Password-Generator/blob/main/LICENSE). See the LICENSE file in this repository for details.

## GitHub Repository  
The complete project can be found on GitHub at [this link](https://github.com/Harshuqt/Python-Password-Generator).

