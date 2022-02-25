'use strict';

// USE FOR DJANGO WEBSITE ?

// Selecting elements we need -> Store into Variables
const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');

// QuerySelector ONLY picks first one it finds!! so we need "querySelectorAll"
// Nodelist, not exactly as an array but for us it will work as one
const btnsOpenModal = document.querySelectorAll('.show-modal');
console.log(btnsOpenModal);

// instead of having an annonymous function we create our! DRY!
const closeModal = function () {
  modal.classList.add('hidden');
  overlay.classList.add('hidden');
};

const openModal = function () {
  // not dot, only for selector.. can add more classes with ","
  // can also add classes
  modal.classList.remove('hidden');
  overlay.classList.remove('hidden');
};

// Looping over buttons Modals and adding an eventlisteners functions on all
// <div class="modal hidden"> 2 classes on the div, WE REMOVE the hidden class.
for (let i = 0; i < btnsOpenModal.length; i++) {
  btnsOpenModal[i].addEventListener('click', openModal);
}

// WITHOUT () else it will call the function and exit eventlistener, we saved it with an function expression as an variable
// ---------- Eventlistener for closing button
btnCloseModal.addEventListener('click', closeModal);
// ------------ Eventlistener for closing when pressing outside window
overlay.addEventListener('click', closeModal);

// Handling Key press events - GLOBAL, not element specific
// Global === document, basically listening EVERYWHERE, ANY keypress

// call the function with the event object as an argument
//   console.log(event); // To find out info about the spec key
//   console.log(event.key);
document.addEventListener('keydown', function (event) {
  // check if key pressed was ESC
  // AND if modal does not contain the hidden css class, add it (close)
  if (event.key === 'Escape' && !modal.classList.contains('hidden')) {
    closeModal();
  }
});