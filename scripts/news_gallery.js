// Initialize the current image index to 0
let currentImageIndex = 0;

// Function to set the display style of the modal
function setModalDisplay(displayStyle) {
  document.getElementById("myModal").style.display = displayStyle;
}

// Function to open the modal and display the clicked image
function openModal(img) {
  setModalDisplay("flex"); // Set the modal display to flex
  document.getElementById("image_preview").src = img.src; // Set the source of the image preview to the clicked image's source
  currentImageIndex = Array.from(document.querySelectorAll('.news-photo-gallery img')).indexOf(img); // Get the index of the clicked image
}

// Function to close the modal
function closeModal() {
  setModalDisplay("none"); // Set the modal display to none
}

// Function to show the image at the specified index
function showImage(index) {
  const images = document.querySelectorAll('.news-photo-gallery img');
  if (index >= 0 && index < images.length) { // Check if the index is within bounds
    document.getElementById("image_preview").src = images[index].src; // Set the source of the image preview to the image at the specified index
    currentImageIndex = index; // Update the current image index
  }
}

// Function to show a specific set of images in a gallery
function showImageSet(gallery, startIndex) {
    const images = gallery.querySelectorAll('img');
    if (startIndex >= 0 && startIndex < images.length) {
      for (let i = 0; i < images.length; i++) {
        if (i >= startIndex && i < startIndex + 3) {
          images[i].style.display = "block"; // Show the image
        } else {
          images[i].style.display = "none"; // Hide the image
        }
      }
    }
  }

// Function to initialize all galleries
function initializeGalleries() {
    const galleries = document.querySelectorAll('.news-photo-gallery');
    galleries.forEach(gallery => showImageSet(gallery, 0));
  }

// Add event listener for Escape, Left, Right, Home, and End keys
document.addEventListener("keydown", function(event) {
  if (event.key === "Escape") { // If the Escape key is pressed
    closeModal(); // Close the modal
  } else if (event.key === "ArrowLeft") { // If the Left arrow key is pressed
    showImage(currentImageIndex - 1); // Show the previous image
  } else if (event.key === "ArrowRight") { // If the Right arrow key is pressed
    showImage(currentImageIndex + 1); // Show the next image
  } else if (event.key === "Home") { // If the Home key is pressed
    showImage(0); // Show the first image
  } else if (event.key === "End") { // If the End key is pressed
    showImage(document.querySelectorAll('.news-photo-gallery img').length - 1); // Show the last image
  }
});

// Add event listener for the previous image button
document.getElementById("previous_image_button").addEventListener("click", function(event) {
  event.stopPropagation(); // Prevent the modal from closing
  showImage(currentImageIndex - 1); // Show the previous image
});

// Add event listener for the next image button
document.getElementById("next_image_button").addEventListener("click", function(event) {
  event.stopPropagation(); // Prevent the modal from closing
  showImage(currentImageIndex + 1); // Show the next image
});