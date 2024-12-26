let currentImageIndex = 0;
const gallery = document.querySelector('.photo-gallery');
const images = gallery.querySelectorAll('img'); // Select images within the photo gallery

function openModal(img) {
  document.getElementById("myModal").style.display = "flex";
  document.getElementById("image_preview").src = img.src;
  currentImageIndex = Array.from(images).indexOf(img); // Get the index of the clicked image
}

function closeModal() {
  document.getElementById("myModal").style.display = "none";
}

function showImage(index) {
  if (index >= 0 && index < images.length) {
    document.getElementById("image_preview").src = images[index].src;
    currentImageIndex = index;
  }
}

// Add event listener for Escape, Left, and Right keys
document.addEventListener("keydown", function(event) {
  if (event.key === "Escape") {
    closeModal();
  } else if (event.key === "ArrowLeft") {
    showImage(currentImageIndex - 1);
  } else if (event.key === "ArrowRight") {
    showImage(currentImageIndex + 1);
  }
});

// Add event listeners for prev and next arrows
document.getElementById("previous_image_button").addEventListener("click", function(event) {
  event.stopPropagation(); // Prevent modal close
  showImage(currentImageIndex - 1);
});

document.getElementById("next_image_button").addEventListener("click", function(event) {
  event.stopPropagation(); // Prevent modal close
  showImage(currentImageIndex + 1);
});