More information about .css files

1. Normalize:

Normalize.css makes browsers render all elements more consistently and in line with modern standards.
It precisely targets only the styles that need normalizing.

To integrate Normalize.css into your existing stylesheet:
    1. Download Normalize.css ( or copy link to it from https://necolas.github.io/normalize.css/8.0.1/normalize.css )
    2. Include the Normalize.css file in your project.
    3. Import Normalize.css at the beginning of your css file (here in styles.css).

@import url('normalize.css');
/*
or
@import url('https://raw.githubusercontent.com/jce-git/k11/main/css/normalize.css');
or
@import url('https://necolas.github.io/normalize.css/8.0.1/normalize.css');
*/