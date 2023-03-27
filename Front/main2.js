
const dropdowns = document.querySelectorAll('.dropdown');

dropdowns.forEach((dropdown) => {
  const angleIcon = dropdown.querySelector('i');
  dropdown.addEventListener('click', () => {
    dropdown.nextElementSibling.classList.toggle('sublist');
    angleIcon.classList.toggle('first');
    angleIcon.classList.toggle('second');

  });
});

