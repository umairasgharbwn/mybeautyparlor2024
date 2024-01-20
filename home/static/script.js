'use strict';

const addEvenOnElem = function (elem, type, callback) {
      if(elem.length > 1) {
        for(let i = 0; i < elem.length; i++) {
            elem[i].addEventListener(type, callback);
        }
      } else {
        elem.addEventListener(type, callback);
      }
}


const navbar = document.querySelector("[data-navbar]");
const navtoggler = document.querySelector("[data-nav-toggler]");
const navlinks = document.querySelectorAll("[data-nav-link]");

const toggleNavbar = () => navbar.classList.toggle("active");

addEventOnElem(navToggler, "click", toggleNavbar);

const closeNavbar = () => navbar.classList.remove("active");

addEvenOnElem(navlinks, "click", closeNavbar);





const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

const headerActive = function () {
  if (window.scrollY > 100) {
    header.classList.add("active");
    backTopBtnclassList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
}

addEventOnElem(window, "scroll", headerActive);



const filterBtns = document.querySelectorAll("[data-filter-btn]");
const filterItems = document.querySelectorAll("[data-filter]");

let lastClickedFilterBtn = filterBtns[0];

const filter = function () {
  lastClickedFilterBtn.classList.remove("active");
  this.classList.add("active");
  lastClickedFilterBtn = this;

  for (let i = 0; i < filterItems.length; i++) {
    if (this.dataset.filterBtn === filterItems[i].dataset.filter || 
      this.dataset.filterBtn === "all") {

      filterItems[i].style.display = "block";
      filterItems[i].classList.add("active");

    } else {
      
      filterItems[i].style.display = "none";
      filterItems[i].classList.remove("active");
    }
  }
}

addEvenOnElem(filterBtns, "click", filter);
