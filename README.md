# URLYZER
URLYZER is a website that classifies an URL as benign or malicious, according to the _Random Forest_ classificator and the URL lexical features extracted. This project was presented as a final paper in Bachelor's degree in Information Systems, at Universidade Federal de Mato Grosso do Sul, Brazil 🇧🇷, 2021.
## Website Folder 📁
> This folder contains all the files about the website.
### > How to run the project
> Make sure to have [Python](https://www.python.org/) installed in your computer (in this project the version used was 3.9.5). After that follow the steps below:

**1.** Create a folder to this project and put the **_urlyzer_** folder inside it.

2. Install the _python virtual environment_ in your computer and create one, after that you can active the virtual environment. You can see more about it [here](https://docs.python.org/3/library/venv.html).

**3.** With the virtual environment **activated** and in the right path of the **_urlyzer_** folder, install all the requirements used in this project. </h4>
```
pip install -r requirements.txt
```
**4.** Modify the _settings.py_ inside _urlyzer_ folder putting the host(s) you want to run the server.
In the line **28** (you can edit this parameter putting the allowed host(s) to run the project):
```
ALLOWED_HOSTS=['127.0.0.1']
```

**5.** Now you can run the django server with the command:
```
python manage.py runserver --insecure
```
The parameter ```--insecure``` is needed because of the parameter ```DEBUG``` setted as```False```.

### > How URLYZER works
According to the URL string put in the _home page_ the site analyzes it and classifies as benign or malicious, putting a web page according to the classification. In the respective page you can come back to the start or go ahead and access the website related to the input URL.

#### Observation ⚠️
If your choice was to access the website represented by the URL, URLYZER will try to access a website with that **exactly URL string given**. Then make sure it's in the right form.

## AI Folder 🖿
> In this folder are the files about the _python_ modules used to build the classificator model, some datasets, the main _jupyter notebook_ about the training, test and results process and the final classificator model used in the project.
### > Datas 🗀
Contains the main datasets used to training and test the classificator model.
### > Jupyter notebook 🗀
Contains the main _jupyter notebook_ used in the project.
### > Python modules 🗀
The python modules used during the project.
### > Random Forest classificator 🗀
The folder containing the final classificator model used in the project.
## URLYZER Screenshots 📷
### Homepage

![image](https://user-images.githubusercontent.com/51066402/123690758-be696d00-d822-11eb-9949-4854946242fd.png)

### Benign URL ✔️

![image](https://user-images.githubusercontent.com/51066402/123690992-10aa8e00-d823-11eb-86bc-6b9df6e555ac.png)
### Malicious URL ❌

![image](https://user-images.githubusercontent.com/51066402/123691155-3fc0ff80-d823-11eb-91b2-3527666f9baa.png)

![image](https://user-images.githubusercontent.com/51066402/123691229-59fadd80-d823-11eb-8020-92612cfb94fa.png)

## Related Technologies
The technologies used to build the website are in the _requirements.txt_ file. Besides that some of the others are related:

- [Scikit learning](https://scikit-learn.org/stable/)
- [Nltk](https://www.nltk.org/)
- [Jupyter](https://jupyter.org/?__cf_chl_managed_tk__=52f5cc98e30b0da14b096418d2fade230790cec2-1624906911-0-AYE26ElB5rNWdYn2xQJP5szz8Ce4koOXIVJjrgaVp3WvHmcLKOsGnhO_tLasUKn_umTcR8AQoybnO26bSR-eO_-ooqEKu6w7Jz9lgpXk4yO7OeaVpWDKKia9RYrZVFubQi85dF131os5SuTZ__4ks6LRNnHbBHYJWQ_yd_U0cCqa1wf0-OAW_tIUDcZLFLIi3DKCMbEcQRZUscxIZXqZ2jYfawoMnByUS0bT95x9oGAGvkrpuxXMg6g-Uh6XAbK94LHJyTbacQPOvbxa9MhJzwK4TqkbZhyCSUYab6JT32oE5tqr6lGrF5d2za-Rl16al17xu9PE_DEpLJTsVbHW7H1eKdhHUY84nMWBEB1kbEH_Glb_Mg4dEx9LBiVf8oadQXckNc6fnh26PC30JGUIKem95gIKIdepNKfZ3M808xDSKmb-Rg0sU1hoC37HCYX28nBngEnAg3viSgdDR-ci1XavSTW5pMbMlab4wxb5Zvit3bOVwpNrScu_wSDemc0ziGNzNcCpND98vOjshzO6Vxh-a2ceMGnJx_6xhDpjDsLevIlr9MBjTbWdHp8Z6HetAPuXH_iN6b0QAKliguAP9u7NoCjDzEe9HzNoNCb5mryLV27V4jKM77YD7BBkAttinQ)
- [Bootstrap 5.0.2](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
