#!/usr/bin/node

const request = require('request');

// Get the movie ID from the first command-line argument
const movieId = process.argv[2];

// Define the base URL for the Star Wars API
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch a character and log their name
function fetchCharacter(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        resolve();
      }
    });
  });
}

// Main function to handle the movie request and process characters sequentially
request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  for (const characterUrl of characters) {
    try {
      await fetchCharacter(characterUrl);
    } catch (error) {
      console.error(error);
    }
  }
});

