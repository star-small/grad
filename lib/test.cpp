#include <SFML/Graphics.hpp>

int main()
{
    // create the window
    sf::RenderWindow window(sf::VideoMode(800, 600), "OpenGL");
    sf::RectangleShape shape(sf::Vector2f(150.f, 5.f));
    shape.setFillColor(sf::Color(100, 250, 10));
    // run the program as long as the window is open
    while (window.isOpen())
    {
        // check all the window's events that were triggered since the last iteration of the loop
        sf::Event event;
        while (window.pollEvent(event))
        {
            // "close requested" event: we close the window
            if (event.type == sf::Event::Closed)
                window.close();
        }
        
        // clear the window with black color
        window.clear(sf::Color::Black);
        window.draw(shape);
        window.display();
        // draw everything here...
        // window.draw(...);

        // end the current frame
        window.display();
    }

    return 0;
}

