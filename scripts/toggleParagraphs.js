/*
HOW TO USE EXAMPLE:
<div class="hidden-paragraphs" style="display: none;">
  <p>This sentence will be hidden until you'll press button that is responsible for showing hidden text.</p>
</div>
*/
function toggleParagraphs() {
  const paragraphs = document.querySelector('.hidden-paragraphs');
  const button = document.getElementById('toggle-button');
  
  if (paragraphs.style.display === 'none') {
    paragraphs.style.display = 'block';
    button.textContent = 'Zwiń';
  } else {
    paragraphs.style.display = 'none';
    button.textContent = 'Rozwiń';
  }
}