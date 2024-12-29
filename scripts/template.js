// Set the document title with the help of siteTitle variable from variables.js file (no need to manually enter <title> code on each webpage)
document.title = siteTitle;

// Set the site title in the footer
document.getElementById('site-title').textContent = siteTitle;

// Year when the site was published first time. publishYearFrom is set in the variables.js file
document.getElementById('publish-year-from').textContent = publishYearFrom;

// Set the current year in the footer
document.getElementById('current-year').textContent = new Date().getFullYear();