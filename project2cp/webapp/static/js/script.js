const profile = document.querySelector('.profile');
const dropdown = document.querySelector('.dropdown');

profile.addEventListener('click', () => {
  profile.classList.toggle('open'); // ajouter ou supprimer la classe 'open' sur l'élément '.profile'
  dropdown.classList.toggle('show'); // ajouter ou supprimer la classe 'show' sur l'élément '.dropdown'
});