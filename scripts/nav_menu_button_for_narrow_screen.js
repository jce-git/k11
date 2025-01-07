function toggleMenu() {
  const navMenu = document.getElementById('nav-menu');
  if (navMenu.style.display === 'flex') {
    navMenu.style.display = 'none';
  } else {
    navMenu.style.display = 'flex';
    navMenu.style.flexDirection = 'column';
  }
}

// Ensure nav menu is hidden by default on smaller screens
window.addEventListener('resize', function() {
  const navMenu = document.getElementById('nav-menu');
  if (window.innerWidth <= 768) {
    navMenu.style.display = 'none';
  } else {
    navMenu.style.display = 'flex';
    navMenu.style.flexDirection = 'row';
  }
});

// Initial check to set the correct display on page load
document.addEventListener('DOMContentLoaded', function() {
  const navMenu = document.getElementById('nav-menu');
  if (window.innerWidth <= 768) {
    navMenu.style.display = 'none';
  } else {
    navMenu.style.display = 'flex';
    navMenu.style.flexDirection = 'row';
  }

  // Add event listeners to nav links
  const navLinks = navMenu.querySelectorAll('a');
  navLinks.forEach(link => {
    link.addEventListener('click', function() {
      if (window.innerWidth <= 768) {
        navMenu.style.display = 'none';
      }
    });
  });
});