# Healthcare-AI-WebApp

![slide1](https://user-images.githubusercontent.com/83681204/132836093-c80aca67-b58d-420b-8155-23d1e54d46ac.jpg)

## AltairCare app can be accessed [here](https://altaircare.onrender.com)

Artificial intelligence is a rapidly developing field with new improvements that happen every day, it allows the automation and simplification of human activities in different industries like agriculture, Banking and Financial Services, healthcare, travel...
<br>
The integration of artificial intelligence in the world of health is an application that attracts a large number of companies such as Microsoft, Google, Apple and IBM, because it simplifies the lives of patients, doctors and hospital administrators by performing tasks that are typically done by humans, but in less time and at a fraction of the cost, it also allows medical services to be provided in remote and difficult to reach places and it's able to diagnose diseases in the early stages and thus increases the chances of recovery. 
<br>
In my application AltairCare i used machine learning and deep learning algorithms to train highly accurate models and thus allowing users to check their chance of having one of the following diseases:
<ul>
  <li>Liver Disease</li>
  <li>Pneumonia Disease</li>
  <li>Kidney Disease</li>
  <li>Diabete Disease</li>
  <li>Stroke Disease</li>
  <li>Heart Disease</li>
</ul>



![slide2](https://user-images.githubusercontent.com/83681204/132843407-0d59dca9-d0cc-4a3d-a75b-6d995aca761e.jpg)


Each Disease have it's own page with an overview and symptoms that patient may have, and also the prediction model information and required parameters that user must provide

<h2> Disease page : </h2>

![Capture d’écran 2022-03-21 à 17 43 16](https://user-images.githubusercontent.com/83681204/159312257-c9382514-bf8a-4dd2-afc6-777e2e0f812d.png)

<h2> Prediction page : </h2>

![Capture d’écran 2022-03-21 à 17 43 50](https://user-images.githubusercontent.com/83681204/159312337-8a8f8932-473b-4c66-a7f2-c63f1b045c5b.png)

All the datasets used to train the models can be found in the Kaggle website

<h2> Libraries Used : </h2>
<ul>
  <li>Flask: for backend web development </li>
  <li>Scikit-learn & tensorflow: for training the diseases prediction models </li>
  <li>sqlalchemy: library for handling sqlite database </li>
</ul>
<br/>
<h2> How to run this project : </h2>
<h3>Clone this repository: </h3>

```sh
git clone https://github.com/kaymen99/Healthcare-AI-WebApp.git
cd Healthcare-AI-WebApp
```

<h3>Install requirements (using a virtual environment is preferable): </h3>

```sh
pip install -r requirements.txt
```

<h3>Run this command to start local server: </h3>

```sh
python app.py
```





