# Counting-pi-with-colliding-blocks

This project explores the concept presented by G. Galperin and its visualization on YouTube by 3Blue1Brown, focusing on the collision dynamics of rectangular blocks governed by the value of π (pi). The goal is to simulate a pool game scenario where two blocks collide based on the calculated value of π. The user has the ability to input the desired number of digits of pi to be considered, and the program calculates the value of pi accordingly, utilizing it in the simulation. The project is implemented using the Pygame library in conjunction with OpenGL.

## Project Background

Through this project, a pattern has been discovered regarding the collision dynamics of two objects. Specifically, the ratio of the masses of the two blocks should be chosen as the Nth power of 100, where N represents the desired number of digits of pi to be considered. By computing the number of collisions between these two objects, a pattern emerges in which the count of collisions corresponds to the digits present in the value of pi. Furthermore, as the mass of the second object is increased to the Nth power of 100, the number of collisions will match the value of pi accurate to the Nth decimal place.

For instance:
- If the mass of the larger object (M) is equal to the mass of the smaller object (m), the collisions will be equal to 3.
- If M = 100<sup>1</sup> m, the collisions will be equal to 31.
- If M = 100<sup>2</sup> m, the collisions will be equal to 314.
- And so on.

## Program Structure

The project follows the subsequent structure:

1. **Setting Up the Game**
   - The program starts by initializing the screen using the Pygame library.
   - The screen dimensions are defined, and the OpenGL settings are configured.

2. **Block Class**
   - The Block class is created to represent the blocks in the game.
   - Each block possesses attributes such as mass, position, velocity, and color.
   - The class also encompasses methods for rendering and updating the blocks.

3. **User Input**
   - The user is prompted to enter the number of digits of pi they want to check.
   - The program displays a text prompt and captures the user's input using the Pygame event system.
   - Once the user presses the Enter key, the input is processed, and the mass of the second block is calculated based on the user's input.

4. **Main Game Loop**
   - After calculating the value of pi, the main game loop commences.
   - This loop handles user events, updates the positions of the blocks, and checks for collisions between the blocks and the walls.
   - In case of a collision, the appropriate collision response is applied, and the collision count is incremented.
   - The blocks are rendered on the screen, accompanied by the collision count and the expected value of pi.

5. **Game Termination**
   - The game loop continues running until the user closes the window or chooses to quit the program.

## Dependencies

To run this project, the following dependencies are required:

- Pygame library
- OpenGL

Ensure that these dependencies are properly installed before executing the project.

## Usage

1. Clone this repository to your local machine.

2. Install the necessary dependencies using the following command:
   ```
   pip install -r requirements.txt
   ```

3. Run the program by executing the main script:
   ```
   python main.py
   ```

4. Follow the on-screen instructions to input the desired number of digits of pi.

5. Observe the simulation, including the collision count and the expected value of pi.

6. Close the window or terminate the program when you wish to exit.

![Initial prompt to input the number of digits of pi](https://github.com/lokeshsapkota/Counting-pi-with-colliding-blocks/assets/64772372/3f0d41c6-5d84-4503-933f-653308af988b)

*Initial prompt to input the number of digits of pi*

![Post-Simulation window when the input number of digits of pi is 3. Here, the Collisions and expected pi value are equal i.e., 3141](https://github.com/lokeshsapkota/Counting-pi-with-colliding-blocks/assets/64772372/87d1197d-4462-4da4-b1da-3d479e7b54bd)

*Post-Simulation window when the input number of digits of pi is 3. Here, the Collisions and expected pi value are equal i.e., 3141*




<!-- ## Contributing

Contributions to this project are welcome.

 If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue in the repository.
 -->
<!-- ## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute this code as per the terms of the license. -->
