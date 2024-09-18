#!/usr/bin/node

const request = require('request');

// Get the movie ID from the first command-line argument
const movieId = process.argv[2];

// Define the base URL for the Star Wars API
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a GET request to fetch the film details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const filmData = JSON.parse(body);

  // Extract the list of character URLs
  const characters = filmData.characters;

  // Loop through the characters and make a GET request to fetch each one
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Parse the character details and print the name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

