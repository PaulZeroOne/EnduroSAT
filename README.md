<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/PaulZeroOne/EnduroSAT">
    <img src="images/logo.png" alt="CubeSat Project Logo" width="80" height="80">
  </a>

  <h3 align="center">SHIELD CubeSat Debris Detection System</h3>

  <p align="center">
    A CubeSat project aimed at detecting and monitoring space debris in Low Earth Orbit (LEO) using radar technology.
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
        <li><a href="#cubesat-details">CubeSAT Details</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
  <img src="https://github.com/PaulZeroOne/EnduroSAT/raw/master/images/CubeSAT.jpg" alt="CubeSat Prototype Image" style="object-fit: cover; max-width: 100%;">
</p>

SHIELD CubeSat aims to address the growing problem of space debris in Low Earth Orbit (LEO) by providing a real-time monitoring system. Equipped with an ultrasonic radar system, the CubeSat detects debris and predicts potential collisions, offering a reliable early-warning system for satellite operators and agencies.

### Mission
The goal of the SHIELD project is to create a 1U CubeSat equipped with radar sensors to detect space debris and monitor its movement. Using a combination of radar and mathematical modeling, the CubeSat processes debris trajectory and provides real-time feedback to ground stations, reducing the risk of collisions.

Key features:
- **Debris Detection**: Radar sensors detect debris in LEO.
- **Real-Time Monitoring**: Track and analyze debris movement using prediction models.
- **Data Visualization**: Provide clear and actionable insights for collision avoidance.

### Built With

* [STM32](https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html) - Microcontroller platform for processing data from the radar system.
* [Arduino](https://www.arduino.cc) - Used for prototyping and sensor data acquisition.
* [Python](https://www.python.org)

### CubeSAT Details

#### Electrical Schematics
The CubeSAT's electrical architecture incorporates key components for both data acquisition and power distribution. These include the Arduino R4 Minima, HC-SR04 ultrasonic sensors, and EnduroSat modules such as the Electric Power System (EPS), On-Board Computer (OBC), and UHF transceiver. The Arduino processes data from the ultrasonic sensors, which detect nearby debris by measuring the time it takes for an ultrasonic pulse to travel to and reflect back from an object.

The sensors are powered through a 5V supply, and data communication occurs between the Arduino and the OBC via UART. EnduroSat’s 1U solar panels power the system through the EPS, which efficiently distributes energy to the sensors, Arduino, and other critical electronics. This ensures reliable operation even in the space environment.

#### Data Acquisition and Plotting of Trajectory
Data acquisition is handled by the Arduino, which activates the ultrasonic sensors to emit pulses and records the time of the returning echoes. The Arduino processes this data, filters noise using a moving average filter, and calculates the distance and speed of nearby debris.

To plot the trajectory of detected debris, the system uses Verlet integration. This method tracks the debris' position over time, calculating new positions based on velocity and acceleration, without the need for direct force calculations. It’s highly effective for real-time data acquisition in space. The trajectory is visualized on a 2D plot, helping to predict potential collisions with debris.

<p align="center">
  <img src="https://github.com/PaulZeroOne/EnduroSAT/raw/master/images/ballistic_trajectory_predicted.gif" alt="Ballistic Trajectory Prediction" style="max-width: 100%;">
</p>

#### Mechanical Structures
The CubeSAT integrates off-the-shelf systems from EnduroSat and custom-built components developed by the team. The structure includes a 1U CubeSat frame, sensor mounts, and Arduino housing. The ultrasonic sensors are mounted on a custom plate positioned to maximize detection range.

3D-printed mounts are used to secure the Arduino and sensors within the CubeSat. These mounts are attached to the satellite’s internal framework using springs and spacers, ensuring structural integrity and preventing interference with wiring. The mechanical design ensures that the sensors are optimally deployed to detect debris, providing wide coverage in Low Earth Orbit (LEO).

<p align="center">
  <img src="https://github.com/PaulZeroOne/EnduroSAT/raw/master/images/Assemb_3.3_(1)_2024-Aug-05_11-04-50AM-000_CustomizedView37173395950.png" alt="CubeSat Mechanical Assembly" style="max-width: 100%;">
</p>
