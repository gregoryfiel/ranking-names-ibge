<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/gregoryfiel/ranking-names-ibge">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">IBGE Names Ranking System</h3>

  <p align="center">
    This Python project implements a names ranking system using the IBGE API. It fetches and analyzes data to provide insights into the frequency of names in Brazil, supporting various parameters such as location, sex, and time periods.
    <br />
    <a href="https://github.com/gregoryfiel/ranking-names-ibge"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/gregoryfiel/ranking-names-ibge">View Demo</a>
    ·
    <a href="https://github.com/gregoryfiel/ranking-names-ibge/issues">Report Bug</a>
    ·
    <a href="https://github.com/gregoryfiel/ranking-names-ibge/issues">Request Feature</a>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This project is designed to help you analyze and rank names using the IBGE API.

### Prerequisites

This is an example of how to list things you need to use the software.
* requirements
  ```sh
  pip install -r requirements.txt
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/gregoryfiel/ranking-names-ibge.git
   ```
2. Run the script:
   ```sh
   python main.py --nomes --localidade SP --sexo M --decada 1980
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To use this names ranking system, follow these steps:

### 1. Prepare Input (Optional)

Create a file named `nomes.json` in the project directory and list the names you want to rank. If not provided, the script will use a default set of names for a general ranking:

```json
["Joao", "Maria", "Carlos", "Ana"]
```

### 2. Run the script

If you prepared a list of names in `nomes.json`, you can use the follow command:
```bash
python main.py --nomes
```

If not, you can simply call
```bash
python main.py
```

(A basic list of names has already been provided for exploring the code.)

### Advanced Options

Customize the ranking criteria with some flags according to your preferences:

```bash
python main.py --localidade SP --sexo M --decada 1980
```

* Additional options can be used to refine the ranking:
  * --localidade: Filter by location (e.g., SP for São Paulo).
  * --sexo: Filter by sex (e.g., M for male).
  * --decada: Filter by decade (e.g., 1980).
 
### Additional Settings

Adjust optional settings to suit your needs:
```bash
--retryTimeout 3 15
```  
* --retryTimeout: Set the number of retry attempts and the API request timeout in seconds (e.g., --retryTimeout 3 10 for 3 retries and a timeout of 10 seconds).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Gregory - [@twitter_handle](https://twitter.com/gregoryfiel)

Project Link: [https://github.com/gregoryfiel/ranking-names-IBGE](https://github.com/gregoryfiel/ranking-names-ibge)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Thanks to Ilegra for providing this opportunity to learn by doing.
* Thanks to the IBGE API for providing valuable data.
* Special mention to the Clean Code principles for code maintainability.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/gregoryfiel/ranking-names-ibge.svg?style=for-the-badge
[contributors-url]: https://github.com/gregoryfiel/ranking-names-ibge/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/gregoryfiel/ranking-names-ibge.svg?style=for-the-badge
[forks-url]: https://github.com/gregoryfiel/ranking-names-ibge/network/members
[stars-shield]: https://img.shields.io/github/stars/gregoryfiel/ranking-names-ibge.svg?style=for-the-badge
[stars-url]: https://github.com/gregoryfiel/ranking-names-ibge/stargazers
[issues-shield]: https://img.shields.io/github/issues/gregoryfiel/ranking-names-ibge.svg?style=for-the-badge
[issues-url]: https://github.com/gregoryfiel/ranking-names-ibge/issues
[license-shield]: https://img.shields.io/github/license/gregoryfiel/ranking-names-ibge.svg?style=for-the-badge
[license-url]: https://github.com/gregoryfiel/ranking-names-ibge/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/gregoryfiel
[product-screenshot]: images/screenshot.png
[Python]:https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]:https://www.python.org/
