# Rickroll App

This README provides instructions on how to build the Rickroll App using PyInstaller and how to distribute the generated .exe file.

## Prerequisites
- Make sure you have Python installed (preferably Python 3.7 or higher).
- Install PyInstaller via pip:
  ```bash
  pip install pyinstaller
  ```

## Building the Rickroll App
1. **Download the source code:**  Clone the repository or download the source code files for the Rickroll App.

2. **Navigate to the application directory:**  Open your terminal or command prompt and navigate to the folder containing the Rickroll App files.

3. **Run PyInstaller:**  Execute the following command to build the application:
   ```bash
   pyinstaller --onefile rickroll.py
   ```
   Replace `rickroll.py` with the name of your main Python file if it's different.

4. **Locate the executable:**  After the build process is complete, you will find the `.exe` file in the `dist` directory created by PyInstaller.

## Distributing the .exe File
- You can distribute the .exe file located in the `dist` folder. 
- Ensure your users know that they need to have the Microsoft Visual C++ Redistributable installed on their machines to run the application properly.

## Note
- For additional options and configurations, refer to the [PyInstaller documentation](https://pyinstaller.readthedocs.io/en/stable/).