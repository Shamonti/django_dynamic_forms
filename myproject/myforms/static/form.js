const nextButton01 = document.getElementById('nextButton01');
const nextButton02 = document.getElementById('nextButton02');

nextButton01.addEventListener('click', function () {
  const displayText01 = document.getElementById('displayText01');

  displayText01.style.display = 'block';
});

nextButton02.addEventListener('click', function () {
  const displayText02 = document.getElementById('displayText02');

  displayText02.style.display = 'block';
});
