# Fetch and read data from zed races

In their API doc they mentioned that one required an api key, but I didn't really need it to get the data.
The API uses a query structure called GraphQL which was created by FaceBook.

I have been able to fetch some data that will enable you see all the data returned by zed and analyze it. You can do this ananlysis in different ways. I am not much for datascience but there are many libraries out there.

Please ensure you have python installed on your system, if you do not I have also included a data.json file that contains all the horse racing data.

Before running the application unzip the file and cd into the zed folder:

        cd /path/to/folder/zed

To run this application, run the line below in a cmdline after unzipping the file

        source venv/bin/activate

after this is done and you are in the python virtual environment, run below to start application

        flask run

after this is done and no errors show up, go to your browser and type

        localhost:5000/

this will automatically fetch data from zed and display in readable format for you, and it will also save the latest data to the data.json file.

To read the file in future, type in your browser

        localhost:5000/read-data


### To make it less complicated
I have deployed to a website which you can access by typing:

        https://zed-data.herokuapp.com

and to read the file later, type

        https://zed-data.herokuapp.com/read-data
