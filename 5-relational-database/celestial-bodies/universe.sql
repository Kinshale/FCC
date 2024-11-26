CREATE DATABASE universe;

-- Galaxy, star, planet, moon

CREATE TABLE galaxy (
    galaxy_id SERIAL PRIMARY KEY,                   
    name VARCHAR(100) NOT NULL UNIQUE,             
    width_km INT NOT NULL,                         
    distance_from_earth_light_years NUMERIC(10, 2),  
    is_visible BOOLEAN DEFAULT TRUE NOT NULL       
);

CREATE TABLE star (
    star_id SERIAL PRIMARY KEY,                   
    name VARCHAR(100) NOT NULL UNIQUE,            
    brightness NUMERIC(5, 2) NOT NULL,            
    star_type TEXT NOT NULL,                      
    galaxy_id INT NOT NULL,                       
    FOREIGN KEY (galaxy_id) REFERENCES galaxy(galaxy_id) ON DELETE CASCADE
);

CREATE TABLE planet (
    planet_id SERIAL PRIMARY KEY,                 
    name VARCHAR(100) NOT NULL UNIQUE,            
    distance_from_star_kkm INT NOT NULL,           
    is_habitable BOOLEAN DEFAULT FALSE NOT NULL,  
    star_id INT NOT NULL,                         
    FOREIGN KEY (star_id) REFERENCES star(star_id) ON DELETE CASCADE
);

CREATE TABLE moon (
    moon_id SERIAL PRIMARY KEY,                   
    name VARCHAR(100) NOT NULL UNIQUE,            
    diameter_km INT NOT NULL,                     
    is_spherical BOOLEAN DEFAULT TRUE NOT NULL,   
    planet_id INT NOT NULL,                       
    FOREIGN KEY (planet_id) REFERENCES planet(planet_id) ON DELETE CASCADE
);

CREATE TABLE cosmic_event (
    cosmic_event_id SERIAL PRIMARY KEY,                 
    name VARCHAR(100) NOT NULL UNIQUE,           
    event_description TEXT NOT NULL,             
    galaxy_id INT NOT NULL,                       
    FOREIGN KEY (galaxy_id) REFERENCES galaxy(galaxy_id) ON DELETE CASCADE
);

INSERT INTO galaxy (name, width_km, distance_from_earth_light_years, is_visible)
VALUES
('Milky Way', 105700, 0, TRUE),
('Andromeda', 220000, 2537000, TRUE),
('Triangulum', 60000, 3000000, TRUE),
('Large Magellanic Cloud', 14000, 163000, TRUE),
('Small Magellanic Cloud', 7000, 200000, TRUE),
('Sombrero', 50000, 29000000, FALSE);

INSERT INTO star (name, brightness, star_type, galaxy_id)
VALUES
('Sun', 1.00, 'G-type Main-Sequence', 1),
('Proxima Centauri', 0.17, 'M-type Main-Sequence', 1),
('Sirius', 25.4, 'A-type Main-Sequence', 1),
('Betelgeuse', 12.5, 'Red Supergiant', 2),
('Rigel', 85.03, 'Blue Supergiant', 2),
('Vega', 37.23, 'A-type Main-Sequence', 1);


INSERT INTO planet (name, distance_from_star_kkm, is_habitable, star_id)
VALUES
('Earth', 14960, TRUE, 1),
('Mars', 22794, FALSE, 1),
('Venus', 10820, FALSE, 1),
('Jupiter', 77834, FALSE, 1),
('Saturn', 142670, FALSE, 1),
('Proxima b', 750, TRUE, 2),
('Proxima c', 1200, FALSE, 2),
('Kepler-22b', 60000, TRUE, 3),
('Kepler-69c', 90000, TRUE, 3),
('Kepler-442b', 1200, TRUE, 3),
('Trappist-1e', 4000, TRUE, 4),
('Trappist-1f', 4500, TRUE, 4);

INSERT INTO moon (name, diameter_km, is_spherical, planet_id)
VALUES
('Moon', 3474, TRUE, 1),
('Phobos', 22, FALSE, 2),
('Deimos', 12, FALSE, 2),
('Io', 3643, TRUE, 4),
('Europa', 3122, TRUE, 4),
('Ganymede', 5268, TRUE, 4),
('Callisto', 4821, TRUE, 4),
('Titan', 5152, TRUE, 5),
('Rhea', 1528, TRUE, 5),
('Iapetus', 1470, TRUE, 5),
('Dione', 1122, TRUE, 5),
('Triton', 2706, TRUE, 6),
('Charon', 1212, TRUE, 6),
('Oberon', 1523, TRUE, 6),
('Titania', 1578, TRUE, 6),
('Umbriel', 1169, TRUE, 6),
('Ariel', 1158, TRUE, 6),
('Miranda', 471, TRUE, 6),
('Mimas', 396, TRUE, 5),
('Enceladus', 504, TRUE, 5);

INSERT INTO cosmic_event (name, event_description, galaxy_id)
VALUES
('Supernova Explosion', 'A massive star explosion resulting in a neutron star or black hole.', 1),
('Black Hole Formation', 'Formation of a black hole in the galaxy core.', 2),
('Gamma Ray Burst', 'Intense burst of gamma rays from a collapsing star.', 2),
('Quasar Activity', 'Extreme luminosity from the supermassive black hole.', 3),
('Starburst Event', 'Rapid star formation occurring in a galaxy.', 4);