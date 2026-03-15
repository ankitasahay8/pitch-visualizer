# Pitch Visualizer – From Words to Storyboard

## Overview

The **Pitch Visualizer** is an AI-powered web application that converts narrative text into a visual storyboard.
Users can paste a short story or sales pitch, and the system automatically breaks it into key scenes and generates visual images representing each scene.

The goal of this project is to demonstrate how artificial intelligence can transform textual narratives into engaging visual storytelling content.

This tool can help teams quickly visualize ideas, presentations, product pitches, and success stories without manually designing slides or storyboards.

---

# Problem Statement

Translating written narratives into compelling visual presentations requires creativity, design skills, and time.
Many teams struggle to quickly convert ideas into visual content for presentations or storytelling.

The **Pitch Visualizer** solves this problem by automatically:

1. Accepting narrative text input.
2. Segmenting the narrative into key scenes.
3. Enhancing each scene using AI prompt engineering.
4. Generating images for each scene.
5. Displaying the results as a visual storyboard.

---

# Features

• Accepts narrative text input from users
• Automatically splits the story into multiple scenes
• Uses AI prompt engineering to create descriptive image prompts
• Generates images for each scene
• Displays the results as a storyboard
• Supports user-selectable visual styles (Digital Art, Photorealistic, Anime, etc.)
• Uses a Large Language Model (Gemini) to refine prompts for better visual results

---

# System Workflow

The application follows this pipeline:

User Story Input
↓
Sentence Segmentation using NLTK
↓
Prompt Refinement using Gemini LLM
↓
Image Generation using an Image API
↓
Storyboard Presentation on the Web Interface

---

# Technology Stack

**Programming Language**

* Python

**Backend Framework**

* Flask

**Natural Language Processing**

* NLTK (Natural Language Toolkit)

**Large Language Model**

* Google Gemini API

**Image Generation**

* AI Image Generation API

**Frontend**

* HTML
* Jinja2 Templates

---

# Project Structure

```
pitch_visualizer
│
├── app.py
├── image_generator.py
├── prompt_engine.py
├── requirements.txt
├── README.md
│
├── templates
│   └── index.html
│
└── static
    └── images
        ├── scene_0.png
        ├── scene_1.png
        └── scene_2.png
```

---

# Installation and Setup

Follow these steps to run the project locally.

## 1. Clone the repository

```
git clone https://github.com/yourusername/pitch-visualizer.git
```

## 2. Navigate to the project folder

```
cd pitch-visualizer
```

## 3. Create a virtual environment

```
python -m venv venv
```

Activate the environment:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

## 4. Install required libraries

```
pip install -r requirements.txt
```

---

## 5. Add Gemini API Key

Create a Gemini API key from:

https://aistudio.google.com/app/apikey

Open the file:

```
prompt_engine.py
```

Replace:

```
genai.configure(api_key="YOUR_API_KEY")
```

with your actual API key.

---

## 6. Run the application

```
python app.py
```

Open the browser and go to:

```
http://127.0.0.1:5000
```

---

# Example Input

```
A startup created an AI healthcare assistant. Doctors in hospitals began using the system to analyze patient data quickly. The AI helped detect diseases earlier and improved patient outcomes.
```

---

# Example Output

The system generates a storyboard consisting of multiple scenes:

Scene 1 – Startup developing AI healthcare technology
Scene 2 – Doctors using AI tools inside hospitals
Scene 3 – Improved patient diagnosis and treatment

Each scene is accompanied by a generated image.

---

# Prompt Engineering Methodology

To improve image generation quality, each narrative sentence is transformed into a detailed visual prompt.

The Gemini LLM expands simple sentences into descriptive prompts including:

• Environment details
• Lighting and cinematic elements
• Artistic style
• Scene context

Example:

Input sentence:

```
Doctors use AI in hospitals
```

Refined prompt:

```
Doctors interacting with an advanced AI diagnostic system inside a modern hospital environment, cinematic lighting, highly detailed concept art
```

This approach produces more visually meaningful images.

---

# Bonus Features Implemented

The project also includes several advanced features:

• **Visual Consistency** – consistent artistic style across generated scenes
• **User Selectable Styles** – users can choose the visual style before generating images
• **LLM Powered Prompt Refinement** – Gemini enhances prompts before image generation
• **Dynamic Web Interface** – users can generate storyboards directly from the browser

---

# Future Improvements

Possible improvements include:

• Adding animation or slideshow storyboard display
• Allowing users to download the storyboard as a PDF
• Supporting video storyboard generation
• Adding multiple AI image generation models
• Implementing caching for faster image loading

---

# Author

Pitch Visualizer Project- ANKITA SAHAY
