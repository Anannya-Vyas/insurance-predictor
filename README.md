# 📊 Insurance Predictor


**Estimate your medical insurance charges based on your profile.**

[Live Demo](https://insurance-predictor-anannya.streamlit.app/)



## 📖 Overview

This project provides an interactive web application that allows users to estimate their medical insurance charges. Built with Streamlit and powered by a pre-trained Machine Learning model, it takes various personal and health-related parameters as input and predicts the likely insurance cost. This tool is designed to offer a quick and accessible way for individuals to understand potential insurance expenses based on key demographic and health indicators.

## ✨ Features

-   🎯 **Personalized Cost Estimation**: Predicts insurance charges based on individual profiles.
-   📈 **Machine Learning Powered**: Utilizes a pre-trained predictive model for accurate estimations.
-   🌐 **Interactive Web Interface**: User-friendly input forms built with Streamlit for seamless interaction.
-   ⚙️ **Key Parameter Inputs**: Accepts inputs for age, sex, BMI, number of children, smoking status, and region.
-   💻 **Development Container Ready**: Includes `.devcontainer` configuration for a consistent development setup.



## 🛠️ Tech Stack

**Programming Language:**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**Frameworks & Libraries:**
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

**DevOps & Tools:**
![VS Code Dev Containers](https://img.shields.io/badge/Dev%20Containers-0471DE?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## 🚀 Quick Start

Follow these steps to get the Insurance Predictor application up and running on your local machine.

### Prerequisites
-   **Python 3.x** (version 3.8 or higher recommended)

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Anannya-Vyas/insurance-predictor.git
    cd insurance-predictor
    ```

2.  **Create a virtual environment** (recommended)
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application**
    ```bash
    streamlit run app.py
    ```

5.  **Open your browser**
    The application will automatically open in your default browser at `http://localhost:8501` (or a similar local address).

## 📁 Project Structure

```
insurance-predictor/
├── .devcontainer/     # Development container configurations (e.g., for VS Code)
│   └── devcontainer.json
├── app.py             # Main Streamlit application file
├── model.pkl          # Pre-trained machine learning model (e.g., Linear Regression)
├── requirements.txt   # Python dependencies
└── scaler.pkl         # Pre-fitted data scaler (e.g., StandardScaler)
```

## ⚙️ Configuration

The application's core logic and pre-trained components are encapsulated in the following files:

-   **`model.pkl`**: This file contains the serialized (pickled) machine learning model. The `app.py` loads this model to make predictions.
-   **`scaler.pkl`**: This file contains the serialized data scaler, used to preprocess input features before they are fed into the `model.pkl`. This ensures consistency with how the model was trained.

There are no external environment variables to configure for this simple application. All inputs are handled directly through the Streamlit UI.

## 🔧 Development

### Development Container
This repository includes a `.devcontainer` folder, enabling you to open the project directly in a consistent development environment using Visual Studio Code's Dev Containers extension or GitHub Codespaces.

1.  **Install VS Code Dev Containers Extension**: If you're using VS Code.
2.  **Reopen in Container**: When prompted, click "Reopen in Container".
    This will set up a containerized environment with all necessary dependencies pre-installed, ready for development.

### Running the Application in Development Mode
To run the Streamlit application locally:
```bash
streamlit run app.py
```

Any changes saved to `app.py` will automatically trigger a re-run of the application in your browser.

## 🚀 Deployment

This application is designed to be easily deployable on platforms that support Streamlit applications, such as Streamlit Community Cloud.

The project currently has a live demo deployed on Streamlit Community Cloud, as indicated by the `homepage` URL. For custom deployments, simply ensure the Python environment with `requirements.txt` is set up, and then run `streamlit run app.py` on your desired server.

## 🤝 Contributing

We welcome contributions to enhance the Insurance Predictor! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

1.  **Fork** this repository.
2.  **Create a new branch** (`git checkout -b feature/your-feature-name` or `bugfix/your-fix-name`).
3.  **Make your changes**.
4.  **Commit your changes** (`git commit -m 'feat: Add new feature'` or `fix: Fix bug`).
5.  **Push to the branch** (`git push origin feature/your-feature-name`).
6.  **Open a Pull Request**.

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details. <!-- TODO: Verify or add a LICENSE file if not present. -->

##  Acknowledgments

-   **Streamlit**: For providing an amazing framework for building data apps.
-   **Scikit-learn**: For robust machine learning tools.
-   **Pandas & NumPy**: For powerful data manipulation and numerical operations.
-   **Anannya-Vyas**: The original author of this repository.

## 📞 Support & Contact

-   🐛 Issues: [GitHub Issues](https://github.com/Anannya-Vyas/insurance-predictor/issues)

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [Anannya-Vyas](https://github.com/Anannya-Vyas)

</div>
