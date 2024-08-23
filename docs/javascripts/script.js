const ioConfiguration = {
    rootMargin: '0% 0% -100px 0%',
    threshold: 0
  };

const observer = new IntersectionObserver(entries => {
    
    entries.forEach(entry => {
        
        let entryClasses = Array.from(entry.target.classList.values())
        let intersects = entryClasses.filter(class_ => class_.includes("intersect") );

        if (entry.isIntersecting) {
            intersects.forEach((intersect_class) => {
                entry.target.classList.add(intersect_class + '--active');
            })
        } 
    });
}, ioConfiguration);

const intersects = document.querySelectorAll('[class*="intersect"]');
intersects.forEach( intersect => {
    observer.observe(intersect);
});


let currentScrollPosition = window.scrollY;
let navBarTabs = document.body.querySelector("nav.md-tabs");
let header = document.body.querySelector("header.md-header");
let headerTitle = document.body.querySelector("header .md-header__title");

setUpNavBar = () => {
  navBarTabs.classList.add("md-tabs--show");
  navBarTabs.hidden = false;
  header.classList.remove("md-header--shadow");
  headerTitle.classList.remove("md-header__title--active");
}
document.addEventListener('DOMContentLoaded', setUpNavBar, false);


window.addEventListener('scroll', () => {
  
  const newScrollPosition = window.scrollY;

  if (newScrollPosition < currentScrollPosition) {
    console.log("scrolling up")

    header.classList.remove("md-header--shadow");
    headerTitle.classList.remove("md-header__title--active");

    navBarTabs.hidden = false;
    navBarTabs.classList.add("md-tabs--show");
  } else {
    console.log("scrolling down")

    header.classList.add("md-header--shadow");

    headerTitle.classList.add("md-header__title--active")
    
    navBarTabs.hidden = true;
    navBarTabs.classList.remove("md-tabs--show");
  }

  currentScrollPosition = newScrollPosition;
});