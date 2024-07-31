const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

const characterElement = document.querySelector('#character');

fetch(url)
  .then(response =>
    {
      if (!response.ok) {
        throw new Error('Bad Network Response');
      }
      return response.json();
    })
    .then(data =>
      {
        characterElement.textContent = data.name;
      })
    .catch(error =>
      {
        console.error('problem with fetch operation:', error);
      });
