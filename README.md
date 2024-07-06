# AnReal: Towards an Extended Reality Low-Cost System for Kinesiophobia

## Overview
AnReal is a novel mobile-based extended reality (XR) system designed to treat kinesiophobia, especially in patients with chronic low back pain. This system combines views of the real world with simulated video trajectories, aiming to provide an affordable and effective treatment option. Unlike traditional VR systems, AnReal uses a simple VR headset with an Android application, making it a low-cost solution suitable for low-income countries.

It combines development in Android Studio and Python to comunicate the angles on which the person is.

## Features
- **Low-Cost Hardware**: Uses an Android mobile phone and a basic VR headset.
- **Extended Reality (XR)**: Combines real-world views with pre-recorded simulated trajectories.
- **User Experience**: Designed to provide a good user experience while minimizing cybersickness.
- **Rehabilitation Exercise**: Specifically targets bending forward exercises, common in patients with chronic low back pain.

## System Architecture
The AnReal system architecture consists of three layers:
1. **Application Framework Layer**: Developed using React Native and Android Studio.
2. **Runtime and Libraries Layer**: Utilizes the Camera2 API for real-time camera feed and SensorManager API for motion sensing.
3. **Kernel Layer**: Manages hardware interactions and real-time processing.

## Setup and Installation
### Requirements
- **Hardware**: Android phone (Samsung S21 FE recommended), VR headset (approximately 32 USD).
- **Software**: React Native, Android Studio, Node.js.

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/AnReal.git
   cd AnReal
   ```
2. **Install dependencies**
3. **Open in Android Studio:**:
    - Open the project in Android Studio.
    - Ensure all dependencies are resolved.
4. **Run the Application**:
   - Connect your Android phone.
   - Run the application from Android Studio.

## Usage
1. **Prepare the Environment**:
   - Mark a line on the wall to indicate the bending limit (approximately 30 degrees of inclination).
   - Ensure a stable, well-lit environment without moving elements.

2. **Using the Headset**:
   - Wear the headset and get accustomed to the view.
   - Perform the bending forward exercise while the headset displays the real environment and simulated trajectory.

3. **Data Collection**:
   - Use the provided questionnaires to collect user experience data, cybersickness levels, and sense of presence.

## Evaluation
The system was initially evaluated with physical therapy students. Key findings include:
- **User Experience**: High scores in novelty and attractiveness, lower scores in dependability.
- **Cybersickness**: High levels of cybersickness were noted, with recommendations for improvement.
- **Sense of Presence**: Moderate sense of presence, with potential for enhancement.

## Future Work
- **Improve Transition**: Smoother transition between camera preview and video simulation.
- **Expand Exercises**: Incorporate additional rehabilitation exercises.
- **User Testing**: Conduct further studies with diverse participant groups, including patients with kinesiophobia.

## Acknowledgements
This research was partially funded by the Sociedad Chilena de Ortopedia y Traumatología. Special thanks to all the participants and contributors.

## Contact
For any questions or further information, please contact:
- **Diego Arredondo**: diego.arredondom@gmail.com

