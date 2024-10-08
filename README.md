<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/your_username/SHIELD-CubeSat">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SHIELD CubeSat Debris Detection System</h3>

  <p align="center">
    A CubeSat project aimed at detecting and monitoring space debris in Low Earth Orbit (LEO) using radar technology.
    <br />
    <a href="https://github.com/your_username/SHIELD-CubeSat"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/your_username/SHIELD-CubeSat">View Demo</a>
    ·
    <a href="https://github.com/your_username/SHIELD-CubeSat/issues">Report Bug</a>
    ·
    <a href="https://github.com/your_username/SHIELD-CubeSat/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#mission">Mission</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![CubeSat Screenshot][product-screenshot]](https://github.com/PaulZeroOne/EnduroSAT/blob/master/images/CubeSAT.jpg)

SHIELD CubeSat aims to address the growing problem of space debris in Low Earth Orbit (LEO) by providing a real-time monitoring system. Equipped with an ultrasonic radar system, the CubeSat detects debris and predicts potential collisions, offering a reliable early-warning system for satellite operators and agencies.

### Mission
The goal of the SHIELD project is to create a 1U CubeSat equipped with radar sensors to detect space debris and monitor its movement. Using a combination of radar and mathematical modeling, the CubeSat processes debris trajectory and provides real-time feedback to ground stations, reducing the risk of collisions.

Key features:
- **Debris Detection**: Radar sensors detect debris in LEO.
- **Real-Time Monitoring**: Track and analyze debris movement using prediction models.
- **Data Visualization**: Provide clear and actionable insights for collision avoidance.

### Built With

* [Arduino](https://www.arduino.cc)
* [HC-SR04](https://www.electronicscomp.com/hc-sr04-ultrasonic-distance-sensor-india)
* [Verlet Integration](https://en.wikipedia.org/wiki/Verlet_integration)
* [Python](https://www.python.org)

<!-- GETTING STARTED -->
## Getting Started

Follow these instructions to get a local copy of the SHIELD CubeSat project up and running.

### Prerequisites

* Arduino IDE
  ```sh
  sudo apt-get install arduino
