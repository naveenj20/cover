# Ex.06 Book Front Cover Page Design
## Date: 29/10/2025

## AIM:
To design a book front cover page using HTML and CSS.

## DESIGN STEPS:

### Step 1:
Create a Django Admin project.

### Step 2:
Create an app in the Django interface.

### Step 3:
Create a folder named 'static' in the app folder.

### Step 4:
Create a new HTML file in the static folder.

### Step 5:
Write the HTML code with relevant CSS properties.

### Step 6:
Choose the appropriate style and color scheme.

### Step 7:
Insert the images in their appropriate places.

### Step 8:
Publish the website in the LocalHost.

## PROGRAM:

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Book Cover</title>
    <style>
        .imagecontainer {
            width: 400px;
            height: 700px;
            color: black;
            margin-left: auto;
            margin-right: auto;
            padding: 20px;
            font-family: 'Arial, sans-serif';
            background-image: url("{% static 'frontcover/forest.jpg' %}");
            background-size: cover;
            background-position: center;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
            border: 5px solid #fff;
        }

        .publisher {
            color: rgb(248, 245, 245);
            font-size: medium;
            text-align: left;
        }

        .divider {
            width: 400px;
        }

        .title {
            color: #fdfdfd;
            font-family: Georgia, serif;
            font-size: 2.2em;
            text-align: center;
            position: relative;
            top: 30px;
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.6);
        }

        .subtitle {
            color: #f5e1d8;
            font-family: 'Verdana', sans-serif;
            font-size: 1.1em;
            text-align: center;
            position: relative;
            top: 50px;
            font-style: italic;
            text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.7);
        }

        .photo {
            position: relative;
            top: 120px;
            left: 260px;
            width: 90px;
            height: 110px;
        }

        .photo img {
            width: 90px;
            height: 110px;
            border: 2px solid #fff;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.6);
        }

        .authorname {
            display: inline;
            position: relative;
            color: #fff3e0;
            top: 180px;
            left: 10px;
            font-family: Georgia, serif;
            font-size: medium;
            text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.8);
        }

        .line {
            width: 400px;
            position: relative;
            top: 170px;
        }

        .edition {
            color: #f7c9c9;
            font-size: medium;
            font-family: Verdana, sans-serif;
            position: relative;
            top: 100px;
            text-align: left;
        }

        .publisherbottom {
            color: #f5d5d5;
            font-size: medium;
            position: relative;
            top: 170px;
            left: 330px;
        }
    </style>
</head>

<body>
    <div class="imagecontainer">
        <div class="publisher">SEC Publications</div>

        <div class="divider">
            <hr style="color: rgb(233, 210, 210)">
        </div>

        <div class="title">
            <h1>Emerald Hills</h1>
        </div>

        <div class="subtitle">
            where greenery meets serenity...
        </div>

        <div class="photo">
            <img src="{% static 'frontcover/naveenphoto.jpg' %}" alt="Book Logo">
        </div>

        <div class="line">
            <hr style="color: rgba(255, 255, 255, 0.4)">
        </div>

        <div class="authorname">
            <b>Naveen J</b>
        </div>

        <div class="publisherbottom">
            SEC
        </div>

        <div class="edition">
            <b>Special Edition</b>
        </div>
    </div>
</body>
</html>
```

## OUTPUT:

![alt text](<Screenshot 2025-10-29 113850.png>)
![alt text](<Screenshot 2025-10-29 113832.png>)

## RESULT:
The program for designing book front cover page using HTML and CSS is completed successfully.
