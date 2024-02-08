output: sfml-app
	./sfml-app
sfml-app: test.o
	g++ test.o -o sfml-app -lsfml-graphics -lsfml-window -lsfml-system
test.o: test.cpp
	g++ -c test.cpp
