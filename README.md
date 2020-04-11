# prism_audio_sharing
World Music Hackathon submission: Secure audio sharing to control piracy.

# Project Setup
1. Check if Django exist in your system by executing the following command on terminal
   <blockquote> $python -m django --version </blockquote>
  
   If not install please go through the following documentation and install Django
   https://docs.djangoproject.com/en/3.0/topics/install/.
   
2. Once installed successfully, open you termipython manage.py makemigrationsnal and go to your project location/src. Run you project by executing following command
   <blockquote> python manage.py runserver </blockquote>
   
3. Open the localhost on your system and check if server is running. Run the migrations with the following commands
    <blockquote> python manage.py makemigrations <br>
     python manage.py migration </blockquote>
     
4. If you have installed Django than super-user needs to be created.
  <blockquote> winpty python manage.py createsuperuser </lockquote>
  
5. Log In through the Django Dashboard using username and password
