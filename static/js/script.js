class TypeWriter {
  constructor(txtElement, words, wait = 3000) {
    this.txtElement = txtElement;
    this.words = words;
    this.txt = '';
    this.wordIndex = 0;
    this.wait = parseInt(wait, 10);
    this.type();
    this.isDeleting = false;
  }
  type() {
    // Current index of word
    const current = this.wordIndex % this.words.length;
    // Get full text of current word
    const fullTxt = this.words[current];

    // Check if deleting
    if (this.isDeleting) {
      // Remove char
      this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
      // Add char
      this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    // Insert txt into element
    this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;

    // Initial Type Speed
    let typeSpeed = 300;

    if (this.isDeleting) {
      typeSpeed /= 2;
    }

    // If word is complete
    if (!this.isDeleting && this.txt === fullTxt) {
      // Make pause at end
      typeSpeed = this.wait;
      // Set delete to true
      this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
      this.isDeleting = false;
      // Move to next word
      this.wordIndex++;
      // Pause before start typing
      typeSpeed = 500;
    }

    setTimeout(() => this.type(), typeSpeed);
  }
}

// Init On DOM Load
document.addEventListener('DOMContentLoaded', init);

// Init App
function init() {
  const h1Element = document.querySelector('.moving.text');
  const spanElement = h1Element.querySelector('.move-txt');
  const words = JSON.parse(spanElement.getAttribute('data-words'));
  const wait = spanElement.getAttribute('data-wait');
  // Init TypeWriter
  new TypeWriter(spanElement, words, wait);
}


// dismiss messages accross the website
setTimeout(function () {
  let messages = document.getElementById("msg");
  let alert = new bootstrap.Alert(messages);
  alert.close();

}, 2500);


function initMap() {
  var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 8,
    center: {
      lat: 51.98945,
      lng: -9.497680
    }
  });

  var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  var locations = [{
      lat: 51.975419966873176,
      lng: -9.480041904900212
      
    },
    {
      lat: 51.85419966873176,
      lng: -9.180041904900212
    },
    {
      lat: 52.009966873176,
      lng: -9.6841904900212
    },
    {
      lat: 51.95419966873176,
      lng: -9.6041904900212
    },
    {
      lat: 51.975419966873176,
      lng: -9.77041904900212
    },
    {
      lat: 52.01757,
      lng: -9.59041904900212
    },
    {
      lat: 52.11757,
      lng: -9.62041904900212
    },
    {
      lat: 51.96757,
      lng: -9.78041904900212
    },
    {
      lat: 51.98757,
      lng: -9.72041904900212
    },
    {
      lat: 51.89757,
      lng: -9.68041904900212
    },
    {
      lat: 51.76757,
      lng: -9.38041904900212
    },
    {
      lat: 51.76757,
      lng: -9.704900212
    },
   
   

  ];
  var markers = locations.map(function (location, i) {
    return new google.maps.Marker({
      position: location,
      label: labels[i % labels.length]
    });
  });

  const markerCluster = new MarkerClusterer(map, markers, {
    imagePath: "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m",
  });
};
