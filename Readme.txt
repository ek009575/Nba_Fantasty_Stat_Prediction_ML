Project Documentation: Overview and Workflow
Data Collection and Preprocessing
Due to the large size of the data and the nature of continuous data collection, the initial work for "data collection" and "NBA notebook" files cannot be seen in the Jupiter environment. There is only one way to see them to use visual studio code. These files handle the raw data acquisition and are optimized for a continuous workflow.

The "Creating Main Dataset" notebook is an integral part of the project. It continues from the data collected in the files above and focuses on data preprocessing and feature engineering to create the final dataset. This process is fully documented and accessible via Google Colab or Jupyter Notebook for a more interactive experience.

Model Development
The GBM_Model_NBA notebook demonstrates the training pipeline of the Gradient Boosting Machine (GBM) model, including feature selection and hyperparameter tuning.
Principal Component Analysis (PCA) has been applied to reduce dimensionality and improve model efficiency. After model optimization is completed, the model is integrated into pickle which will be used to create Flask API.
Then, the model prepared for the flask is used for docker container.

Key Dataset
The "updated_gbm.csv" file serves as the final dataset for training and testing the machine learning model. It has been preprocessed and is ready for direct use in the pipeline. gbm_data.csv is version of "update_gbm.csv" not having rolling feature. you can also see this process on "GBM Model NBA.ipyn" file.

Deployment
The ultimate model and its dependencies are encapsulated in a Docker container for scalability and "AWS" cloud deployment. The Docker image includes the Flask API, which integrates the trained model for real-time predictions.


Docker Structure
/nba-flask-api
    ├── Dockerfile          # docker file
    ├── app.py              # Flask app
    ├── requirements.txt    # requirement text
    ├── nba_fantasy_model.pkl  # pickle will be used for flask
# NBA Fantasy Stats Prediction

## Proje Explanation
The project or model is used to predict NBA fantasy prediction according to players' live performance in the game. The project uses technologies like docker, flask, and cloud environment in terms of scalability and reliability.

1. **Clone the project:**
   ```bash
   git clone https://github.com/username/nba-flask-api.git
   cd nba-flask-api

docker build -t nba-flask-api . #Create docker image
docker run -p 5000:5000 nba-flask-api #start docker container
You can use Postman or browser to test the API.
URL: http://127.0.0.1:5000 
#I have used postman in order to send the data

To use aws for the project
1. **Create AWS EC2 Instance:**
- Amazon Linux 2 AMI, t2.micro instance, and open port (5000).

2. **Docker Installation:**
```bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
