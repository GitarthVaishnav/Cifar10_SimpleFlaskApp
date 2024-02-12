<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">CIFAR-10 Flask App for Image Classification</h3>
  <p align="center">
    A Flask-based web application for classifying CIFAR-10 images using a pre-trained model, with support for ClearML integration for model management and versioning.
    <br />
    <a href="https://github.com/GitarthVaishnav/Cifar10_SimpleFlaskApp"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/GitarthVaishnav/Cifar10_SimpleFlaskApp/issues">Report Bug</a>
    ·
    <a href="https://github.com/GitarthVaishnav/Cifar10_SimpleFlaskApp/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This Flask application provides an interface for users to classify images from the CIFAR-10 dataset. It leverages a pre-trained convolutional neural network model and integrates with ClearML for seamless model management and versioning. The app supports uploading images and displays the classification results in real-time.

### Built With
[![Python][Python.org]][Python-url]
[![Flask][Flask]][Flask-url]
[![HTML5][HTML5]][HTML5-url]
[![JavaScript][JavaScript]][JAvaScript-url]
[![CSS3][CSS3]][CSS3-url]
[![NumPy][NumPy]][NumPy-url]
[![Bootstrap][Bootstrap.com]][Bootstrap-url]

### Compatible with
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![nVIDIA](https://img.shields.io/badge/nVIDIA-%2376B900.svg?style=for-the-badge&logo=nVIDIA&logoColor=white)
![Firebase](https://img.shields.io/badge/firebase-%23039BE5.svg?style=for-the-badge&logo=firebase)

### Can be Deployed on
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)

### Works with
[![Chrome][Chrome]][Chrome-url]
[![Edge][Edge]][Edge-url]
[![Safari][Safari]][Safari-url]
[![Firefox][Firefox]][Firefox-url]
[![Opera][Opera]][Opera-url]
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To set up this project locally, follow these simple steps.

### Prerequisites

- Python 3.10 or newer
- Poetry for Python package management

### Installation

1. Install Poetry:
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone the repo:
    ```sh
   git clone https://github.com/GitarthVaishnav/Cifar10_SimpleFlaskApp.git
   
   cd Cifar10_SimpleFlaskApp
   ```

3. Install dependencies using Poetry:
    ```sh 
   poetry install
   ```

4. Activate the Poetry shell:
    ```sh
   poetry shell
   ```


5. Run the pipeline:
    ```sh
   python server.py
   ```


<!-- USAGE -->
## Usage

Navigate to the web application URL, usually `http://127.0.0.1:5000`, and use the interface to upload CIFAR-10 images for classification.

<!-- CONTRIBUTING -->
## Contributing

Contributions make the open-source community thrive. Any contributions you make are **greatly appreciated**. Please refer to the contributing guidelines for more information.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Your Name - [Your Email](mailto:your_email@example.com)

Project Link: [https://github.com/GitarthVaishnav/Cifar10_SimpleFlaskApp](https://github.com/GitarthVaishnav/Cifar10_SimpleFlaskApp)

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/GitarthVaishnav/Cifar10_SimpleFlaskApp.svg?style=for-the-badge
[contributors-url]: https://github.com/GitarthVaishnav/Cifar10_SimpleFlaskApp/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/GitarthVaishnav/Cifar10_SimpleFlaskApp.svg?style=for-the-badge
[forks-url]: https://github.com/GitarthVaishnav/Cifar10_SimpleFlaskApp/network/members
[stars-shield]: https://img.shields.io/github/stars/GitarthVaishnav/Cifar10_SimpleFlaskApp.svg?style=for-the-badge
[stars-url]: https://github.com/GitarthVaishnav/Cifar10_SimpleFlaskApp/stargazers
[issues-shield]: https://img.shields.io/github/issues/GitarthVaishnav/Cifar10_SimpleFlaskApp.svg?style=for-the-badge
[issues-url]: https://github.com/GitarthVaishnav/Cifar10_SimpleFlaskApp
[license-shield]: https://img.shields.io/github/license/GitarthVaishnav/Cifar10_SimpleFlaskApp.svg?style=for-the-badge
[license-url]: https://github.com/GitarthVaishnav/Cifar10_SimpleFlaskAppblob/master/LICENCE

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/gitarthvaishnav
[product-screenshot]: images/screenshot.png
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Python.org]:https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://python.org
[OpenCV.org]:https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white
[OpenCV-url]: https://opencv.org/
[Flask]:https://img.shields.io/badge/flask-%23092E20.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/
[HTML5]:https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[HTML5-url]: https://html.spec.whatwg.org/
[JavaScript]:https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[JavaScript-url]: https://www.javascript.com/
[MarkDown]:https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white
[MarkDown-url]: https://www.markdownguide.org/
[NumPy]:https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/
[Chrome]:https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white
[Chrome-url]: https://www.google.com/chrome/
[Edge]:https://img.shields.io/badge/Edge-0078D7?style=for-the-badge&logo=Microsoft-edge&logoColor=white
[Edge-url]: https://www.microsoft.com/edge
[Safari]:https://img.shields.io/badge/Safari-000000?style=for-the-badge&logo=Safari&logoColor=white
[Safari-url]: https://www.apple.com/safari/
[Firefox]:https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white
[Firefox-url]: https://www.mozilla.org/en-US/firefox/new/
[Opera]:https://img.shields.io/badge/Opera-FF1B2D?style=for-the-badge&logo=Opera&logoColor=white
[Opera-url]: https://www.opera.com/
[CSS3]:https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white
[CSS3-url]: https://www.opera.com/