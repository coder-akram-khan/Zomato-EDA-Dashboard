# Zomato EDA Dashboard 🍴

An interactive dashboard for exploratory data analysis (EDA) of Zomato restaurant data. The dashboard allows users to filter data, view insights, and visualize various aspects of the restaurant data through interactive charts and maps.
![cover](https://github.com/coder-akram-khan/Zomato-EDA-Dashboard/blob/main/assets/zomatodash.png?raw=true)
## Table of Contents
- [Features](#features)
- [File Structure](#file-structure)
- [Setup and Installation](#setup-and-installation)
- [How to Run the App](#how-to-run-the-app)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [License](#license)

---

## Features
- **Dynamic Filtering**: Filter data by country, city, price range, and aggregate rating.
- **Interactive Metrics**: View total restaurants, average rating, and total votes with real-time updates.
- **Charts and Visualizations**:
  - Bar charts (e.g., top cuisines, ratings)
  - Pie and donut charts (e.g., table booking availability)
  - Correlation heatmaps
  - Geographic visualizations (e.g., restaurant locations on a world map)
  - Sunburst and treemap charts
- **Download Filtered Data**: Export filtered datasets as CSV files.
- **Custom Styling**: Responsive design with a clean UI and a custom theme.

---

## File Structure
    Zomato_EDA_Dashboard/  
    ├── assets/  
    │   ├── logo.png               # Zomato logo  
    │   ├── styles.css             # Custom CSS styles  
    ├── dataset/  
    │   └── Zomatodataset/  
    │       ├── Country-Code.xlsx  # Country metadata  
    │       ├── zomato.csv         # Zomato dataset  
    ├── app.py                     # Main Streamlit application  
    ├── requirements.txt           # Python dependencies  


---

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/coder-akram-khan/Zomato_EDA_Dashboard.git
    cd Zomato_EDA_Dashboard
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure the dataset files (`zomato.csv` and `Country-Code.xlsx`) are in the correct directory:
    ```
    dataset/Zomatodataset/
    ```

4. Start the Streamlit app:
    ```bash
    streamlit run app.py
    ```

---

## How to Run the App
1. Launch the app using the command:
    ```bash
    streamlit run app.py
    ```
2. Open the app in your browser at `http://localhost:8501`.
3. Use the sidebar to apply filters and explore the interactive visualizations.

---

## Screenshots
![Dashboard Overview](https://github.com/coder-akram-khan/Zomato-EDA-Dashboard/blob/main/assets/zomatodash.png?raw=true)


---

## Technologies Used
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/)
- **Visualizations**: [Plotly](https://plotly.com/)
- **Styling**: Custom CSS

---

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/coder-akram-khan/Zomato-EDA-Dashboard/blob/main/LICENSE) file for details.

---

## Contact
Developed by **Akram Khan**  
- [GitHub](https://github.com/coder-akram-khan)  
- [LinkedIn](https://www.linkedin.com/in/mr-akram-khan/)  

