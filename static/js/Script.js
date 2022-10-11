function onEntry(entry) {
    entry.forEach( (change) => {
    if (change.isIntersecting) {
     change.target.classList.add('act');
    } else {
        change.target.classList.remove('act');
    }
  });
}

let options_bottom = {
  threshold: [0.5] };
let observer_bottom = new IntersectionObserver(onEntry, options_bottom);
let elements_bottom = document.querySelectorAll('.bottom');

for (let elm of elements_bottom) {
  observer_bottom.observe(elm);
}

function onEntry(entry) {
    entry.forEach( (change) => {
    if (change.isIntersecting) {
     change.target.classList.add('act');
    } else {
        change.target.classList.remove('act');
    }
  });
}

let options_left = {
  threshold: [0.5] };
let observer_left = new IntersectionObserver(onEntry, options_left);
let elements_left = document.querySelectorAll('.left');

for (let elm of elements_left) {
  observer_left.observe(elm);
}

function onEntry(entry) {
    entry.forEach( (change) => {
    if (change.isIntersecting) {
     change.target.classList.add('act');
  } else {
        change.target.classList.remove('act');
    }
  });
}

let options_right = {
  threshold: [0.5] };
let observer_right = new IntersectionObserver(onEntry, options_right);
let elements_right = document.querySelectorAll('.right');

for (let elm of elements_right) {
  observer_right.observe(elm);
}

