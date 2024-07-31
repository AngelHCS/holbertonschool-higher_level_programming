const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

const helloElement = document.querySelector('#hello');

fetch(url)
  .then(response =>
    {
      if (!response.ok)
      {
        throw new Error('Bad Network Response');
      }
      return response.json();
    })
    .then(data =>
      {
        const helloText = data.hello;

        helloElement.textContent = helloText;
      })
    .catch(error =>
      {
        console.error('Problem with fetch operation:', error);
      });
